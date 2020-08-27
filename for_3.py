""" Escriba un programa que pregunte cuántos números se van a introducir, pida esos
números y escriba cuántos negativos ha introducido. """

max_num = int(input('Ingrese un número: '))
counter = 0
if max_num > 0:
    for i in range(max_num):
        n_number = int(input('Ingrese un número: '))
        if n_number < 0:
            counter += 1
    print(f'Ha ingresado {counter} numeros negativos')
else:
    print('No puede ingresar ni el cero, ni números negativos')
