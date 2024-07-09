import random

numero_secreto = random.randint(1,20)

# FIXME: Declarando variáveis

tentativas = 0
max_tentativas = 5
acertou = False

print("Bem-vindo ao jogo Python Adivinha")
print(f'Você tem {max_tentativas} de tentativas para adivinha o numero entre 1 a 20')

# Loop


while tentativas < max_tentativas:
    palpite = int(input('Digite um número inteiro: '))
    
    tentativas += 1
    
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('TEnte um numero maior')
    else:
        print('Tente um numero menor')
if acertou:
    print(f'Parabéns! Você acertou!')
else: 
    print(f'Você gastou todas as suas tentativas, que pena.')