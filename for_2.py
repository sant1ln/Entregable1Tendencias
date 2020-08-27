""" Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de
veces dada. En cada iteración, solicitar al usuario que ingrese un número. Al finalizar,
mostrar la suma de todos los números ingresados
 """

max_num = int(input('Ingrese el total de numeros a sumar: '))
add = 0
if max_num > 0:
    for i in range(max_num):
        n_number = int(input('Ingrese un número: '))
        add += n_number
    print(f'La suma de los números ingresados es: {add}')
else:
    print('No puede ingresar ni el cero, ni números negativos')
