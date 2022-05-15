def primeraParte():
    from random import randint
    from os.path import exists

    file='./Ficheros/ejercicio02.txt'
    if exists(file):
        return
    personas=[randint(0,123) for n in range(1,101)]    
    file="./Ficheros/ejercicio02.txt"
    fichero = open(file,"wt")
    fichero.write(str(personas))
    fichero.close()

    personas=[]
    for n in range(1,101):
        personas.append(randint(0,123))
    file="./Ficheros/ejercicio02a.txt"
    fichero = open(file,"wt")
    fichero.write(str(personas))
    fichero.close()

if __name__ == "__main__":
    primeraParte()