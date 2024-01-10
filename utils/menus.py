def menu_main() -> None:
    print('[1] - Cadastrar produto(s)')
    print('[2] - Comprar produto(s)')
    print('[3] - Listar produto(s)')
    print('[4] - Visualizar carrinho')
    print('[5] - Sair')

def menu_cadastrar_produto() -> None:
    print('[1] - Gerar dados manualmente')
    print('[2] - Gerar dados randomicos')
    print('[3] - Limpar arquivo')
    print('[4] - Voltar')

def menu_comprar_produto() -> None:
    print('comprando produtos')
    print('[1] - realizar pesquisa pelo codigo')
    print('[2] - realizar pesquisa pelo nome')
    print('[3] - voltar')

def menu_visualizar_carrinho() -> None:
    print('\n[1] - Fechar a compra')
    print('[2] - Excluir produto')
    print('[3] - Voltar')

def sub_menu_visualizar_carrinho() -> None:
    print('[1] - Buscar por código')
    print('[2] - Buscar por nome')
    print('[3] - Voltar')
