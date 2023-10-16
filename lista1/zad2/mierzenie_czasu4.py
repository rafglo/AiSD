import time, funkcje, generator_ciagu, statistics, timeit
import matplotlib.pyplot as plt

"""def stoper(funkcja, ile, roznica_dlugosci, start, koniec_0, n_0):
    listy1 = generator_list.gen_list(ile, roznica_dlugosci, start, koniec_0, n_0)
    listy2 = generator_list.gen_list(ile, roznica_dlugosci, start, koniec_0, n_0)
    czasy_e1 = []
    for i in range(len(listy1)):
        start_czasu1 = time.time()
        funkcja(listy1[i], listy2[i])
        koniec_czasu1 = time.time()
        czasy_e1.append(koniec_czasu1 - start_czasu1)
    return czasy_e1
"""

def stoper(funkcja, ile, roznica_dlugosci, start, koniec_0, n_0):
    czasy1 = []
    dlugosc = n_0
    for i in range(ile):
        lista1, lista2 = generator_ciagu.gen(start, koniec_0, dlugosc), generator_ciagu.gen(start, koniec_0, dlugosc)
        czasy1.append(timeit.timeit(lambda: funkcja(lista1, lista2), number=100))
        dlugosc += roznica_dlugosci
    return czasy1


czasy_e3 = stoper(funkcje.example4, 10, 1, 1, 100, 1)
xs = range(1, 11, 1)
plt.plot(xs, czasy_e3, "ro")
plt.xlabel("Długość ciągu")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji example4")
plt.show()
