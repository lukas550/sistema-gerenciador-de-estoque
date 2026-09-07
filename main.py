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
        pass

    elif escolha == "2":
        pass

    elif escolha == "3":
        pass

    elif escolha == "4":
        pass

    elif escolha == "5":
        pass

    elif escolha == "6":
        pass

    elif escolha == "7":
        print("\nEncerrando...\n")
        break