
# Parlo - Programmare in Italiano

Parlo è un linguaggio di programmazione progettato per essere intuitivo e semplice per utenti di lingua italiana. Questo repository contiene l'interprete per eseguire script scritti in Parlo.

## Prova Parlo Online

Puoi testare Parlo direttamente su GitPod con un ambiente di sviluppo completo:

[Apri questo progetto su GitPod](https://gitpod.io/#https://github.com/Onissum/Parlo-Programmare-in-Italiano)

## Caratteristiche

- **Sintassi in Italiano**: I comandi sono in italiano, rendendo la programmazione più accessibile per chi parla italiano.
- **Esempi di Codice**: Include script di esempio per aiutarti a iniziare.

## Esempio di Codice in Parlo

```plaintext
colore rosso
stampa =============================
stampa      Analisi delle Materie    
stampa =============================

stampa Inserisci il nome dello studente:
inserisci nome

stampa Inserisci il voto in Matematica:
inserisci voto_matematica
stampa Il voto di {nome} in Matematica è {voto_matematica}

stampa Inserisci il voto in Scienze:
inserisci voto_scienze
stampa Il voto di {nome} in Scienze è {voto_scienze}

stampa Inserisci il voto in Italiano:
inserisci voto_italiano
stampa Il voto di {nome} in Italiano è {voto_italiano}

colore verde
stampa Analisi dei voti di {nome}:

colore blu
stampa --- MATEMATICA ---
se voto_matematica è maggiore di 8:
    stampa Ottima prestazione in Matematica!
altrimenti:
    stampa Prestazione in Matematica nella media o inferiore
fine_se

colore blu
stampa --- SCIENZE ---
se voto_scienze è maggiore di 8:
    stampa Ottima prestazione in Scienze!
altrimenti:
    stampa Prestazione in Scienze nella media o inferiore
fine_se

colore blu
stampa --- ITALIANO ---
se voto_italiano è uguale a 6:
    stampa Prestazione nella media in Italiano
altrimenti:
    stampa Prestazione in Italiano non nella media
fine_se

colore reset
```

## Come Usare l'Interprete

1. Clona questo repository:
   ```bash
   git clone https://github.com/Onissum/Parlo-Programmare-in-Italiano.git
   ```

2. Spostati nella directory del progetto:
   ```bash
   cd Parlo-Programmare-in-Italiano
   ```

3. Esegui l'interprete con:
   ```bash
   python interprete_parlo.py
   ```

## Documentazione

Consulta i file di documentazione per maggiori dettagli sul linguaggio e sulle funzionalità:

- **Guida alla Programmazione in Parlo.docx**
- **Guida alla Programmazione in Parlo.pdf**

Questi file forniscono una panoramica completa della sintassi e degli esempi pratici per utilizzare Parlo.

---

Questo README è strutturato per essere facilmente leggibile e fornisce una guida chiara su come utilizzare il tuo progetto.
