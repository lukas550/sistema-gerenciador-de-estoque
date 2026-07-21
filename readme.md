# Sistema de Estoque

Sistema de terminal desenvolvido em Python para gerenciamento de produtos em estoque. O usuário pode cadastrar, listar, buscar, atualizar e remover produtos, além de gerar um relatório geral com informações sobre o estoque.

## Como funciona

Ao iniciar o programa, um menu é exibido com sete opções. O usuário navega pelo sistema digitando o número da opção desejada ou o comando "tabela" para exibir o menu novamente a qualquer momento.

Cada produto cadastrado possui quatro informações: nome, preço, quantidade e categoria. Todos os dados ficam armazenados em memória durante a execução do programa.

## Funcionalidades

- Adicionar produto ao estoque, com verificação de duplicatas
- Listar todos os produtos cadastrados com suas informações completas
- Buscar produto pelo nome
- Atualizar preço ou quantidade de um produto existente
- Remover produto do estoque
- Relatório geral com total de produtos, valor total em estoque e produtos com quantidade zero
- Comando "tabela" para exibir o menu a qualquer momento

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório ou baixe o arquivo `sistemadeestoque.py`.
3. Execute o programa pelo terminal:
   ```
   python sistemadeestoque.py
   ```
4. Siga as instruções exibidas na tela.

## Estrutura do código

O programa é dividido em funções, cada uma responsável por uma parte específica:

- `lin`: imprime uma linha decorativa no terminal para organizar a saída visualmente.

- `funcionalidades`: exibe o menu com todas as opções disponíveis.

- `adicionar_produto`: cadastra um produto no dicionário de estoque e exibe uma confirmação.

O tratamento de erros com `try/except` garante que entradas inválidas não travem o programa, especialmente nas opções de atualização de preço e quantidade.

## Tecnologias utilizadas

- Python 3

## Autor

Lukas — projeto desenvolvido durante os estudos de Python, aplicando os conceitos de dicionários, funções, loops, condicionais e tratamento de erros.