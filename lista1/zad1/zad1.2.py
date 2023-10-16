def wielomian3(wspolczynniki, x):
    """
    Function 
    Funkcja wykorzystująca algorytm divide and conquer do obliczenia wartości wielomianu w punkcie.
    Wykorzystana została tu rekurencja, której głębokość wynosi logn.
    W każdym wywołaniu funkcji wykonujemy n/2 mnożeń.
    Co w konsekwencji daje nam złożoność O(n) * O(logn) = O(nlogn)

    Input
    wspolczynniki(list) - lista wspołczynników posortowanych rozpoczynając od wyrazu wolnego
    x(float) - punkt, w którym chcemy obliczyć wartość wielomianu

    Output
    suma(float) - wartość wielomianu w punkcie
    """
    n = len(wspolczynniki)
    while n > 1:
        srodek = n // 2

        wsp_lewo = wspolczynniki[:srodek]
        wsp_prawo = wspolczynniki[srodek:]

        wart_lewo = wielomian3(wsp_lewo, x)
        wart_prawo = wielomian3(wsp_prawo, x)

        x_n = x ** (srodek)
        wynik = wart_lewo + wart_prawo * x_n
        
        return wynik
    return wspolczynniki[0]
print(wielomian3([1,2,3], 5))
