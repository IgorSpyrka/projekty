"""
Analizator wydatkow - prosty skrypt w Pythonie.

Co robi:
  1. Wczytuje wydatki z pliku CSV (data, kategoria, opis, kwota).
  2. Liczy sume wydatkow w kazdej kategorii.
  3. Wypisuje podsumowanie w konsoli.
  4. Rysuje prosty wykres slupkowy i zapisuje go jako obrazek PNG.

Uzyte biblioteki:
  - pandas    -> wczytywanie i grupowanie danych (standard w analizie danych w Pythonie)
  - matplotlib -> rysowanie wykresu

Uruchomienie:
  python3 analizator.py
"""

import pandas as pd
import matplotlib.pyplot as plt

PLIK_CSV = "wydatki.csv"
PLIK_WYKRESU = "wykres_wydatkow.png"

# Kolory kategorii - stala kolejnosc, kazda kategoria ma zawsze ten sam
# kolor niezaleznie od tego, ile ma slupkow. To wazne dla czytelnosci,
# gdy porownuje sie kilka wykresow tych samych danych.
KOLORY_KATEGORII = {
    "Jedzenie": "#2a78d6",   # niebieski
    "Transport": "#eb6834",  # pomaranczowy
    "Rachunki": "#1baf7a",   # turkusowy
    "Rozrywka": "#eda100",   # zolty
}


def wczytaj_dane(sciezka: str) -> pd.DataFrame:
    """Wczytuje plik CSV do tabeli (DataFrame) i konwertuje kolumne 'data' na daty."""
    dane = pd.read_csv(sciezka, parse_dates=["data"])
    return dane


def policz_podsumowanie(dane: pd.DataFrame) -> pd.Series:
    """
    Grupuje wydatki wg kategorii i sumuje kolumne 'kwota'.

    To jest odpowiednik formuly SUMIF z Excela (patrz projekt
    excel-projects/02-analiza-sprzedazy) - tylko zapisany w Pythonie:
    zamiast SUMIF(warunek, zakres) uzywamy dane.groupby("kategoria")["kwota"].sum().
    """
    podsumowanie = dane.groupby("kategoria")["kwota"].sum().sort_values(ascending=False)
    return podsumowanie


def wypisz_podsumowanie(podsumowanie: pd.Series, suma_calkowita: float) -> None:
    """Wypisuje czytelne podsumowanie w konsoli."""
    print("=" * 40)
    print("PODSUMOWANIE WYDATKOW WG KATEGORII")
    print("=" * 40)
    for kategoria, kwota in podsumowanie.items():
        udzial_procentowy = kwota / suma_calkowita * 100
        print(f"{kategoria:<12} {kwota:>10.2f} zl   ({udzial_procentowy:5.1f}%)")
    print("-" * 40)
    print(f"{'RAZEM':<12} {suma_calkowita:>10.2f} zl")


def narysuj_wykres(podsumowanie: pd.Series, sciezka_wyjscia: str) -> None:
    """Rysuje wykres slupkowy wydatkow wg kategorii i zapisuje go jako PNG."""
    kategorie = podsumowanie.index.tolist()
    kolory = [KOLORY_KATEGORII.get(kat, "#898781") for kat in kategorie]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    slupki = ax.bar(kategorie, podsumowanie.values, color=kolory, width=0.6)

    # Podpisz kazdy slupek jego wartoscia - latwiej czytac niz sama os Y
    for slupek in slupki:
        wysokosc = slupek.get_height()
        ax.annotate(
            f"{wysokosc:.0f} zl",
            xy=(slupek.get_x() + slupek.get_width() / 2, wysokosc),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            fontsize=9,
        )

    ax.set_title("Wydatki wg kategorii - styczen 2026", fontsize=13, weight="bold")
    ax.set_ylabel("Kwota (zl)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color="#e1e0d9", linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(sciezka_wyjscia, dpi=150)
    print(f"\nWykres zapisany do pliku: {sciezka_wyjscia}")


def main() -> None:
    dane = wczytaj_dane(PLIK_CSV)
    podsumowanie = policz_podsumowanie(dane)
    suma_calkowita = dane["kwota"].sum()

    wypisz_podsumowanie(podsumowanie, suma_calkowita)
    narysuj_wykres(podsumowanie, PLIK_WYKRESU)


if __name__ == "__main__":
    main()
