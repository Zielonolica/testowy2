macierz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def pokazMacierz():
    for i in range(len(macierz)):
        print('\n')
        for j in range(len(macierz[i])):
            macierz[i][j] = i * j
            print(macierz[i][j], end = ' ')
#pokazMacierz()