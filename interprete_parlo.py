import re
from colorama import Fore, Back, Style, init

# Inizializza Colorama
init(autoreset=True)

def gestisci_colori(comando_principale, argomenti, colore_corrente, sfondo_corrente):
    colori = {
        "nero": Fore.BLACK,
        "rosso": Fore.RED,
        "verde": Fore.GREEN,
        "giallo": Fore.YELLOW,
        "blu": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "ciano": Fore.CYAN,
        "bianco": Fore.WHITE,
        "reset": Fore.RESET
    }
    if argomenti:
        colore_nome = argomenti[0].lower()
        if comando_principale == "colore":
            colore_corrente = colori.get(colore_nome, Fore.RESET)
    else:
        print(f"Errore: Nessun colore specificato per '{comando_principale}'.")
    return colore_corrente, sfondo_corrente

def traduci_e_esegui_riga_parlo(riga, variabili, colore_corrente=Fore.RESET, sfondo_corrente=Back.RESET):
    riga = riga.strip()
    
    if riga.startswith("inserisci "):
        nome_variabile = riga[9:].strip()
        valore = input(f"Inserisci il valore per {nome_variabile}: ")
        # Riconosce numeri interi e float, altrimenti considera il valore come stringa
        try:
            valore_numerico = float(valore)
            if valore_numerico.is_integer():
                variabili[nome_variabile] = int(valore_numerico)
            else:
                variabili[nome_variabile] = valore_numerico
        except ValueError:
            variabili[nome_variabile] = valore  # Salva come stringa senza virgolette
        return "", colore_corrente, sfondo_corrente
    
    elif riga.startswith("colore "):
        comando_principale, *argomenti = riga.split()
        colore_corrente, sfondo_corrente = gestisci_colori(comando_principale, argomenti, colore_corrente, sfondo_corrente)
        return "", colore_corrente, sfondo_corrente
    
    elif riga.startswith("se "):
        # Prepara la condizione per riconoscere le stringhe senza virgolette
        condizione = (riga[3:]
            .replace(" è maggiore di ", " > ")
            .replace(" è minore di ", " < ")
            .replace(" è uguale a ", " == ")
            .replace(":", "")
            .strip())
        
        # Aggiunge virgolette a stringhe letterali senza virgolette
        for nome in variabili.keys():
            condizione = condizione.replace(nome, f'variabili["{nome}"]')
        
        try:
            risultato = eval(condizione)
            return risultato, colore_corrente, sfondo_corrente
        except Exception as e:
            print(f"Errore nella valutazione della condizione: {e}")
            return False, colore_corrente, sfondo_corrente
    
    elif riga == "altrimenti:":
        return "else_block", colore_corrente, sfondo_corrente
    
    elif riga.startswith("stampa "):
        messaggio = riga[7:].strip()
        for nome, valore in variabili.items():
            messaggio = messaggio.replace(f"{{{nome}}}", str(valore))
        print(f"{colore_corrente}{sfondo_corrente}{messaggio}{Style.RESET_ALL}")
        return "", colore_corrente, sfondo_corrente
    
    elif riga == "fine_se":
        return "end_if", colore_corrente, sfondo_corrente
    
    return "", colore_corrente, sfondo_corrente

def esegui_parlo(parlo_code, variabili={}):
    colore_corrente = Fore.RESET
    sfondo_corrente = Back.RESET

    lines = parlo_code.replace('\r\n', '\n').strip().split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        risultato, colore_corrente, sfondo_corrente = traduci_e_esegui_riga_parlo(
            line, variabili, colore_corrente, sfondo_corrente
        )
        
        if isinstance(risultato, bool):  # È una condizione if
            i += 1  # Spostati alla riga successiva
            if risultato:  # Condizione vera
                # Esegui il blocco if
                while i < len(lines):
                    current_line = lines[i].strip()
                    if current_line == "altrimenti:":
                        # Salta il blocco altrimenti
                        while i < len(lines) and lines[i].strip() != "fine_se":
                            i += 1
                        break
                    elif current_line == "fine_se":
                        break
                    else:
                        _, colore_corrente, sfondo_corrente = traduci_e_esegui_riga_parlo(
                            current_line, variabili, colore_corrente, sfondo_corrente)
                    i += 1
            else:  # Condizione falsa
                # Salta il blocco if ed esegui altrimenti se presente
                while i < len(lines):
                    current_line = lines[i].strip()
                    if current_line == "altrimenti:":
                        i += 1  # Salta 'altrimenti:'
                        # Esegui il blocco altrimenti
                        while i < len(lines) and lines[i].strip() != "fine_se":
                            _, colore_corrente, sfondo_corrente = traduci_e_esegui_riga_parlo(
                                lines[i].strip(), variabili, colore_corrente, sfondo_corrente)
                            i += 1
                        break
                    elif current_line == "fine_se":
                        break
                    i += 1
        elif risultato == "end_if":
            i += 1  # Salta 'fine_se'
        else:
            # La riga è già stata eseguita
            i += 1

# Caricamento ed esecuzione del file
try:
    with open("codice.parlo", "r", encoding="utf-8") as file:
        parlo_code = file.read()
    esegui_parlo(parlo_code, variabili={})
except FileNotFoundError:
    print("File 'codice.parlo' non trovato")
except Exception as e:
    print(f"Errore durante l'esecuzione: {str(e)}")


