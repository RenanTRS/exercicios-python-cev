#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma 
#listagem de preços, organizando os dados em forma tabular.

produtos = ('Cola', '1.50', 'Lápis', '3.00', 'Caderno', '12.00', 'Mochila', '55.00')

for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}  R${produtos[c+1]:>8}')