#
class Time:
    def __init__(self, nome, vitorias, empates, derrotas):
        self.nome = nome
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas

    def calcular_pontos(self):
        return self.vitorias * 3 + self.empates * 1

# Exemplo de uso
if __name__ == "__main__":
    Corinthians = Time("Corinthians", 5, 3, 2)
    Porcada = Time("Porcada", 3, 3, 2)

    print(f"Pontuação do {Corinthians.nome}: {Corinthians.calcular_pontos()} pontos")
    print(f"Pontuação do {Porcada.nome}: {Porcada.calcular_pontos()} pontos")
