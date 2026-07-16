print()
print('PROJETO 3: Sistema de estoques') # TODO Status: Completo // total: 160 linhas
print()
opcoes = ('Adicionar produto', 'Listar todos os produtos', 'Buscar produto pelo nome', 'Atualizar preço ou quantidade', 'Remover produto', 'Relátorio geral', 'Sair') # Funcionalidades, total: 7 (NÃO ALTERAR A ORDEM!)

estoque = { # Todos o produtos devem conter nome, preço, quantidade e uma categoria!

}

def lin(char, qtd=30): # Função organizadora
    return print(char * qtd)

def funcionalidades(): # mostrar funcionalidades
    lin('-')
    for i, opcao in enumerate(opcoes, 1):
        print(f'{i}. {opcao}')
    print()
    print('OBS: sempre que quiser chamar a tabela, digite "tabela"!')
    lin('-')

def adicionar_produto(nome, preco, quantidade, categoria): # adicionar um produto
    estoque[nome] = {
        'preco': preco,
        'quantidade': quantidade,
        'categoria': categoria
    }
    lin('*')
    print('Adicionando...')
    lin('*')
    print('\nProduto adicionado!\n')


# Código principal
funcionalidades()
while True:
    print('Digite o número que deseja ou comando:')
    escolha = input('= ').lower().strip()
    print()

    if escolha == 'tabela': # CMD = tabela
        funcionalidades()

    elif escolha == '1': # Opção 1 (adicionar produto);

        nome_do_produto = input('Digite o nome do produto: ')
        preco_do_produto = float(input(f'Digite o preço de {nome_do_produto}: R$ '))
        quantidade_do_produto = int(input(f'Digite o estoque de {nome_do_produto}: '))
        categoria_do_produto = input(f'Digite a categoria de {nome_do_produto}: ')
        print()

        if nome_do_produto in estoque: # Produto já existe, pede confirmação
            print('Esse produto aparenta já está no estoque, tem certeza de adicionar ele?')
            entrada = input('(sim/não): ').lower().strip()
            print()
            if entrada == 'sim':
                adicionar_produto(nome_do_produto, preco_do_produto, quantidade_do_produto, categoria_do_produto)
                continue
            else:
                continue
        else: # Produto novo, adiciona direto
            adicionar_produto(nome_do_produto, preco_do_produto, quantidade_do_produto, categoria_do_produto)
            continue

    elif escolha == '2': # Opção 2 (listar todos os produtos);
        if not estoque:
            print('Adicione itens no estoque primeiro!')
            print()
            continue
        else:
            lin('*')
            print('Lista:')
            for i, (nome, dados) in enumerate(estoque.items(), 1):
                print(f'{i}. NOME: {nome} / PREÇO: {dados['preco']} / QUANTIDADE: {dados['quantidade']} / CATEGORIA: {dados['categoria']}')
            lin('*')

    elif escolha == '3': # Opção 3 (buscar produto pelo nome);
        if not estoque:
            print('Você não adicionou produtos ao estoque!')
        else:
            try:
                busca = input('Digite o nome do produto que procura: ')
            except ValueError:
                print('Digite uma opção válida.')
            else:
                if busca in estoque:
                    dados2 = estoque[busca]
                    lin('*')
                    print(f'Produto encontrado!')
                    print(f'Nome: {busca}')
                    print(f'Preço: R$ {dados2["preco"]:.2f}')
                    print(f'Quantidade: {dados2["quantidade"]}')
                    print(f'Categoria: {dados2["categoria"]}')
                    lin('*')
                else:
                    print('\nProduto não encontrado!\n')

    elif escolha == '4': # Opção 4 (Atualizar preço e quantidade);
        if not estoque:
            print('Você não adiciomou produtos ao estoques!')
        else:
            busca = input('Digite o nome do produto que procura: ')
            if busca in estoque:
                dados2 = estoque[busca]
                entrada = input('Desejar alterar o preço ou quantidade: ').lower().strip()
                if entrada == 'preço': # Preço
                    lin('*')
                    print(f'Preço atual: {dados2['preco']}')
                    try:
                        novo_preco = float(input('Novo preço: '))
                    except ValueError:
                        print('Valor inválido!')
                    else:
                        dados2['preco'] = novo_preco
                        print('\nPreço Atualizado\n')
                elif entrada == 'quantidade': # Quantidade
                    lin('*')
                    print(f'Quantidade atual: {dados2['quantidade']}')
                    try:
                        nova_quantidade = int(input('Nova quantidade: '))
                    except ValueError:
                        print('Valor inválido!')
                    else:
                        dados2['quantidade'] = nova_quantidade
                        print('\nQuantidade atualizada!\n')
                        lin('*')
                else:
                    print('\nEntrada inválida!\n')
                    continue
            else:
                print('\nProduto não encontrado!\n')
                continue

    elif escolha == '5': # Opção 5 (Remover produto);
        if not estoque:
            print('Você não adicionou produtos ao estoque!')
        else:
            excluir = input('Digite o nome do produto que deseja excluir: ')
            if excluir in estoque:
                del estoque[excluir]
                lin('*')
                print('Excluindo...')
                lin('*')
                print('\nProduto excluído!\n')
                continue
            else:
                print('\nProduto não encontrado!\n')
                continue

    elif escolha == '6': # Opção 6 (Relátorio Geral)
        if not estoque:
            print('Estoque vazio!')
        else:
            lin('-')
            print(f'Total de produtos cadastrados: {(len(estoque))}')
            print()
            valor_total_em_estoque = 0
            for nome, dados in estoque.items():
                valor_total_em_estoque += dados['preco'] * dados['quantidade']
            print(f'Valor total em produtos: {valor_total_em_estoque}')
            print()
            lin('*')
            print('Produtos com estoque vazio:')
            for nome, dados in estoque.items():
                if dados['quantidade'] == 0:
                    print(f'O produto {nome} está sem estoque!')
                else:
                    continue
            lin('*')
            print('\nRelátorio Finalizado!\n')
            lin('-')

    elif escolha == '7': # Opção 7 (Encerrar)
        entrada = input('DESEJA ENCERRAR (sim/não): ')
        if entrada == 'sim':
            lin('*')
            print('Encerrando . . .')
            lin('*')
            break
        else:
            continue

    else: # Opções inválidas
        print('Digite um comando válido!\n')

print('Obrigado por testar!!!!')