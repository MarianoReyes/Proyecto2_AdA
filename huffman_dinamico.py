import numpy as np


def Huffman_DP(simbolos, frecuencias):
    n = len(simbolos)
    tabla = np.inf * np.ones((n + 1, n + 1))

    for i in range(n):
        tabla[i][i] = frecuencias[i]

    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            tabla[i][j] = np.inf

            for k in range(i, j):
                costo = tabla[i][k] + tabla[k + 1][j]
                if costo < tabla[i][j]:
                    tabla[i][j] = costo

            for k in range(i, j + 1):
                tabla[i][j] += frecuencias[k]

    return tabla[0][n - 1]


simbolos = ["a", "b", "c", "d", "e", "f"]
frecuencias = [5, 9, 12, 13, 16, 45]

print(Huffman_DP(simbolos, frecuencias))
