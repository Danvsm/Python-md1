#--------------------------------------------
#QUANTOS ANOS TEM SEU CARRO?
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')

print('\nFim do Programa')

nome = input('Qual é seu nome? ').lower()
if nome == 'gustavo':
    print(f'O seu nome é muito lindo {nome.capitalize()}')
elif nome == 'arthur':
    print(f'{nome.capitalize()} seu nome é feio!')
else:
    print(f'Seja Bem vindo {nome.capitalize()}')


#CHUTA MEU 'PENSAMENTO'
import random
from time import sleep

valor = random.randint(0,5)
r = input('Vamos jogar? S/N ').lower()
if r == 's':
    chute = eval(input('Eba! Chute que numero eu pensei! 0 a 5 '))
    if valor == chute:
            print('PROCESSANDO...')
            sleep(1.8)
            print("ACERTOU! béeeh perdi ;-; to chorando")
    else:
        sleep(1.8)
        print('PROCESSANDO...')
        print(f"errou! eu pensei em {valor}")

else:
    print("Ate aproxima!")


#VELOCIDADE PERMITIDA
# print("Oi, seja bem vindo! Eu vim analisar a sua velocidade que vocês estava na estrada")
# km = eval(input('Qual era velocidade você estava? Não minta! '))
# if km > 80:
#     print("Que coisa feia, você ultrapassou o limite!")
#     print(f'você ultrapassou {km - 80}km, sua multa é R$: {(km - 80) * 7}')
# else:
#     print('Continua assim! Estamos feliz pela sua atitude :)')
#
#----------------------------------------------------
#
#IMPAR OU PAR
# print('Minha função aqui é ver o numero é impar ou par')
# num = eval(input('Está esperando o que? Digite um numero: '))
# if (num % 2) == 0:
#     print("Esse numero é par!")
# else:
#     print("Impar, imparesmos KKK não bato bem da cabeça")

#------------------------------------------------

#VALOR DA PASSAGEM
# print("Agora minha função é calcular o preço da viagem, viagem acima 200km tem descontos")
# distancia = eval(input('Quantos KM de distancia para chegar no seu destino? '))
# if distancia <= 200:
#     print(f'o valor mutiplicado por 0,50 x km é  {distancia*0.5}')
# else:
#     print(f'o valor mutiplicado por 0,45 x km é {distancia*0.45}')
#

#-------------------------------------

# ANO BISSEXTO?
# from datetime import date
# print("Vou descobrir para você se esse ano é bissexto")
# print("Não se acostume humano!")
# ano = eval(input('Diga o ano: '))
# if ano == 0:
#     ano = date.today().year
# if ano % 2 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print(f'O ano {ano} é bissexto')
# else:
#     print('Eita eita não é')

#--------------------------------------

# AUMENTAR SALARIO DE ACORDO DO VALOR
# print('Agora irei aumentar o salario dependendo quanto você recebe')
# salario = eval(input('Digite o seu salario R$: '))
# if salario <= 1250:
#     print(f'Teve aumento de 15%, seu salario atual é R$: {salario + (salario * 15 / 100)}')
# else:
#     print(f'Seu aumento foi de 10%, seu salario atual é R$: {salario + (salario * 10 / 100)}')

#---------------------------------------

# print('PODE FORMA UM TRIANGULO?')
# r1 = eval(input("Primeira reta: "))
# r2 = eval(input("Segunda Reta: "))
# r3 = eval(input("Terceira Reta: "))
# if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
#     print("\033[7:1:40mé possivel!\033[m")
# else:
#      print("Não é possivel")

#--------------------------------------------
#
# n1 = eval(input('Primeiro valor: '))
# n2 = eval(input('Segundo valor: '))
# n3 = eval(input('Terceiro valor: '))
#
# menor = n1 if n1 < n2 else n2
# maior = n1 if n1 > n2 else n2
#
# if maior < n3:
#     maior = n3
# if menor > n3:
#     menor = n3
#
# print(f'O maior: {maior} e o menor: {menor}')
#
#--------------------------------------
