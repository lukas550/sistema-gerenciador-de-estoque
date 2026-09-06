# Módulo para a lógica do main.py, funções do CRUD, incluindo: Adicionar Produto, Listar Produtos, Buscar Produto, Editar Produto, Excluir Produto e Relatório

def adicionar_produto(nome, preco, quantidade, categoria):

    if not nome.strip() or not categoria.strip():
        raise ValueError("\nNome e categoria são obrigatório!\n")

    try:
        preco_float = float(preco)
        quantidade_int = int(quantidade)

        if preco_float < 0 or quantidade_int < 0:
            raise ValueError("\nPreço e quantidade não podem ser negativos!\n")

    except (ValueError, TypeError):
        raise ValueError("\nPreço ou quantidade inválidos!\n")

    produto = {
        "produto": nome.strip().lower(),
        "preco": preco_float,
        "quantidade": quantidade_int,
        "categoria": categoria.strip().lower()
    }

    return produto

def listar_produtos(estoque):

    if not estoque:
        print("\nSem produtos no estoque!\n")
    else:
        for produto in estoque:
            print(f"- Nome: {produto['produto']} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']} | Categoria: {produto['categoria']}")

def buscar_produto(produto_buscado, estoque):

    if not estoque or not produto_buscado.strip().lower():
        print("\nEstoque ou produto buscado inválidos!\n")
    else:
        encontrado = False

        for produto in estoque:
            if produto["produto"].lower().strip() == produto_buscado.strip().lower():
                print(f"\n- Nome: {produto['produto']} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']} | Categoria: {produto['categoria']}")

                encontrado = True
                break

        if not encontrado:
            print(f"\nO produto {produto_buscado} não foi encontrado!\n")

def editar_produto():
    pass

def excluir_produto():
    pass

def gerar_relatorio():
    pass