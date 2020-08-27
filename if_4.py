""" Crear un programa que permita al usuario elegir un candidato por el cual votar. Las
posibilidades son: candidato A por el partido rojo, candidato B por el partido verde,
candidato C por el partido azul. Según el candidato elegido /(A, B ó C) se le debe
imprimir el mensaje “Usted ha votado por el partido [color que corresponda al
candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno
de los candidatos disponibles, indicar “Opción errónea”. """

user_vote = str.upper(input("""Escoja: 
A. Partido rojo\n
B. Partido verde\n
C  Partido azul\n
> """))

def print_election(election):
    print(f'Usted a votado por el partido {election}')


if(user_vote == 'A'):
    print_election('rojo')
elif(user_vote == 'B'):
    print_election('verde')
elif(user_vote == 'C'):
    print_election('azul')
else:
    print('Opción errónea')