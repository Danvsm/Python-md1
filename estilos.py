import time

import emoji


def tempo():
    for i in range(0, 3):
        print('\033[32mPROCESSANDO...\033[m')
        time.sleep(1)

def estilo1():
    print("\033[35m=\033[m"*60)

def estilo2(x):
    print(f"{'-'*12} {x} {'-'*12}")

def azul(x):
    print(f"\033[34m{x}\033[m")