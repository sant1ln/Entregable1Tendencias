"""Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números negativos ingresados. """

#Nota: Como el ejercicio estaba repetido, supuse que era la suma de negativos.

number = int(input("Ingrese un número: "))
sumator = 0
while(number!=0):
    if number < 0:
        sumator = sumator + number
    number = int(input("Ingrese otro número: "))
if(sumator != 0):
    print(f'La sumatoria de los negativos es: {sumator}')
