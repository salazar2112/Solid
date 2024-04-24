#código que respeita o principio de responsabilidade unica:
class Jogador:
    def __init__(self, nome, time):
        self.nome = nome
        self.time = time

    def jogar(self):
        print(f"{self.nome} está jogando pelo time {self.time}.")

if __name__ == "__main__":
    jogador1 = Jogador("Yuri Alberto", "Corinthians")
    
    jogador1.jogar()



#código que não respeita o principio de responsabilidade unica:


class Jogador:
    def __init__(self, nome, time, posicao, estatistica):
        self.nome = nome
        self.time = time
        self.posicao = posicao
        self.estatisticas = estatistica

    def jogar(self):
        print(f"{self.nome} está jogando pelo time {self.time}.")
        self.verificar_posicao()
        self.atualizar_estatistica()

    def verificar_posicao(self):
        print(f"posição de {self.nome} no time do {self.time} é {self.posicao} .")

    def atualizar_estatistica(self):
        print(f"estatísticas de {self.nome} no time do {self.time} é: {self.estatisticas} .")

if __name__ == "__main__":
    jogador1 = Jogador("Yuri Alberto", "Corinthians", "centro-avante", "gols - 8 e assistencias - 4")
    jogador1.jogar()
