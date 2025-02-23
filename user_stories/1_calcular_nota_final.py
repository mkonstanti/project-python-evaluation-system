#Definir funcion para calcular la nota final del estudiante
def calcular_nota_final(): 
    nombre = input("Introduce tu nombre: ")
    suma = 0
    for i in range(3): 
        nota = float(input(f"Introduce la nota número {i+1} : "))
        suma += nota
    media_nota = suma / 3
    nombre_mayuscula = nombre.upper()
    #Mostrar la media nota en la consola
    print(f"{nombre_mayuscula} tu nota final es {media_nota:.2f}")

#Llamamos la función
calcular_nota_final()
