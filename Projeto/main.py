from tkinter import *

janela = Tk()
janela.title("Sistema de estacionamento UNIESP 1.0")
janela.configure(bg="black")
janela.geometry("1000x600")
janela.resizable(False, False)
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
    text_login.pack()
    entry_login.pack()
    text_senha.pack()
    entry_senha.pack()
    button_enter.pack()



tela_login()
janela.mainloop()
