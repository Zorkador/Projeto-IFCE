# --------------- lojito del tadeo carnes -----------------
# | ENTRAR                                                |
# | se for adm: programa solicita código de adm (1234)    |
# | se for usuario: entra direto                          |
#  -------------------------------------------------------
# Adm: Função Cadastrar
# Adm: Função Remover
# Adm: Função Editar
# Cliente: Função Avaliar (Avalia em Estrelas)
# Cliente: Função Comprar.
# Lojita: Função para listar (tela pra listar todos os produtos e informações (código(posição), preço, quantia no estoque))
# Lojita: Tela Inicial.

import Funcoes

lista = {}
carrinho = {}

def TelaInicial ():
    Painel("Lojito Del Tadeo")
    print("1 - Admnistrador\n2 - Cliente\n0 - Sair")
    r = input("Opção: ")
    while r not in "120":
        r = input("Opção inválida. Tente novamente: ")
    return r


def Painel(mensagem):
    print("~" * (len(mensagem) + 4))
    print(mensagem.center(len(mensagem) + 4))
    print("~" * (len(mensagem) + 4))

def Cadastrar(produto):
    Funcoes.Painel("Cadastrar Produto")
    while True:
        produto = input("Nome do produto: ").capitalize().strip()
        preco = float(input("Preço: R$"))
        quantidade = int(input("Quantidade: "))
        confirmacao = input("Confirmar cadastro [S/N]? ").upper().strip()
        while confirmacao not in "SN":
            confirmacao = input("Resposta inválida. Confirmar cadastro [S/N]? ")
        if confirmacao == "S":
            lista[produto] = (preco, quantidade)
        resp = input("\nDeseja continuar [S/N]? ").upper()
        while resp not in "SN":
            resp = input("Resposta inválida. Deseja continuar [S/N]? ").upper()
        if resp == "N":
            break
        print()

def Remover(elementoRetirar):
    while True:
        if len(lista) != 0:
            Funcoes.Listar()
            elementoRetirar = input("Digite o item que deseja remover: ").capitalize().strip()
            while elementoRetirar not in lista:
                elementoRetirar = input("Resposta inválida. Digite o item que deseja remover: ").capitalize().strip()
            confirmacao = input("Confirmar remoção [S/N]? ").upper().strip()
            while confirmacao not in "SN":
                confirmacao = input("Resposta inválida. Confirmar remoção [S/N]? ")
            if confirmacao == "S":
                del lista[elementoRetirar]
                print(f"{elementoRetirar} retirado com sucesso!")
            resp = input("\nDeseja continuar [S/N]? ").upper()
            while resp not in "SN":
                resp = input("Resposta inválida. Deseja continuar [S/N]? ").upper()
            if resp == "N":
                break
        else:
            print("Não há itens cadastrados para remover...")
            break

def Alterar(elementoAlterar):
    if len(lista) != 0:
        Funcoes.Listar()
        elementoAlterar = input("Digite o item que deseja alterar: ").capitalize().strip()
        


def Listar():
    if len(lista) != 0:
        Painel("Lista dos Produtos")
        print(("=-" * 30) + "=")
        for item, values in lista.items():
            print(f"Produto: {item}. Preço: R${values[0]:.2f}. Quantidade: {values[1]}")
        print(("=-" * 30) + "=")
    else:
        print("Não há nenhum item no estoque até o momento.")


def Acao():
    while True:
        Painel("Função ADM || Lojito del Tadeo")
        acao = input("1 - Cadastrar\n2 - Remover\n3 - Listar\n0 - Sair\nO que deseja fazer? ").strip()
        while acao not in "1230":
            acao = input("Resposta incorreta. Tente novamente: ")
        if acao == "1":
            Funcoes.Cadastrar("Item")
        if acao == "2":
            Funcoes.Remover("Item")
        if acao == "3":
            Listar()
        if acao == "0":
            break


def Cliente():
    while True:
        Painel("Função Cliente || Lojito del Tadeo")
        acao = input("1 - Comprar Produtos\n2 - Meu Carrinho\n3 - Finalizar Compra\n0 - Sair\nO que deseja fazer? ").upper().strip()
        while acao not in "1230":
            acao = input("Resposta incorreta. Tente novamente: ")
        if acao == "1":
            Listar()
            Funcoes.Comprar("Item")
        if acao == "2":
            Funcoes.MeuCarrinho(carrinho)
        if acao == "3":
            Funcoes.Encerrar()
        if acao == "0":
            break


def Alterar(elementoRetirar):
    Funcoes.Listar()
    opcao = input("Informe o item que deseja alterar: ")


def Comprar(produto, quantidade):
    while True:
        produto = input('Selecione o produto para adicionar ao carrinho: ').capitalize().strip()
        quantidade = int(input("Selecione a quantidade do produto: "))
        while produto not in lista:
            print('Produto incorreto. Tente novamente.')
            produto = input('Selecione o produto para adicionar ao carrinho: ').capitalize().strip()
        confirmacao = input("Confirmar produto [S/N]? ").upper().strip()
        while confirmacao not in "SN":
            confirmacao = input("Resposta inválida. Confirmar produto [S/N]? ")
        if confirmacao == "S":
            carrinho[produto] = lista[produto][0], lista[produto][1]
        resp = input("\nDeseja continuar [S/N]? ").upper()
        while resp not in "SN":
            resp = input("Resposta inválida. Deseja continuar [S/N]? ").upper()
        if resp == "N":
            break


def MeuCarrinho(produtos):
    while True:
        Painel('Meu Carrinho')
        if len(produtos) != 0:
            c = 1
            for key, valeus in carrinho.items():
                print(f'{c} - {key}, R${valeus[0]}, Quantidade:{valeus[1]}')
                c += 1
            break
        else:
            resp = input('Carrinho vazio! Deseja voltar ao menu? [S/N]').upper()
            while resp not in 'SN':
                resp = input("Resposta inválida.\n Deseja voltar ao menu? [S/N]? ").upper()
            if resp == 'S':
                Cliente()
            else:
                break
            
def Avaliar():
    print('a')


def ValorCompra():
    print('')


def Feedback():
    print('')

def Encerrar():
    print('')

