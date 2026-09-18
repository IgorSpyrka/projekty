# Lista zadań (HTML + CSS + JavaScript)

Prosta aplikacja "to-do list" napisana w czystym JavaScripcie — bez
frameworków (bez Reacta, bez Vue), bez procesu budowania (bez `npm install`,
bez webpacka). Wystarczy otworzyć `index.html` w przeglądarce.

Celowo taka forma: żeby dało się przeczytać **cały** kod od góry do dołu i
zrozumieć, jak działa strona internetowa "od podszewki", zanim zacznie się
używać frameworków, które chowają wiele z tych mechanizmów.

## Jak uruchomić

Po prostu otwórz plik `index.html` w przeglądarce (dwuklik, albo przeciągnij
do okna przeglądarki). Nie trzeba niczego instalować.

## Struktura projektu

```
index.html   - szkielet strony (co jest na ekranie)
style.css    - wygląd (kolory, odstępy, układ)
script.js    - logika (co się dzieje, gdy klikasz)
```

To standardowy podział w web developmencie: **HTML** to treść, **CSS** to
wygląd, **JavaScript** to zachowanie. Rozdzielenie ich na osobne pliki to
dobra praktyka — ułatwia znalezienie tego, czego się szuka.

## Jak działa `script.js` — najważniejsza część do zrozumienia

1. **Stan aplikacji** to jedna tablica `zadania`, np.:
   ```js
   [
     { id: 123, tekst: "Kupić mleko", ukonczone: false },
     { id: 456, tekst: "Zadzwonić do mamy", ukonczone: true },
   ]
   ```
2. **Funkcja `rysujListe()`** za każdym razem czyści listę na ekranie
   (`listaZadan.innerHTML = ""`) i buduje ją od nowa na podstawie tablicy
   `zadania`. To jest kluczowy wzorzec, który wraca też w Reakcie, Vue itd.,
   tylko tam robi to framework, a nie my ręcznie:
   ```
   zmiana danych → funkcja rysująca → to, co widzisz na ekranie
   ```
3. Każda operacja (dodanie, oznaczenie jako zrobione, usunięcie,
   wyczyszczenie ukończonych) robi dokładnie trzy rzeczy:
   - zmienia tablicę `zadania`,
   - zapisuje ją w pamięci przeglądarki (`localStorage`), żeby zadania
     przetrwały odświeżenie strony,
   - wywołuje `rysujListe()`, żeby ekran pokazał nowy stan.

## Czego się nauczyć / co poklikać w kodzie

1. Otwórz stronę, dodaj kilka zadań, odśwież stronę (F5) — zadania zostają.
   To dzięki `localStorage.setItem(...)` / `localStorage.getItem(...)` w
   `script.js`. Otwórz konsolę przeglądarki (F12) i wpisz
   `localStorage.getItem("lista-zadan")`, żeby zobaczyć surowe dane.
2. W `script.js` znajdź funkcję `dodajZadanie` i dodaj `console.log(zadania)`
   na końcu — zobaczysz w konsoli, jak zmienia się tablica po każdym
   dodaniu.
3. Spróbuj dodać nową funkcję, np. licznik znaków w polu tekstowym, albo
   zmień kolory w `style.css`.
4. Naturalny następny krok po zrozumieniu tego wzorca "od ręki" to zobaczenie,
   jak ten sam mechanizm (`rysujListe()`) wygląda w React — tam framework
   robi to za kulisami automatycznie.
