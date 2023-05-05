class Pessoa():
    def __init__(self, nome, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11):
        self.__nome = nome
        self.personagem = r1
        self.famoso = r2
        self.homem = r3
        self.conheco_pessoalmente = r4
        self.vivo = r5
        self.loiro = r6
        self.trabalha_bosch = r7
        self.instrutor = r8
        self.heroi = r9
        self.cantor = r10
        self.ator = r11

    @property
    def nome(self):
        return self.__nome
