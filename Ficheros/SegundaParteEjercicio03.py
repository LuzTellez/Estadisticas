def SegundaParte():
    file='./Ficheros/ejercicio3.txt'
    fichero = open(file,"rt")
    contenido = fichero.read()
    fichero.close()
    personas=eval(contenido)

    #print(personas)
    lista_edad_hombres = [persona[1] for persona in personas if persona[0]=="H"]
    #print(lista_edad_hombres)
    lista_genero_hombres_mayores_de_edad = [persona[1] for persona in personas if persona[0]=="H" and persona[1]>=18]
    lista_edad_mujeres = [persona[1] for persona in personas if persona[0]=="M"]
    print(f"las mujeres mayores de edad son:{len([edad for edad in lista_edad_mujeres if edad>=18])}")
    print(f"los hombres menores de edad son:{len([edad for edad in lista_edad_hombres if edad<18])}")
    print(f"el hombre con menor edad es:{min(lista_edad_hombres)}")
    print(f"la mujer con menor edad es:{min(lista_edad_mujeres)}")
    print(f"el hombre con mayor edad es:{max(lista_edad_hombres)}")
    print(f"la mujer con mayor edad es:{max(lista_edad_mujeres)}")
    print(f"El promedio de edad de las mujeres es:{sum(lista_edad_mujeres)/len(lista_edad_mujeres):.2f}")
    print(f" y de los hombres:{sum(lista_edad_hombres)/len(lista_edad_hombres):.2f}")

    file='./Ficheros/ejercicio03Resultado.txt'
    fichero = open(file,"wt")
    sl='\n'
    linea="{}{}".format('='*80,sl)
    fichero.write(f"Resultado del ejercicio 03 de colecciones:{sl}")
    fichero.write(linea)
    fichero.write("las mujeres mayores de edad son:{} {}".format(len([edad for edad in lista_edad_mujeres if edad>=18]),sl))
    fichero.write("los hombres menores de edad son:{} {}".format(len([edad for edad in lista_edad_hombres if edad<18]),sl))
    fichero.write("el hombre con menor edad es:{} {}".format(min(lista_edad_hombres),sl))
    fichero.write("la mujer con menor edad es:{} {}".format(min(lista_edad_mujeres),sl))
    fichero.write("el hombre con mayor edad es:{} {}".format(max(lista_edad_hombres),sl))
    fichero.write("la mujer con mayor edad es:{} {}".format(max(lista_edad_mujeres),sl))
    fichero.write("El promedio de edad de las mujeres es:{:.2f}{}".format(sum(lista_edad_mujeres)/len(lista_edad_mujeres),sl))
    fichero.write(" y de los hombres:{:.2f}".format(sum(lista_edad_hombres)/len(lista_edad_hombres),sl))
    fichero.write(f"{sl}{linea}")
    fichero.close()

    
if __name__ == "__main__":
    SegundaParte()
