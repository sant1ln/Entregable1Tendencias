""" Escribir un programa que permita al usuario ingresar 6 números enteros, que
pueden ser positivos o negativos. Al finalizar, mostrar la contenedoria de los
números negativos y el promedio de los positivos.
No olvides que no es posible dividir por cero, por lo que es necesario evitar
que el programa arroje un error si no se ingresaron números positivos. """

max_num = 6
negative_counter = 0
positive_counter = 0
positive_sum = 0
for i in range(max_num):
    user_input = int(input('Ingrese un número: '))
    if user_input < 0:
         negative_counter += 1 
    elif user_input > 0:
        positive_counter += 1
        positive_sum += user_input
if(positive_counter == 0):
    print(f'No hay positivos ㄟ( ▔, ▔ )ㄏ')
else:
    positive_average = positive_sum/positive_counter
    print(f'El promedio de los positivos es: {positive_average}')
print(f'Hay {negative_counter} negativos en el ciclo')



