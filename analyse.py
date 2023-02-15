import matplotlib.pyplot as plt
import numpy as np
def main():
    Strassen = [1.6450881958007812e-05,0.0001371145248413086,0.0009649991989135742,0.006725311279296875,0.04689393043518066,0.329443097114563,2.314519476890564,16.254245281219482,114.21375489234924,794.9579849243164]
    # Strassen = [4.122257232666016e-05, 0.00028395652770996094, 0.0019381523132324218,0.013549137115478515,0.09511361122131348,0.6795965909957886, 4.744695520401001, 32.60858302116394,224.98111987113953, 1635.810642004013]
    StrassenSeuil = [0.017222476005554,0.12352747917175293, 0.8383497714996337, 5.8706234216690065]
    Conv = [1.2326240539550782e-05, 5.3501129150390626e-05,0.00033326148986816405 ,0.0023606061935424806,0.01736428737640381, 0.13493261337280274,1.0698513746261598,8.351716041564941,69.3525288105011,560.8297510147095]
    X =[2**1,2**2,2**3,2**4,2**5,2**6,2**7,2**8,2**9,2**10]
    Xseuil = [2**5,2**6,2**7,2**8]
    #test_puissance(X,Conv, Strassen)

    #test_rapport(X,Conv, Strassen, 2.9804685257856955, 2.8099104555936734)
    #test_constante(X,Conv, Strassen, 2.9804685257856955, 2.8099104555936734)
    #test_puissance_Seuil(Xseuil,StrassenSeuil)
    #test_rapport_Seuil(Xseuil, StrassenSeuil, 2.8)
    test_constante_Seuil(Xseuil, StrassenSeuil, 2.8)
def test_puissance(X,Conv,Strassen):
    logConv = np.log(Conv)
    logStrassen = np.log(Strassen)
    logX = np.log(X)
    mC,bC = np.polyfit(logX[3:],logConv[3:],1)
    mS, bS = np.polyfit(logX[3:],logStrassen[3:],1)
    print("parameter for Conv m = ", str(mC), " b =",str(bC))
    print("parameter for Strassen m = ", str(mS), " b =",str(bS))

    plt.plot(logX,logStrassen, label = "Strassen")
    plt.plot(logX,logConv, label = "Conventionnel")
    # plt.xscale("log")
    # plt.yscale("log")
    plt.legend()
    plt.show()

def test_puissance_Seuil(X,StrassenS):

    logStrassen = np.log(StrassenS)
    logX = np.log(X)
    mS, bS = np.polyfit(logX,logStrassen,1)
    print("parameter for Strassen m = ", str(mS), " b =",str(bS))

    plt.plot(logX,logStrassen, label = "Strassen avec seuil")
    # plt.xscale("log")
    # plt.yscale("log")
    plt.legend()
    plt.show()
def test_rapport(X, Conv, Strassen, mC, mS):
    fC = f(X, mC)
    fS = f(X, mS)
    rapportC = [Conv[i]/fC[i] for i in range(len(Conv))]
    rapportS = [Strassen[i]/fS[i] for i in range(len(Strassen))]
    plt.plot(X,rapportS, label="Strassen")
    plt.plot(X,rapportC, label = "Conventionnel")
    plt.legend()
    plt.show()
def test_rapport_Seuil(X, Strassen, mS):
    fS = f(X, mS)
    rapportS = [Strassen[i]/fS[i] for i in range(len(Strassen))]
    plt.plot(X,rapportS, label="Strassen avec seuil")
    plt.legend()
    plt.ylim(0,0.00001)
    plt.show()
def test_constante(X,Conv, Strassen ,mC, mS):
    fC = f(X, mC)
    fS = f(X, mS)
    C, bC = np.polyfit(fC, Conv, 1)
    S, bS = np.polyfit(fS, Strassen, 1)
    print("parameter for Conv m = ", str(C), " b =", str(bC))
    print("parameter for Strassen m = ", str(S), " b =", str(bS))
    plt.plot(fS, Strassen, label="Strassen")
    plt.plot(fC,Conv, label="Conventionnel")
    plt.legend()


    plt.show()

def test_constante_Seuil(X, Strassen, mS):
    fS = f(X, mS)
    S, bS = np.polyfit(fS, Strassen, 1)
    print("parameter for Strassen m = ", str(S), " b =", str(bS))
    plt.plot(fS, Strassen, label="Strassen avec seuil")
    plt.legend()
    plt.show()
def f(X, n):
    return [i**n for i in X]

if __name__ == '__main__':
    main()