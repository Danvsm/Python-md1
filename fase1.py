from estilos import  *
import emoji
def fase1():
    tempo()
    estilo2('\033[32mENTROU NO PROGRAMA!\033[m')
    print('Olá, sou uma android me chamo \033[32mEster Pendleton\033[m')
    nome = input('Qual é seu nome? ').capitalize()
    if nome == 'Clarissa':
        print(f'Que nome lindo {nome}!')
    else:
        print(emoji.emojize('\033[33mAinda bem que não é Clarissa, eu não gosto dela. Mas fui programada para fingir que gosto :rage:\033[m', language='alias'))

    print(f'\033[32m{nome}\033[m, eu espero que nós podemos ser amigas! Eu nasci recentemente, e ainda estou aprendendo')
    estilo1()

    resp = input('\nEu conheço um jogo \033[32m"FAZ DE CONTA"\033[m, vamos jogar? S/N ').lower()

    if resp == 's':
        estilo2('\033[32mFASE 001\033[m')
        print("Você é uma cozinheira bem famosa! chamada de \033[32mCamilla D'Vhuar\033[m")
        print(emoji.emojize(f'\nVocê está sendo entrevistada por uma mulher famosa que tem um restaurante {emoji.emojize(":star:"*5)} \n'
                            'nome dela é \033[34mPoliana\033[m, uma mulher de 23 anos e ela está :smile:!', language='alias'))
        estilo1()
        azul(x="Poliana: Camilla D'Vhuar, dizem que você é muito esperta!")
        resp = input('Diga para mim um nome com 6 letras: ')
        cont = len(resp)
        if cont == 6:
            print('\033[32mVOCÊ É MUITO ESPERTA CAMILLA!\033[m')
            print('Vou fazer mais teste para saber é verdadeira Camilla')
            resp = eval(input('Quanto que é 2 + 3? '))
            if resp == 5:
                print(emoji.emojize(f'Foi moleza para você né querida :nail_care:', language='alias'))
                print('Você está contratada! Amanhã você pode vim!')
                tempo()
                estilo2('FASE 002')
                print('Um garçom chega até você diz que o PRESIDENTE DO ESTADOS UNIDOS, QUER SUA MELHOR JANTA!')
                resp = eval(input(emoji.emojize('Escolha algo para fazer: \n[1] Pão :bread:\n[2] Biscoito :cookie: \n[3] Sopa :stew: ', language='alias')))
                if resp == 1:
                    print('O presidente não da brincadeira! Você foi pressa')
                    tempo()
                    print('\033[31mPERDEU O JOGO\033[m')
                elif resp == 2:
                    print('\033[32mTodos RIU ver só um biscoito no PRATO\033[m')
                    print('\033[31mE SUA MÃE FOI PRESSA!\033[m')
                    tempo()
                    print('FIM DE GAME')
                else:
                    tempo()
                    tempo()
                    print('\033[32mO PRESIDENTE FICOU TÃO EMOCIONADO QUE TE DEU UMA MEDALHE DE HONRA!\033[m')
        else:
            print(emoji.emojize('VOCÊ NÃO É CAMILLA VERDADEIRA!:rage:', language='alias'))
            print('FIM DE GAMER')

    else:
        print('Não queria brincar com você mesmo.')
