#O princípio de responsabilidade única (SRP) diz que uma classe deve ter uma única responsabilidade e 
#não deve ser responsável por mais de uma área de funcionalidade. E no código é o que esta acontecendo,
# a classe Jogador esta seguindo o princípio de responsabilidade única, pois sua única responsabilidade é 
#mostrar onde o jogador joga, armazenando seu nome e o time ao qual pertence, e fornece um método para indicar 
#que o jogador está jogando.



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


#agora um código que não respeita o principio de responsabilidade unica, pois tem varias funcionalidades,
#como por exemplo calcular o desempenho do jogador, e tambem reponsavel pela representação do jogador.
#código que não respeita o principio de responsabilidade unica:


class Jogador:
    def __init__(self, nome, time, posicao, estatisticas):
        self.nome = nome
        self.time = time
        self.posicao = posicao
        self.estatisticas = estatisticas

    def jogar(self):
        print(f"{self.nome} está jogando pelo time {self.time}.")
        self.verificar_posicao()
        self.atualizar_estatistica()
        self.calcular_desempenho()  

    def verificar_posicao(self):
        print(f"posição de {self.nome} no time do {self.time} é {self.posicao}.")

    def atualizar_estatistica(self):
        print(f"estatísticas de {self.nome} no time do {self.time} é: {self.estatisticas}.")

    def calcular_desempenho(self):
        gols_feitos, gols_perdidos = map(int, self.estatisticas.split(' e '))
        eficiencia = gols_feitos - gols_perdidos
        print(f"{self.nome} fez {gols_feitos} gols e perdeu {gols_perdidos} gols.")
        print(f"O desempenho de {self.nome} é {eficiencia}.")

if __name__ == "__main__":
    jogador1 = Jogador("Yuri Alberto", "Corinthians", "centro-avante", "8 e 4")
    jogador1.jogar()

