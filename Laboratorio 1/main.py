from Trig import * 

PI = Trig()

option = ''

while option != 'salir':
    option = input('\nElija si desea calcular el seno, coseno o tangente de PI (Salir para terminar el programa): ').lower()
    
    if option == 'seno':
        print('\nEl valor de PI es:',PI.valordePI())
        print('El seno de Pi es:',PI.sinPI())
        archivo = PI.createfile('log.txt')
        hora = PI.gettime()
        valor = PI.sinPI()
        archivo.write(f'Hora: {hora}, Valor de seno es: {valor}\n')
        archivo.close()

    elif option == 'coseno':
        print('\nEl valor de PI es:',PI.valordePI())
        print('El coseno de Pi es:',PI.cosPI())
        archivo = PI.createfile('log.txt')
        hora = PI.gettime()
        valor = PI.cosPI()
        archivo.write(f'Hora: {hora}, Valor del coseno es: {valor}\n')
        archivo.close()

    elif option == 'tangente':
        print('\nEl valor de PI es:',PI.valordePI())
        print('El tangente de Pi es:',PI.tanPI())
        archivo = PI.createfile('log.txt')
        hora = PI.gettime()
        valor = PI.tanPI()
        archivo.write(f'Hora: {hora}, Valor de la tangente es: {valor}\n')
        archivo.close()

    elif option == 'salir':
        print('\nSaliendo del programa.')
        break

    else:
        print('Opcion no valida, elija: seno, coceno o tangente.')
