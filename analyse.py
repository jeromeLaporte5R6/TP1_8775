import matplotlib.pyplot as plt
import numpy as np
def main():
    Strassen = [4.122257232666016e-05, 0.00028395652770996094, 0.0019381523132324218,0.013549137115478515,0.09511361122131348,0.6795965909957886, 4.744695520401001, 32.60858302116394,224.98111987113953, 1635.810642004013, 6470.8585]
    Conv = [1.4591217041015626e-05, 5.5694580078125e-05,0.0003448486328125 ,0.002523493766784668,0.018650126457214356, 0.1438572883605957,1.1203683137893676,8.847075080871582, 73.87312293052673,580.3827638626099,4987.982868909]
    X =[2**1,2**2,2**3,2**4,2**5,2**6,2**7,2**8,2**9,2**10,2**11]
    #test_puissance(X,Conv, Strassen)
    #test_rapport(X,Conv, Strassen, 2.9883798322794908, 2.74168263855981)
    test_constante(X,Conv, Strassen, 2.9883798322794908, 2.74168263855981)
def test_puissance(X,Conv,Strassen):
    logConv = np.log(Conv)
    logStrassen = np.log(Strassen)
    logX = np.log(X)
    mC,bC = np.polyfit(logX,logConv,1)
    mS, bS = np.polyfit(logX,logStrassen,1)
    print("parameter for Conv m = ", str(mC), " b =",str(bC))
    print("parameter for Strassen m = ", str(mS), " b =",str(bS))

    plt.plot(logX,logStrassen)
    plt.plot(logX,logConv)
    # plt.xscale("log")
    # plt.yscale("log")
    plt.show()

def test_rapport(X, Conv, Strassen, mC, mS):
    fC = f(X, mC)
    fS = f(X, mS)
    rapportC = [fC[i]/Conv[i] for i in range(len(Conv))]
    rapportS = [fS[i]/Strassen[i] for i in range(len(Strassen))]
    plt.plot(X,rapportS)
    plt.plot(X,rapportC)
    plt.show()

def test_constante(X,Conv, Strassen ,mC, mS):

    yC = [x**mC for x in X]
    yS = [x**mS for x in X]

    C, bC = np.polyfit(Conv, yC, 1)
    mS, bS = np.polyfit(Strassen, yS, 1)
    print("parameter for Conv m = ", str(mC), " b =", str(bC))
    print("parameter for Strassen m = ", str(mS), " b =", str(bS))

    plt.plot(Conv, yC)
    plt.plot(Strassen, yS)


    plt.show()
def f(X, n):
    return [i**n for i in X]

if __name__ == '__main__':
    main()