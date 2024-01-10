from random import random as ram
from typing import List, Union
from utils import menus as menu
from utils.helper import (
    gerar_arquivo_csv,
    adicionar_carrinho,
    limpando_aquivo,
    LendoArquivos
)
from Models.produto import Produto


#   Arquivos a serem usados
arquivo_produtos: str = 'arq_produtos.csv'
arquivo_carrinho: str = 'arq_carrinho.txt'
leitor = LendoArquivos

#   Lista e Dicionarios. apesar de ser algo talvez redundante, isso serveria para organizar no que sera pesquisado.
produtos = []
carrinho = []


def tratar_erros(funcao):
    def func(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except ValueError as ve:
            print(f'Erro de valor: {ve}')
        except FileNotFoundError as fne:
            print(f'Erro de arquivo não encontrado: {fne}')
        except Exception as e:
            print(f'Erro: {e}')
    return func


@tratar_erros
def main() -> None:
    while True:
        print(' Bem-vindo '.center(50, '*'))
        print(' Geek Shop '.center(50, '*'))

        menu.menu_main()

        opc: int = int(input('Opção: '))

        if opc == 1:
            cadastrar_produto(arquivo_produtos)
        elif opc == 2:
            comprar_produto(arquivo_produtos)
        elif opc == 3:
            listar_produtos(arquivo_produtos)
        elif opc == 4:
            visualizar_carrinho(arquivo_carrinho)
        elif opc == 5:
            print('Volte sempre')
            exit(0)


def cadastrar_produto(arquivo: str) -> None:
    print(' Menu de Cadastramento '.center(50, '*'))

    menu.menu_cadastrar_produto()

    opc: int = int(input('Opção: '))

    if opc == 1:
        cadastrar_manualmente(arquivo)
    elif opc == 2:
        cadastrar_randomicamente(arquivo)
    elif opc == 3:
        limpando_aquivo(arquivo)
    else:
        print('opção invalida')


def cadastrar_manualmente(arquivo: str) -> None:
    print('Cadastrando o dado manualmente...')

    nome: str = input('Informe o nome do produto: ')
    preco: float = obter_float_input(f'Informe o preço do produto {nome}: ')

    if not isinstance(nome, str) or not isinstance(preco, float) or preco <= 0:
        print('Houve um erro, tente novamente.')
    else:
        produto: Produto = Produto(nome=nome, preco=preco)
        produtos.append(produto)
        gerar_arquivo_csv(arquivo, 1, produtos)


def cadastrar_randomicamente(arquivo: str) -> None:
    print('Cadastrando os dados randomicamente...')

    qtd: int = obter_inteiro_input('Informar a quantidade de dados a ser criado: ')

    if qtd <= 0:
        print('A quantidade deve ser maior que zero. Tente novamente.')
    else:
        for i in range(1, qtd+1, 1):
            nome: str = f"Item-{i}"
            preco: float = float(ram() * 10)
            produto: Produto = Produto(nome=nome, preco=preco)
            produtos.append(produto)

        gerar_arquivo_csv(arquivo, 2, produtos)


def obter_inteiro_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Por favor, digite um número inteiro válido.')


def obter_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Por favor, digite um número decimal válido.')


def limpar_arquivo(arquivo: str) -> None:
    print('Limpando arquivo')
    limpando_aquivo(arquivo)


@tratar_erros
def comprar_produto(arquivo) -> None:
    arquivo_lido = list(leitor.lendo_arquivo_csv(arquivo))
    if len(arquivo_lido) > 0:
        while True:
            menu.menu_comprar_produto()

            opc = int(input('Opção: '))

            if opc == 1:
                carrinho.append(buscar_por_codigo(arquivo))
            elif opc == 2:
                carrinho.append(buscar_por_nome(arquivo))
            elif opc == 3:
                adicionar_carrinho(arquivo_carrinho, carrinho)
                carrinho.clear()
                break
            else:
                print('opção invalida')
    else:
        print('Não tem produtos catalogados para realizar as compras')


@tratar_erros
def buscar_por_codigo(arquivo) -> Produto:
    codigo: str = input('Informe o código do produto: ')
    produto = buscar_produto(arquivo, codigo)
    if produto:
        print('Produto encontrado...')
        return produto
    else:
        print('Produto não encontrado')


@tratar_erros
def buscar_por_nome(arquivo) -> Produto:
    nome: str = input('Informe o nome do produto: ').title()
    produto = buscar_produto(arquivo, nome)
    if produto:
        print('Produto encontrado...')
        return produto
    else:
        print('Produto não encontrado')


@tratar_erros
def buscar_produto(arquivo: str, nome_ou_codigo: str) -> Union[Produto, None]:
    for produto in leitor.lendo_arquivo_csv(arquivo):
        if produto['Código'] == nome_ou_codigo:
            return produto
        elif produto['Nome'] == nome_ou_codigo:
            return produto
    return None


@tratar_erros
def listar_produtos(arquivo: str) -> None:
    for produto in list(leitor.lendo_arquivo_csv(arquivo)):
        print(f'{produto["Código"]}, {produto["Nome"]}, {produto["Preço"]}')


@tratar_erros
def visualizar_carrinho(arquivo: str) -> None:
    if len(list(leitor.lendo_carrinho(arquivo))):
        # imprimindo o carrinho
        for produto in list(leitor.lendo_carrinho(arquivo)):
            print(produto)

        menu.menu_visualizar_carrinho()

        opc: int = int(input('Opção: '))

        if opc == 1:
            valor_total: float = 0
            for item in list(leitor.lendo_carrinho(arquivo)):
                valor_total += float(item["Preço"].split(" ")[1])
            print(f'Sua fatura é R$ {valor_total}')
            limpando_aquivo(arquivo)
            print('Volte sempre!')

        elif opc == 2:
            print('Qual produto deseja tirar do carrinho?')

            menu.sub_menu_visualizar_carrinho()

            opc_excluir: int = int(input('Opção: '))

            if opc_excluir == 1:
                codigo: str = input('Informe o código do produto: ')

                # Criando uma nova lista sem o produto a ser excluído
                linhas: List = list(leitor.lendo_carrinho(arquivo))
                linhas_novas: List = [item for item in linhas if item["Código"] != codigo]

                # Atualizando o arquivo do carrinho
                limpando_aquivo(arquivo)
                adicionar_carrinho(arquivo, linhas_novas)

                print('Produto removido do carrinho com sucesso!')

            elif opc_excluir == 2:
                nome: str = input('Informe o nome do produto: ').title()

                # Criando uma nova lista sem o produto a ser excluído
                linhas: List = list(leitor.lendo_carrinho(arquivo))
                linhas_novas: List = [item for item in linhas if item["Nome"] != nome]

                # Atualizando o arquivo do carrinho
                limpando_aquivo(arquivo)
                adicionar_carrinho(arquivo, linhas_novas)

                print('Produto removido do carrinho com sucesso!')

            elif opc_excluir == 3:
                main()
        elif opc == 3:
            main()
        else:
            print('Opção invalida')
    else:
        print('Não tem produtos no carrinho')


if __name__ == "__main__":
    main()
