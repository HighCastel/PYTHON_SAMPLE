while True:
    print("Ingrese su calificación en una escala del 1 al 5. Ingrese "6" para salir")
    calificación = input()
    if calificación.isdecimal():
        calificación = int(calificación)
        if calificación == 6:
            print("salir")
            break
        elif 1 <= calificación <= 5:
            print("Por favor escriba un comentario")
            comentario = input()
            print(f"Su calificación: {calificación}")
            print(f"Su comentario: {comentario}")
    else:
        print("Por favor introcuzca un número")