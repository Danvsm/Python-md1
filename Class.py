def cale(x):
    try:
        x = eval(input(x))
        return x
    except:
        return print('Digite somente inteiros!')


titulo = lambda z, a ='-' * 30, b ='\n': print('', a, b, z, b, a)


separar = lambda: print('-'*30)


valor = lambda numero: print(f'O dobro é {numero*2}, \ntriplo: {numero*3} \na raiz quadrada {pow(numero, 1/2)}')




