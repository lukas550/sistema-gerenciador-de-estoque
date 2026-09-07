# Módulo para a organização do main.py

def lin(char, qtd=30):
    # Imprime linha decorativa no terminal
    print(char * qtd)

def menu(obj):
    # Exibe as opções de um menu a partir de um dicionário.
    if isinstance(obj, dict):
        for nu, opcao in obj.items():
            print(f"{nu}. {opcao}")
    else:
        raise TypeError(f"\nObjeto inválido! Esperado dict, recebido {type(obj).__name__}\n")