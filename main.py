import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint
from GeometriaDefinicja import GeometriaDefinicja
from AutomatycznyGeneratorGeometrii import AutomatycznyGeneratorGeometrii
from RysujGeometrie import RysujGeometrie
from Alokacja import Alokacja
from FunkcjeBazowe import FunkcjeBazowe
from Aij import Aij





if __name__ == '__main__':
    
    #Preprocesing
    
    
    
    #Parametry sterujace
    c=0;
    f=lambda x: 1 #Wymuszenie
    
    #Geomatria - Definicja
    WEZLY,ELEMENTY,WB = GeometriaDefinicja()
    n = np.shape(WEZLY)[0]
    
    
    # #Automatyczne wygenerowanie geometrii
    
    # x_a=0
    # x_b=1
    # n=5
    
    
    # WEZLY, ELEMENTY = AutomatycznyGeneratorGeometrii(x_a, x_b, n)
    
    
    # #Warunki brzegowe
    # WB = [{"Index": 1, "TYP":'D', "Wartosc":0},
    #      {"Index": n, "TYP":'D', "Wartosc":1},]
    
    RysujGeometrie(WEZLY,ELEMENTY,WB)
    
    print(WEZLY)
    
    
    
    
    
    #Processing
    
    [A,b]= Alokacja(n)
    stop_funkcji = 1
    phi, dphi = FunkcjeBazowe(stop_funkcji)
    
    # x2 = np.linspace(-1,1,101)
    # plt.plot(x2, phi[0](x2),'r')
    # plt.plot(x2, phi[1](x2),'g')
    # plt.plot(x2, dphi[0](x2),'b')
    # plt.plot(x2, dphi[1](x2),'y')

    
    
    
    #PROCESSING
    
    for k in np.arange(0,np.shape(ELEMENTY)[0]):
        
        elemIndRow = k
        elemGlobalInd = ELEMENTY[k,0]
        elemWezel1= ELEMENTY[k,1]
        elemWezel2 = ELEMENTY[k,2]
        
        x_a=WEZLY[elemWezel1-1,1]
        x_b=WEZLY[elemWezel2-1,1]
        
        temp = np.zeros([stop_funkcji+1, stop_funkcji+1])

        J = (x_b-x_a)/2
        
        n=0; m=0;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)
        n=0; m=1;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)
        n=1; m=0;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)
        n=1; m=1;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)


        
        



















# import numpy as np
# import matplotlib.pyplot as plt
# def generator(xstart,xstop,n):

#     val = (xstop-xstart)/(n-1)
#     wezly = np.array([xstart])

#     for i in range(1,n,1):
#         wezly = np.block([wezly, i * val + xstart])

#     elementy = np.zeros((n-1,2))

#     for i in range(0, n-1, 1):
#         elementy[i][0] = i+1
#         elementy[i][1] = i+2

#     return wezly,elementy

# def plot_g(wezly,elementy, n):
#     tab=np.zeros((n))
#     l1 = plt.plot(wezly,tab)
#     for i in range(0,n-1,1):
#         plt.text(wezly[i], 0, "|")
#         plt.text(wezly[i+1]/2+wezly[i]/2, 0.003 ,str(i+1))
#         plt.text(wezly[i], -0.02, str(i+1))

# wezly, elementy = generator(0,1,4)
# plot_g(wezly, elementy, len(wezly))






