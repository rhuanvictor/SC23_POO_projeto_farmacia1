from clientes import Cliente
from clientes import CadastroCliente
from medicamentos import Quimioterapicos
class Venda:
    def __init__(self, data_hora: str, produtos_vendidos: list, cliente: Cliente, valor_total: float) -> None:
        self.data_hora = data_hora
        self.produtos_vendidos = produtos_vendidos
        self.cliente = cliente
        self.valor_total = valor_total
        self.clientes = CadastroCliente()
        
    
    
    def efetuar_venda(farmacia):
        cpf_cliente = input("Digite o CPF do cliente: ")
        nome_medicamento = input("Digite o nome do medicamento: ")
        data_hora = input("Digite a data e hora da venda: ")

        cliente = farmacia.clientes.buscar_cliente_por_cpf(cpf_cliente)
        if cliente:
            medicamento = farmacia.medicamentos.buscar_medicamento_por_nome1(nome_medicamento)
            if medicamento:
                # Verificar se o medicamento é um quimioterápico e necessita de receita
                if isinstance(medicamento, Quimioterapicos) and medicamento.receita:
                    possui_receita = input("Este medicamento requer receita médica. Você possui uma receita? (S/N): ").lower()
                    if possui_receita == 's':
                        
                        produtos_venda = [medicamento]
                        valor_total = medicamento.preco

                        if cliente.calcular_idade() > 65:
                            valor_desconto = valor_total * 0.2
                            valor_total -= valor_desconto
                        elif valor_total > 150:
                            valor_desconto = valor_total * 0.1
                            valor_total -= valor_desconto

                        venda = Venda(data_hora, produtos_venda, cliente, valor_total)
                        farmacia.vendas.append(venda)

                        # Exibir informações da venda
                        print(f"Venda efetuada com sucesso!\n"
                            f"Preço original: R${medicamento.preco:.2f}\n"
                            f"Preço com desconto: R${valor_total:.2f}")
                    else:
                        print("Compra não autorizada. Medicamento requer receita médica.")
                else:
                    
                    produtos_venda = [medicamento]
                    valor_total = medicamento.preco

                    if cliente.calcular_idade() > 65:
                        valor_desconto = valor_total * 0.2
                        valor_total -= valor_desconto
                    elif valor_total > 150:
                        valor_desconto = valor_total * 0.1
                        valor_total -= valor_desconto

                    venda = Venda(data_hora, produtos_venda, cliente, valor_total)
                    farmacia.vendas.append(venda)

                    # Exibir informações da venda
                    print(f"Venda efetuada com sucesso!\n"
                        f"Preço original: R${medicamento.preco:.2f}\n"
                        f"Preço com desconto: R${valor_total:.2f}")
            else:
                print("Medicamento não cadastrado.")
        else:
            print("Cliente não encontrado.")


    def imprimir_venda(self):
        print("Data e Hora da Venda:", self.data_hora)
        print("Produtos Vendidos:")
        for produto in self.produtos_vendidos:
            print("Nome:", produto.nome)
            print("Composto:", produto.comp_principal) 
            
        if self.cliente is not None:
            print("Cliente:")
            print("Nome:", self.cliente.nome)
            print("CPF:", self.cliente.cpf)
        else:
            print("Cliente não encontrado.")
        print("Valor Total:", self.valor_total)