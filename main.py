from kompresor_huffman import Huffman_kompresor

sciezka = "barbaramarabarbar.txt"
sciezka2 = "dokompresji.txt"
sciezka3 = "lorem.txt"

kodyhuffmana = Huffman_kompresor(sciezka)
kodyhuffmana2 = Huffman_kompresor(sciezka2)
kodyhuffmana3 = Huffman_kompresor(sciezka3)

wyjscie = kodyhuffmana.kompresja()
wyjscie2 = kodyhuffmana2.kompresja()
wyjscie3 = kodyhuffmana3.kompresja()
