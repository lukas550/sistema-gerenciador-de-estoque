funcionalidades = {
    "1": "Adicionar Produto",
    "2": "Listar Produtos",
    "3": "Buscar Produto",
    "4": "Editar produto",
    "5": "Remover produto",
    "6": "Relátorio Geral",
    "7": 'Sair'
}
edicoes = {
    "1": "Editar preço",
    "2": "Editar quantidade",
    "3": "Editar categoria",
    "4": "Sair"
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
    print(char * qtd)

def menu(opcoes=False, edicao=True): # mostrar menu
    lin('-')
    if opcoes:
        for nu, funcionalidade in funcionalidades.items():
            print(f"{nu}. {funcionalidade}")
    if edicao:
        for nu, edit in edicoes.items():
            print(f"{nu}. {edit}")
    lin('-')

# Funções operacionais
def adicionar_produto(): # Opção 1
    nome_do_produto = input("Digite o nome do produto: ").lower().strip()

    if not nome_do_produto:
        print("\nO nome do produto não pode ser vazio!\n")
        return

    if nome_do_produto in estoque:
        escolha = input("Esse produto já está cadastrado no estoque. Deseja sobreescrever os dados?\n").lower().strip()
        if escolha not in ["sim", "ss", "s"]:
            print("\nOperação cancelada.\n")
            return

    while True: # Validação do preço
        try:
            preco_do_produto = float(input(f"Digite o preço de {nome_do_produto.capitalize()}: "))
            if preco_do_produto < 0:
                print("\nO preço do produto não pode ser negativo!\n")
                continue
            break
        except ValueError:
            print("\nDigite um valor númerico válido ao preço!\n")

    while True: # Validação de quantidade
        try:
            quantidade_do_produto = int(input(f"Digite a quantidade de {nome_do_produto.capitalize()}: "))
            if quantidade_do_produto < 0:
                print("\nA quantidade não pode ser negativa!\n")
                continue
            break
        except ValueError:
            print("\nDigite um valor inteiro válido a quantidade!\n")

    categoria_do_produto = input(f"Digite a categoria de {nome_do_produto.capitalize()}")

    estoque[nome_do_produto] = {
        "preco": preco_do_produto,
        "quantidade": quantidade_do_produto,
        "categoria": categoria_do_produto
    }
    print("\nProduto Cadastrado!\n")

def listar_produtos(): # Opção 2
    for produto in estoque:
        dados = estoque[produto]
        print(f"- {produto.capitalize()} / Preço: {dados['preco']:.2f} / Quantidade: {dados['quantidade']} / Categoria: {dados['categoria']}")

def buscar_produto(): # Opção 3
    busca = input("Qual produto deseja buscar: ").lower().strip()

    if busca in estoque:
        dados = estoque[busca]
        print(f"Nome: {busca.capitalize()} / Preço: {dados['preco']:.2f} / Quantidade: {dados['quantidade']} / Categoria: {dados['categoria']}")
    else:
        print("\nProduto não encontrado!\n")

def editar_produto(produto): # Opção 4
    menu(False, True)
    print('\nSempre que quiser chamar a tabela, digite "tabela"!')
    while True:
        print("\nDigite o número que deseja ou comando:")
        escolha = input('= ').lower().strip()
        print()
        if escolha == "tabela":

            menu(False, True)
        
        elif escolha == "1":
            print(f"Preço antigo: {estoque[produto]['preco']:.2f}")
            while True:
                try:
                    novo_preco = float(input(f"Digite o novo preço de {produto.capitalize()}: "))
                except ValueError:
                    print("\nDigite um valor válido!\n")
                else:
                    estoque[produto]["preco"] = novo_preco
                    print(f"\nPreço de {produto.capitalize()} atulizado!\n")
                    break

        elif escolha == "2":
            print(f"Quantidade antiga: {estoque[produto]['quantidade']}")
            while True:
                try:
                    nova_quantidade = int(input(f"Digite a nova quantidade de {produto.capitalize()}: "))
                except ValueError:
                    print("\nDigite um valor válido!\n")
                else:
                    estoque[produto]["quantidade"] = nova_quantidade
                    print(f"\nQuantidade de {produto.capitalize()} atualizada!")
                    break

        elif escolha == "3":
            print(f"Categoria antiga: {estoque[produto]['categoria']}")
            nova_categoria = input(f"Digite a nova categoria de {produto.capitalize()}: ")

            estoque[produto]["categoria"] = nova_categoria
            print(f"\nCategoria de {produto.capitalize()} atualizada!")
                
        elif escolha == "4":
            print("\nEncerrando...\n")
            break

def excluir_produto(produto): # Opção 5
    while True:
        escolha = input(f"Tem certeza que deseja excluir {produto.capitalize()}? Essa ação é IRREVERSÍVEL\n").lower().strip()

        if escolha in ["sim", "ss", "s"]:
            print("\nProduto excluido!\n")
            del estoque[produto]
            break
        elif escolha in ["nao", "não", "nn", "n"]:
            print("\nAção interrompida.\n")
            break
        else:
            print("\nDigite algo válido!\n")

def relatorio_geral():

    total_quantidade = 0
    total_investido = 0.0

    mais_caro = max(estoque, key=lambda p: estoque[p]["preco"])
    mais_barato = min(estoque, key=lambda p: estoque[p]["preco"])

    baixo_estoque = [p for p in estoque if estoque[p]["quantidade"] < 5]

    for produto in estoque:
        dados = estoque[produto]
        total_quantidade += dados["quantidade"]
        total_investido += dados["preco"] * dados["quantidade"]

    preco_medio = total_investido / total_quantidade if total_quantidade > 0 else 0.0

    # Principal
    lin('-')
    print("[1] Resumo Financeiro e de estoque")
    lin('-')
    print()

    print(f"* Total de produtos cadastrados: {len(estoque)}")
    print(f"* Total em quantidade no estoque: {total_quantidade}")
    print(f"* Valor total investido: {total_investido:.2f}")
    print(f"* Preço médio dos produtos: {preco_medio:.2f}")
    print()

    lin('-')
    print("[2] Destaques")
    lin('-')
    print()

    print(f"* Produto mais caro: {mais_caro.capitalize()} (R$ {estoque[mais_caro]['preco']:.2f})")
    print(f"* Produto mais barato: {mais_barato.capitalize()} (R$ {estoque[mais_barato]['preco']:.2f})")
    if not baixo_estoque:
        print("\nTodos os produtos estão reeabastecidos!\n")
    else:
        lin('~', 40)
        print("     Produtos em baixo estoque ou sem estoque     ")
        lin('~', 40)
        for p in baixo_estoque:
            print(f"- {p.capitalize()}: {estoque[p]['quantidade']} unidades")


# Código principal
menu(True, False)
print('OBS: sempre que quiser chamar a tabela, digite "tabela"!')
while True:
    print("\nDigite o número que deseja ou comando:")
    escolha = input('= ').lower().strip()
    print()

    if escolha == 'tabela': # tabela
        menu(True, False)

    elif escolha == '1': # Opção 1 (adicionar produto);

        lin('-')
        adicionar_produto()
        lin('-')

    elif escolha == '2': # Opção 2 (listar todos os produtos);

        lin('*')
        if not estoque:
            print("\nSem produtos no estoque!\n")
        else:
            listar_produtos()
        lin('*')

    elif escolha == '3': # Opção 3 (buscar produto pelo nome);

        lin('-')
        if not estoque:
            print("\nSem produtos no estoque!\n")
        else:
            buscar_produto()
        lin('-')

    elif escolha == '4': # Opção 4 (Atualizar preço e quantidade);

        lin('-')
        if not estoque:
            print("\nSem produtos no estoque!\n")
        else:
            busca = input("Digite o nome do produto que deseja editar:\n").lower().strip()

            if busca in estoque:
                editar_produto(busca)
            else:
                print("\nProduto não encontrado!\n")
        lin('-')

    elif escolha == '5': # Opção 5 (Remover produto);

        lin('-')
        if not estoque:
            print("\nSem produtos no estoque!\n")
        else:
            busca = input("Digite o nome do produto que deseja excluir:\n").lower().strip()

            if busca in estoque:
                excluir_produto(busca)
            else:
                print("\nProduto não encontrado!\n")
        lin('-')

    elif escolha == '6': # Opção 6 (Relátorio Geral)

        lin('-')
        if not estoque:
            print("\nSem produtos no estoque!\n")
        else:
            lin('=', 40)
            print("     RELATÓRIO GERAL     ")
            lin('=', 40)
            relatorio_geral()
        lin('-')

    elif escolha == '7': # Opção 7 (Encerrar)
        print("\nEncerrando...\n")
        break

    else: # Opções inválidas
        print('Digite um comando válido!\n')