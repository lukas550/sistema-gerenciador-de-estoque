# Sistema de Estoque

Sistema de terminal desenvolvido em Python para gerenciamento de produtos em estoque. O usuário pode cadastrar, listar, buscar, atualizar e remover produtos, além de gerar um relatório geral com informações sobre o estoque. Os dados são persistidos em um arquivo JSON, mantendo o estoque entre sessões.

## Como funciona

Ao iniciar o programa, um menu é exibido com sete opções. O usuário navega pelo sistema digitando o número da opção desejada ou o comando "tabela" para exibir o menu novamente a qualquer momento.

Cada produto cadastrado possui quatro informações: nome, preço, quantidade e categoria. Ao iniciar a aplicação, o estoque é carregado automaticamente do arquivo `estoque.json`; toda alteração (cadastro, edição ou remoção) é salva de volta nesse arquivo.

## Funcionalidades

- Adicionar produto ao estoque, com verificação de duplicatas e confirmação para sobrescrita
- Listar todos os produtos cadastrados com suas informações completas
- Buscar produto pelo nome
- Editar preço, quantidade ou categoria de um produto existente
- Remover produto do estoque, com confirmação obrigatória antes da exclusão
- Relatório geral com total de produtos, quantidade total, valor investido, preço médio, produto mais caro e mais barato, e produtos com baixo estoque
- Comando "tabela" para exibir o menu a qualquer momento
- Persistência automática dos dados em JSON entre sessões

## Como executar

1. Certifique-se de ter o Python 3.10 ou superior instalado.
2. Clone este repositório:
   ```
   git clone https://github.com/lukas550/sistema-gerenciador-de-estoque.git
   ```
3. Acesse o diretório do projeto:
   ```
   cd sistema-gerenciador-de-estoque
   ```
4. Execute o programa pelo terminal:
   ```
   python main.py
   ```
5. Siga as instruções exibidas na tela.

Nenhuma dependência externa é necessária. A aplicação utiliza apenas a biblioteca padrão do Python (`json`).

## Estrutura do projeto

O projeto é dividido em módulos organizados por responsabilidade:

```
sistema-gerenciador-de-estoque/
│
├── main.py              — Arquivo principal, orquestra os módulos e controla o menu
│
└── core/
    ├── logica.py         — Funções de CRUD: adicionar, listar, buscar, editar, excluir e gerar relatório
    ├── armazenamento.py  — Salvamento e carregamento do estoque em arquivo JSON
    └── organizacao.py    — Funções auxiliares de interface (linhas decorativas, exibição de menus)
```

**Responsabilidade de cada módulo:**

- `main.py`: contém o loop principal e a lógica de navegação entre as opções do menu, chamando as funções dos demais módulos.

- `core/logica.py`: implementa as regras de negócio do estoque, incluindo validação de dados (preço e quantidade numéricos e não negativos, nome e categoria obrigatórios).

- `core/armazenamento.py`: responsável por `salvar_arquivo` e `carregar_arquivo`, com tratamento de erros para arquivo inexistente, JSON corrompido e falhas de escrita.

- `core/organizacao.py`: contém `lin` (linha decorativa) e `menu` (exibição de opções a partir de um dicionário), reutilizadas em várias partes do projeto.

**Estrutura de dados de cada produto:**

```python
{
    "produto": str,
    "preco": float,
    "quantidade": int,
    "categoria": str
}
```

O estoque é uma lista de dicionários nesse formato, persistida no arquivo `estoque.json` (ignorado pelo Git, por se tratar de dado gerado em tempo de execução).

## Tecnologias utilizadas

**Linguagem:**
- Python 3.10+

**Fundamentos aplicados:**
- Estrutura modular com múltiplos arquivos e importação entre módulos
- Persistência de dados em JSON (`json.dump`, `json.load`)
- Tipos de dados: strings, floats, inteiros, listas e dicionários
- Funções com parâmetros e retorno
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`, `for`)
- Tratamento de erros com `try`, `except` e `raise` (incluindo exceções específicas como `OSError` e `json.JSONDecodeError`)
- Métodos de string: `.lower()`, `.strip()`, `.capitalize()`
- Funções nativas: `len()`, `max()`, `min()`, `any()`

## Autor

Lukas — projeto desenvolvido durante os estudos de Python, aplicando os conceitos de dicionários, funções, loops, condicionais, tratamento de erros e organização modular de código.