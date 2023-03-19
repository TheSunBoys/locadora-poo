class App():
    def __init__(self):
        pass

    def consultar_disponibilidade_de_veiculos(self, carList):
        vList = carList
        print(dir(vList))
        for i, veicle in enumerate(vList):
            print(veicle)
            print(f'Carro {i} [\n{veicle.marca},{veicle.modelo},{veicle.ano}\n{veicle.placa}{veicle.quilometragem}Km, {veicle.valorDaDiaria} R$ por dia]\n\n')

    def listar_veiculos_por_marca(self): #Thiago
        pass

    def listar_veiculos_por_modelo(self): #thiago
        pass

    def listar_veiculos_por_ano(self):
        pass

    def cadastrar_veiculo(self):
        marca = input('Digite a MARCA do veiculo: ')
        modelo = input('Digite o MODELO do veiculo: ')
        ano = input('Digite o ANO do veiculo: ')
        placa = input('Digite a PLACA do carro: ')
        quilometragem = input('Digite a QUILOMETRAGEM do veiculo: ')
        valorDaDiaria = input('Digite o VALOR DA DIARIA do Carro: ')
        car = self.Carro(marca, modelo, ano, placa, quilometragem, valorDaDiaria)
        return car

    def cadastrar_usuario(self):
        pass
    class Veiculo():
        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
    
    class Carro(Veiculo):
        def __init__(self, marca, modelo, ano, placa, quilometragem, valorDaDiaria):
            super().__init__(marca, modelo, ano)
            self.placa = placa
            self.quilometragem = quilometragem
            self.valorDaDiaria = valorDaDiaria

    class Cliente():
        def __init__(self, nome, id, historicoDeCarrosAlugados=None):
            self.nome = nome
            self.id = id
            self.historicoDeCarrosAlugados = historicoDeCarrosAlugados