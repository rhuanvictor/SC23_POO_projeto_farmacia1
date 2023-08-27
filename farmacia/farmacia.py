from clientes import CadastroCliente
from medicamentos import CadastroMedicamentos, Quimioterapicos, Fitoterapicos
#from medicamentos import CadastroMedicamentos
#from  import Venda
from laboratorios import CadastroLaboratorios



class Farmacia:
    def __init__(self):
        self.clientes = CadastroCliente()
        self.medicamentos = CadastroMedicamentos()
        self.laboratorios = CadastroLaboratorios()
        self.vendas = []        
        

    def emitir_relatorio(self):
        print("Relatório de Vendas e Estatísticas")
        print("=" * 30)

        # Estatísticas dos atendimentos realizados no dia
        remedio_mais_vendido = None
        max_quantidade = 0
        total_vendas = 0
        total_quimioterapicos = 0
        total_fitoterapicos = 0
        total_vendas2 = len(self.vendas)
        
        for venda in self.vendas:
            total_vendas += 1
            for produto in venda.produtos_vendidos:
                if isinstance(produto, Quimioterapicos):
                    total_quimioterapicos += 1
                elif isinstance(produto, Fitoterapicos):
                    total_fitoterapicos += 1

                if venda.produtos_vendidos.count(produto) > max_quantidade:
                    max_quantidade = venda.produtos_vendidos.count(produto)
                    remedio_mais_vendido = produto

        print("Estatísticas dos Atendimentos")
        print("Total de Atendimentos:", total_vendas)
        print("Total de Atendimentos com Remédios Quimioterápicos:", total_quimioterapicos)
        print("Total de Atendimentos com Remédios Fitoterápicos:", total_fitoterapicos)

        if remedio_mais_vendido:
            print("Remédio mais vendido:")
            print("Nome:", remedio_mais_vendido.nome)
            print("Quantidade vendida:", total_vendas2)
            print("Valor total:", remedio_mais_vendido.preco * max_quantidade)
        else:
            print("Nenhum remédio vendido.")

        # Listagem de clientes cadastrados por nome em ordem alfabética crescente
        print("\nListagem de Clientes Cadastrados")
        print("=" * 30)
        clientes_ordenados = sorted(self.clientes.cadastrados.values(), key=lambda x: x.nome)
        for cliente in clientes_ordenados:
            print(cliente)

        # Listagem de medicamentos por ordem alfabética
        print("\nListagem de Medicamentos por Ordem Alfabética")
        print("=" * 30)
        medicamentos_ordenados = sorted(self.medicamentos.medicamentos, key=lambda x: x.nome)
        for medicamento in medicamentos_ordenados:
            print(medicamento)

        # Listagem de medicamentos quimioterápicos ou fitoterápicos
        print("\nListagem de Medicamentos Quimioterápicos ou Fitoterápicos")
        print("=" * 30)
        for medicamento in self.medicamentos.medicamentos:
            if isinstance(medicamento, Quimioterapicos) or isinstance(medicamento, Fitoterapicos):
                print(medicamento)

        print("=" * 30)
