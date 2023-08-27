class Laboratorio:
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
    
    def __repr__(self):
        representacao = 'Nome: ' + self.nome
        representacao += '\nEndereço: ' + self.endereco
        representacao += '\nTelefone: ' + self.telefone
        representacao += '\nCidade: ' + self.cidade
        representacao += '\nEstado: ' + self.estado
        return representacao

class CadastroLaboratorios:
    def __init__(self):
        self.laboratorios = []

    def cadastrar_laboratorio(self):
        nome = input("Nome do laboratório: ")
        endereco = input("Endereço do laboratório: ")
        telefone = input("Telefone do laboratório: ")
        cidade = input("Cidade do laboratório: ")
        estado = input("Estado do laboratório: ")
        laboratorio = Laboratorio(nome, endereco, telefone, cidade, estado)
        
        self.laboratorios.append(laboratorio)
        print("Laboratório cadastrado com sucesso!")
        

    def listar_laboratorios(self):
        print("Laboratórios cadastrados:")
        for laboratorio in self.laboratorios:
            print(f"Nome: {laboratorio.nome}")
            print(f"Endereço: {laboratorio.endereco}")
            print(f"Telefone: {laboratorio.telefone}")
            print(f"Cidade: {laboratorio.cidade}")
            print(f"Estado: {laboratorio.estado}")
            print("=" * 30)
    
    def buscar_laboratorio(self, nome_laboratorio):
        for lab in self.laboratorios:
            if lab.nome == nome_laboratorio:
                return lab
        return None