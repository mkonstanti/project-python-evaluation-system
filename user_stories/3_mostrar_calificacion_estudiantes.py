#Definir función para calcular la nota final del estudiante y su calificación
def calcular_nota_final_y_calificacion(cantidad_notas): 
    nombre = input("Introduce el nombre del estudiante: ")
    suma = 0
    for i in range(cantidad_notas): 
        nota = float(input(f"Introduce la nota número {i+1} : "))
        if nota <= 0 or nota > 10:
            print("Número inválido, la nota debe estar entre 0 y 10.")
            return
        suma += nota
    nota_final = suma / cantidad_notas
    nombre_mayuscula = nombre.upper()

    print(f"La nota final de {nombre_mayuscula} es {nota_final:.2f}")
    if nota_final < 5 :
        calificacion = "SUSPENSO"
    elif 5 <= nota_final < 7 :
        calificacion = "APROBADO"
    elif 7 <= nota_final < 9 :
        calificacion = "NOTABLE"
    else: 
        calificacion = "SOBRESALIENTE"

    print(f"Su calificación es: {calificacion}")


#Definir funcion para calcular la nota final de cada estudiante
def mostrar_calificacion_estudiantes(numero_estudiantes, cantidad_notas): 
    for i in range(numero_estudiantes):
            print(f"\n Estudiante {i+1}:")
            calcular_nota_final_y_calificacion(cantidad_notas)


mostrar_calificacion_estudiantes(5,3)
    

