// Prosta lista zadan - czysty JavaScript, bez zadnych bibliotek.
//
// Kluczowa idea: trzymamy zadania w jednej tablicy (`zadania`) i za kazdym
// razem, gdy cos sie zmieni (dodanie, oznaczenie jako zrobione, usuniecie),
// wywolujemy funkcje `rysujListe()`, ktora czysci widok i buduje go od nowa
// na podstawie aktualnego stanu tablicy. To najprostszy mozliwy wzorzec:
// "stan -> funkcja renderujaca -> widok".

// --- 1. Pobranie elementow ze strony (HTML) ---
const formularz = document.getElementById("formularz");
const poleTekstowe = document.getElementById("pole-tekstowe");
const listaZadan = document.getElementById("lista-zadan");
const pustaLista = document.getElementById("pusta-lista");
const licznik = document.getElementById("licznik");
const przyciskWyczysc = document.getElementById("wyczysc-ukonczone");

// --- 2. Stan aplikacji ---
// Kazde zadanie to obiekt: { id, tekst, ukonczone }.
// Wczytujemy zapisana wczesniej liste z pamieci przegladarki (localStorage),
// zeby zadania nie znikaly po odswiezeniu strony.
let zadania = wczytajZPamieci();

// --- 3. Funkcje pomocnicze do localStorage ---
function wczytajZPamieci() {
  const zapisane = localStorage.getItem("lista-zadan");
  return zapisane ? JSON.parse(zapisane) : [];
}

function zapiszWPamieci() {
  localStorage.setItem("lista-zadan", JSON.stringify(zadania));
}

// --- 4. Rysowanie listy na ekranie ---
function rysujListe() {
  // Czyscimy cala liste i budujemy ja od nowa - prostsze niz recznie
  // sledzic, ktory element dodac/usunac/zmienic.
  listaZadan.innerHTML = "";

  zadania.forEach((zadanie) => {
    const li = document.createElement("li");
    li.className = "zadanie" + (zadanie.ukonczone ? " ukonczone" : "");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = zadanie.ukonczone;
    checkbox.addEventListener("change", () => przelaczUkonczone(zadanie.id));

    const span = document.createElement("span");
    span.textContent = zadanie.tekst;

    const przyciskUsun = document.createElement("button");
    przyciskUsun.className = "usun";
    przyciskUsun.textContent = "×"; // znak "x"
    przyciskUsun.type = "button";
    przyciskUsun.addEventListener("click", () => usunZadanie(zadanie.id));

    li.append(checkbox, span, przyciskUsun);
    listaZadan.appendChild(li);
  });

  // Pokaz/ukryj komunikat "brak zadan"
  pustaLista.style.display = zadania.length === 0 ? "block" : "none";

  // Zaktualizuj licznik u dolu
  const nieukonczone = zadania.filter((z) => !z.ukonczone).length;
  licznik.textContent = `${nieukonczone} z ${zadania.length} zadan do zrobienia`;
}

// --- 5. Operacje na zadaniach ---
function dodajZadanie(tekst) {
  zadania.push({
    id: Date.now(), // prosty, unikalny identyfikator
    tekst: tekst,
    ukonczone: false,
  });
  zapiszWPamieci();
  rysujListe();
}

function przelaczUkonczone(id) {
  const zadanie = zadania.find((z) => z.id === id);
  zadanie.ukonczone = !zadanie.ukonczone;
  zapiszWPamieci();
  rysujListe();
}

function usunZadanie(id) {
  zadania = zadania.filter((z) => z.id !== id);
  zapiszWPamieci();
  rysujListe();
}

function wyczyscUkonczone() {
  zadania = zadania.filter((z) => !z.ukonczone);
  zapiszWPamieci();
  rysujListe();
}

// --- 6. Podpiecie zdarzen ---
formularz.addEventListener("submit", (event) => {
  event.preventDefault(); // zeby strona sie nie przeladowala
  const tekst = poleTekstowe.value.trim();
  if (tekst === "") return;
  dodajZadanie(tekst);
  poleTekstowe.value = "";
  poleTekstowe.focus();
});

przyciskWyczysc.addEventListener("click", wyczyscUkonczone);

// --- 7. Pierwsze narysowanie listy po wczytaniu strony ---
rysujListe();
