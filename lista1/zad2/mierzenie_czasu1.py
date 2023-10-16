import time, funkcje, generator_ciagu, statistics
import matplotlib.pyplot as plt
import timeit

def stoper(funkcja, ile, roznica_dlugosci, start, koniec, n_0):
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
    dlugosc = n_0
    for i in range(ile):
        lista = generator_ciagu.gen(start, koniec, dlugosc)
        czasy1.append(timeit.timeit(lambda: funkcja(lista), number=100))
        dlugosc += roznica_dlugosci
    return czasy1

czasy_e1 = stoper(funkcje.example1, 10, 100, 1, 100, 100)
xs = range(100, 1001, 100)
plt.plot(xs, czasy_e1, "ro")
plt.xlabel("Długość ciągu")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji example1")

plt.show()
