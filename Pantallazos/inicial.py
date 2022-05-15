def principal():
    sl='\n'
    linea="{}{}".format('='*80,sl)
    print(linea)
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    resultado = input('Selección: (1/2/3/4 - 0 Salir)')
    return resultado

if __name__ == '__main__':
    principal()

