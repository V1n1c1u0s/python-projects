from cadastro import *

app = Tk()
app.title('Login')
app.geometry('490x560+610+153')
app.resizable(width=0, height=0)

#funcoes
def telaDeCadastro():
    app.destroy()
    telaCadastro()
def verificarLogin():
    usuario = validarLogin(inEmail.get(), inSenha.get())
    if usuario:
        app.destroy()
        logado(usuario[0],usuario[1],usuario[2])
    else:
        global alertBackground
        alert = Label(app, image = alertBackground)
        alert.pack()
        alert.place(x=72, y=95)

#imagens
alertBackground = PhotoImage(file="img/alert/loginIncorreto.png")
background = PhotoImage(file="img/screen/teladelogin.png")
btnCadastro = PhotoImage(file="img/button/botaocadastrarusuario.png")
btnLogin = PhotoImage(file="img/button/botaodelogin.png")

#labels
labelBackground = Label(app, image = background)
labelBackground.pack()

#inputs
inEmail = Entry(app, bd=2, font=("Calibri",15), justify=CENTER)
inEmail.place(width=347, height=64, x=72, y=194)

escondaSenha = StringVar()

inSenha = Entry(app, textvariable=escondaSenha, show='*', bd=2, font=("Calibri",15), justify=CENTER)
inSenha.place(width=347, height=64, x=72, y=301)

#botao
botaoCadastro = Button(app, bd=0, image=btnCadastro, command=telaDeCadastro)
botaoCadastro.place(width=158, height=65, x=73, y=428)
botaoLogin = Button(app, bd=0, image=btnLogin, command=verificarLogin)
botaoLogin.place(width=158,height=65,x=258, y=428)

app.mainloop()