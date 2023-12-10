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
import time

def stoper(inds, x, arr_len):
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
    time_values = [] 
    arr = [1 for i in range(arr_len)]
    for ind in inds:
        full_time = 0
        for j in range(x):
            start = time.time()
            arr.pop(ind)
            end = time.time()
            full_time += end - start
            arr.append(1)
        time_values.append(full_time / x)
    return time_values, inds

czasy, xs = stoper(range(0, 10**7, 10**6), 100, 10**7)
print(len(czasy))
plt.plot(xs, czasy, "ro")
plt.xlabel("Indeks")
plt.ylabel("Czas wykonania")
plt.title("Eksperymentalna złożoność obliczeniowa funkcji pop")

plt.show()
