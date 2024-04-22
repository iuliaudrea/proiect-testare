# Clasa _MathQuiz_

## Descriere:
Clasa `MathQuiz` implementează un quiz de matematică care generează întrebări aleatorii cu operații de bază (adunare, scădere, înmulțire, împărțire) și evaluează răspunsurile utilizatorului, oferind feedback și înregistrând scorul.

## Specificația problemei

### Comportamentul așteptat

- **Generarea Întrebărilor:** Întrebările trebuie să fie corect formulate cu operații matematice valide și numere între 1 și 10.
- **Evaluarea Răspunsurilor:** Utilizatorul trebuie să fie capabil să introducă răspunsuri sub formă de numere. Răspunsurile greșite nu modifică scorul, pe când răspunsurile corecte îl incrementează.
- **Finalizarea Quiz-ului:** Quiz-ul trebuie să ofere feedback adecvat la final, bazat pe numărul de răspunsuri corecte: un mesaj de succes dacă scorul este mai mare sau egal cu jumătate din numărul total de întrebări, altfel un mesaj de eșec.
- **Oprirea Prematură:** Dacă numărul de răspunsuri greșite face imposibilă atingerea scorului de trecere, quiz-ul se oprește și informează utilizatorul că nu mai poate atinge scorul necesar.


### Metodele clasei

| Metodă| Descriere                                                                                                                   | Parametri                                   | Valoare returnată                  |
|-|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|------------------------------------|
|`__init__`| Inițializează un nou quiz și setează scorul la 0.                                                                           | -                                           | -                                  |
| `generate_question` | Generează o întrebare matematică aleatoare. Dacă operația este de împărțire, răspunsul este trunchiat la două zecimale.     | -                                           | Tuplu: întrebare și răspuns corect |
| `ask_question` | Solicită și verifică răspunsul la o întrebare dată. Dacă răspunsul e corect, scorul e incrementat.                          | `question`: str, `correct_answer`: float    | -                                  |
| `run_quiz`| Rulează quiz-ul cu un număr specificat de întrebări. Quiz-ul se oprește dacă numărul maxim de răspunsuri greșite este atins | `num_questions`: int (opțional, implicit 5) | -                                  |

Metodele conțin validări de date, de exemplu pentru numărul de întrebări din quiz sau pentru răspunsul oferit de jucător. 

## Testarea funcțională

### Partiționarea în clase de echivalență
Clasele de echivalență rezultă din de datele de intrare și cele de ieșire, în funcție de următorii parametri:
#### Numărul de întrebări
Input-ul principal îl reprezintă numărul de întrebări din quiz, care trebuie să fie între 1 și 10. Pentru acesta, se disting 3 clase de echivalență:
- `1 ≤ num_questions ≤ 10`: număr de întrebări valid;
- `num_questions < 1`: număr sub limita validă, nepermis;
- `num_questions > 10`: număr este peste limita validă, nepermis.

#### Input-ul utulizatorului
Răspunsurile jucătorului pot clasificate astfel:
*  corecte: utilizatorul introduce exact valoarea corectă așteptată;
*  incorecte: utilizatorul introduce o valoare numerică care nu reprezintă răspunsul corect;
*  invalide: utilizatorul introduce date care nu pot fi convertite într-un număr (de exemplu text).

#### Domeniul de ieșiri
Output-ul quiz-ului este determinat de numărul de răspunsuri corecte și poate fi descris în funcție de performanța utilizatorului:

* Toate răspunsurile sunt corecte: Output-ul este un mesaj de felicitare pentru scorul perfect.
* Majoritatea răspunsurilor sunt corecte: Utilizatorul primește un mesaj că a trecut, dar poate face progrese.
* Peste jumătate din răspunsuri greșite înainte de finalizarea quiz-ului: Utilizatorul primește un mesaj că nu a trecut quiz-ul și că acesta s-a terminat prematur.



| Număr întrebări | Număr răspunsuri corecte | Răspuns utilizator per întrebare | Output așteptat                                                                     |
|-----------------|--------------------------|----------------------------------|-------------------------------------------------------------------------------------|
| 0               | -                        | -                                | Se ridică un `ValueError` care precizează intervalul acceptat                       |
| 11              | -                        | -                                | Se ridică un `ValueError` care precizează intervalul acceptat                       |
| 5               | 5/5                      | -                                | "Quiz completed! Your score: 5/5 (Passed)"<br/>"Perfect score, well done!"          |
| 5               | 3/5                      | -                                | "Quiz completed! Your score: 3/5 (Passed)"<br/>"Good job, but you can do better!"   |
| 5               | 0/3                      | -                                | "Can't reach passing score anymore."<br/>"Quiz completed! Your score: 0/5 (Failed)" |
| 5               | -                        | Nevalid                          | Repetate solicitări de "Please enter a valid number." până la un răspuns valid      |
| 5               | -                        | Corect                           | "Correct!"                                                                          |
| 5               | -                        | Greșit                           | "Wrong! The correct answer was __"                                                  |
### Analiza valorilor de frontieră
Pentru `num_questions` vom considera următoarele valori de frontieră care trebuie testate:
- inferioară: valoarea imediat mai mică decât limita inferioară a intervalului valid, adică 0;
- superioară: valoarea imediat mai mare decât limita superioară a intervalului valid, adică 11

Pentru răspunsurile utilizatorului, trebuie luate în considerare răspunsurile la limita corectitudinii, precum următoarele. Toate răspunsurile sunt trunchiate la două zecimale.

```
What is 6 / 9? (Maximum of the two MSD.) 0.666
Correct!

What is 6 / 9? (Maximum of the two MSD.) 0.67
Wrong! The correct answer was 0.66.

What is 9 + 10? 19.000000000000000000000000000000001
Correct!
```

## Testarea structurală
