# Raport zadań zespołu — formuły na wielu arkuszach (Excel)

Ten projekt pokazuje kolejny poziom formuł Excela: **sumowanie danych z wielu
arkuszy naraz**. To bardzo częsty wzorzec w prawdziwej pracy biurowej —
codzienny raport na osobnej zakładce (np. "01", "02", "03"... jeden arkusz na
dzień miesiąca) i jeden arkusz zbiorczy, który liczy sumy miesięczne, zbierając
dane ze wszystkich zakładek naraz.

**Ważne:** to jest wersja edukacyjna, zbudowana na bazie szablonu z prawdziwej
pracy biurowej (śledzenie liczby telefonów, maili, czatów itd. na osobę i
dzień). **Wszystkie dane w pliku są zmyślone**, a osoby to "Osoba 1", "Osoba 2",
"Osoba 3" — żadnych prawdziwych imion, nazwisk ani prawdziwych liczb z
oryginalnego pliku. Struktura arkuszy i formuły zostały odtworzone wiernie,
bo to one są tu wartością edukacyjną.

## Co jest w pliku

33 arkusze:

- **`suma miesiaca`** — podsumowanie miesięczne (3 osoby, jeden wiersz na osobę)
- **`01` do `31`** — jeden arkusz na każdy dzień maja 2026, ta sama struktura
  w każdym: 3 osoby, 8 kolumn z licznikami zadań (telefony, różne typy maili,
  TODO, czat, NTO), suma dzienna i godziny robocze

Dni robocze (poniedziałek–piątek) mają wypełnione dane. Weekendy są celowo
puste — pokazuje to, że formuła `SUM` radzi sobie z pustymi komórkami bez
błędu (po prostu traktuje je jako zero).

## Formuły użyte w arkuszu — to jest sedno tego projektu

### 1. Suma z jednego arkusza (arkusze dzienne, kolumna "suma")

```
=SUM(B2:I2)
```

To już znasz z poprzednich projektów — zwykła suma zakresu w jednym wierszu.

### 2. Suma z **wielu arkuszy naraz** (arkusz "suma miesiaca")

To jest nowość. Formuła w komórce B2 arkusza `suma miesiaca` wygląda tak
(skrócone dla czytelności):

```
=SUM('01'!B2,'02'!B2,'03'!B2, ... ,'31'!B2)
```

Czytamy to tak: *"weź komórkę B2 z arkusza `01`, komórkę B2 z arkusza `02`,
komórkę B2 z arkusza `03`... i tak dalej przez wszystkie 31 arkuszy — i
zsumuj je wszystkie razem"*. Innymi słowy: **ile telefonów odebrała Osoba 1
przez cały miesiąc**, licząc dzień po dniu.

Nazwa arkusza w cudzysłowie + wykrzyknik (`'01'!B2`) to sposób, w jaki Excel
odwołuje się do komórki **w innym arkuszu**. Warto to zapamiętać — to jedna
z najczęściej używanych technik w większych skoroszytach.

### 3. `IFERROR` — zabezpieczenie przed błędem dzielenia przez zero

```
=IFERROR(J2/K2,"")
```

Kolumna "średnia zadań/godz" dzieli sumę zadań przez liczbę przepracowanych
godzin. W weekend, gdy nikt nie pracował, godziny robocze (`K`) są puste — a
dzielenie przez pustą komórkę (czyli de facto przez zero) normalnie dałoby
błąd `#DZIEL/0!`. `IFERROR(formuła, "co pokazać zamiast błędu")` przechwytuje
taki błąd i pokazuje zamiast niego pusty tekst `""`, więc arkusz wygląda
czysto zamiast być pełen błędów.

### 4. Kolumna "liczba ulotki" — dane wpisywane ręcznie

Nie wszystko w arkuszu musi być formułą. Kolumna "liczba ulotki" w
podsumowaniu (żółte tło) to liczba wpisywana **ręcznie raz na miesiąc** — nie
da się jej policzyć automatycznie, bo w arkuszach dziennych jej po prostu
nie ma. To normalna sytuacja w prawdziwych arkuszach: część danych liczy się
formułami, część trzeba wpisać samemu.

## Jak się z tym pobawić / czego się nauczyć

1. Otwórz dowolny arkusz dzienny (np. `05`) i zmień liczbę telefonów dla
   "Osoba 1". Przejdź do arkusza `suma miesiaca` — suma automatycznie się
   zmieni, mimo że jest liczona z 31 różnych arkuszy.
2. Kliknij w komórkę `B2` w arkuszu `suma miesiaca` i spójrz na pasek formuł
   na górze Excela — zobaczysz pełne odwołanie do wszystkich 31 arkuszy.
3. Spróbuj dodać 4. osobę: skopiuj wiersz w każdym z 31 arkuszy dziennych
   *oraz* w podsumowaniu, a potem popraw formuły w podsumowaniu, żeby
   odwoływały się do nowego wiersza.
4. To dobry moment, żeby zobaczyć ograniczenie tego podejścia: 31 osobnych
   arkuszy to dużo klikania przy każdej zmianie struktury. W bardziej
   zaawansowanych arkuszach zamiast osobnej zakładki na dzień używa się
   jednej długiej tabeli (data w kolumnie) i formuł typu `SUMIFS` z
   warunkiem na datę — patrz projekt `excel-projects/02-analiza-sprzedazy`
   dla podstaw `SUMIF`.

## Jak zrobiony jest ten plik

Wygenerowany skryptem Pythona (`openpyxl`) — ręczne stworzenie 33 arkuszy z
formułami byłoby żmudne, więc kod buduje je w pętli. Mogę pokazać skrypt
źródłowy, jeśli interesuje Cię, jak wygenerować dziesiątki podobnych do
siebie arkuszy naraz.
