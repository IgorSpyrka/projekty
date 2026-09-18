# Budżet domowy (Excel)

Prosty arkusz do śledzenia domowych finansów: przychody, wydatki i to, ile
zostaje na koniec miesiąca. To najprostszy typ arkusza, jaki można zrobić —
celowo, żeby dało się go w całości zrozumieć w 10 minut.

## Co jest w pliku

Jeden arkusz `Budzet` podzielony na trzy części:

1. **PRZYCHODY** — lista źródeł dochodu i kwot (kolumna B: nazwa, kolumna C: kwota).
2. **WYDATKI** — lista kategorii wydatków i kwot.
3. **BILANS** — różnica między sumą przychodów a sumą wydatków.

## Formuły użyte w arkuszu

W pliku są tylko 3 formuły — celowo mało, żeby każdą dało się prześledzić.

| Komórka | Formuła | Co robi |
|---|---|---|
| `C8` (Suma przychodów) | `=SUM(C5:C7)` | Dodaje do siebie wszystkie kwoty w zakresie od C5 do C7 |
| `C18` (Suma wydatków) | `=SUM(C11:C17)` | To samo, ale dla zakresu wydatków |
| `C20` (Bilans) | `=C8-C18` | Odejmuje sumę wydatków od sumy przychodów |

**Ważna rzecz do zapamiętania:** w Excelu polskim formuły *widzisz* po polsku
(np. `=SUMA(...)`), ale w środku pliku zawsze zapisane są po angielsku
(`=SUM(...)`). Excel sam je tłumaczy na ekranie — nie trzeba się tym
przejmować, ale warto wiedzieć, że tak to działa, gdyby ktoś pytał, dlaczego
w pliku "nie ma polskich formuł".

## Jak się z tym pobawić / czego się nauczyć

1. Otwórz plik i zmień dowolną kwotę wydatku (np. "Jedzenie") — zobacz, jak
   automatycznie przeliczają się `Suma wydatków` i `Bilans`. To jest cała
   idea arkusza kalkulacyjnego: liczysz raz formułę, a dane możesz zmieniać
   dowolnie.
2. Dodaj nowy wiersz przychodu (np. "Zwrot podatku") — zauważysz, że formuła
   `SUM` **nie** obejmie go automatycznie, jeśli wstawisz go poza dotychczasowy
   zakres. Trzeba wtedy albo wstawić wiersz *wewnątrz* zakresu (Excel
   rozszerzy wtedy formułę sam), albo ręcznie poprawić zakres w formule.
3. Spróbuj dodać kolumnę "% budżetu" przy wydatkach, np.
   `=C11/$C$18` (ile % sumy wydatków stanowi czynsz, komórka C11) i sformatuj
   ją jako procent.
