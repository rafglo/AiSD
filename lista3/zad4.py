import timeit, random
import matplotlib.pyplot as plt

def multi_append(array1, array2):
    for num in array2:
        array1.append(num)

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

def multi_gen(ile, roznica_dlugosci, n_0):
    result = []
    n = n_0
    for i in range(ile):
        result.append(gen(1,1,n))
        n += roznica_dlugosci
    return result

def stoper1(arrays):
    czasy = []
    def_arr = []
    for array in arrays:
        czasy.append(timeit.timeit(lambda: def_arr.extend(array), number=100))
        def_arr = []
    return czasy

def stoper2(arrays):
    czasy = []
    def_arr = []
    for array in arrays:
        czasy.append(timeit.timeit(lambda: multi_append(def_arr, array), number=100))
        def_arr = []
    return czasy

czasy1 = stoper1(multi_gen(10, 1000, 10))
czasy2 = stoper2(multi_gen(10, 1000, 10))
xs = range(10, 10010, 1000)
plt.plot(xs, czasy1, "ro")
plt.plot(xs, czasy2, "bo")
plt.xlabel("Dlugosc listy")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji extend i multi_append")
plt.show()

