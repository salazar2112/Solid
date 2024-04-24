#A classe Cliente possui um método chamado adicionar_pedido, ela adiciona um pedido à lista de pedidos do 
#cliente. Este esta em conformidade com o Princípio de Demeter, pois está apenas interagindo 
#com a lista de pedidos do próprio cliente. O método get_quantidade_total_itens na classe Cliente itera 
#sobre a lista de pedidos do cliente para calcular a quantidade total de itens. Isso também está em 
#conformidade com o Princípio de Demeter, pois o método está apenas interagindo com os pedidos do cliente.


#código que respeita o principio de Demeter:
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

cliente = Cliente("Alice")
pedido1 = Pedido(5)
pedido2 = Pedido(3)

cliente.adicionar_pedido(pedido1)
cliente.adicionar_pedido(pedido2)

nome_cliente = cliente.nome
quantidade_itens = cliente.get_quantidade_total_itens()

print(f"{nome_cliente} - {quantidade_itens} itens")

#Nesta versão do código, a violação do Princípio de Demeter ocorre na linha 
#quantidade_itens = sum(pedido.quantidade_itens for pedido in cliente.pedidos). Aqui, o cliente está 
#acessando diretamente a lista de pedidos (cliente.pedidos) e, em seguida, cada pedido dentro dessa 
#lista para obter a quantidade de itens. Isso viola o princípio, pois o cliente está "falando com estranhos",
#ou seja, acessando indiretamente o interno dos objetos de seus pedidos.

#código que não respeita o principio de Demeter:
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


cliente = Cliente("Alice")
pedido1 = Pedido(5)
pedido2 = Pedido(3)

cliente.adicionar_pedido(pedido1)
cliente.adicionar_pedido(pedido2)


nome_cliente = cliente.nome
quantidade_itens = sum(pedido.quantidade_itens for pedido in cliente.pedidos)

print(f"{nome_cliente} - {quantidade_itens} itens")
