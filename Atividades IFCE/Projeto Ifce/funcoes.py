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

lista = {}

def TelaInicial ():
    Painel("Lojita Del Tadeo")
    print("1 - Admnistrador\n2 - Cliente\n0 - Sair")
    r = int(input("Opção: "))
    return r
    
def Painel(mensagem):
    print("~" * (len(mensagem) + 4))
    print(mensagem.center(len(mensagem) + 4))
    print("~" * (len(mensagem) + 4))

def Cadastrar(produto):
    Painel("Cadastrar Produto")
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
            Painel("Remover produto")
            print(lista)
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

def Listar():
    if len(lista) != 0:
        Painel("Lista dos Produtos")
        for item, values in lista.items():
            print(f"Produto: {item}. Preço: R${values[0]:.2f}. Quantidade: {values[1]}")
        print("~" * 22)
    else:
        print("Não há nenhum item no estoque até o momento.")

def Ação():
    while True:
        Painel("Função ADM || Lojito del Tadeo")
        acao = input("1 - Cadastrar\n2 - Remover\n3 - Listar\n0 - Sair\nO que deseja fazer? ").upper().strip()
        while acao not in "1230":
            acao = input("Resposta incorreta. Tente novamente: ")
        if acao == "1":
            Cadastrar("Item")
        if acao == "2":
            Remover("Item")
        if acao == "3":
            Listar()
        if acao == "0":
            break

def Cliente():
    while True:
        Painel("Função Cliente || Lojito del Tadeo")
        acao = input("1 - Lista de Produtos\n2 - Meu Carrinho\n3 - Finalizar Compra\n0 - Sair\nO que deseja fazer? ").upper().strip()
        while acao not in "1230":
            acao = input("Resposta incorreta. Tente novamente: ")
        if acao == "1":
            Listar()
            Comprar("Item", lista)
        if acao == "2":
            Carrinho()
        if acao == "3":
            ValorCompra()
        if acao == "0":
            break
def Alterar():
    print('a')

def Comprar(produto, lista):
    carrinho = []
    while True:
        produto = input('Selecione o produto para adicionar ao carrinho: ').lower().strip()
        while produto not in lista:
            print('Produto incorreto. Tente novamente.')
        if produto in lista:
            carrinho.append(produto)
        
        return carrinho

def Avaliar():
    print('a')

def ValorCompra():
    print(1)

def Carrinho(carrinho):
    while True:
        Painel('Meu Carrinho')
        if len(carrinho) != 0:
            c = 1
            for e in carrinho:
                print(f'{c}- {e}')
                c += 1
        else:
            resp = input('Carrinho vazio! Deseja voltar ao menu? [S/N]').upper()
            while resp not in 'SN':
                resp = input("Resposta inválida.\n Deseja voltar ao menu? [S/N]? ").upper()
            if resp == 'S':
                Cliente()
            else:
                break
            

def Feedback():
    print(3)

