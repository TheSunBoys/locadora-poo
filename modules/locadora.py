class App():
    def __init__(self):
        pass

    def consultar_disponibilidade_de_veiculos(self):
        pass

    def listar_veiculos_por_marca(self):
        pass

    def listar_veiculos_por_modelo(self):
        pass

    def listar_veiculos_por_ano(self):
        pass

    def cadastrar_veiculo(self):
        pass

    def cadastrar_usuario(self):
        pass
    class Veiculo():
        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
    
    class Carro(Veiculo):
        def __init__(self, placa, quilometragem, valorDaDiaria):
            self.placa = placa
            self.quilometragem = quilometragem
            self.valorDaDiaria = valorDaDiaria
            
    class Cliente():
        def __init__(self, nome, id, historicoDeCarrosAlugados=None):
            self.nome = nome
            self.id = id
            self.historicoDeCarrosAlugados = historicoDeCarrosAlugados