""" Requerir al usuario que ingrese un día de la semana e imprimir
 un mensaje si es lunes, otro mensaje diferente si es viernes, 
 otro mensaje diferente si es sábado o domingo.
 Si el día ingresado no es ninguno de esos, imprimir otro mensaje. """

input_day = str.upper(input('Ingrese un día de la semana: '))
if(input_day == 'LUNES'):
    print('Hoy es Lunes, necesitaremos mucho café')
elif(input_day == 'VIERNES'):
    print('Finalmente es Viernes')
elif(input_day == 'SABADO'):
    print('Me Encantan estos Sabados De flojera...')
elif(input_day == 'DOMINGO'):
    print('¿Mañana es festivo?')
else:
    print(f'{input_day.capitalize()}, un día sin igual, y siempre igual')