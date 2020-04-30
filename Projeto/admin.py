from tkinter import *

janela = Tk()
janela.title("Sistema de estacionamento UNIESP 1.0")
janela.configure(bg="black")
janela.geometry("1000x600")
janela.resizable(False, False)


#   BACKGROUNDS:

image1 = PhotoImage(file="images/login.png")
image1 = image1.subsample(1, 1)
labelimage = Label(janela,bg='black', image=image1)


#   FRAMES:
framelogin = Frame(janela)

#   FUNÇÕES:


def tela_login():
    labelimage.place(x=5, y=5, relwidth=1.0, relheight=1.0)
    framelogin.pack(side=BOTTOM, pady='93', padx='1')
    text_login.pack()
    entry_login.pack()
    text_senha.pack()
    entry_senha.pack()
    button_enter.pack()
def button_enter():


#   WIDJETS:

text_login = Label(framelogin, text='Login:')
text_senha = Label(framelogin, text='Senha:')
entry_login = Entry(framelogin, width=35)
entry_senha = Entry(framelogin, width=35)
button_enter = Button(framelogin,text='Entrar', command=button_enter())
tela_login()

janela.mainloop()