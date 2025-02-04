import os

# funções:

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_nome_programa():
    print("""
        𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
        """)

def exibir_menu():
    menu_opcoes = ["Cadastrar Resturante", "Listar Restaurantes", "Ativar Restaurante", "Sair"]

    for indice, opcao in enumerate(menu_opcoes):
        print(f"[{indice}] - {opcao}")

def encerrar_aplicacao():
    limpar_tela()
    print("Encerrando Aplicação")

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
        print("Cadastro de Restaurante")
    elif indice_escolhido == 1:
        print("Listar Restaurante")
    elif indice_escolhido == 2:
        print("Listar Restaurante")
    else:
        encerrar_aplicacao()

def main():
    limpar_tela()
    exibir_nome_programa()
    exibir_menu()
    escolhendo_opcao()

if __name__ == "__main__":
    main()