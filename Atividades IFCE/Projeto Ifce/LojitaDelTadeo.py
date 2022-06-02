from time import sleep
import csv

lista = {}

f = open('a:/Projeto IFCE/Atividades IFCE/Projeto Ifce/estoque.csv', 'w', newline='', encoding='utf-8')
w = csv.writer(f)
# 1. cria o arquivo


# 2. cria o objeto de gravação


# 3. grava as linhas

# Recomendado: feche o arquivo

'''
# 1. abrir o arquivo
with open('a:/Projeto IFCE/Atividades IFCE/Projeto Ifce/estoque.csv', encoding='utf-8') as arquivo_referencia:

  # 2. ler a tabela
  tabela = csv.reader(arquivo_referencia, delimiter=',')

  # 3. navegar pela tabela
  for l in tabela:
    id_autor = l[0]
    nome = l[1]

    print(id_autor, nome) # 191149, Diego C B Mariano
'''

def Painel(mensagem):
    print("~" * (len(mensagem) + 4))
    print(mensagem.center(len(mensagem) + 4))
    print("~" * (len(mensagem) + 4))

def Cadastrar(produto):
    Painel("Cadastrar Produto")
    while True:
        produto = input("Nome do produto: ").capitalize().strip()
        preco = float(input("Preço unitário: R$"))
        quantidade = int(input("Quantidade: "))
        confirmacao = input("Confirmar cadastro [S/N]? ").upper().strip()[0]
        while confirmacao not in "SN":
            confirmacao = input("Resposta inválida. Confirmar cadastro [S/N]? ").upper().strip()
        if confirmacao == "S":
            lista[produto] = preco, quantidade
            for item, valores in lista.items():
                w.writerow(f"{item},{valores[0]},{valores[1]}\n")
        resp = input("Deseja continuar [S/N]? ").upper()
        while resp not in "SN":
            resp = input("Resposta inválida. Deseja Continuar [S/N]? ").upper()
        if resp == "N":
            break
        print()
    print(lista)

def Remover(elementoRetirar):
    Painel("Remover Produto")
    if len(lista) != 0:
        print(lista)
        elementoRetirar = input("Digite o item que deseja remover: ").capitalize().strip()
        while elementoRetirar not in lista:
            elementoRetirar = input("Resposta inválida. Digite o item que deseja remover: ").capitalize().strip()
        confirmacao = input("Confirmar remoção [S/N]? ").upper().strip()[0]
        while confirmacao not in "SN":
            confirmacao = input("Resposta inválida. Confirmar remoção [S/N]? ").upper().strip()[0]
        if confirmacao == "S":
            del lista[elementoRetirar]
    else:
        print("Não há itens cadastrados para remover...")

def Listar():
    if len(lista) != 0:
        for item, valores in lista.items():
            print(f"Produto: {item}. Preço: R${valores[0]}. Quantidade: {valores[1]}")
    else:
        print("Não há nenhum item na lista até o momento.")

def Ação():
    while True:
        Painel("Função ADM || Lojita del Tadeo")
        acao = input("1 - Cadastrar\n2 - Remover\n3 - Listar\n0 - Sair\nO que deseja fazer? ").upper().strip()
        while acao not in "1230":
            acao = input("Resposta incorreta. Tente novamente: ")
        if acao == "1":
            Cadastrar("Item")
        if acao == "2":
            Remover("Item")
        if acao == "3":
            Listar()
            sleep(1)
        if acao == "0":
            break

while True:
    Painel("Função ADM || Lojita del Tadeo")
    acao = input("1 - Cadastrar\n2 - Remover\n3 - Listar\n0 - Sair\nO que deseja fazer? ").upper().strip()
    while acao not in "1230":
        acao = input("Resposta incorreta. Tente novamente: ")
    if acao == "1":
        Cadastrar("Item")
    if acao == "2":
        Remover("Item")
    if acao == "3":
        Listar()
        sleep(1)
    if acao == "0":
        break

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
