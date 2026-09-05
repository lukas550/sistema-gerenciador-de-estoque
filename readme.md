# Sistema de Estoque

Sistema de terminal desenvolvido em Python para gerenciamento de produtos em estoque. O usuário pode cadastrar, listar, buscar, atualizar e remover produtos, além de gerar um relatório geral com informações sobre o estoque.

## Como funciona

Ao iniciar o programa, um menu é exibido com sete opções. O usuário navega pelo sistema digitando o número da opção desejada ou o comando "tabela" para exibir o menu novamente a qualquer momento.

Cada produto cadastrado possui quatro informações: nome, preço, quantidade e categoria. Todos os dados ficam armazenados em memória durante a execução do programa.

## Funcionalidades

- Adicionar produto ao estoque, com verificação de duplicatas
- Listar todos os produtos cadastrados com suas informações completas
- Buscar produto pelo nome
- Atualizar preço, quantidade ou categoria de um produto existente
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

- `menu`: exibe o menu principal ou o submenu de edição, dependendo dos parâmetros recebidos.

- `adicionar_produto`: cadastra um produto no dicionário de estoque, com validação de preço, quantidade e verificação de duplicatas.

- `listar_produtos`: exibe todos os produtos cadastrados com suas informações formatadas.

- `buscar_produto`: localiza um produto pelo nome e exibe seus dados.

- `editar_produto`: permite alterar preço, quantidade ou categoria de um produto existente.

- `excluir_produto`: remove um produto do estoque após confirmação do usuário.

- `relatorio_geral`: exibe um resumo financeiro do estoque, incluindo valor total investido, preço médio, produto mais caro, mais barato e itens em baixo estoque.

O tratamento de erros com `try/except` garante que entradas inválidas não travem o programa, especialmente nas opções de atualização de preço e quantidade.

## Alterações futuras

### Estrutura modular

- Dividir o projeto em módulos organizados por responsabilidade (ex: operações de estoque, interface de menu, persistência de dados), substituindo o arquivo único atual por um pacote com múltiplos arquivos
- Transformar `sistemadeestoque.py` no arquivo principal do projeto, responsável apenas por orquestrar a execução e importar as funcionalidades dos módulos
- Substituir a variável global `estoque` por uma abordagem com passagem explícita de parâmetros nas funções, tornando o código mais modular e testável

### Persistência de dados

- Implementar persistência em **JSON**, permitindo salvar e carregar o estoque entre sessões de forma estruturada
- Adicionar tratamento de erros para leitura e escrita de arquivos (ex: arquivo inexistente, JSON corrompido)

### Melhorias de UX

- Formatar todos os valores monetários com `R$ {valor:.2f}` de forma consistente
- Adicionar feedback visual após ações como atualizar preço ou listar produtos (ex: confirmação com os novos dados)
- Padronizar as mensagens de erro e sucesso para seguir o mesmo estilo em todas as opções

## Tecnologias utilizadas

- Python 3

## Autor

Lukas — projeto desenvolvido durante os estudos de Python, aplicando os conceitos de dicionários, funções, loops, condicionais e tratamento de erros.