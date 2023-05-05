from tkinter import *
from pessoas import Pessoa
import random

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.escolhido = self.escolhe_pessoa()
        self.texto = 'Vamos iniciar?'
        self.vidas = 6
        self.fonte2 = ('Arial', 10, 'bold')
        self.s_n = "Faça sua pergunta"
        self.photo = PhotoImage(file=r"C:\Users\47829927855\Downloads\lupa.png")
        self.photoimage = self.photo.subsample(3, 3)
        self.perguntas = []
        self.respostas = []
        print(self.escolhido.nome)
        self.tela()
        self.frames()
        self.labels()
        self.combo_box()
        self.botoes()
        self.logica()
        self.sim_ou_nao()
        self.conta_vidas()

        janela.mainloop()

    def tela(self):
        self.janela.title('CARA A CARA')
        self.janela.geometry('500x500')
        self.janela.configure(background='#fff')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)
        self.janela.minsize(width=500, height=500)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg= '#3598D2',)
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.13)

        self.frame_1 = Frame(self.janela, bg= '#3598D2',)
        self.frame_1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.06)

        self.frame_2 = Frame(self.janela, bg= '#1B9044',)
        self.frame_2.place(relx=0.03, rely=0.30, relwidth=0.94, relheight=0.06)

        self.frame_3 = Frame(self.janela, bg= '#1B9044',)
        self.frame_3.place(relx=0.03, rely=0.48, relwidth=0.94, relheight=0.06)

        self.frame_4 = Frame(self.janela, bg='#3598D2')
        self.frame_4.place(relx=0.76, rely=0.8, relwidth= 0.2, relheight= 0.09)


    def labels(self):
        fontetitulo = ('Arial', 18, 'bold')
        self.fonte = ('Arial', 15, 'bold')
        self.lbtitulo = Label(self.frame_0, text='CARA A CARA', font=fontetitulo, fg='white', background='#3598D2')
        self.lbtitulo.place(relx=0.00, rely=0.25, relwidth=1.0, relheight=0.48)

        self.msg = Label(self.frame_1, text='Pessoa sorteada! Tente adivinhar', font=self.fonte, fg='white', bg='#3598D2')
        self.msg.place(relx=0.00, rely=0.20, relwidth=1.0, relheight=0.60)


    def conta_vidas(self):
        self.msg3 = Label(self.frame_4, text=f'Vidas: {self.vidas}', font=self.fonte, fg='white', bg='#3598D2')
        self.msg3.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

    def muda_tela(self, texto):
        self.msg4 = Label(self.janela, text=f'{texto}', font=self.fonte2, fg='black', bg='#fff')
        self.msg4.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        self.btRodadnv = Button(self.janela, text='SORTEAR OUTRA PESSOA', bg='#3598D2', fg='white', image=self.photo, compound= LEFT, command=Aplicacao)
        self.btRodadnv.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.09)


    def sim_ou_nao(self):
        self.dica = Label(self.frame_2, text=f'{self.s_n}', font=self.fonte, fg='white', bg='#1B9044')
        self.dica.place(relx=0.0, rely=0.01, relwidth=1.0, relheight=1.0)


    def pessoas(self):
        pessoas = [Pessoa('Michael Jackson', False, True, True, False, False, False, False, False, False, True, False),
                   Pessoa('Justin Bieber', False, True, True, False, True, True, False, False, False, True, False),
                   Pessoa('Selena Gomez', False, True, False, False, True, False, False, False, False, True, True),
                   Pessoa('Bruna Marquezine', False, True, False, False, True, False, False, False, False, True, True),
                   Pessoa('Virginia Fonseca', False, True, False, False, True, True, False, False, False, False, False),
                   Pessoa('Cleber Augusto', False, False, True, True, True, False, True, True, False, False, False),
                   Pessoa('Francis', False, False, True, True, True, False, True, True, False, False, False),
                   Pessoa('Henrique Doná',False, False, True, True, True, True, True, False, False, False, False),
                   Pessoa('Robert Bosch', False, True, True, False, False, False, True, False, True, False, False),
                   Pessoa('Lucca Dias', False, False, True, True, True, True, True, True, False, False, False),
                   Pessoa('Gaston', False, True, True, True, True, False, True, False, False, False, False),
                   Pessoa('Batman', True, True, True, False, True, False, False, False, True, False, False),
                   Pessoa('Superman', True, True, True, False, True, False, False, False, True, False, False)]
        random.shuffle(pessoas)
        return pessoas[0]

    def escolhe_pessoa(self):
        pessoa = self.pessoas()
        return pessoa


    def logica(self):
        pergunta = self.opcao.get()

        if pergunta != 'ESCOLHA' and pergunta not in self.perguntas:
            self.perguntas.append(pergunta)
            if pergunta != 'ESCOLHA':
                self.vidas -= 1
                self.conta_vidas()
            if 'homem' in pergunta:
                self.testa_pergunta("homem")
            elif 'famoso' in pergunta:
                self.testa_pergunta("famoso")
            elif 'personagem' in pergunta:
                self.testa_pergunta("personagem")
            elif 'vivo' in pergunta:
                self.testa_pergunta("vivo")
            elif 'loiro' in pergunta:
                self.testa_pergunta("loiro")
            elif 'cantor' in pergunta:
                self.testa_pergunta("cantor")
            elif 'ator' in pergunta:
                self.testa_pergunta("ator")
            elif 'conhece' in pergunta:
                self.testa_pergunta("conheco_pessoalmente")
            elif 'bosch' in pergunta:
                self.testa_pergunta("trabalha_bosch")
            elif 'instrutor' in pergunta:
                self.testa_pergunta("instrutor")
            elif 'Heroi' in pergunta:
                self.testa_pergunta("heroi")
            elif 'conhece' in pergunta:
                self.testa_pergunta("conheco_pessoalmente")
            if self.vidas <= 0:
                self.combobox_resposta()
        elif pergunta == 'ESCOLHA':
            self.s_n = "Faça sua pergunta abaixo"
            self.sim_ou_nao()
        else:
            self.s_n = "Você ja fez essa pergunta"
            self.sim_ou_nao()


    def perguntas_usadas(self):
        questions = ''
        for i in self.perguntas:
            questions += i + ': ' + self.respostas[self.perguntas.index(i)] + '\n'
        return questions





    def testa_pergunta(self, palavra):
        metodo = getattr(self.escolhido, palavra)
        print(metodo)
        if metodo == True:
            self.s_n = "Sim!"
            self.respostas.append(self.s_n)
            self.sim_ou_nao()
        else:
            self.s_n = "Não!"
            self.respostas.append(self.s_n)
            self.sim_ou_nao()

    def combo_box(self):
        resposta = ['Sou um  personagem?',
                   'Sou famoso?',
                   'Sou homem?',
                   'Voce me conhece pessoalmente?',
                   'Estou vivo?',
                   'Sou loiro?',
                   'Trabalho ou já trabalhei na bosch?',
                   'Sou instrutor?',
                    'Sou Heroi? ',
                    'Sou cantor?',
                    'Sou ator?']
        self.opcao = StringVar()
        self.opcao.set("ESCOLHA")
        option_menu = OptionMenu(self.frame_3, self.opcao, *resposta)
        option_menu.config(width=200, height=30, background='#1B9044', fg='white')
        option_menu.pack()

    def combobox_resposta(self):
        self.resposta = Frame(self.janela, bg='#fff')
        self.resposta.place(relx=0.0, rely=0.0, relwidth= 1.0, relheight= 1.0)

        self.combo = Frame(self.janela, bg='#fff')
        self.combo.place(relx=0.10, rely=0.62, relwidth= 0.8, relheight= 0.6)

        self.btValida = Button(self.janela, text='Validar', bg='white', fg='black', command=self.valida_vencedor)
        self.btValida.place(relx=0.39, rely=0.7, relwidth=0.2, relheight=0.09)

        self.msg2 = Label(self.janela, text='Quem sou eu?', font=self.fonte, fg='black', bg='#fff')
        self.msg2.place(relx=0.0, rely=0.50, relwidth=1.0, relheight=0.10)

        self.msg1 = Label(self.janela, text= f'{self.perguntas_usadas()}', font=self.fonte, fg='black', bg='#fff')
        self.msg1.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.5)

        pergunta = ['Henrique Dona',
                   'Justin Bieber',
                   'Cleber Augusto',
                   'Robert Bosch',
                   'Selena Gomez',
                   'Bruna Marquezine',
                   'Lucca Dias',
                   'Gaston',
                    'Batman',
                    'Superman',
                    'Francis',
                    'Virgina Fonseca',
                    'Michael Jackson']
        self.responda = StringVar()
        self.responda.set("ESCOLHA")
        option_menu = OptionMenu(self.combo, self.responda, *pergunta)
        option_menu.config(width=200,background='green', fg='white')
        option_menu.pack()

    def botoes(self):
        self.btValida = Button(self.janela, text='Perguntar', bg='#3598D2', fg='white', command=self.logica)
        self.btValida.place(relx=0.30, rely=0.58, relwidth=0.2, relheight=0.09)

        self.btRodadnv = Button(self.janela, text='SORTEAR OUTRA PESSOA',image=self.photo, compound= LEFT, bg='#3598D2', fg='white', command=Aplicacao)
        self.btRodadnv.place(relx=0.03, rely=0.8, relwidth=0.72, relheight=0.09)

        self.btChutar = Button(self.janela, text='Chutar', bg='#3598D2', fg='white', command=self.combobox_resposta)
        self.btChutar.place(relx=0.53, rely=0.58, relwidth=0.1, relheight=0.09)

    def valida_vencedor(self):
        if self.responda.get() == self.escolhido.nome:
            self.muda_tela("Você acertou!!")
        else:
            self.muda_tela(f"Que pena!! Você errou!! O sorteado foi {self.escolhido.nome}")
