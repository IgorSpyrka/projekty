# Analizator wydatków (Python)

Prosty skrypt w Pythonie, który wczytuje wydatki z pliku CSV, liczy
podsumowanie wg kategorii i rysuje wykres. To odpowiednik projektu
`excel-projects/02-analiza-sprzedazy`, tylko zrobiony w kodzie zamiast w
Excelu — dobry przykład, żeby zobaczyć, że **ten sam problem** (zsumuj coś
wg kategorii) da się rozwiązać dwoma różnymi narzędziami.

## Jak uruchomić

Potrzebne biblioteki: `pandas` i `matplotlib` (obie bardzo popularne w
analizie danych w Pythonie).

```bash
pip install pandas matplotlib
python3 analizator.py
```

Skrypt wypisze podsumowanie w konsoli i zapisze wykres do pliku
`wykres_wydatkow.png` (w repo jest już przykładowy wygenerowany wykres,
żeby było widać efekt bez uruchamiania kodu).

## Struktura projektu

```
wydatki.csv           - przykładowe dane wejściowe (20 wydatków ze stycznia)
analizator.py          - cały kod
wykres_wydatkow.png    - wygenerowany wykres (przykładowy wynik)
```

## Jak czytać `analizator.py`

Kod jest podzielony na małe funkcje, z których każda robi jedną rzecz —
to dobra praktyka: łatwiej przetestować i zrozumieć kod, kiedy każda funkcja
ma jedno, jasne zadanie.

1. **`wczytaj_dane()`** — otwiera plik CSV i zamienia go w tabelę danych
   (tzw. `DataFrame` z biblioteki pandas). To jest odpowiednik otwarcia
   arkusza w Excelu, tylko w kodzie.

2. **`policz_podsumowanie()`** — kluczowa linijka to:
   ```python
   dane.groupby("kategoria")["kwota"].sum()
   ```
   Po polsku: "podziel wiersze wg kolumny `kategoria`, a w każdej grupie
   zsumuj kolumnę `kwota`". To dokładnie to samo, co robi formuła `SUMIF`
   w Excelu — tylko jedna linijka kodu liczy to dla **wszystkich** kategorii
   naraz, zamiast pisać osobną formułę dla każdej z nich.

3. **`wypisz_podsumowanie()`** — zwykłe wypisywanie tekstu w konsoli, z
   ładnym wyrównaniem kolumn (`{:<12}`, `{:>10.2f}` to formatowanie liczb
   i tekstu w Pythonie).

4. **`narysuj_wykres()`** — rysuje wykres słupkowy (`matplotlib`), z
   opisanymi wartościami nad słupkami i stałym kolorem dla każdej kategorii
   (słownik `KOLORY_KATEGORII` na górze pliku).

5. **`main()`** — spina wszystko w całość: wczytaj → policz → wypisz →
   narysuj. To dobra konwencja w Pythonie: trzymać "główny scenariusz"
   programu w jednej krótkiej funkcji na dole pliku.

## Czego się nauczyć / co poklikać w kodzie

1. Dodaj nowy wiersz do `wydatki.csv` (np. nową kategorię "Zdrowie") i
   uruchom skrypt ponownie — zobacz, że podsumowanie i wykres same
   uwzględnią nową kategorię (dodaj dla niej kolor w `KOLORY_KATEGORII`,
   inaczej dostanie domyślny szary).
2. Zmień `dane.groupby("kategoria")` na `dane.groupby("data")` — zobaczysz
   sumę wydatków dziennie zamiast wg kategorii.
3. Spróbuj policzyć **średni wydatek** w każdej kategorii zamiast sumy:
   `dane.groupby("kategoria")["kwota"].mean()`.
4. Jeśli chcesz iść dalej — pandas ma dużo więcej takich operacji
   (`min()`, `max()`, `count()`, sortowanie, filtrowanie wierszy warunkiem)
   i to jest naturalny następny krok po tym przykładzie.
