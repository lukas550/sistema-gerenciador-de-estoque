# Módulo para o salvar e carregar os arquivos JSON, usado para a pesistência dos dados.
import json

"""
Estrutura de um arquivo:
[
    {
        "produto": str,
        "preco": float,
        "quantidade": int,
        "categoria": str
    }
]
"""

ARQUIVO = "estoque.json"

def salvar_arquivo(dados_a_salvar):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(dados_a_salvar, f, indent=4, ensure_ascii=False)

        print("\nArquivo Salvo!\n")

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"\nErro no salvamento do arquivo: {e}\n")

def carregar_arquivo():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)

            return dados

    except FileNotFoundError:
        salvar_arquivo([])

        return []

    except json.JSONDecodeError as e:
        print(f"\nErro ao ler o arquivo JSON (conteúdo inválido ou corrompido): {e}\n")

        return []