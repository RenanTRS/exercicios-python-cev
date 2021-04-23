#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas 
#ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.

player = {}
goals = []
total = 0

#inputs
player['name'] = str(input('Name: ')).strip().title().split()[0]
qtd = int(input(f"How many matches {player['name']} played: "))

#for logic
for c in range(0, qtd):
    goals.append(int(input(f'How many goals in game {c+1}: ')))
    total += goals[c]

player['goals'] = goals[:]
player['total'] = total

#code exit
print('==' * 20)
print(player)
print('==' * 20)

#for logic exit
for k, v in player.items():
    print(f'The {k} field has a value of {v}.')