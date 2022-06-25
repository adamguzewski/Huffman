def dodajdokopca(kopiec, element):
    """Wkładanie elementu do kopca"""
    kopiec.append(element)
    przesunwdol(kopiec, 0, len(kopiec)-1)

def wyciagnijzkopca(kopiec):
    """Wyciąganie najmniejszego elementu z kopca."""
    ostatni = kopiec.pop()
    if kopiec:
        oddany = kopiec[0]
        kopiec[0] = ostatni
        przesunwgore(kopiec, 0)
        return oddany
    return ostatni

def przesunwgore(kopiec, pozycja):
    koniec = len(kopiec)
    start = pozycja
    nowy = kopiec[pozycja]
    # przesuwanie do liscia
    pozycjadziecka = 2*pozycja + 1    # najbardziej lewe dziecko
    while pozycjadziecka < koniec:
        # ustawianie pozycjadziecka do indexu mniejszego dziecka.
        prawedziecko = pozycjadziecka + 1
        if prawedziecko < koniec and not kopiec[pozycjadziecka] < kopiec[prawedziecko]:
            pozycjadziecka = prawedziecko
        # Przesuwamy mniejsze dziecko
        kopiec[pozycja] = kopiec[pozycjadziecka]
        pozycja = pozycjadziecka
        pozycjadziecka = 2*pozycja + 1
    kopiec[pozycja] = nowy
    przesunwdol(kopiec, start, pozycja)

def przesunwdol(kopiec, start, pozycja):
    nowy = kopiec[pozycja]
    # przesuwanie do korzenia
    while pozycja > start:
        pozycjarodzica = (pozycja - 1) >> 1
        rodzic = kopiec[pozycjarodzica]
        if nowy < rodzic:
            kopiec[pozycja] = rodzic
            pozycja = pozycjarodzica
            continue
        break
    kopiec[pozycja] = nowy

def doheap(x):
    n = len(x)
    for i in reversed(range(n // 2)):
        przesunwgore(x, i)