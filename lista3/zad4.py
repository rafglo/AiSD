import timeit, random
import matplotlib.pyplot as plt
import time

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
"""
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
"""

def stoper(arrays, x):
    czasy_extend = []
    czasy_multi_append = []
    default_array = []
    for array in arrays:
        full_time_extend = 0
        full_time_multi_append = 0
        for i in range(x):
            start_extend = time.time()
            default_array.extend(array)
            end_extend = time.time()
            default_array = []
            start_multi_append = time.time()
            multi_append(default_array, array)
            end_multi_array = time.time()
            default_array = []
            full_time_extend += end_extend - start_extend
            full_time_multi_append += end_multi_array - start_multi_append
        czasy_extend.append(full_time_extend/x)
        czasy_multi_append.append(full_time_multi_append/x)
    return czasy_extend, czasy_multi_append
        


"""czasy1 = stoper1(multi_gen(10, 1000, 10))
czasy2 = stoper2(multi_gen(10, 1000, 10))"""

czasy_extend, czasy_multi_append = stoper(multi_gen(10, 10000, 100), 100)
xs = range(10, 100000, 10000)
plt.plot(xs, czasy_extend, "ro")
plt.plot(xs, czasy_multi_append, "bo")
plt.xlabel("Dlugosc listy")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji extend i multi_append")
plt.show()

