# Analiza sprzedaży (Excel)

Prosty przykład jednej z najbardziej przydatnych formuł w Excelu:
**sumowanie z warunkiem** (`SUMIF`, po polsku `SUMA.JEŻELI`). To formuła,
której używa się praktycznie w każdej firmie — do liczenia sprzedaży wg
kategorii, kosztów wg działu, godzin wg projektu itd.

## Co jest w pliku

Dwa arkusze:

1. **Dane sprzedaży** — surowa tabela: data, produkt, kategoria, ilość, cena,
   wartość (16 transakcji — mało, żeby dało się je policzyć "na oko" i
   sprawdzić, czy formuły się zgadzają).
2. **Podsumowanie** — automatyczne zestawienie: ile sprzedano w każdej
   kategorii (Pieczywo / Nabiał / Owoce), ile było transakcji i jaka była
   średnia wartość.

Podsumowanie **nie jest przepisane ręcznie** — liczy się samo na podstawie
danych z pierwszego arkusza. Zmień dowolną liczbę w "Dane sprzedaży", a
wartości w "Podsumowaniu" przeliczą się same.

## Formuły użyte w arkuszu

| Formuła | Przykład z pliku | Co robi |
|---|---|---|
| `=D2*E2` (arkusz Dane sprzedaży) | Ilość × Cena jednostkowa | Zwykłe mnożenie — liczy wartość jednej transakcji |
| `SUMIF(zakres_warunku, warunek, zakres_do_zsumowania)` | `=SUMIF('Dane sprzedaży'!$C$2:$C$17,B6,'Dane sprzedaży'!$F$2:$F$17)` | Sumuje kolumnę "Wartość", ale **tylko** dla wierszy, gdzie kolumna "Kategoria" (C) jest równa nazwie kategorii z komórki B6 (np. "Pieczywo") |
| `COUNTIF(zakres, warunek)` | `=COUNTIF('Dane sprzedaży'!$C$2:$C$17,B6)` | Liczy, ile wierszy pasuje do warunku (ile było transakcji w danej kategorii) |
| `=C6/D6` | Wartość / Liczba transakcji | Zwykłe dzielenie — liczy średnią wartość transakcji |
| `=SUM(C6:C8)` | Suma trzech kategorii | Suma całkowita na dole tabeli |

### Jak czytać `SUMIF` krok po kroku

```
=SUMIF( 'Dane sprzedaży'!$C$2:$C$17 ,  B6      , 'Dane sprzedaży'!$F$2:$F$17 )
          gdzie szukać warunku          czego szukać    co zsumować, jeśli warunek pasuje
```

Znaki `$` (np. `$C$2`) to tzw. **odwołanie bezwzględne** — oznaczają "nie
zmieniaj tego zakresu, gdy skopiujesz formułę w dół". Dzięki temu każda z
trzech kategorii (Pieczywo, Nabiał, Owoce) patrzy na te same 16 wierszy
danych, a zmienia się tylko `B6` → `B7` → `B8`.

## Jak się z tym pobawić / czego się nauczyć

1. Dodaj nowy wiersz danych w "Dane sprzedaży" (np. kolejny "Chleb") —
   **ale wewnątrz** istniejącego zakresu tabeli (wstaw wiersz, nie dopisuj na
   końcu). Zobacz, że "Podsumowanie" samo doliczy nową wartość.
2. Dodaj nową kategorię, np. "Słodycze", w kolumnie C danych, a potem dodaj
   dla niej wiersz w "Podsumowaniu" (skopiuj formuły z sąsiedniego wiersza).
3. Spróbuj policzyć **udział procentowy** każdej kategorii w sprzedaży
   ogółem — nowa kolumna z formułą `=C6/$C$9` (gdzie C9 to wiersz RAZEM),
   sformatowana jako procent.
