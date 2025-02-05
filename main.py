import os
import string

# variáveis globais
menu_opcoes = ["Cadastrar Restaurante", "Listar Restaurantes", "Alterar Status do Restaurante", "Sair"]

restaurantes_cadastrados = [
    {"nome_restaurante":"Duka Doces", "categoria":"Doceria", "status":True}
]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
def retornar_menu_principal():
    opcoes = ["Retornar ao Menu Principal", "Encerrar Aplicação"]

    print("\nO que deseja fazer? \n")

    for indice, opcao in enumerate(opcoes):
        print(f"[{indice}] - {opcao}")

    while True:
        try:
            resposta = int(input("\n> "))

            if resposta in range(len(opcoes)):
                break
            else:
                print("\nOPÇÃO INVÁLIDA! Por favor, digite 0 ou 1")                 
        except ValueError:
            print("\nOPÇÃO INVÁLIDA! Por favor, digite um n° inteiro")    

    if resposta == 0:
        limpar_tela()
        main()
    else:
        limpar_tela()
        encerrar_aplicacao()

def cadastrar_restaurante():
    limpar_tela()
    print("""
          ℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕠 𝕕𝕖 ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖
          """)
    
    restaurante = {
        "nome_restaurante":string.capwords(input("Digite o nome do restaurante: ")),
        "categoria":string.capwords(input("Digite a categoria do restaurante: ")),
        "status":False
    }

    restaurantes_cadastrados.append(restaurante)

    retornar_menu_principal()
def listar_restaurantes():
    limpar_tela()

    print(f"{"Nome Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}")

    for restaurante in restaurantes_cadastrados:
        print(f"{restaurante["nome_restaurante"].ljust(25)} | {restaurante["categoria"].ljust(25)} | {'Ativo' if restaurante["status"] else 'Desativado'}")

    retornar_menu_principal() 
def alterar_status_restaurante():
    limpar_tela()

    nome_restaurante_digitado = input("\nDigite o nome do restaurante: ")

    for restaurante in restaurantes_cadastrados:
        if nome_restaurante_digitado == restaurante["nome_restaurante"]:
            restaurante["status"] = not restaurante["status"]

            print(f"\nO restaurante foi {'ativado' if restaurante["status"] == True else 'desativado'} com sucesso.")

    retornar_menu_principal()
def encerrar_aplicacao():
    limpar_tela()
    print("Aplicação Encerrada!")

def exibir_titulo():
    print("""
          𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
          """)
def exibir_menu():
    for indice, opcao in enumerate(menu_opcoes):
        print(f"[{indice}] - {opcao}")
def escolher_menu():
    while True:
        try:
            opcao_escolhida = int(input("\nO que você quer fazer? "))

            if opcao_escolhida in range(len(menu_opcoes)):
                break
            else:
                print(f"\nOPÇÃO INVÁLIDA! Por favor, selecione uma opção entre 0 e {len(menu_opcoes)-1}")                
        except ValueError:
            print("\nOPÇÃO INVÁLIDA! Por favor, informe um n° inteiro")
    
    if opcao_escolhida == 0:
        cadastrar_restaurante()
    elif opcao_escolhida == 1:
        listar_restaurantes()
    elif opcao_escolhida == 2:
        alterar_status_restaurante()
    else:
        encerrar_aplicacao()

def main():
    exibir_titulo()
    exibir_menu()
    escolher_menu()

if __name__ == "__main__":
    main()