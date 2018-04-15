macierz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def pokazMacierz():
    for i in range(len(macierz)):
        print('\n')
        for j in range(len(macierz[i])):
            macierz[i][j] = i * j
            print(macierz[i][j], end = ' ')
#pokazMacierz()

def dodawanie(x, y):
    print(x + y)

def odejmowanie(x, y):
    roznica = x - y
    return roznica

def mnozenie(x, y):
    iloczyn = x * y
    return iloczyn

def dzielenie(x, y):
    iloraz = x / y
    return iloraz

dodawanie(5, 4)
print(odejmowanie(7, 5))
print(mnozenie(3, 5))
print(dzielenie(6, 2))