from laboratorios import CadastroLaboratorios
from laboratorios import Laboratorio

class Medicamento:
    def __init__(self, nome: str, comp_principal: str, laboratorio: Laboratorio, descricao: str, preco: float, tipo_medicamento : str) -> None:
        self.nome = nome
        self.comp_principal = comp_principal
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.preco = preco
        self.tipo_medicamento = tipo_medicamento

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nComposto Principal: ' + self.comp_principal
        representacao += '\nLaboratório: ' + self.laboratorio.nome
        representacao += '\nDescrição: ' + self.descricao
        representacao += '\nPreço: R$ ' + str(self.preco)
        representacao += '\nTipo Medicamento: ' + str(self.tipo_medicamento)
        return representacao

class Quimioterapicos(Medicamento):
    def __init__(self, nome, comp_principal, laboratorio, descricao, receita, preco, tipo_medicamento):
        super().__init__(nome, comp_principal, laboratorio, descricao, preco, tipo_medicamento)
        self.receita = receita

    def __repr__(self):
        representacao = super().__repr__()
        representacao += '\nNecessita Receita: ' + ('Sim' if self.receita else 'Não')
        return representacao

class Fitoterapicos(Medicamento):
    def __init__(self, nome, comp_principal, laboratorio, descricao, preco, tipo_medicamento):
        super().__init__(nome, comp_principal, laboratorio, descricao, preco, tipo_medicamento)

    def __repr__(self):
        representacao = super().__repr__()
        representacao += '\nNecessita Receita: ' + ('Não')
        return representacao  
        
class CadastroMedicamentos:
    def __init__(self):
        self.medicamentos = []
        self.laboratorios = CadastroLaboratorios()

    def cadastrar_medicamento(self, cadastro_laboratorios, tipo_medicamento):
        nome = input("Nome do medicamento: ")
        comp_principal = input("Composto do medicamento: ")
        nome_laboratorio = input("Laboratório do medicamento: ")
        descricao = input("Descrição do medicamento: ")
        if tipo_medicamento == "quimioterapico":
            receita = input("Necessita receita? (S/N): ").lower() == "s"
        
        if tipo_medicamento == "quimioterapico" and not receita:
            print("Medicamento quimioterápico requer receita. O medicamento não foi cadastrado.")
            return
        
        preco = float(input("Preço do medicamento: "))

        laboratorio = cadastro_laboratorios.buscar_laboratorio(nome_laboratorio)
        print(f"Resultado da busca do laboratório: {laboratorio}")
        
        if laboratorio:
            if tipo_medicamento == "quimioterapico":
                medicamento = Quimioterapicos(nome, comp_principal, laboratorio, descricao, receita, preco,"quimioterapico")
                self.medicamentos.append(medicamento)
                print("Medicamento quimioterápico cadastrado com sucesso!")
            elif tipo_medicamento == "fitoterapico":
                medicamento = Fitoterapicos(nome, comp_principal, laboratorio, descricao, preco,"fitoterapico")
                self.medicamentos.append(medicamento)
                print("Medicamento fitoterápico cadastrado com sucesso!")
        else:
            print("Laboratório não encontrado. O medicamento não foi cadastrado.")

    def buscar_medicamento_por_nome(self):
        nome_medicamento = input("Digite o nome do medicamento: ")
        for medicamento in self.medicamentos:
            if nome_medicamento.lower() in medicamento.nome.lower():
                return print(medicamento)
        return print("Medicamento não encontrado.")
    
    def buscar_medicamento_por_nome1(self,nome):
        for medicamento in self.medicamentos:
            if nome.lower() in medicamento.nome.lower():
                return medicamento
        return None