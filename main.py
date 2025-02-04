print("""
      𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
      """)

menu_opcoes = ["Cadastrar Resturante", "Listar Restaurantes", "Ativar Restaurante", "Sair"]

for indice, opcao in enumerate(menu_opcoes):
    print(f"[{indice}] - {opcao}")

indice_escolhido = int(input("\nO que deseja fazer? "))