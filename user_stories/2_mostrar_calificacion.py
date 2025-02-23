#Definir funcion para mostrar la calificación del estudiante
def mostrar_calificacion():
    nota_final = float(input("Introduce la nota final del estudiante: "))

    if nota_final < 0 or nota_final > 10:
        print("Número inválido, la nota debe estar entre 0 y 10.")
        return
    if nota_final < 5 :
        calificacion = "SUSPENSO"
    elif 5 <= nota_final < 7 :
        calificacion = "APROBADO"
    elif 7 <= nota_final < 9 :
        calificacion = "NOTABLE"
    else: 
        calificacion = "SOBRESALIENTE"

    print(f"La calificación del estudiante con nota final {nota_final} es: {calificacion}")

mostrar_calificacion()
