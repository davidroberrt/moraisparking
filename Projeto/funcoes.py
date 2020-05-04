from tkinter import *

class telas:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Sistema de estacionamento UNIESP 1.0")
        self.janela.configure(bg="black")
        self.janela.geometry("1000x600")
        self.janela.resizable(False, False)
        self.image1 = PhotoImage(file="images/login.png")
        self.image1 = self.image1.subsample(1, 1)
        self.labelimage = Label(bg='black', image=self.image1)

            # FRAMES :

        self.framec = Frame(self.janela, bg='#ffffff')
        self.frametext = Frame(self.janela)
        self.text_login = Label(self.framec, text='Login: ')
        self.text_senha = Label(self.framec, text='Senha: ')
        self.entry_login = Entry(self.framec, width=35)
        self.entry_senha = Entry(self.framec, width=35)
        self.button_enter = Button(self.framec, text='Entrar')
        self.janela.mainloop()

        def admin(self):
            self.labelimage.place(x=5, y=5, relwidth=1.0, relheight=1.0)
            self.pack(side=BOTTOM, pady='93', padx='1')
            self.text_login.pack()
            self.entry_login.pack()
            self.text_senha.pack()
            self.entry_senha.pack()
            self.button_enter.pack()
