""" Solicitar al usuario un número de cliente. 
Si el número es el 1000, imprimir "Ganaste
un premio"  """

user_number = int(input('Ingrese su número de usuario: '))
winner_number = 1000

if(user_number == winner_number):
    print('Ganaste un premio')
else:
    print('Sigue intentando...')   

