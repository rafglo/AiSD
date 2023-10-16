import generator_ciagu, time, statistics, timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def stoper(ile, roznica_dlugosci, start, koniec_0, n_0):
    czasy1 = []
    dlugosc = n_0
    for i in range(ile):
        lista = generator_ciagu.gen(start, koniec_0, dlugosc)
        czasy1.append(timeit.timeit(lambda: sorted(lista), number=100))
        dlugosc += roznica_dlugosci
    return czasy1

def func(x,a,b,c):
    return a*x*np.log(x+b) + c

czasy = stoper(200, 100, 1, 20000, 1)
xs = range(1, 20001, 100)
popt, pcov = curve_fit(func, xs, czasy)

plt.plot(xs, czasy, "ro")
plt.xlabel("Długość ciągu")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji sorted")
plt.plot(xs, func(xs, *popt))
plt.show()
