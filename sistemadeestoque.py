funcionalidades = {
    "1": "Adicionar Produto",
    "2": "Listar Produtos",
    "3": "Buscar Produto",
    "4": "Atulizar preço/quantidade",
    "5": "Remover produto",
    "6": "Relátorio Geral",
    "7": 'Sair'
}

estoque = {

}
"""
Estrutura dos dados:
produto = {
    preco: float,
    quantidade: int,
    categoria: string
}
"""

# Funções organizadoras e estruturais
def lin(char, qtd=30): # Função organizadora
    return print(char * qtd)

def menu(): # mostrar menu
    lin('-')
    for nu, funcionalidade in funcionalidades.items():
        print(f'{nu}. {funcionalidade}')
    lin('-')

# Funções operacionais
def adicionar_produto():
        nome_do_produto = input("Digite o nome do produto: ").lower().strip()

        if nome_do_produto in estoque:
            escolha = input("Esse produto já está cadastrado no estoque, deseja continuar mesmo assim?\n").lower().strip()
            if escolha in ["não", 'nao', "nn", "n"]:
                return

        while True:
            try:
                preco_do_produto = float(input(f"Digite o preço de {nome_do_produto.capitalize()}: "))
                quantidade_do_produto = int(input(f"Digite a quantidade de {nome_do_produto.capitalize()}: "))
                categoria_do_produto = input(f"Digite a categoria de {nome_do_produto.capitalize()}: ")
            except ValueError:
                print("\nDigite um valor válido!\n")
                continue
            else:
                estoque[nome_do_produto] = {
                    "preco": preco_do_produto,
                    "quantidade": quantidade_do_produto,
                    "categoria": categoria_do_produto
                }
                print("\nProduto Cadastrado!\n")
                break

# Código principal
menu()
print('OBS: sempre que quiser chamar a tabela, digite "tabela"!')
while True:
    print("\nDigite o número que deseja ou comando:")
    escolha = input('= ').lower().strip()
    print()

    if escolha == 'tabela': # CMD = tabela
        menu()

    elif escolha == 'teste': # TEMPÓRARIO
        print(estoque)

    elif escolha == '1': # Opção 1 (adicionar produto);

        lin('-')
        adicionar_produto()
        lin('-')

    elif escolha == '2': # Opção 2 (listar todos os produtos);
        pass

    elif escolha == '3': # Opção 3 (buscar produto pelo nome);
        pass

    elif escolha == '4': # Opção 4 (Atualizar preço e quantidade);
        pass

    elif escolha == '5': # Opção 5 (Remover produto);
        pass

    elif escolha == '6': # Opção 6 (Relátorio Geral)
        pass

    elif escolha == '7': # Opção 7 (Encerrar)
        pass

    else: # Opções inválidas
        print('Digite um comando válido!\n')