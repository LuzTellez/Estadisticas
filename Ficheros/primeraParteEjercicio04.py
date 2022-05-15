def primeraParte():
    from random import randint
    from os.path import exists
    
    file='./Ficheros/ejercicio03.txt'
    if exists(file):
        return

    ciudades=['Viena','Sofia','Berlín','Nicosia','Copenhague','Bratislava','Madrid','Bruselas','Paris','Oslo']
    ciudade1=['Roma','Dublin','Londres','Lisboa','Budapest','Atenas','Reikiavik','Varsovia','Berna','Bucarest']
    ciudades.extend(ciudade1)
    ciudad_temperatura={}
    for ciudad in ciudades:
        ciudad_temperatura[ciudad]=[randint(-5,43) for i in range(1,13)]
    #ciudad_temperatura={ciudad:[randint(-5,43) for i in range(1,13)] for ciudad in ciudades}    # equivale a las lineas 11,12 y 13
    #print(ciudad_temperatura)

    file='./Ficheros/ejercicio04.txt'
    fichero=open(file,"wt",encoding='UTF-8')
    fichero.write(str(ciudad_temperatura))
    fichero.close()

if __name__ == "__main__":
    primeraParte()
