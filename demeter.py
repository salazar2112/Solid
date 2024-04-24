class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def get_quantidade_total_itens(self):
        return sum(pedido.quantidade_itens for pedido in self.pedidos)

class Pedido:
    def __init__(self, quantidade_itens):
        self.quantidade_itens = quantidade_itens

# Exemplo de uso
cliente = Cliente("Alice")
pedido1 = Pedido(5)
pedido2 = Pedido(3)

cliente.adicionar_pedido(pedido1)
cliente.adicionar_pedido(pedido2)

# Respeitando o Princípio de Demeter
nome_cliente = cliente.nome
quantidade_itens = cliente.get_quantidade_total_itens()

print(f"{nome_cliente} - {quantidade_itens} itens")
