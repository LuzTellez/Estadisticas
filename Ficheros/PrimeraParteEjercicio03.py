def primeraParte():
    from random import randint
    from os.path import exists
    file='./Ficheros/ejercicio03.txt'
    if exists(file):
        return

    personasIniciales = [(randint(0,1),randint(0,115)) for n in range(1,101) ]
    personas = [(("H" if n[0]==1 else "M"),n[1]) for n in personasIniciales]
    file='./Ficheros/ejercicio3.txt'
    fichero = open(file,"wt")
    fichero.write(str(personas))
    fichero.close()

if __name__ == "__main__":
    primeraParte()    