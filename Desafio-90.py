aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]} :'))
if aluno['Media'] > 6.9:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situaçao'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')

