import sys
from itertools import combinations
import numpy as np
import os
import re
import time
import matplotlib.pyplot as plt
import sys
import timeit
import argparse

def load_mat(file):
    return np.loadtxt(file, skiprows = 1)
def mat_mul(A,B):
    """
    Implémente la multiplication conventionnel
    :param A: matrice A
    :param B: matrice B
    :return: matrice C résultat de la multiplication de A par B
    """
    n = np.shape(A)[0]
    C = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            C[i,j] = sum([A[i,k]*B[k,j] for k in range(n)])
    return C

def mat_mul_Strassen(A,B, seuil = 1):
    """
    Implémente la multiplication de matrice avec l'algo de strassen
    :param A: matrice A
    :param B: matrice B
    :param seuil: seuil de récursivité
    :return: matrice C résultat de la multiplication de A par B
    """
    n = np.shape(A)[0]
    C = np.zeros((n,n))
    if int(np.log(n)) == seuil:
        C = mat_mul(A,B)
    else :
        m = int(n/2)
        A11 = A[:m,:m]
        A12 = A[:m,m:]
        A21 = A[m:,:m]
        A22 = A[m:,m:]
        B11 = B[:m, :m]
        B12 = B[:m, m:]
        B21 = B[m:, :m]
        B22 = B[m:, m:]

        M1 = mat_mul_Strassen(A11 + A22, B11 + B22)
        M2 = mat_mul_Strassen(A21 + A22, B11)
        M3 = mat_mul_Strassen(A11, B12 - B22)
        M4 = mat_mul_Strassen(A22, B21 - B11)
        M5 = mat_mul_Strassen(A11 + A12, B22)
        M6 = mat_mul_Strassen(A21 - A11, B11 + B12)
        M7 = mat_mul_Strassen(A12 - A22, B21 + B22)

        C[:m,:m] = M1 + M4 - M5 + M7 # C11
        C[:m,m:] = M3 + M5
        C[m:,:m] = M2 + M4
        C[m:,m:] = M1 - M2 + M3 + M6
    return C

parser = argparse.ArgumentParser()
parser.add_argument("-a",'--algo', required=True, type=str,
                    help="algorithme choisi")
parser.add_argument("-e1",'--path1', required=True, type=str,
                    help="path vers e1")
parser.add_argument("-e2",'--path2', required=True, type=str,
                    help="path vers e2")
parser.add_argument("-p",action = 'store_true',
                    help="affiche la matrice résultat")
parser.add_argument("-t",action = 'store_true',
                    help="affiche la matrice résultat")
args = parser.parse_args()



algo = args.algo
mat1 = load_mat(args.path1)
mat2 = load_mat(args.path2)
begin_mul = timeit.default_timer()
if algo == 'conv' :
    res = mat_mul(mat1, mat2)
elif algo == 'strassen':
    res = mat_mul_Strassen(mat1,mat2)
elif algo == 'strassenSeuil':
    res = mat_mul_Strassen(mat1,mat2,3)
else :
    print("Wrong argument for -a, please choose between {conv, strassen, strassenSeuil}")
end_mul = timeit.default_timer()
t_mul = end_mul - begin_mul
if args.p:
    for row in res :
        print(" ".join(str(int(x)) for x in row))
if args.t:
    print(t_mul*1000)

