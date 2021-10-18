class Serviço:

    def __init__(self, nomeCliente, tipoServico, atendente, data, horario):
        self.nomeCliente = str(nomeCliente)
        self.tiposServico = str(tipoServico)
        self.atendente = str(atendente)
        self.data = str(data)
        self.horario = str(horario)
        pass

    def to_string(self):
        return f"O cliente {self.nomeCliente}, foi atendido no dia {self.data} as {self.horario} por {self.atendente} "\
               f"para a realização do seguinte(s) serviços {self.tiposServico} "
    
    def get__nome_cliente(self):
        return self.nomeCliente
        
    def get__tipos_servico(self):
        return self.tiposServico
    
    def get__atendente(self):
        return self.atendente
    
    def get__data(self):
        return self.data
    
    def get__horario(self):
        return self.horario
    
    def set__nomeCliente(self,nomeCliente ):
        self.nomeCliente = nomeCliente
    
    def set__servico(self, tipoServico):
        self.tiposServico = tipoServico
    
    def set__atendente(self, atendente):
        self.atendente = atendente



