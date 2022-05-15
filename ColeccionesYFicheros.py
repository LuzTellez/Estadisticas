from operator import imod
import os

# from Ficheros.PrimeraParteEjercicio01 import primeraParte as primeraParte01
# from Ficheros.PrimeraParteEjercicio02 import primeraParte as primeraParte02
# from Ficheros.PrimeraParteEjercicio03 import primeraParte as primeraParte03
# from Ficheros.primeraParteEjercicio04 import primeraParte as primeraParte04

# from Ficheros.SegundaParteEjercicio01 import SegundaParte as segundaParte01
# from Ficheros.SegundaParteEjercicio02 import SegundaParte as segundaParte02
# from Ficheros.SegundaParteEjercicio03 import SegundaParte as segundaParte03
# from Ficheros.SegundaParteEjercicio04 import SegundaParte as segundaParte04
from Ficheros import primeraParte01,segundaParte01,primeraParte02,segundaParte02
from Ficheros import primeraParte03,segundaParte03,primeraParte04,segundaParte04

from Pantallazos.inicial import principal

def primera():
    os.system('cls')
    print('Datos del genero de 100 hombres y mujeres:')
    primeraParte01()
    segundaParte01()
    respuesta = input('\nEnter para continuar...')

def segunda():
    os.system('cls')
    print('Datos de las edades de 100 personas:')
    primeraParte02()
    segundaParte02()
    respuesta = input('\nEnter para continuar...')

def tercera():
    os.system('cls')
    print('Datos de las edades de 100 personas por género:')
    primeraParte03()
    segundaParte03()
    respuesta = input('\nEnter para continuar...')

def cuarta():
    os.system('cls')
    print('Datos de temperaturas anuales de 12 ciudades:')
    primeraParte04()
    segundaParte04()
    respuesta = input('Enter para continuar...')

def main():
    while True:
        os.system('cls') # Limpiar pantalla
        respuesta=principal()
        if "1" in respuesta:
            primera()
        elif "2" in respuesta:
            segunda()
        elif "3" in respuesta:
            tercera()
        elif "4" in respuesta:
            cuarta()
        elif "0" in respuesta:
            print("Gracias por utilizar nuestra aplicación")
            break
        else:
            print("Invalid option, try again")

if __name__ == "__main__":
    main()

