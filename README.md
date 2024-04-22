# Clasa `MathQuiz`

## Descriere:
Clasa `MathQuiz` implementează un quiz de matematică care generează întrebări aleatorii cu operații de bază (adunare, scădere, înmulțire, împărțire) și evaluează răspunsurile utilizatorului, oferind feedback și înregistrând scorul.

## Specificația problemei

### Comportamentul așteptat:

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

