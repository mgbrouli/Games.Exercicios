from random import randint
from time import sleep
lista = ['pedra', 'papel', 'tesoura']


def escolha(item, ganha, perde):
    if player == item and lista[pc] == ganha:
        print(f'Você escolheu {item} o computador escolheu {ganha}')
        print(f'Parabéns você ganhou!!!')
    elif player == item and lista[pc] == perde:
        print(f'Você escolheu {item}, o computador escolheu {perde}')
        print('Foi mal você perdeu!!!')
    elif player == item and lista[pc] == item:
        print('Empate! Jogue Novamente')
        


print('--'*30)
print(f'{"BEM VINDO JO KEN PÔ":^40}')
print('--'*30)
sleep(1)
pc = randint(0, 2)

print('Escolha entre Pedra, Papel ou Tesoura')
player = str(input('O que você escolhe: ')).lower()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('O computador escolheu {}'.format(lista[pc]))

escolha('pedra', 'tesoura', 'papel')
escolha('tesoura', 'papel', 'pedra')
escolha('papel','pedra','tesoura')
