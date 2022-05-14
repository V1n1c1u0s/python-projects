import sqlite3
from threading import local
from tkinter import *

def telaEditarCadastro(nome, email, senha):
    app = Tk()
    app.title("Editar Cadastro")
    app.geometry('490x560+610+153')
    app.resizable(width=0, height=0)

    #imagens
    background = PhotoImage(file="img/screen/telaEditarCadastro.png")
    btnSair = PhotoImage(file="img/button/botaoSair.png")

    usuario = 0

    #funcoes
    def sair():
        nonlocal usuario
        usuario = editDados(nome, email, senha, inNome.get(), inEmail.get(), inSenha.get())
        if usuario:
            app.destroy()

    #labels
    labelBackground = Label(app, image=background)
    labelBackground.pack()

    #inputs
    inNome = Entry(app, bd=2, font=("Calibri",15), justify=CENTER)
    inNome.place(width=347, height=64, x=72, y=137)
    inEmail = Entry(app, bd=2, font=("Calibri",15), justify=CENTER)
    inEmail.place(width=347, height=64, x=72, y=248)

    escondaSenha = StringVar()

    inSenha = Entry(app, textvariable=escondaSenha, show='*', bd=2, font=("Calibri",15), justify=CENTER)
    inSenha.place(width=347, height=64, x=72, y=356)

    inNome.insert(0, nome)
    inEmail.insert(0, email)
    inSenha.insert(0, senha)

    #botao
    botaoSair = Button(app, bd=0, image=btnSair, command=sair)
    botaoSair.place(width=158, height=65, x=165, y=462)

    app.mainloop()

    if usuario:
        return [usuario[0], usuario[1], usuario[2]]

def editDados(nome, email, senha, inNome, inEmail, inSenha):
    if nome == inNome and email == inEmail and senha == inSenha:
        return [nome, email, senha]
    try:
        db = sqlite3.connect('dataUser.db')
        command = db.cursor()
        command.execute(f"UPDATE dataUser SET nome='{inNome}', email='{inEmail}', senha='{inSenha}' WHERE email='{email}'")
        db.commit()
        db.close()
        return [inNome, inEmail, inSenha]
    except sqlite3.Error as error:
        print(error)
        return 0

def validarDados(nome, email, senha):
    erros = 0
    if nome:
        pass
    else:
        print('Nome Inválido!')
        erros += 1
    if '@' in email and '.com' in email:
        '''
        db = sqlite3.connect('dataUser.db')
        command = db.cursor()
        if email == emailsql: ajeitar esse comando
            return 0
        '''
        pass
    else:
        print('Email Inválido!')
        erros += 1
    if len(senha) > 6:
        pass
    else:
        print('Senha muito curta!')
        erros += 1
    if erros >= 1:
        return 0
    return 1