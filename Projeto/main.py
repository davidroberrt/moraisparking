from tkinter import *
<<<<<<< HEAD
from admin import Admin

adm = Admin()
=======

>>>>>>> 20713994b2dc01b05f6dcb2dade749d36a4974e3
janela = Tk()
janela.title("Sistema de estacionamento UNIESP 1.0")
janela.configure(bg="black")
janela.geometry("1000x600")
janela.resizable(False, False)
<<<<<<< HEAD


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
=======
#janela.iconbitmap("icon/favicon.ico") //no windows

# IMPORTAÇÃO DE IMAGENS:

image1 = PhotoImage(file="images/login.png")
image1 = image1.subsample(1, 1)
labelimage = Label(bg='black', image=image1)

# FRAMES :

framec = Frame(janela)
frametext = Frame(janela)

# WIDJETS: LABEL, ENTRY, BUTTON:
def bton():
    entry_login.get()
text_login = Label(framec, text='Login:')
text_senha = Label(framec, text='Senha:')
entry_login = Entry(framec, width=35)
entry_senha = Entry(framec, width=35)
button_enter = Button(framec,text='Entrar', command=bton())


# FUNÇÕES DE EMPACOTAMENTO:

def tela_login():
    labelimage.place(x=5, y=5, relwidth=1.0, relheight=1.0)
    framec.pack(side=BOTTOM, pady='93', padx='1')
>>>>>>> 20713994b2dc01b05f6dcb2dade749d36a4974e3
    text_login.pack()
    entry_login.pack()
    text_senha.pack()
    entry_senha.pack()
    button_enter.pack()


<<<<<<< HEAD
def enter_login():
    login = entry_login.get()
    senha = entry_senha.get()
    for i in range(0,1):
        if login == adm.admin[i][0]:
            if senha == adm.admin[i][1]:
                print("user on")
            else:
                print("erro")


#   WIDJETS:

text_login = Label(framelogin, text='Login:')
text_senha = Label(framelogin, text='Senha:')
entry_login = Entry(framelogin, width=35)
entry_senha = Entry(framelogin, width=35)
button_enter = Button(framelogin,text='Entrar', command=enter_login)

tela_login()
janela.mainloop()
=======

tela_login()
janela.mainloop()
>>>>>>> 20713994b2dc01b05f6dcb2dade749d36a4974e3
