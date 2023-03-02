from Class import *
import math

def escolha():
    titulo(z='ESCOLHE UM PROGRAMA A SEGUIR'.center(30))
    print('[ 1 ] - Contas Aritméticas.\n'
          '[ 2 ] - Antecessor e Sucessor de um numero.\n'
          '[ 3 ] - Dobro, Triplo e Raiz Quadrada.\n'
          '[ 4 ] - Média Aritmética.\n'
          '[ 5 ] - Converter Metros em CM e MM.\n'
          '[ 6 ] - Tabuada.\n'
          '[ 7 ] - Converter Real em Dolar.\n'
          '[ 8 ] - Quantos Litros de tinta precisa.\n'
          '[ 9 ] - Desconto de uma Produto.\n'
          '[ 10 ] - Aumentar o Valor do Salario %.\n'
          '[ 11 ] - PORCETAGEM\n'
          '[ 12 ] - Converter C para F\n'
          '[ 13 ] - Carro Alugado\n'
          '[ 0 ] - SAIR')

    num = 1

    while num != 0:
        print('-' * 30)
        num = cale('>>>>> ESCOLHA UM PROGRAMA: '.center(15))
        match num:

            case 1:
#1 OPERADORES ARITMÉTICOS
                titulo(z='CONTAS ARITMÉTICAS'.center(29))
                n1 = cale(' Digite um numero: ')
                n2 = cale(' Digite outro numero: ')
                titulo(z='RESULTADO DO CALCULO'.center(30))
                print(f'Soma entre [{n1}] e [{n2}]: {n1+n2}\nDivisão entre [{n1}] e [{n2}]: {n1/n2:.2f}\n'
                      f'Multiplicação entre [{n1}] e [{n2}]: {n1*n2}\n'
                      f'Resto da divisão entre [{n1}] e [{n2}]: {n1//n2}'
                      f'\nPontência entre [{n1}] e [{n2}]: {n1**n2}\n')

            case 2:
#2 ANTECESSOR E SUCESSOR
                titulo(z='ANTECESSOR E SUCESSOR'.center(30))
                x = cale(' Digite um numero: ')
                print(f' Antecessor de {x} é {x-1} e o seu Sucessor é {x+1}')

            case 3:
#3 DOBRO, TRIPLO E RAIZ QUADRADA
                titulo('DOBRO, TRIPLO E RAIZ QUADRADO DO NUMERO'.center(30))
                z = cale('Digite um numero: ')
                valor(z)

            case 4:
#4 MEDIA DA NOTA
                titulo('MÉDIA ARITMÉTICA'.center(30))
                x1 = cale('Primeira Nota: ')
                x2 = cale('Segunda Nota: ')
                print(f'Sua media é: {(x1+x2)/2}')

            case 5:
#5 METROS PARA CM E MM
                titulo('CONVERSOR DE MM PARA CM E MM'.center(30))
                metro = cale('Quantos metros? ')
                print(f'Em CM é: {metro*100} e MM é: {metro*1000}')

            case 6:
#6 TABUADA
                titulo('TABUADA DE UM NÚMERO'.center(30))
                tab = cale('Digite um numero: ')
                for i in range(1, 11):
                    print(f' {tab} x {i} = {tab*i}')

            case 7:
#7 CARTEIRA, REAL E DOLAR
                titulo('CONVERTER REAL PARA DOLAR'.center(30))
                real = cale('Quanto R$: ')
                print(f'CARTEIRA: R$: {real}\nDolar: {float(real/5)}')

            case 8:
#8 PINTAR PAREDE
                titulo('QUANTOS LITROS DE TINTA PARA PINTAR UMA PAREDE'.center(30))
                alt = cale('Altura: ')
                larg = cale('Largura: ')
                print(f'{alt*larg/2} quantidade litro de tinta')

            case 9:
#9 DESCONTO NO PRODUTO
                titulo('DESCONTO DE UM PRODUTO'.center(30))
                sal = cale('Valor do produto: ')
                print(f'{sal - (sal*1.05 - sal):.7}')

            case 10:
#10 SALARIO MAIS %15
                titulo('AUMENTO DO SALÁRIO EM 15%'.center(30))
                sal = cale('Qual é seu salario: ')
                print(f'{sal*1.15:.7}')

            case 11:
                titulo('PORCETAGEM DIMINUIR E AUMENTAR')
                x = cale('Valor do Produto: ')
                y = cale('%')
                z = x * y / 100
                print(f'aumento do produto de {y}% é {z+x} e o desconto é {x-z}')

            case 12:
#CONVERSOR DE TEMPERATURA
                titulo('CONVERTER GRAU CELSIUS PARA FHARENHEIT')
                c = cale('Quantos graus celsus está: ')
                print(f'A conversão é: {c * 1.8 + 32:.1f}')

            case 13:
#Carro Alugado
                titulo('ALUGUEL DE CARROS')
                dia = cale('Quantos dias alugados? ')
                km = cale('Quantos KM rodados? ')
                pagar = (dia * 60) + (km * 0.15)
                print(f'O total a pagar R$: {pagar:.2f}')

            case 0:
                print("ENCERROU O PROGRAMA!")
                break

            case _:
                print('VALOR INVALIDO!')

escolha()
