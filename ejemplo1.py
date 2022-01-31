from math import sqrt
import csv

def leeValoraciones(nomFich="u.data" ):
    lineas = [(l.strip()).split("\t")
        for l in (open(nomFich ).readlines ( )) ]
    diccio = { int(l[0]): {} for l in lineas}

    for l in lineas:
        diccio[int(l[0])][int(l[1])] = int(l[2])
    return diccio

def distEuclidea(dic1, dic2):
    # Calcular la suma de cuadrados de los elementos comunes
    # a los dos diccionarios
    suma2 = sum([pow(dic1[elem]-dic2[elem],2)
                 for elem in dic1 if elem in dic2])
    return sqrt (suma2)

def similEuclidea(dic1, dic2):
    return 1/(1+distEuclidea(dic1, dic2))

def coefPearson ( dic1 , dic2 ):
    # Obtener los elementos comunes a los dos diccionarios
    comunes = [x for x in dic1 if x in dic2]
    nComunes = float(len(comunes))

    # Si no hay elementos comunes , se devuelve # se calcula el coeficiente
    if nComunes == 0:
        return 0

    # Calculo de las medias de cada diccionario
    media1 = sum([dic1[x] for x in comunes]) / nComunes
    media2 = sum([dic2[x] for x in comunes]) / nComunes

    # Calculo del numerador y del denominador
    num = sum([(dic1[x]-media1)*(dic2[x]-media2) for x in comunes])
    den1 = sqrt(sum([pow(dic1[x]-media1, 2) for x in comunes]))
    den2 = sqrt(sum([pow(dic2[x]-media2, 2) for x in comunes]))
    den = den1*den2

    # Calculo del coeficiente si es posible , o devuelve 0
    if den == 0:
        return 0

    return num/den

#Codigo principal

valoraciones = {1: {52:3, 590:1, 2020:4, 2414:3, 3210:5},
                2: {47:4, 52:1, 590:3, 2020:5, 4006:2},
                3: {47:2 ,52:1, 1110:5, 4006:1},
                4: {47:3 ,590:2 ,2014:5, 4006:4},
                5: {590:5, 2014:3, 4006:4}}

for elem in range(1,6,1):
    for elem2 in range(1, 6, 1):
        similitud=similEuclidea(valoraciones[elem],valoraciones[elem2])
        print ('la similitud Euclidiana:  ',elem, '   y  ',elem2,'  es  ', similitud)
    print()

for elem in range(1,6,1):
    for elem2 in range(1, 6, 1):
        person=coefPearson(valoraciones[elem],valoraciones[elem2])
        print ('la similitud de Pearson:  ',elem, '   y  ',elem2,'  es  ', person)
    print()

# valoraciones = leeValoraciones()
# for x in valoraciones:
#     print (x,":",valoraciones[x])
#     print ( "  ")


with open('ratings.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    diccio={}
    for row in reader:
        print (row['userId'],row['movieId'],row['rating'])
        if not(diccio.has_key(int(row['userId']))):
            diccio = {int(row['userId']): {}}
        else:
            diccio[int(row['userId'])].update({int(row['movieId']):row['rating']})
    print(diccio)
    print ()
