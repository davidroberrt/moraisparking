from tkinter import *
from admin import Admin

class Main:
    def gestor(self):
        self.janela = Tk()
        self.janela.title("Sistema de estacionamento UNIESP 1.0")
        self.janela.configure(bg="black")
        self.janela.geometry("1000x600")
        self.janela.resizable(False, False)
        self.image1 = PhotoImage(file="images/bg_inicial.png")
        self.image1 = self.image1.subsample(1, 1)
        self.labelimage = Label(bg='black', image=self.image1)
        self.janela.mainloop()
    def login(self):

        #Instâncias:
        self.adm = Admin()
        self.janela = Tk()

        # Propriedades da janela:
        self.janela.title("Sistema de estacionamento UNIESP 1.0")
        self.janela.configure(bg="black")
        self.janela.geometry("1000x600")
        self.janela.resizable(False, False)

        #   BACKGROUNDS:

        self.image1 = PhotoImage(file="images/login.png")
        self.image1 = self.image1.subsample(1, 1)
        self.labelimage = Label(self.janela, bg='black', image=self.image1)

        #   FRAMES:
        self.framelogin = Frame(self.janela, bg='#6d0d10')


        #   FUNÇÕES:

        def tela_login():
            self.labelimage.place(x=5, y=5, relwidth=1.0, relheight=1.0)
            self.framelogin.pack(side=BOTTOM, pady='93', padx='1')
            self.text_login.grid(row=0, column=0, padx='2')
            self.text_senha.grid(row=1, column=0, padx='2')
            self.entry_login.grid(row=0, column=1)
            self.entry_senha.grid(row=1, column=1)
            self.button_enter.grid(row=2, column=1, pady='8')


        def enter_login():
            self.login = self.entry_login.get()
            self.senha = self.entry_senha.get()
            for i in range(0, 1):
                if (self.login) in self.adm.gestor:
                    if (self.login == self.adm.gestor[i][0]) and self.senha == self.adm.gestor[i][1]:
                        self.gestor()
                    else:
                        print("erro")
                else:
                    print("erro")

            #   WIDJETS:

        # login:

        self.text_login = Label(self.framelogin, text='Login:', bg='#6d0d10', fg='white')
        self.text_senha = Label(self.framelogin, text='Senha:', bg='#6d0d10', fg='white')
        self.entry_login = Entry(self.framelogin, width=35)
        self.entry_senha = Entry(self.framelogin, width=35)
        self.button_enter = Button(self.framelogin, text='Entrar', bg='#C02', fg='white', command=enter_login)

        # página 1:

        tela_login()
        self.janela.mainloop()

