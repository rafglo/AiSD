import random
def gen(start, koniec, n):
    """
    Function 
    Funkcja generująca losowy ciąg n liczb

    Input
    start(integer) - początek zakresu
    koniec(integer) - koniec zakresu
    n(integer) - liczba wyrazów ciągu

    Output 
    wynik(list) - wygenerowany ciąg
    """
    wynik = []
    for i in range(n):
        wynik.append(random.randint(start,koniec))
    return wynik


import matplotlib.pyplot as plt
import timeit

def stoper(dlugosc_listy, indeksy):
    """
    Function
    Funkcja Licząca czas wykonywania danej funkcji dla rosnących długości ciągów 

    Input
    funkcja(function) - funkcja, której złożoność chcemy sprawdzić
    ile(integer) - dla ilu list chcemy sprawdzić funkcję
    roznica_dlugosci(integer) - o ile mają się różnić długości kolejnych list
    start(integer) - początek zakresu dla losowania listy
    koniec(integer) - koniec zakresu dla losowania listy
    n_0(integer) - długość pierwszej listy

    Output
    czasy1(list) - lista z czasami odpowiadającymi kolejnym długościom 
    
    """
    czasy1 = []
    lista = gen(1,100, 10000)
    for indeks in indeksy:
        czasy1.append(timeit.timeit(lambda: lista.pop(indeks), number=100))
    return czasy1

czasy_e1 = stoper(100, [i for i in range(100, 1, -1)])
xs = range(100, 1, -1)
plt.plot(xs, czasy_e1, "ro")
plt.xlabel("Indeks")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji pop")

plt.show()
