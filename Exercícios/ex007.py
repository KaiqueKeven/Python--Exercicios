#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma área de 2m² 
largura = float(input('Digite a largura (m): '))
altura = float(input('Digite a altura (m): '))
area = largura * altura
tinta = area / 2
print(f'A sua dimenção e {largura}x{altura} e sua área {area:.2f}m²')
print(f'E necessario {tinta:.2f}L de tinta para pinta a parede')
