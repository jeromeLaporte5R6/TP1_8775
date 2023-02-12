from itertools import combinations
import numpy as np
import os
import re
import time
import matplotlib.pyplot as plt


def load_mat(file):
    return np.loadtxt(file, skiprows=1)


def mat_mul(A, B):
    """
    Implémente la multiplication conventionnel
    :param A: matrice A
    :param B: matrice B
    :return: matrice C résultat de la multiplication de A par B
    """
    n = np.shape(A)[0]
    C = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            C[i, j] = sum([A[i, k] * B[k, j] for k in range(n)])
    return C


def mat_mul_Strassen(A, B, seuil):
    """
    Implémente la multiplication de matrice avec l'algo de strassen
    :param A: matrice A
    :param B: matrice B
    :param seuil: seuil de récursivité
    :return: matrice C résultat de la multiplication de A par B
    """
    n = np.shape(A)[0]
    C = np.zeros((n, n))
    if int(np.log2(n)) <= seuil:
        C = mat_mul(A, B)
    else:
        m = int(n / 2)
        A11 = A[:m, :m]
        A12 = A[:m, m:]
        A21 = A[m:, :m]
        A22 = A[m:, m:]
        B11 = B[:m, :m]
        B12 = B[:m, m:]
        B21 = B[m:, :m]
        B22 = B[m:, m:]

        M1 = mat_mul_Strassen(A11 + A22, B11 + B22, seuil)
        M2 = mat_mul_Strassen(A21 + A22, B11, seuil)
        M3 = mat_mul_Strassen(A11, B12 - B22, seuil)
        M4 = mat_mul_Strassen(A22, B21 - B11, seuil)
        M5 = mat_mul_Strassen(A11 + A12, B22, seuil)
        M6 = mat_mul_Strassen(A21 - A11, B11 + B12, seuil)
        M7 = mat_mul_Strassen(A12 - A22, B21 + B22, seuil)

        C[:m, :m] = M1 + M4 - M5 + M7  # C11
        C[:m, m:] = M3 + M5
        C[m:, :m] = M2 + M4
        C[m:, m:] = M1 - M2 + M3 + M6
    return C


if __name__ == '__main__':
    folder = './'
    dico_matrice = {}  # dictionnaire des différents chemins des fichiers en fonction de la taille de la matrice contenue
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if 'ex' in filename:
            filepath = os.path.join(folder, filename)
            match = re.search(r'\d+', filename)
            nb = int(match.group())
            dico_matrice.setdefault(nb, []).append(filename)
    for seuil in range(1,8):
        Taille = []
        Time_Strassen = []
        for key, value in dico_matrice.items():  # Pour chaque taille de matrice, on fait la moyenne du temps de calcul sur toutes les combinaisons
            combinations_list = list(combinations(value, 2))  # liste des combinaisons de 2 matrices
            Taille.append(key)
            t_strassen = []
            for c in combinations_list:
                A = load_mat(c[0])
                B = load_mat(c[1])

                begin_strassen = time.time()
                res = mat_mul_Strassen(A, B, seuil)
                end_strassen = time.time()
                t_strassen.append(end_strassen - begin_strassen)
            Time_Strassen.append(sum(t_strassen) / len(t_strassen))
        print("Seuil : ", seuil)
        print(Taille)
        print(Time_Strassen)
        print("\n")

    # A = np.array([[1,8,5,6],[4,2,5,9],[8,2,4,6],[7,2,4,1]])
    # B = np.array([[1,2],[3,4]])
    # n = int(np.shape(A)[0])
    # m = int(n/2)
    # C = mat_mul(A,A)
    # print(C)
    # print(mat_mul_Strassen(A,A))
    #

