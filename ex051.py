#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa prograssão.

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
f = r * 10

for c in range(p, f, r):
    print('{} ->'.format(c), end='')

print('Acabou')