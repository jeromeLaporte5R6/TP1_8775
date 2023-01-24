
import numpy as np
import os

def load_mat():
    pass

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
    if n == seuil:
        C[0,0] = A[0,0]*B[0,0]
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


if __name__ == '__main__':

    folder = './'

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            if "ex" in filename :
                pass

    A = np.array([[1,8,5,6],[4,2,5,9],[8,2,4,6],[7,2,4,1]])
    B = np.array([[1,2],[3,4]])
    n = int(np.shape(A)[0])
    m = int(n/2)
    C = mat_mul(A,A)
    print(C)
    print(mat_mul_Strassen(A,A))


