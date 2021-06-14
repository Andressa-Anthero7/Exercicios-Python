
resp = ''
cadastro = list()
pessoa = dict()
tot_pessoas = media_idade =  0
mulheres = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo M/F: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    tot_pessoas += 1
    media_idade = + pessoa['idade']/tot_pessoas
    cadastro.append(pessoa.copy())
    resp = str(input('Quer continuar? S/N:'))
    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])
    if resp in 'Nn':
        print(f'Ao todo temos {tot_pessoas} pessoas cadastradas.')
        print(f'A média de idade do grupo é de {media_idade:.2f} anos.')
        print(f'{mulheres[0]}')


        #if v['sexo'] in 'F':
            #mulheres = v['nome']
        #print(mulheres)

