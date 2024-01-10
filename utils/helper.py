from csv import DictWriter

def gerar_arquivo_csv(arquivo, opc, produtos) -> None:
    """Função para gerar o arquivo CSV"""

    cabecalho = ['Código', 'Nome', 'Preço']

    with open(arquivo, 'w', encoding='UTF-8', newline='') as arq:
        escritor_csv = DictWriter(arq, fieldnames=cabecalho)
        escritor_csv.writeheader()

        if opc == 1:
            escritor_csv.writerows([
                {'Código': produto.codigo, 'Nome': produto.nome, 'Preço': formata_float_str_moeda(produto.preco)}
                for produto in produtos
            ])
            print(f'Produto cadastrado com sucesso!\n')

        elif opc == 2:
            escritor_csv.writerows([
                {'Código': produto.codigo, 'Nome': produto.nome, 'Preço': formata_float_str_moeda(produto.preco)}
                for produto in produtos
            ])
            print(f'{len(produtos)} Produtos cadastrados com sucesso!\n')


class LendoArquivos:

    @staticmethod
    def lendo_arquivo_csv(arquivo) -> dict:
        """Função para listar os dados do arquivo"""
        with open(arquivo, 'r', encoding='UTF-8') as arq:
            for linha in arq:
                codigo, nome, preco = linha.strip().split(',')
                yield {'Código': codigo, 'Nome': nome, 'Preço': preco}


    @staticmethod
    def lendo_carrinho(arquivo) -> dict:
        with open(arquivo, 'r', encoding='UTF-8') as arq:
            for linha in arq:
                codigo, nome, preco = linha.strip().split(',')
                yield {'Código': codigo, 'Nome': nome, 'Preço': preco}


def adicionar_carrinho(arquivo, lista_de_produtos) -> None:
    with open(arquivo, 'a', encoding='UTF-8') as arq:
        for produto in lista_de_produtos:
            arq.write(f'{produto["Código"]},{produto["Nome"]},{produto["Preço"]}\n')


def limpando_aquivo(arquivo) -> None:
    """Função para limpar o arquivo gerado, seja random ou manualmente"""
    with open(arquivo, 'w', newline=''):
        pass


def formata_float_str_moeda(valor: float) -> str:
    return f'R${valor:,.2f}'
