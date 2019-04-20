from random import randint
from time import sleep

print('--'*30)
print('você escolha par ou impar')
escolha = str(input('par ou impar[P/I]: ')).upper().strip()[0]
while escolha not in 'PI':
    escolha = str(input('par ou impar[P/I]: ')).upper().strip()[0]
variavel = ''
if escolha == 'P':
    variavel = 'Par'
elif escolha == 'I':  
    variavel = 'Impar'
print('--'*30)
print(f'Você escolheu {variavel}')
print('--'*30)
pc = randint(0, 10)
player = int(input('Digite um numero de 1 a 10: '))
soma = player + pc
sleep(2)
print(f'Você escolheu {player} e a maquina escolheu {pc}')
print('--'*30)
print('Deu: ', end='')
sleep(2)
if soma % 2 == 0:
    print('Par')
    print('--'*30)
    if variavel == 'Par':
        print('Você Ganhou')
    else:
        print('Você perdeu')
else:
    print('Impar')
    print('--'*30)
    if variavel == 'Impar':
        print('Você Ganhou')
    else:
        print('Você perdeu')
