class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
            print(f"{quantidade} unidades adicionadas ao estoque.")
        else:
            print("A quantidade deve ser maior que zero.")

    def remover_estoque(self, quantidade):
        if quantidade > 0:
            if self.quantidade >= quantidade:
                self.quantidade -= quantidade
                print(f"{quantidade} unidades removidas do estoque.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("A quantidade deve ser maior que zero.")

    def exibir_estoque(self):
        print(f"Produto: {self.nome}\nQuantidade em estoque: {self.quantidade}")


estoque = {}

while True:
    print("=== Sistema de Gerenciamento de Inventário ===")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Exibir estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_produto = input("Nome do produto: ")
        quantidade_produto = int(input("Quantidade: "))

        if quantidade_produto > 0:
            if nome_produto in estoque:
                estoque[nome_produto].adicionar_estoque(quantidade_produto)
            else:
                estoque[nome_produto] = Produto(nome_produto, quantidade_produto)
                print("Produto adicionado ao estoque.")
        else:
            print("A quantidade deve ser maior que zero.")

    elif opcao == "2":
        nome_produto = input("Nome do produto: ")

        if nome_produto in estoque:
            quantidade_produto = int(input("Quantidade: "))
            estoque[nome_produto].remover_estoque(quantidade_produto)
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        print("=== Estoque ===")
        for produto in estoque.values():
            produto.exibir_estoque()

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")