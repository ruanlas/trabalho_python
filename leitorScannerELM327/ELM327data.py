
class ELM327data:

    def __init__(self, modelo = '', chassi = '', dataLeitura = '',
                 horarioLeitura = '', rpm = ''):
        self.modelo = modelo
        self.chassi = chassi
        self.dataLeitura = dataLeitura
        self.horarioLeitura = horarioLeitura
        self.rpm = rpm
