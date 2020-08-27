"""Solicitar al usuario que ingrese dos números y 
mostrar cuál de los dos es menor.
No considerar el caso en que ambos números son iguales."""

number1 = int(input('Ingrese el primer número: '))
number2 = int(input('Ingrese el segundo número: '))

if(number1 < number2):
    print(f'El número {str(number1)} es menor que el número {str(number2)} ')
else:
    print(f'El número {str(number2)} es menor que el número {str(number1)} ')