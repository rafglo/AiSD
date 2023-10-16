def wielomian1(wspolczynniki, x):
    """
    Function
    Funkcja obliczająca wartość wielomianu w punkcie

    Input
    wspolczynniki(list) - lista wspołczynników posortowanych rozpoczynając od wyrazu wolnego
    x(float) - punkt, w którym chcemy obliczyć wartość wielomianu

    Output
    suma(float) - wartość wielomianu w punkcie

    """
    n = len(wspolczynniki)
    suma = 0
    for i in range(n): #idziemy po koljenych współczynnikach
        xn = 1
        for j in range(i): #potęgowanie x-a
            xn *= x
        suma += wspolczynniki[i] * xn #dodawanie potęgi x-a pomnożonej przez współczynnik
    return suma
print(wielomian1([1,2,3],5))

def wielomian2(wspolczynniki, x):
    n = len(wspolczynniki)
    suma = 0
    for i in range(n):
        suma += wspolczynniki[i] * x**i
    return suma
print(wielomian2([1,2,3],5))


