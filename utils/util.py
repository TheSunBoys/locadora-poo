import os
import platform
import sys

def pauseAndClear():
        input('\n\nPressione [ENTER] para continuar...')
        so = platform.system()
        if so == 'Linux':
            os.system('clear')
        else:
            os.system('cls')

def brokenProgram():
    print('\na locadora quebrou!\n')

def error():
    erro = sys.exc_info()
    print("Ocorreu um erro: ", erro)