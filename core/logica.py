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
            print(f"- Nome: {produto['produto']} | Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']} | Categoria: {produto['categoria']}")

def buscar_produto():
    pass

def editar_produto():
    pass

def excluir_produto():
    pass

def gerar_relatorio():
    pass