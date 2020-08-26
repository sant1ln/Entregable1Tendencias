""" Escriba un programa que pida dos números enteros y escriba la suma de todos los
enteros desde el primer número hasta el segundo. """

start = int(input('Escriba el número inical: '))
end = int(input('Escriba el número final: '))
addr = 0
for i in range(start,end+1):
    addr += i
print(f'La suma entre {start} y {end} es: {addr}')