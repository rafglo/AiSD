import time, funkcje, generator_ciagu, statistics
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import timeit

def stoper(funkcja, ile, roznica_dlugosci, start, koniec_0, n_0):
    czasy1 = []
    dlugosc = n_0
    for i in range(ile):
        lista = generator_ciagu.gen(start, koniec_0, dlugosc)
        czasy1.append(timeit.timeit(lambda: funkcja(lista), number=100))
        dlugosc += roznica_dlugosci
    return czasy1


czasy_e2 = stoper(funkcje.example2, 10, 100, 1, 100, 100)
xs = range(100, 1001, 100)
plt.plot(xs, czasy_e2, "ro")
plt.xlabel("Długość ciągu")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji example2")
plt.xscale('log')
plt.yscale('log')
plt.show()

