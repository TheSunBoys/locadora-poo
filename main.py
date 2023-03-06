from modules import locadora

if __name__ == '__main__':
    app = locadora.App()
    while(True):
        print('Tabela da Locadora')
        print('0 - cadastrar veiculo')
        print('1 - consultar disponibilidade de veículos')
        print('2 - listar veículos por marca')
        print('3 - listar veículos por modelo')
        print('4 - listar veículos por ano')
        resp = input('Digite sua escolha: ')

        if resp == 0:
            app.cadastrar_veiculo()
        elif resp == 1:
            app.consultar_disponibilidade_de_veiculos()
        elif resp == 2:
            app.listar_veiculos_por_marca()
        elif resp == 3:
            app.listar_veiculos_por_modelo()
        elif resp == 4:
            app.listar_veiculos_por_ano()

        
