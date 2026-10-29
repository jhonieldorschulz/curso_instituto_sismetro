nome = input('Digite o seu nome:')

idade = input('Digite sua idade: ')

def processar_presenca(status_presenca):
    if(status_presenca == 'P') or (status_presenca == 'Presente'): 
        return True 
    return False 

status_presenca = input('Status de Presença: ')

resposta_presenca = processar_presenca(status_presenca)

print(f'Nome: {nome}, Idade: {idade}, Presença:{resposta_presenca}')
