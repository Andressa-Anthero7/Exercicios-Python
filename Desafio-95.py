gols_marcados = list()
time = list()
jogador = dict()
tot_gols = 0
opcao = 0
resp = ''
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).upper()
    partidas = int(input('Quantas partidas {} jogou?: '.format(jogador['nome'])))
    for c in range(0, partidas):
        gols_marcados.append(int(input(f'Quantos gols na {c + 1}ª partida : ')))
        tot_gols = gols_marcados[c]
    jogador['gols'] = gols_marcados[:]
    gols_marcados.clear()
    jogador['total'] = tot_gols
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar?\n S/N: '))
        if resp in 'SsNn':
            break
        else :
            print('Comando inválido,Digite S-(sim) / N-(não):')
    if resp in 'Nn':
        break
print('-='*50)
print(f'{"Nº":<3}{"Nome":^12}{"Gols":>8}{"Total de gols":^25}')
print('-'*50)
for pos, c in enumerate(time):
    print(f'{pos} {c["nome"]:^12} {c["gols"]}     {jogador["total"]}')
    if pos == len(time)-1:
        print('-='*50)
        while opcao != 999:
            opcao = int(input('Digite número do aluno: '))
            if opcao == 999:
                print('Fechando Programa')
                break
            if opcao > len(time)-1:
                print(f'Não existe jogador com número {opcao} ')
            if opcao < len(time):
                print(f'O jogador{time[opcao]["nome"]} teve aproveitamento ')
                for i, v in enumerate(time):
                    print(f'Na partida {i+1}, fez {v["total"]} gols')


