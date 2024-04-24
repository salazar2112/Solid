#O Princípio de Substituição de Liskov diz que os objetos de uma classe derivada devem ser 
#substituíveis por objetos da classe base sem interferir no funcionamento do programa,
#e isso está acontecendo no código. As classes derivadas (Atacante, Zagueiro e Goleiro) substituem a classe 
#base (Jogador) de forma que, quando uma instância dessas classes derivadas é passada para a função
#acao_do_jogo, o comportamento esperado é mantido.
#Isso significa que a função acao_do_jogo pode aceitar qualquer instância de Jogador
#(ou de suas subclasses) sem problemas, pois todas elas implementam o método jogar() de maneira apropriada.

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



# Já essa versão, não respeita o principio, porque coloquei uma classe(Gandula),e ela não se comporta como as 
#outras classes (Atacante, Zagueiro e Goleiro) e não segue o mesmo padrão de comportamento. 
# Enquanto as classes Atacante, Zagueiro e Goleiro representam diferentes posições em um jogo de futebol
# e têm um comportamento relacionado a essa posição, a classe Gandula não representa uma posição de jogador
# e tem um comportamento diferente. 

# código que não respeita o principio de Liskov:

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
