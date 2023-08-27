from farmacia import Farmacia
from vendas import Venda 

def exibir_menu():
    print("1.  Cliente/Cadastro/Alteração/Consulta")
    print("2.  Medicamento Quimioterápico/Fitoterápico")
    print("3.  Laboratório/Cadastro/Listar")    
    print("4.  Efetuar Venda")
    print("5.  Emitir Relatórios")
    print("6. Sair")

def menu_clientes():
    print("Menu de Gerenciamento de Clientes:")
    print("0. Voltar para o menu principal")
    print("1. Cadastrar novo cliente")
    print("2. Consultar cliente")
    print("3. Alterar dados do cliente")
    
def menu_medicamentos():
    print("Menu de Medicamentos:")
    print("0.  Voltar para o menu principal")
    print("1.  Cadastrar Medicamento Quimioterápico")
    print("2.  Cadastrar Medicamento Fitoterápico")
    print("3.  Buscar Medicamento por Nome")

def menu_laboratorios():
    print("Menu de Laboratorios:")
    print("0.  Voltar para o menu principal")
    print("1.  Cadastrar Laboratórios")
    print("2.  Listar Laboratórios Cadastrados")

def main():
    farmacia = Farmacia()
    opcao = None
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
         
        if opcao == "1":
            sub_opcao = None
            while sub_opcao != "0":
                menu_clientes()
                sub_opcao = input("Escolha uma opção: ")

                if sub_opcao == "1":
                    farmacia.clientes.cadastrar_novo()
                elif sub_opcao == "2":
                    cpf = input("Digite o CPF do cliente: ")  
                    farmacia.clientes.visualizar_cadastro(cpf)
                elif sub_opcao == "3":
                    cpf = input("Digite o CPF do cliente: ")
                    farmacia.clientes.alterar_cadastro(cpf)
                elif sub_opcao == "0":
                    print("Voltando para tela anterior")
                else:
                    print("Opção inválida")                  
        elif opcao == "2":
            sub_opcao = None
            while sub_opcao != "0":
                menu_medicamentos()
                sub_opcao = input("Escolha uma opção: ")

                if sub_opcao == "1":
                    farmacia.medicamentos.cadastrar_medicamento(farmacia.laboratorios,'quimioterapico')
                elif sub_opcao == "2":
                    farmacia.medicamentos.cadastrar_medicamento(farmacia.laboratorios,'fitoterapico')
                elif sub_opcao == "3":
                    farmacia.medicamentos.buscar_medicamento_por_nome() 
                elif sub_opcao == "0":
                    print("Voltando para tela anterior")
                else:
                    print("Opção inválida")           
       
        elif opcao == "3":
            sub_opcao = None
            while sub_opcao != "0":
                menu_laboratorios()
                sub_opcao = input("Escolha uma opção: ")

                if sub_opcao == "1":
                    farmacia.laboratorios.cadastrar_laboratorio()
                elif sub_opcao == "2":
                    farmacia.laboratorios.listar_laboratorios()
                elif sub_opcao == "0":
                    print("Voltando para tela anterior")
                else:
                    print("Opção inválida")          
                       
        elif opcao == "4":
            Venda.efetuar_venda(farmacia)
            # if len(farmacia.vendas) > 0:
            #     ultima_venda = farmacia.vendas[-1]
            #     ultima_venda.imprimir_venda()
        elif opcao == "5":
            farmacia.emitir_relatorio()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()