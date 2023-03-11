from modules import locadora, obj
from utils import util

if __name__ == '__main__':
    app = locadora.App()
    
    userList, carList = obj.loadLists()

    while(True):
        print('Tabela da Locadora')
        print('0 - Cadastrar veiculo')
        print('1 - Consultar disponibilidade de veículos')
        print('2 - Listar veículos por marca')
        print('3 - Listar veículos por modelo')
        print('4 - Listar veículos por ano')
        print('5 - Criar usuario')

        try:
            resp = int(input('Digite sua escolha: '))

            match (resp):
                case 0:
                    car = app.cadastrar_veiculo()
                    print(dir(carList)) # no append function?
                    util.pauseAndClear()
                case 1:
                    app.consultar_disponibilidade_de_veiculos(carList)
                    util.pauseAndClear()
                case 2:
                    app.listar_veiculos_por_marca(carList)
                    util.pauseAndClear()
                case 3:
                    app.listar_veiculos_por_modelo()
                    util.pauseAndClear()
                case 4:
                    app.listar_veiculos_por_ano()
                    util.pauseAndClear()
                case 5:
                    client = app.cadastrar_usuario()
                    util.pauseAndClear()
                case _:
                    util.brokenProgram()
                    util.error()
                    break
        except:
            util.brokenProgram()
            util.error()
            break