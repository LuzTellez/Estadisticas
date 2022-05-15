def SegundaParte():
    #SegundaParteEjercicio01.py
    #Lee la información del fichero en disco y la proceso
    file='./Ficheros/ejercicio01.txt'
    fichero=open(file,"rt")
    contenido=fichero.read()
    personas=eval(contenido)
    nohombres=personas.count("H")
    nomujeres=personas.count("M")
    print("El porcentaje de hombres es:{}%".format(nohombres))
    print("El porcentaje de mujeres es:{}%".format(nomujeres))
    if nohombres==nomujeres:
        print("hay igualdad entre hombres y mujeres")
    elif nohombres>nomujeres:
        print("hay mas hombres que mujeres")
    else:
        print("hay mas mujeres que hombres")

    file='./Ficheros/ejercicio01a.txt'
    fichero=open(file,"rt")
    contenido=fichero.read()
    personas=eval(contenido)
    nohombres=personas.count("H")
    nomujeres=personas.count("M")
    print("El porcentaje de hombres es:{}%".format(nohombres))
    print("El porcentaje de mujeres es:{}%".format(nomujeres))
    if nohombres==nomujeres:
        print("hay igualdad entre hombres y mujeres")
    elif nohombres>nomujeres:
        print("hay mas hombres que mujeres")
    else:
        print("hay mas mujeres que hombres")

    file='./Ficheros/ejercicio01Resultado.txt'
    fichero=open(file,"wt")
    sl='\n'
    linea="{}{}".format('='*80,sl)
    fichero.write(f"Resultado del ejercicio 01 de colecciones:{sl}")
    fichero.write(linea)
    fichero.write("El porcentaje de hombres es:{}%{}".format(nohombres,sl))
    fichero.write("El porcentaje de mujeres es:{}%{}".format(nomujeres,sl))
    if nohombres==nomujeres:
        fichero.write(f"hay igualdad entre hombres y mujeres{sl}")
    elif nohombres>nomujeres:
        fichero.write(f"hay mas hombres que mujeres{sl}")
    else:
        fichero.write(f"hay mas mujeres que hombres{sl}")
    fichero.write(linea)
    fichero.close()
    
if __name__ == "__main__":
    SegundaParte()
