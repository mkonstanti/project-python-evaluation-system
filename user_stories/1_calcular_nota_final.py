#Definir funcion para calcular la nota final del estudiante
def calcular_nota_final(cantidad_notas): 
    nombre = input("Introduce el nombre del estudiante: ")
    suma = 0
    for i in range(cantidad_notas): 
        nota = float(input(f"Introduce la nota número {i+1} : "))
        if nota < 0 or nota > 10:
                print("Número inválido, la nota debe estar entre 0 y 10.")
                return
        suma += nota
    nota_final = suma / cantidad_notas
    nombre_mayuscula = nombre.upper()
    #Mostrar la media nota en la consola
    print(f"La nota final de {nombre_mayuscula} es {nota_final:.2f}")

#Llamamos la función para calcular la media nota de 3 notas en total
calcular_nota_final(3)
