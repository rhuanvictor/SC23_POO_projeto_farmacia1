from datetime import datetime
class Cliente:
    def __init__(self, cpf: str, nome:str, dt_nascimento: str) -> None:
        self._cpf = cpf
        self.nome = nome
        self.dt_nascimento = dt_nascimento

    @property
    def cpf(self):
        return self._cpf

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nCPF: ' + self.cpf
        representacao += '\nData de Nascimento: ' + self.dt_nascimento
        return representacao
    
    def calcular_idade(self):
        hoje = datetime.now()

        if '/' in self.dt_nascimento:
            data_nascimento = datetime.strptime(self.dt_nascimento, '%d/%m/%Y')
        else:
            dia = int(self.dt_nascimento[0:2])
            mes = int(self.dt_nascimento[2:4])
            ano = int(self.dt_nascimento[4:8])
            data_nascimento = datetime(ano, mes, dia)

        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        return idade
    
class CadastroCliente:    
    def __init__(self) -> None:
        self.cadastrados = {}
        #self.clientes = []
        
    def cadastrar_novo(self) -> None:
        cpf = input('Digite o CPF do cliente: ')
        nome = input("Digite o nome do cliente: ")
        dataNascimento = input('Digite a data de nascimento do cliente: ')     
        
        if cpf not in self.cadastrados:
            novo_cliente = Cliente(cpf, nome, dataNascimento)
            self.cadastrados[cpf] = novo_cliente
        else:
            print('CPF já cadastrado')
            
    def _get_cliente(self, cpf):
        if cpf in self.cadastrados:
            return self.cadastrados[cpf]
        else:
            return None
        
    def visualizar_cadastro(self, cpf):
        if cpf in self.cadastrados:
            print(self.cadastrados[cpf])
        else:
            print('Cliente não encontrado.')
            
    def visualizar_cadastro(self, cpf) -> None:
        cliente = self._get_cliente(cpf)
        if cliente:
            print(cliente)
        else:
            print('Cliente não encontrado')
            
    def alterar_cadastro(self, cpf):
        cliente = self._get_cliente(cpf)
        if not cliente:
            print('CPF não cadastrado')
            return
        
        alteracao = input('O que deseja alterar? ')
        
        while alteracao.lower() not in ('nome', 'nascimento', 'cpf'):
            alteracao = input('Não foi possível encontrar o critério informado. O que deseja alterar? ')
        
        if alteracao == 'nome':
            novo_nome = input('Digite o novo nome: ')
            cliente.nome = novo_nome
        
        elif alteracao == 'nascimento':
            nova_dt_nascimento = input('Digite a nova data de nascimento: ')
            cliente.dt_nascimento = nova_dt_nascimento 
            
        elif alteracao == 'cpf':
            novo_cpf = input('Digite o novo CPF: ')
            cliente.cpf = novo_cpf
            self.cadastrados.pop(cpf)
            
        self.cadastrados[cliente.cpf] = cliente
        
    def buscar_cliente_por_cpf(self, cpf):
        if cpf in self.cadastrados:
            return self.cadastrados[cpf]
        return None
    
    