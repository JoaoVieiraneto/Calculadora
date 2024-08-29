import time
print('Bem vindo!')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Exponencial')

def Soma(num_1, num_2):
    return num_1 + num_2
def Subt(num_1,num_2):
    return num_1 - num_2
def mult(num_1, num_2):
    return num_1 * num_2
def div(num_1, num_2):
    return num_1 / num_2
def exp(num_1, num_2):
    return num_1 ** num_2
while True: 
    Escolha = int(input('Escolha qual operação você deseja realizar: '))
    num_1 = int(input('\nDigite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))

    if Escolha == 1:
        print('\nA operação escolhida foi a soma ->')
        print('-----------------------------------------')
        time.sleep(1)
        print('\nO resultado da soma é: {}'.format(Soma(num_1,num_2)))
    if Escolha == 2:
        print('\nA operação escolhida foi a subtração ->')
        print('-----------------------------------------')
        time.sleep(1)
        print('\nO resultado da subtração é: {}'.format(Subt(num_1,num_2)))
    if Escolha == 3:
        print('\nA operação escolhida foi a multiplicação ->')
        print('-----------------------------------------')
        time.sleep(1)
        print('\nO resultado da multiplicação é: {}'.format(mult(num_1,num_2)))
    if Escolha == 4:
        print('\nA operação escolhida foi a Divisão ->')
        print('-----------------------------------------')
        time.sleep(1)
        print('\nO resultado da divisão é: {}'.format(div(num_1,num_2)))
    if Escolha == 5:
        print('\nA operação escolhida foi a de Expoente ->')
        print('-----------------------------------------')
        time.sleep(1)
        print('\nO resultado do expoente é: {}'.format(exp(num_1,num_2)))

    Continuar = input('Deseja continuar? Digite "sim" para sim e "não" para não: ')
    if Continuar != 'sim':
        print('Finalizando o programa...')
        time.sleep(1)
        break
