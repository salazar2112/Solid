#colocando a classe CalculadoraEstatisticas ela fica responsável por calcular estatísticas 
#relacionadas aos times de futebol. Quando defino as estatísticas em uma classe separada, permite que 
#novas funcionalidades relacionadas a estatísticas possam ser adicionadas sem modificar a classe Time. 
#Isso mantém a classe Time fechada para modificação.
#o Método calcular_pontos tornou-se estático ele não precisa ser vinculado a uma 
#instância específica de CalculadoraEstatisticas, tornando-o um método estático. Isso significa que ele pode 
#ser chamado diretamente na classe sem a necessidade de criar uma instância de CalculadoraEstatisticas.
#O cálculo de pontos é feito com base em um objeto Time passado como argumento para o método calcular_pontos que 
#permite que você calcule os pontos de qualquer equipe sem precisar modificar a classe Time.

#código que segue a lei do principio Aberto-Fechado:

class Time:
    def __init__(self, nome, vitorias, empates, derrotas):
        self.nome = nome
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas

class CalculadoraEstatisticas:
    @staticmethod
    def calcular_pontos(time):
        return time.vitorias * 3 + time.empates * 1

if __name__ == "__main__":
    Corinthians = Time("Corinthians", 5, 3, 2)
    Porcada = Time("Porcada", 3, 3, 2)

    print(f"Pontuação do {Corinthians.nome}: {CalculadoraEstatisticas.calcular_pontos(Corinthians)} pontos")
    print(f"Pontuação da {Porcada.nome}: {CalculadoraEstatisticas.calcular_pontos(Porcada)} pontos")

#O método calcular_saldo_gols() na classe Time é um exemplo de funcionalidade adicional que viola o OCP.
#Se novos requisitos relacionados ao cálculo do saldo de gols surgirem, isso exigirá a modificação direta
#do código-fonte da classe Time, o que vai contra o princípio de estar fechada para modificações.

#código que não segue a lei do principio Aberto-Fechado:

class Time:
    def __init__(self, nome, vitorias, empates, derrotas):
        self.nome = nome
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas

    def calcular_pontos(self):
        return self.vitorias * 3 + self.empates * 1

    def calcular_saldo_gols(self):
        
        return self.vitorias - self.derrotas

if __name__ == "__main__":
    Corinthians = Time("Corinthians", 5, 3, 2)
    Porcada = Time("Porcada", 3, 3, 2)

    print(f"Pontuação do {Corinthians.nome}: {Corinthians.calcular_pontos()} pontos")
    print(f"Pontuação da {Porcada.nome}: {Porcada.calcular_pontos()} pontos")

    print(f"Saldo de gols do {Corinthians.nome}: {Corinthians.calcular_saldo_gols()}")
    print(f"Saldo de gols da {Porcada.nome}: {Porcada.calcular_saldo_gols()}")
