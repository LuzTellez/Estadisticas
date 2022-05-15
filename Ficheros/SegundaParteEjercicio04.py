def SegundaParte():
    file='./Ficheros/ejercicio04.txt'
    fichero=open(file,"rt",encoding='UTF-8')
    contenido=fichero.read()
    fichero.close()
    ciudad_temperatura=eval(contenido)

    ciudad_promedios = { ciudad: sum(grados)/len(grados) for ciudad,grados in ciudad_temperatura.items() }
    mas_alta = max(ciudad_promedios,key=ciudad_promedios.get)
    mas_baja = min(ciudad_promedios,key=ciudad_promedios.get)
    print("La ciudad con promedio anual de temperatura mas alta es:",mas_alta,"<->{:1.2f} ºC".format(ciudad_promedios[mas_alta]))
    print("La ciudad con promedio anual de temperatura mas baja es:",mas_baja,"<->{:1.2f} ºC".format(ciudad_promedios[mas_baja]))
    promedios_ordenados = sorted(ciudad_promedios,key=ciudad_promedios.get,reverse=True)
    for ciudad in promedios_ordenados:
        print(ciudad,",","{:1.2f} ºC".format(float(ciudad_promedios[ciudad])))

    file='./Ficheros/ejercicio04Resultado.txt'
    fichero = open(file,"wt",encoding='UTF-8')
    sl='\n'
    linea="{}{}".format('='*80,sl)
    fichero.write(f"Resultado del ejercicio 04 de colecciones:{sl}")
    fichero.write(linea)
    fichero.write("La ciudad con promedio anual de temperatura mas alta es:{} {:1.2f} ºC{}".format(mas_alta,ciudad_promedios[mas_alta],sl))
    fichero.write("La ciudad con promedio anual de temperatura mas baja es:{} {:1.2f} ºC{}".format(mas_baja,ciudad_promedios[mas_baja],sl))
    columna=1
    fichero.write(f"{sl}La temperatura por ciudadess es el siguiente:{sl}")
    for ciudad in promedios_ordenados:
        fichero.write("\t{:12}{:1.2f} ºC{}".format(ciudad,float(ciudad_promedios[ciudad]),sl if columna%3 == 0 else '\t'))
        columna+=1
    fichero.write(f"{sl}{linea}")
    fichero.close()

    
if __name__ == "__main__":
    SegundaParte()

