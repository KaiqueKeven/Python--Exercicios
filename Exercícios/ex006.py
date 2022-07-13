# crie um programa que leia quantos dinheiro uma pessoa tem na carteira e
# mostre quantos dolares ela pode compra sendo que R$ 1 real e 5.12
real = float(input('quanros mony você tem na carteira: '))
us = real / 5.12
print(f'Com {real} você pode compra {us:.2f} dolares')