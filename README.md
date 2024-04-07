# Geek Shop

Este é um programa de simulação de uma loja online chamada Geek Shop, onde você pode cadastrar produtos, fazer compras, gerenciar o carrinho e visualizar produtos disponíveis.

## Funcionalidades Principais

1. **Cadastro de Produtos**
   - Você pode cadastrar produtos manualmente ou de forma aleatória.
   - O cadastro manual permite que você insira o nome e o preço do produto.
   - O cadastro aleatório gera produtos com nomes e preços aleatórios.

2. **Compra de Produtos**
   - Você pode adicionar produtos ao carrinho digitando o código ou nome do produto.
   - Após escolher os produtos desejados, você pode finalizar a compra e limpar o carrinho.

3. **Listagem de Produtos**
   - Exibe uma lista de todos os produtos disponíveis na loja.

4. **Visualização e Gerenciamento do Carrinho**
   - Permite visualizar os produtos adicionados ao carrinho.
   - Permite remover produtos do carrinho por código ou nome.

## Instruções de Uso

1. **Executando o Programa**
   - Certifique-se de ter o Python instalado em seu ambiente.
   - Execute o programa `geek_shop.py`.

2. **Opções do Menu Principal**
   - `1`: Cadastrar novo produto
   - `2`: Comprar produtos
   - `3`: Listar produtos disponíveis
   - `4`: Visualizar carrinho
   - `5`: Sair do programa

3. **Cadastro de Produtos**
   - Escolha entre cadastrar manualmente ou aleatoriamente.
   - Para o cadastro manual, insira o nome e o preço do produto.
   - Para o cadastro aleatório, defina a quantidade de produtos a serem gerados.

4. **Compra de Produtos**
   - Adicione produtos ao carrinho digitando o código ou nome.
   - Finalize a compra para limpar o carrinho.

5. **Visualização do Carrinho**
   - Exiba os produtos no carrinho.
   - Opções adicionais permitem calcular o valor total ou remover produtos.

## Requisitos

- Python
- Bibliotecas necessárias (veja `requirements.txt`)

## Estrutura do Código

- `geek_shop.py`: Contém a lógica principal do programa.
- `utils/menus.py`: Módulo com funções para exibir menus.
- `utils/helper.py`: Módulo com funções auxiliares.
- `Models/produto.py`: Classe `Produto` para representar os produtos.
- `arq_produtos.csv`: Arquivo CSV para armazenar os produtos.
- `arq_carrinho.txt`: Arquivo de texto para armazenar os itens do carrinho.

## Executando o Programa

```bash
python geek_shop.py

Esse README fornece uma visão geral das funcionalidades, instruções de uso, requisitos, estrutura do código e informações adicionais sobre como executar e interagir com o programa `geek_shop.py`.
