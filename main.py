import os
import platform
import json
from modules import locadora

if __name__ == '__main__':
    app = locadora.App()
    with open('./json/users.json') as userFile:
        userList = json.load(userFile)
    
    with open('./json/cars.json') as carFile:
        veiculoList = json.load(carFile)
    
    def pauseAndClear():
        input('\n\nPressione [ENTER] para continuar...')
        so = platform.system()
        if so == 'Linux':
            os.system('clear')
        else:
            os.system('cls')

    while(True):

        print('Tabela da Locadora')
        print('0 - Cadastrar veiculo')
        print('1 - Consultar disponibilidade de veículos')
        print('2 - Listar veículos por marca')
        print('3 - Listar veículos por modelo')
        print('4 - Listar veículos por ano')
        print('5 - Criar usuario')
        resp = int(input('Digite sua escolha: '))

        match (resp):
            case 0:
                car = app.cadastrar_veiculo()
                print(dir(veiculoList)) # no append function?
                pauseAndClear()
            case 1:
                app.consultar_disponibilidade_de_veiculos(veiculoList)
                pauseAndClear()
            case 2:
                app.listar_veiculos_por_marca()
                pauseAndClear()
            case 3:
                app.listar_veiculos_por_modelo()
                pauseAndClear()
            case 4:
                app.listar_veiculos_por_ano()
                pauseAndClear()
            case 5:
                client = app.cadastrar_usuario()
                pauseAndClear()
            case _:
                print('quebrou!')