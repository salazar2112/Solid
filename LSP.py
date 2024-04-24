#código que respeita o principio de Liskov:
class Jogador:
    def jogar(self):
        pass

class Atacante(Jogador):
    def jogar(self):
        return "Atacante: Roger Guedes recebe a bola na frente do gol, vai fazer, que gooolaaaço!"

class Zagueiro(Jogador):
    def jogar(self):
        return "Zagueiro: Félix Torres da um bumba meu boi pra frente e evita o perigo!"

class Goleiro(Jogador):
    def jogar(self):
        return "Cassiooo, defendeu Cassiooooo!"
    


def acao_do_jogo(jogador):
    print(jogador.jogar())

if __name__ == "__main__":
    atacante = Atacante()
    zagueiro = Zagueiro()
    goleiro = Goleiro()

    acao_do_jogo(atacante)
    acao_do_jogo(zagueiro)
    acao_do_jogo(goleiro)


#código que não respeita o principio de Liskov:
#não respeita o principio, porque coloquei uma classe(JogadorReserva), e quando
#essa classe é usada com a função acao_do_jogo(), ela não se comporta como as outras 
#classes (Atacante, Zagueiro e Goleiro) e não segue o mesmo padrão de comportamento. 
class Jogador:
    def jogar(self):
        pass

class Atacante(Jogador):
    def jogar(self):
        return "Atacante: Roger Guedes recebe a bola na frente do gol, vai fazer, que gooolaaaço!"

class Zagueiro(Jogador):
    def jogar(self):
        return "Zagueiro: Félix Torres da um bumba meu boi pra frente e evita o perigo!"

class Goleiro(Jogador):
    def jogar(self):
        return "Cassiooo, defendeu Cassiooooo!"
    
class Gandula:  
    def jogar(self):
        return "Gandula: Só estou aqui para aproveitar o passeio e assistir a partida!"
    

def acao_do_jogo(jogador):
    print(jogador.jogar())

if __name__ == "__main__":
    atacante = Atacante()
    zagueiro = Zagueiro()
    goleiro = Goleiro()
    gandula = Gandula()
    
    acao_do_jogo(atacante)
    acao_do_jogo(zagueiro)
    acao_do_jogo(goleiro)
    acao_do_jogo(gandula)  
