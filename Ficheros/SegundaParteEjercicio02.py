def SegundaParte():
    file="./Ficheros/ejercicio02.txt"
    fichero = open(file,"rt")
    contenido = fichero.read()
    fichero.close()
    personas = eval(contenido)

    masdiezyocho1=len([n for n in personas if n>=18])
    print("El número de personas mayores de 18 años es:",masdiezyocho1)
    print("la persona con menor edad:",min(personas))
    print("la persona con mayor edad:",max(personas))
    print("El promedio de edad es:{:1.2f}".format(sum(personas)/100))
    personas.sort()
    #clasificacionEdades=dict((edad,0) for edad in personas) #ESTO ES VALIDO
    clasificacionEdades={edad:0 for edad in personas}
    for n in personas:
        clasificacionEdades[n]+=1
    #print(clasificacionEdades)
    for edad in clasificacionEdades:
        print('{:3} ->{:3.2f}%'.format(edad,clasificacionEdades[edad]),end='\t')
    file='./Ficheros/ejercicio02Resultado.txt'
    fichero = open(file,"wt",encoding='UTF-8')
    sl='\n'
    linea="{}{}".format('='*80,sl)
    fichero.write(f"Resultado del ejercicio 02 de colecciones:{sl}")
    fichero.write(linea)
    fichero.write("El número de personas mayores de 18 años es:{}{}".format(masdiezyocho1,sl))
    fichero.write("la persona con menor edad:{} {}".format(min(personas),sl))
    fichero.write("la persona con mayor edad:{} {}".format(max(personas),sl))
    fichero.write("El promedio de edad es:{:1.2f}{}".format(sum(personas)/100,sl))
    columna=1
    fichero.write(f"{sl}El porcentaje por edades es el siguiente:{sl}")
    for edad in clasificacionEdades:
        fichero.write('\t\t{:3} {:3.2f}%{}'.format(edad,clasificacionEdades[edad],'\n' if columna%4 ==0 else '\t'))
        columna+=1
    fichero.write("{}{}".format(sl,linea))
    fichero.close()

    
if __name__ == "__main__":
    SegundaParte()
