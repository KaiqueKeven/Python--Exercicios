# escreva um programa que leia um valor em metros e 
# a exiba convertido em centimetros e milimetros
metro = float(input('Digite um valor em metros: '))
centimetros = metro * 100
milimetros = metro * 1000
print(f'O valor {metro}m convertido em centimetros fica {centimetros}cm')
print(f'O valor {metro}m convertido em milimetros fica {milimetros}mm')
