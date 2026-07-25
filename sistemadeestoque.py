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
"""
Estrutura dos dados:
Produto = {
    Preco: float,
    Quantidade: int,
    Categoria: string
}
"""
}

# Funções organizadoras e estruturais
def lin(char, qtd=30): # Função organizadora
    return print(char * qtd)

def funcionalidades(): # mostrar funcionalidades
    lin('-')
    for nu, funcionalidade in funcionalidades.items():
        print(f'{nu}. {funcionalidade}')
    print()
    print('OBS: sempre que quiser chamar a tabela, digite "tabela"!')
    lin('-')

# Código principal
funcionalidades()
while True:
    print('Digite o número que deseja ou comando:')
    escolha = input('= ').lower().strip()
    print()

    if escolha == 'tabela': # CMD = tabela
        funcionalidades()

    elif escolha == '1': # Opção 1 (adicionar produto);
        pass

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