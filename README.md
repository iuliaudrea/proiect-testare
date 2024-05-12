# Clasa _MathQuiz_

## Demo
[Demo](https://unibucro0-my.sharepoint.com/:v:/g/personal/tudor-andrei_farcasanu_s_unibuc_ro/ESe-b9YEyWZDjxuBsV5q2h8Bs0C5I22O4RCMBCoW5vQadA?e=Krb1aw&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

[Demo teste](https://unibucro0-my.sharepoint.com/:v:/g/personal/tudor-andrei_farcasanu_s_unibuc_ro/EcRg8cRKoFVNhK2jeoxbEAkBCXCR1HdT0rj4M205Nvtx_w?e=jGJmn3&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## Descriere:
Clasa `MathQuiz` implementează un quiz de matematică interactiv care generează întrebări aleatorii cu operații de bază (adunare, scădere, înmulțire, împărțire) și evaluează răspunsurile utilizatorului, oferind feedback și înregistrând scorul. Quiz-ul poate fi trecut cu minim jumătate din răspunsuri corecte, iar în caz contrat este picat. Dacă pe parcursul quiz-ului utilizatorul depășește numărul maxim de întrebări greșite, quiz-ul se oprește.

## Specificația problemei

### Funcționalități principale

- **Generarea întrebărilor:** Clasa poate genera întrebări matematice aleatorii sau specificate, implicând operațiile de bază.
- **Interacțiune cu utilizatorul**: Solicită răspunsuri de la utilizatori prin intermediul interfeței de linie de comandă și oferă feedback imediat.
- **Evaluarea răspunsurilor:** ăspunsurile greșite nu modifică scorul, pe când răspunsurile corecte îl incrementează.
- **Finalizarea quiz-ului:** Quiz-ul trebuie să ofere feedback adecvat la final, bazat pe numărul de răspunsuri corecte: un mesaj de succes dacă scorul este mai mare sau egal cu jumătate din numărul total de întrebări, altfel un mesaj de eșec.
- **Oprirea prematură:** Dacă numărul de răspunsuri greșite face imposibilă atingerea scorului de trecere, quiz-ul se oprește și informează utilizatorul că nu mai poate atinge scorul necesar.


### Metodele clasei

| Metodă| Descriere                                                                                                                   | Parametri                                                      | Valoare returnată                  |
|-|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|------------------------------------|
|`__init__`| Inițializează un nou quiz și setează scorul la 0.                                                                           | -                                                              | -                                  |
| `generate_question` | Generează o întrebare matematică aleatoare. Dacă operația este de împărțire, răspunsul este trunchiat la două zecimale.     | `operation`: string (implicit `None`, ales aleator în funcție) | Tuplu: întrebare și răspuns corect |
| `ask_question` | Solicită și verifică răspunsul la o întrebare dată. Dacă răspunsul e corect, scorul e incrementat.                          | `question`: str, `correct_answer`: float                       | -                                  |
| `run_quiz`| Rulează quiz-ul cu un număr specificat de întrebări. Quiz-ul se oprește dacă numărul maxim de răspunsuri greșite este atins | `num_questions`: int (opțional, implicit 5)                    | -                                  |

Metodele conțin validări de date, de exemplu pentru numărul de întrebări din quiz sau pentru răspunsul oferit de jucător. 

## Testarea funcțională

Am folosit partiționarea în categorii, identificând parametrii de care depind comportamentul fiecărei metode din clasă.

### Metoda `run_quiz`

Input-ul principal îl reprezintă numărul de întrebări din quiz, care trebuie să fie între 1 și 10. Pentru acesta, se disting 3 clase de echivalență:
- `1 ≤ num_questions ≤ 10`: număr de întrebări valid;
- `num_questions < 1`: număr sub limita validă, nepermis;
- `num_questions > 10`: număr peste limita validă, nepermis.


Output-ul quiz-ului pentru un numar valid de întrebări este determinat de numărul de răspunsuri corecte:
* Toate răspunsurile sunt corecte: Output-ul este un mesaj de felicitare pentru scorul perfect.
* Majoritatea răspunsurilor sunt corecte: Utilizatorul primește un mesaj că a trecut, dar poate face progrese.
* Majoritatea răspunsurilor sunt greșite: Utilizatorul primește un mesaj că nu a trecut quiz-ul și că acesta s-a terminat prematur.

| Număr întrebări | Număr răspunsuri corecte | Output așteptat                                                                     |
|-----------------|--------------------------|-------------------------------------------------------------------------------------|
| 0               | -                        | Se ridică un `ValueError` care precizează intervalul acceptat                       |
| 11              | -                        | Se ridică un `ValueError` care precizează intervalul acceptat                       |
| 5               | 5/5                      | "Quiz completed! Your score: 5/5 (Passed)"<br/>"Perfect score, well done!"          |
| 5               | 3/5                      | "Quiz completed! Your score: 3/5 (Passed)"<br/>"Good job, but you can do better!"   |
| 5               | 0/5                      | "Can't reach passing score anymore."<br/>"Quiz completed! Your score: 0/5 (Failed)" |

### Metoda `generate_question`
În mod implicit, operația folosită în această metodă este aleasă aleator la rularea quiz-ului, însă poate fi transmisă ca parametru. Considerăm operații valide: adunarea, scăderea, înmulțirea, împărțirea, în timp ce orice altceva ar trebui sa ridice un ValueError. Clasele pentru parametrul `operation`:
* valid: `['+', '-', '*', '/']`;
* implicit: `None`, va fi generat în funcție;
* invalid: oricare alt string sau tip de date.

Pentru toate operațiile, operatorii sunt aleși aleator între 1 și 10. Nu va exista problema împărțirii la 0.

Se returnează string-ul 'What is `num1` `operation` `num2`?' și rezultatul evaluat pe baza întrebării. Pentru  împărțire, întrebarea se sufixează cu '(Maximum of the two MSD.)' și rezultatul este trunchiat la două zecimale.

| Parametru `operation` | Output așteptat                                                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `'+'`                 | `question`: 'What is `num1` + `num2`?', <br/> `correct_answer`: rezultatul operației                                             |
| `'/'`                 | `question`: 'What is `num1` / `num2`?  (Maximum of the two MSD.)', <br/> `correct_answer`: rezultatul trunchiat la două zecimale |
| `None`                | Operația este aleasă aleator din setul `['+', '-', '*', '/']` și se procedează ca mai sus.                                       |
| Oricare altă valoare  | Ridicarea unui `ValueError` cu mesajul că operația nu este validă.                                                               |

### Metoda `ask_question`
În metoda principală de rulare a quiz-ului, `ask_question` folosește ca parametrii o întrebare și un răspuns (valide) de la metoda anterioară de generare a întrebării. 
Totuși, metoda se poate apela în afara unui quiz, cu o întrebare și un răspuns numeric oarecare. Metoda afișează întrebarea și așteaptă ca utilizatorul să introducă răspunsul primit ca parametru.

Se disting următoarele clase pentru `correct_answer`:
* numeric valid: int sau float trunchiat la două zecimale;
* numeric invalid: float cu mai mult de două zecimale;
* other invalid: orice altă valoare.


Output-urile sunt in functie de răspunsul primit de utilizator de la tastatura, iar acesta poate fi:
*  corect: utilizatorul introduce exact valoarea corectă așteptată, iar scorul e incrementat;
*  incorect: utilizatorul introduce o valoare numerică care nu reprezintă răspunsul corect;
*  invalid: utilizatorul introduce date care nu pot fi convertite într-un număr (de exemplu text).

| `correct_answer` | Răspunsul utilizatorului | Output așteptat                                                                         |
|------------------|--------------------------|-----------------------------------------------------------------------------------------|
| 3                | 3                        | "Correct!" şi scorul este incrementat                                                   |
| 3                | 5                        | "Wrong! The correct answer was 3."                                                      |
| 3                | 'trei'                   | "Please enter a valid number."<br/> Utilizatorul este invitat să reintroducă un răspuns |
| 'cinci'          | -                        | Metoda ridică un `ValueError` referitor la tipul de date al parametrului                |
| 3.333            | -                        | Metoda ridică un `ValueError` referitor la numărul de zecimale                          |

## Testarea structurală
### Graful de flux de control 
Pentru generarea grafului am folosit libraria `staticfg`. [Graful generat](./graf/quiz.png) trebuie adaptat, înlocuind instrucțiunile propriu-zise cu liniile de cod.


### Acoperire la nivel de instrucțiune

### Acoperire la nivel de decizie

### Acoperire la nivel de condiție

### Testarea circuitelor independente

## Generarea de mutanți

## Compararea testelor cu cele generate de AI

## Alegerea framework-urilor
