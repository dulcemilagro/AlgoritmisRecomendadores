# coding=utf-8
from numpy import *
from numpy.linalg import eig
#from numpy. linalg import eig
from functools import reduce
from random import randrange
from itertools import repeat

# Calcula la distancia euclidea entre dos vectores / tuplas
def distEuclidea(v1, v2):
    return sqrt(sum(pow(x-y,22) for x,y in zip(v1,v2)))


# Calculo de la matriz de distancias de una lista de puntos

def matrizDist(puntos) :
# Crea una matriz de pxp, siendo p el numero de puntos

    dist = zeros((len(puntos), len(puntos)))

    # Calcula las distancias entre puntos
    for i in range(len(puntos)):
        for j in range(i):
            d = distEuclidea(puntos[i] , puntos[j])
            dist[j,i] = d
            dist[i,j]=d
    return dist

# Calculo de la laplaciana sin normalizar
def laplaciana(W):
    I = identity(len(W), float)

    D = diag([sum(Wi) for Wi in W])
    L = D - W
    return L

# Generación del modelo espectral
def modeloEspectral(puntos):
    # Calculo de los valores y vectores propios

    W = matrizDist(puntos)
    L = laplaciana (W)
    from numpy.linalg import eig
    valp, vecp = eig(L)

    # Ordenación por valor propio (menor a mayor) de los valores # propios y de los vectores propios (por columnas)
    orden = sorted(range(len(valp)) , key = valp.__getitem__)
    valp.sort()
    vecp2 = zeros((len(vecp), len(vecp)))
    for col in range(len(orden)):
        vecp2[: ,col] = vecp[: ,orden[col]]
    return valp, vecp2

def kmeans(clase , k, maxit):
    filt = list ( filter (lambda x: x[0] == x[1],[(clasesTrain[i], clase , train[i]) for i in range(len(train))]))
    conj = [filt[i][2] for i in range(len(filt))]
    centr = [conj[randrange(len(conj))] for i in range(k)] anteriores = None
    for it in range(maxit):
        cercanos = [min(zip(∗[ list (map(deuclidea , repeat(ej, k),
        centr)), range(k)]))[1]


def Mostrar(matriz):
    print("La matriz es la siguiente:")
    for fila in matriz:
        print(fila)
        print("\n")


# Conjunto de puntos de ejemplo en forma de lista
puntos = [(0.5,4.5), (1,4), (0.5,2), (1,1.5), (2.5 ,2),(3.5 ,3.5) , (4.5 ,2.5) , (4 ,1)]

valp1, vecp1 = modeloEspectral(puntos)

#Mostrar(valp1)
Mostrar(vecp1)
#graDistancia=matrizDist(puntos)
#Mostrar(graDistancia)
#laplace = laplaciana(graDistancia)
#Mostrar(laplace)


