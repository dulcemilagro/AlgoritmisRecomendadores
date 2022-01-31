import csv

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



