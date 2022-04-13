#SE ASUME QUE LOS NOMBRES LEÍDOS CORRESPONDEN A PERSONAS DISTINTAS

#LECTURA DEL CONTENIDO DE UN ARCHIVO
print("Lectura del contenido de un archivo")
archivo = open ("nombres_1.txt",'r')
print(archivo.read())
archivo.close()
print("FIN DEL PROGRAMA.")
print()
#************************************************
#LECTURA DEL CONTENIDO DE UN ARCHIVO -línea por línea
print("Lectura del contenido de un archivo - línea por línea")
archivo = open ("nombres_1.txt",'r')
cant_lineas = 0
for linea in archivo:
    print(linea)
    cant_lineas = cant_lineas + 1
print(f"La cantidad de líneas que contiene es archivo es: {cant_lineas}.")
archivo.close()
print("FIN DEL PROGRAMA.")
#************************************************
#LECTURA DEL CONTENIDO DE UN ARCHIVO -línea por línea (obtiendo la longitud de cada cadena)
print("Lectura del contenido de un archivo - línea por línea - obteniendo la longitud de cada cadena")
archivo = open ("nombres_1.txt",'r')

for linea in archivo:
    print(len(linea))

archivo.close()
print("FIN DEL PROGRAMA.")
#************************************************
#LECTURA DEL CONTENIDO DE UN ARCHIVO
print("Lectura del contenido de un archivo")
archivo = open ("nombres_1.txt",'r')
nombres = archivo.read().replace("'","").replace(",","").replace(" ","").split("\n")

archivo.close()

nombres = nombres[:len(nombres)-1] #porque me queda el "\n" final
print(nombres)

print(len(nombres))
#Pasar todos los nombres a mayúsculas
for i in range(len(nombres)):
    nombres[i]= nombres[i].upper()
print(nombres)
#**********************************************************************
#generar una lista con las notas de ambas evaluaciones para cada alumno
arch_notas1 = open("eval1.txt") #El modo 'r' viene por defecto
arch_notas2 = open("eval2.txt")
suma_notas = []
notas1 = arch_notas1.read().replace(",","").replace(" ","").split("\n")
notas1 = notas1[:len(notas1)-1]
notas2 = arch_notas2.read().replace(",","").replace(" ","").split("\n")
notas2 = notas2[:len(notas2)-1]

arch_notas1.close()
arch_notas2.close()

print(notas1)
print(notas2)
print()
print(len(notas1))
print(len(notas2))

for i in range(len(notas1)):#elijo cualquiera de los dos porque ambos tienen la misma cantidad de elementos
    suma_notas.append(int(notas1[i]) + int(notas2[i]))

print(suma_notas)
print()
#***************************************************************************
#genero la estructura que contiene la información global de los alumnos
max=len(nombres)
print()
lista_final = []
for i in range(max):
    aux = [nombres[i],suma_notas[i]]
    lista_final.append(aux)
print(lista_final)
print()
#****************************************************************************
total_puntos = 0
for i in range(len(lista_final)):
    total_puntos = total_puntos + lista_final[i][1]
print(f"La cantidad total de puntos de todos los alumnos es: {total_puntos}")
promedio = total_puntos//len(lista_final)
print(f"El promedio de notas del curso es: {promedio}")
print()
#****************************************************************************
#Imprimir los alumnos que se encuentran con notas por debajo del promedio
print(f"Alumnos con notas por debajo del promedio <Nota promedio {promedio}>")
for i in range(len(lista_final)):
    if lista_final[i][1]<promedio:
        print(f"  Alumno nro: {i+1} - Nombre: {lista_final[i][0]} - Nota global: {lista_final[i][1]}")
print()

print("FIN DEL PROGRAMA.")
print()
#************************************************