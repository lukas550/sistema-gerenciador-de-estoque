# Módulo para a lógica do main.py, funções do CRUD, incluindo: Adicionar Produto, Listar Produtos, Buscar Produto, Editar Produto, Excluir Produto e Relatório

def adicionar_produto(nome, preco, quantidade, categoria):

    if not nome.strip() or not categoria.strip():
        raise ValueError("\nNome e categoria são obrigatórios!\n")

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
            print(f"- Nome: {produto['produto'].capitalize()} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']} | Categoria: {produto['categoria'].capitalize()}")

def buscar_produto(produto_buscado, estoque):

    if not estoque or not produto_buscado.strip().lower():
        print("\nEstoque ou produto buscado inválidos!\n")

    else:
        encontrado = False

        for produto in estoque:
            if produto["produto"].lower().strip() == produto_buscado.strip().lower():
                print(f"\n- Nome: {produto['produto'].capitalize()} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']} | Categoria: {produto['categoria'].capitalize()}")

                encontrado = True
                break

        if not encontrado:
            print(f"\nO produto {produto_buscado} não foi encontrado!\n")

def editar_produto(escolha, produto_editado):

    if escolha.strip() == "1":
        print(f"Preço antigo: {produto_editado['preco']}")
        try:
            novo_valor = float(input("\nDigite o novo valor: "))

            if novo_valor < 0:
                raise ValueError

            produto_editado["preco"] = novo_valor
            print(f"\nO valor de {produto_editado['produto'].capitalize()} foi atualizado!\n")

        except ValueError:
            print("\nNovo valor inválido!\n")

    elif escolha.strip() == "2":
        print(f"Quantidade antiga: {produto_editado['quantidade']}")
        try:
            nova_quantidade = int(input("\nDigite a nova quantidade: "))

            if nova_quantidade < 0:
                raise ValueError

            produto_editado["quantidade"] = nova_quantidade
            print(f"\nA quantidade de {produto_editado['produto'].capitalize()} foi atualizada!\n")

        except ValueError:
            print("\nNova quantidade inválida!\n")

    elif escolha.strip() == "3":
        print(f"Categoria antiga: {produto_editado['categoria']}")

        nova_categoria = input(f"Nova categoria de {produto_editado['produto'].capitalize()}: ").lower().strip()

        produto_editado['categoria'] = nova_categoria
        print(f"\nA categoria de {produto_editado['produto'].capitalize()} foi atualizada!\n")

def excluir_produto(produto_para_excluir, estoque):

    if not produto_para_excluir.strip().lower() or not estoque:
        print("\nProduto ou estoque inválidos!\n")

    else:
        encontrado = False
        for produto in estoque:
            if produto["produto"].lower().strip() == produto_para_excluir.strip().lower():
                produto_encontrado = produto

                encontrado = True
                break

        if not encontrado:
            print(f"\nProduto {produto_para_excluir.capitalize()} não encontrado!\n")

            return  
        else:
            return produto_encontrado

def gerar_relatorio(estoque):

    if not estoque:
        print("\nSem produtos no estoque!\n")
        return

    else:

        total_quantidade = 0
        total_investido = 0.0

        mais_caro = max(estoque, key=lambda p: p["preco"])
        mais_barato = min(estoque, key=lambda p: p["preco"])

        baixo_estoque = [p for p in estoque if p["quantidade"] < 5]

        for produto in estoque:
            total_quantidade += produto["quantidade"]
            total_investido += produto["preco"] * produto["quantidade"]

        preco_medio = total_investido / total_quantidade if total_quantidade > 0 else 0.0

        relatorio = {
            "total_quantidade": total_quantidade,
            "total_investido": total_investido,
            "mais_caro": mais_caro,
            "mais_barato": mais_barato,
            "baixo_estoque": baixo_estoque,
            "preco_medio": preco_medio
        }

        return relatorio