# Arquivo principal

from core.logica import (
    adicionar_produto, listar_produtos, buscar_produto, 
    editar_produto, excluir_produto, gerar_relatorio
)
from core.armazenamento import salvar_arquivo, carregar_arquivo
from core.organizacao import lin, menu

# Menus
funcionalidades = {
    "1": "Adicionar Produto",
    "2": "Listar Produtos",
    "3": "Buscar Produto",
    "4": "Editar Produto",
    "5": "Remover Produto",
    "6": "Relatório Geral",
    "7": "Sair"
}

edicoes = {
    "1": "Editar preço",
    "2": "Editar quantidade",
    "3": "Editar categoria",
    "4": "Voltar"
}

# Estoque
estoque = carregar_arquivo()

# Loop principal
lin("-")
menu(funcionalidades)
print('Digite "tabela" para visualizar o menu novamente!')
lin("-")

while True:
    print("\nDigite o número ou comando que deseja:")
    escolha = input("= ").strip().lower()
    print()

    if escolha == "tabela":
        lin("-")
        menu(funcionalidades)
        lin("-")

    elif escolha == "1":

        lin("-")
        try:
            nome = input("Digite o nome do produto: ")
            preco = input(f"Digite o preço de {nome.capitalize()}: ")
            quantidade = input(f"Digite a quantidade de {nome.capitalize()}: ")
            categoria = input(f"Digite a categoria de {nome.capitalize()}: ")

            produto = adicionar_produto(nome, preco, quantidade, categoria)
            estoque.append(produto)
            print("\nProduto cadastrado com sucesso!\n")

            salvar_arquivo(estoque)

        except ValueError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "2":

        lin("-")
        listar_produtos(estoque)
        lin("-")

    elif escolha == "3":

        lin("-")
        produto_buscado = input("\nDigite o nome do produto buscado: ")

        buscar_produto(produto_buscado, estoque)
        lin("-")


    elif escolha == "4":

        lin("-")
        produto_buscado = input("\nDigite o nome do produto buscado para edição: ").strip().lower()

        # Busca produto
        encontrado = False
        produto_editar = None

        for produto in estoque:
            if produto["produto"].lower().strip() == produto_buscado.lower().strip():
                encontrado = True
                produto_editar = produto
                break
        else:
            if not encontrado:
                print("\nProduto não encontrado!\n")
                lin("-")
                continue

        # Edições:
        while True:
            lin("*")
            menu(edicoes)
            lin("*")

            escolha_edicao = input(f"\nDigite o número que deseja editar em {produto_editar["produto"].capitalize()}: ").lower().strip()

            if escolha in ["1", "2", "3"]:
                editar_produto(escolha_edicao, produto_editar)
                salvar_arquivo(estoque)

            elif escolha == "4":
                print("\nEncerrando edições...\n")
                break

            else:
                print("\nDigite uma opção válida!\n")

        lin("-")

    elif escolha == "5":
        pass

    elif escolha == "6":
        pass

    elif escolha == "7":
        print("\nEncerrando...\n")
        break