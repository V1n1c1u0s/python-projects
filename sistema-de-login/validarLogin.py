import os
from editarDados import *

def validarLogin(email, senha):
    try:
        db = sqlite3.connect('dataUser.db')
        command = db.cursor()
        command.execute("SELECT email FROM dataUser")
        searchEmail = command.fetchall()
        emailEncont = 0
        for x in searchEmail:
            if email in x:
                emailEncont = 1
                command.execute(f"SELECT * FROM dataUser WHERE email='{email}'")
                dados = command.fetchall()
                if senha == dados[0][2]:
                    print('Usuario logado')
                    return [dados[0][0], dados[0][1], dados[0][2]]
                else:
                    print("Senha incorreta")
        if emailEncont == 0:
            print('Email não cadastrado!')
    except sqlite3.Error as error:
        print(error)

def logado(nome, email, senha):
    app = Tk()
    app.title('Home')
    app.geometry('490x560+610+153')
    app.resizable(width=0, height=0)

    #imagens
    background = PhotoImage(file="img/screen/telaVazia.png")
    btnSair = PhotoImage(file="img/button/botaoSair.png")
    btnEditDados = PhotoImage(file="img/button/botaoEditarDados.png")

    #funcoes
    def sair():
        app.destroy()
        os.system("python main.py")
    def editarCadastro():
        app.destroy()
        usuario = telaEditarCadastro(nome, email, senha)
        if usuario:
            logado(usuario[0], usuario[1], usuario[2])

    #labels
    labelBackground = Label(app, image=background)
    labelBackground.pack()
    labelBoasVindas = Label(app, text=f"Seja Bem-Vindo, {nome}!", font=("Calibri",22), bg="#cb4d89", fg="white")
    labelBoasVindas.place(width=340,height=30,x=90, y=180)

    #botao
    botaoEditDados = Button(app, bd=0, image=btnEditDados, command=editarCadastro)
    botaoEditDados.place(width=158, height=65, x=79, y=347)
    botaoSair = Button(app, bd=0, image=btnSair, command=sair)
    botaoSair.place(width=158, height=65, x=268, y=347)

    app.mainloop()