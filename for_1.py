"""  Requerir al usuario que ingrese un número entero positivo
e imprimir todos los números correlativos entre el ingresado 
por el usuario y uno menos del doble del
mismo. """

# Si ingreso 5, *2 = 10 - 1 = 9

user_input = int(input('Ingrese un número entero positivo: '))
iterator = (user_input * 2)-1
if user_input > 0:
    for i in range(1,iterator+1):
        print(i)
else:
    print('Error, Ingreso un numero impar')