import os
import funkcje_heap

slownik = []


class Huffman_kompresor:

    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.kopiec = []
        self.kody = {}
        self.mapowanie = {}

    class Wezel:
        def __init__(self, znak, czestosc):
            self.l = None
            self.r = None
            self.znak = znak
            self.czestosc = czestosc

        def __lt__(self, inny):
            return self.czestosc < inny.czestosc


    def wylicz_czestosc(self, tekst):
        czestosc = {}
        for znak in tekst:
            if not znak in czestosc:
                czestosc[znak] = 0
            czestosc[znak] += 1
        print("znak: ", znak, "częstość: ", czestosc)
        return czestosc

    def tworz_kopiec(self, czestosc):
        for element in czestosc:
            wezel = self.Wezel(element, czestosc[element])
            funkcje_heap.dodajdokopca(self.kopiec, wezel)

    def zlacz_dzieci(self):
        while (len(self.kopiec) > 1):
            wezel1 = funkcje_heap.wyciagnijzkopca(self.kopiec)
            funkcje_heap.doheap(self.kopiec)

            wezel2 = funkcje_heap.wyciagnijzkopca(self.kopiec)
            funkcje_heap.doheap(self.kopiec)

            zlaczone = self.Wezel(None, wezel1.czestosc + wezel2.czestosc)

            zlaczone.l = wezel1
            zlaczone.r = wezel2

            funkcje_heap.dodajdokopca(self.kopiec, zlaczone)
            funkcje_heap.doheap(self.kopiec)

    def stworz_kody(self, korzen, aktualny_kod):
        if (korzen == None):
            return

        if (korzen.znak != None):
            self.kody[korzen.znak] = aktualny_kod
            self.mapowanie[aktualny_kod] = korzen.znak
            element = korzen.znak, aktualny_kod
            print(element)

            slownik.append(element)

            print("Słownik: ", slownik)
            return slownik
        # Rekurencyjne tworzenie kodów
        self.stworz_kody(korzen.l, aktualny_kod + "0")
        self.stworz_kody(korzen.r, aktualny_kod + "1")

    def generuj_kody(self):
        korzen = funkcje_heap.wyciagnijzkopca(self.kopiec)
        aktualny_kod = ""
        self.stworz_kody(korzen, aktualny_kod)

    def pobierz_zakodowany_tekst(self, znaki):
        zakodowany_tekst = ""
        for znak in znaki:
            zakodowany_tekst += self.kody[znak]
        return zakodowany_tekst

    def wypelnij(self, zakodowany_tekst):
        dodatkowe_znaki = 8 - len(zakodowany_tekst) % 8
        for i in range(dodatkowe_znaki):
            zakodowany_tekst += "0"

        hash = "{0:08b}".format(dodatkowe_znaki)
        zakodowany_tekst = hash + zakodowany_tekst
        print("Zakodowany tekst z hashem", zakodowany_tekst)
        return zakodowany_tekst

    def tworz_bin(self, zakodowany):
        if (len(zakodowany) % 8 != 0):
            print("Nieprawidłowa ilość znaków. Nie dzieli się przez 8.")
            exit(0)
        # tworzenie ciągu znaków na podstawi 8 kolejnych bitów
        znaczek = bytearray()
        for i in range(0, len(zakodowany), 8):
            bajt = zakodowany[i:i + 8]
            znaczek.append(int(bajt, 2))
        return znaczek

    def kompresja(self):

        nazwa_pliku, rozszerzenie = os.path.splitext(self.sciezka)
        sciezka_wyjsciowa = nazwa_pliku + "_zakodowane" + ".bin"

        tylko_bin = nazwa_pliku + "_tylko_bin" + ".bin"

        with open(self.sciezka, 'r+') as plik, open(sciezka_wyjsciowa, 'wb') as wyjscie:
            tekst = plik.read()
            tekst = tekst.rstrip()  # usuwanie spacji po napisie

            # sprawdzenie częstości występowanie liter
            czestosc = self.wylicz_czestosc(tekst)
            self.tworz_kopiec(czestosc)
            self.zlacz_dzieci()
            self.generuj_kody()

            zakodowane = self.pobierz_zakodowany_tekst(tekst)
            dopelnienie_kodowanie = self.wypelnij(zakodowane)

            # zapisanie znaczków
            znaki = self.tworz_bin(dopelnienie_kodowanie)
            wyjscie.write(znaki)

        # dopisanie słownika oraz ciągu bitów do pliku bin
        with open(sciezka_wyjsciowa, "a") as plik_wyjsciowy:
            # plik_wyjsciowy.write("\n" + self.pobierz_zakodowany_tekst(tekst) + "\n")
            plik_wyjsciowy.write("\n".join(str(el) for el in slownik))

        with open(tylko_bin, "wb") as wyjscie_bin:
            wyjscie_bin.write(znaki)

        return wyjscie
