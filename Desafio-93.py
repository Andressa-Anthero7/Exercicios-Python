gols_marcados = list()
jogador = dict()
tot_gols = 0
jogador['nome'] = str(input('Nome do jogador: ')).upper()
partidas = int(input('Quantas partidas {} jogou?: '.format(jogador['nome'])))
for c in range(0, partidas):
    gols_partidas = int(input(f'Quantos gols na {c+1}ª partida : '))
    tot_gols += gols_partidas
    gols_marcados.append(gols_partidas)
    jogador['gols'] = gols_marcados
    jogador['total'] = tot_gols
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas. ')
for i, v in enumerate(gols_marcados):
    print(f'Na partida {i+1}, fez {v}')
print(f'Foi total de {tot_gols} gols')
