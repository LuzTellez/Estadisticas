def primeraParte():
    from random import randint
    from os.path import exists

    file='./Ficheros/ejercicio01.txt'
    if exists(file):
        return
    #Metodo con list comprehension
    personas = [randint(0,1) for n in range(1,101) ]   
    personas = ["H" if n==1 else "M" for n in personas]
    fichero=open(file,"wt")
    fichero.write(str(personas))
    fichero.close()

    #Método con el bucle for
    personas1=[]
    for n in range(1,101):
        genero=randint(0,1)
        if genero==1:
            personas1.append("H")
        else:
            personas1.append("M")
    file='./Ficheros/ejercicio01a.txt'
    fichero=open(file,"wt")
    fichero.write(str(personas1))
    fichero.close()
    
if __name__ == "__main__":
    primeraParte()

