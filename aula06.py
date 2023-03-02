def numero():
    return eval(input('digite um numero: '))

def deco():
    return print('-'*30)

n1 = numero()
n2 = numero()

deco()
print(f'A soma entre {n1} e {n2} vale {n1+n2} ')
deco()
print("        SEGUNDA ETAPA   ")
deco()
t = input('Digite um tipo: ')
deco()

print(f'Os tipos de -> {t}\n '
      f'\n'
      f'  O tipo primitivo é: {type(t)} \n '
      f' É alfabético? {t.isalpha()} \n '
      f' É alfanumérico? {t.isalnum()} \n'
      f'  É numéro? {t.isalnum()} \n'
      f'  Está em minúsculas? {t.islower()} \n'
      f'  Está em maiúsculas? {t.isupper()} \n '
      f' Está capitalizada? {t.istitle()} \n'
      f'  Só tem espaço? {t.isspace()} \n')
