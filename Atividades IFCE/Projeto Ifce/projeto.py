# --------------- lojito del tadeo carnes -----------------
# | ENTRAR                                                |
# | se for adm: programa solicita código de adm (40028922)|
# | se for usuario: entra direto                          |
#  -------------------------------------------------------
# Adm: Função Cadastrar
# Adm: Função Remover
# Adm: Função Editar
# Cliente: Função Avaliar (Avalia em Estrelas)
# Cliente: Função Comprar.
# Lojita: Função para listar (tela pra listar todos os produtos e informações (código(posição), preço, quantia no estoque))
# Lojita: Tela Inicial.

import funcoes
r = funcoes.TelaInicial()
while r != 0:
    cont = 3
    while r == 1:
        senha = input('Senha:')
        if senha == "40028922":
            funcoes.Ação()
        elif senha != "40028922":
            cont -= 1
            print(f'Senha incorreta! Tentativas restantes: {cont}')
            if cont == 0:
                print('Muitos erros, você foi redirecionado para a página inicial.')
                break
    while r == 2:
        funcoes.Cliente()
        break
    while r != 1 and r != 2:
        r = int(input("Opção inválida. Tente novamente: "))
    r = funcoes.TelaInicial()
print('Volte sempre')


print("\nAté mais! Volte sempre!")

# Ajeitar a função Listar
# Fazer a função Alterar
# Alex: Algumas coisas para a parte do cliente:
# Criar uma lista/dicionário para o carrinho
# Poder remover da lista algum produto que foi adicionado
# Fazer o cálculo do valor total da compra
# Cancelar a compra
# Forma de pagamento
# Talvez uma opção para pedir a entrega a domicílio
# Alex: Algumas outras coisas:
# Adicionar um código a cada produto
# Remover por quantidade
# Uma opção de deixar algum feedbacks