carList = [
    {
        'carro': {
            'marca': 'Monza',
            'modelo': 'Calhambeque',
            'ano': '2007',
            'placa': 'DEVIL',
            'quilometragem': 0,
            'valorDaDiaria': 666
        }
    }, {
        'carro': {
            'marca': 'Flamengo',
            'modelo': 'Fusca',
            'ano': '1986',
            'placa': '_ACDC_',
            'quilometragem': 666,
            'valorDaDiaria': 69
        }
    }
]

userList = [
    {
        'Cliente': {
            'nome': 'Joaquim Tafarel de Fênix',
            'id': '4E2C70',
            'historicoDeCarrosAlugados': [
                {
                    'Carro': {
                        'marca': 'Flamengo',
                        'modelo': 'Calhambeque',
                        'ano': '2007',
                        'placa': 'DEVIL',
                        'quilometragem': 0,
                        'valorDaDiaria': '666'
                    }
                },
                {
                    'Carro': {
                        'marca': 'Vasco',
                        'modelo': 'Fusca',
                        'ano': '1986',
                        'placa': '_ACDC_',
                        'quilometragem': 666,
                        'valorDaDiaria': '69'
                    }
                }
            ]
        }
    },

    {
        'Cliente': {
            'nome': 'Joaquim Tafarel de Fênix',
            'id': '4E2C70',
            'historicoDeCarrosAlugados': [
                {
                  'Carro': {
                    'marca': 'Flamengo',
                    'modelo': 'Calhambeque',
                    'ano': '2007',
                    'placa': 'DEVIL',
                    'quilometragem': 0,
                    'valorDaDiaria': '666'
                  }
                },
                {
                    'Carro': {
                        'marca': 'Vasco',
                        'modelo': 'Fusca',
                        'ano': '1986',
                        'placa': '_ACDC_',
                        'quilometragem': 666,
                        'valorDaDiaria': '69'
                    }
                }
            ]
        }
    }
]

def loadLists():
    return userList, carList