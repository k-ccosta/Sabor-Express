import os

restaurantes = [
    {"nome":"Dogão do Kelvin", "categoria":"lanchonete", "status":False}
]

# funções:

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def retornar_menu_principal():

    opcoes = ["Retornar ao Menu Principal", "Encerrar Aplicação"]

    print("\nO que deseja fazer?\n")

    for indice, opcao in enumerate(opcoes):
        print(f"[{indice}] - {opcao}")
    
    resposta = int(input("\n> "))

    if resposta == 0:
        main()
    else:
        encerrar_aplicacao()

def exibir_nome_programa():
    print("""
        𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
        """)
def exibir_menu():
    menu_opcoes = ["Cadastrar Resturante", "Listar Restaurantes", "Alterar Status Restaurante", "Sair"]

    for indice, opcao in enumerate(menu_opcoes):
        print(f"[{indice}] - {opcao}")
def encerrar_aplicacao():
    limpar_tela()
    print("Encerrando Aplicação")

def cadastrar_restaurante():
    limpar_tela()

    print("""
          ℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕠 𝕕𝕖 ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖
          """)

    restaurante = {
        "nome" : input("Digite o nome do restaurante: "),
        "categoria" : input("Informe a categoria do restaurante: "),
        "status":False
    }

    restaurantes.append(restaurante)

    retornar_menu_principal()

def listar_restaurantes():
    limpar_tela()

    print("""
          𝕃𝕚𝕤𝕥𝕒 𝕕𝕖 ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤
          """)

    for restaurante in restaurantes:
        print(f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}")
        print(f"{restaurante["nome"].ljust(20)} | {restaurante["categoria"].ljust(20)} | {'Ativo' if restaurante["status"] else 'Desativado'}")

    retornar_menu_principal()

def alterar_status_restaurante():

    # limpar_tela()

    # listar_restaurantes()

    # indice = int(input("\nInforme o indice do restaurante que deseja alterar o status: "))

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True

            restaurante["status"] = not restaurante["status"]

            print(f"O restaurante foi {'ativado' if restaurante["status"] == True else 'desativado'} com sucesso.")
        
        if not restaurante_encontrado:
            print("Restaurante não encontrado")

    retornar_menu_principal()    

def escolhendo_opcao():
    while True:
        try:
            indice_escolhido = int(input("\nO que deseja fazer? "))

            if indice_escolhido in range(4):
                break
            else:
                print(f"\nOPÇÃO INVÁLIDA! Por favor, escolha uma opção entre 0 e 3\n")                
        except ValueError:
            print("\nOPÇÃO INVÁLIDA! Por favor, digite um número inteiro")
        
    if indice_escolhido == 0:
        cadastrar_restaurante()
    elif indice_escolhido == 1:
        # limpar_tela()
        listar_restaurantes()
        # retornar_menu_principal()
    elif indice_escolhido == 2:
        alterar_status_restaurante()
    else:
        encerrar_aplicacao()

def main():
    limpar_tela()
    exibir_nome_programa()
    exibir_menu()
    escolhendo_opcao()

if __name__ == "__main__":
    main()