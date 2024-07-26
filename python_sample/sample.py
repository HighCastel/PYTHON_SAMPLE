def ingresar_puntuacion_comentario():
    while True:
        print('Ingrese una puntuación del 1 al 5:')
        Calificación = input()
        if Calificación.isdecimal():
            Calificación = int(Calificación)
            if 1 <= Calificación <= 5:
                print('Ingrese un comentario:')
                Comentario = input()
                post = f'Calificación: {Calificación} Comentario: {Comentario}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Ingrese un valor valido entre 1 y 5.')
        else:
            print('Ingrese un valor numérico para la puntuación.')

def revisar_resultados():
    print('Resultado de Calificacion:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados:
                print(resultados)
            else:
                print('Aún no se a calificado.')
    except FileNotFoundError:
        print('Aún no se a calificado.')

def main():
    while True:
        print('Seleccione la operación que desea realizar:')
        print('1: Ingresar a calificar y comentar')
        print('2: Revisar resultados')
        print('3: Saliendo')
        numero = input()

        if numero.isdecimal():
            numero = int(numero)
            if numero == 1:
                ingresar_puntuacion_comentario()
            elif numero == 2:
                revisar_resultados()
            elif numero == 3:
                print('Saliendo...')
                break
            else:
                print('Ingrese un valor entre 1 y 3.')
        else:
            print('Ingrese un valor valido entre 1 y 3.')

if __name__ == "__main__":
    main()
