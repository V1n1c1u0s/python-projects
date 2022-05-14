from turtle import width
from validarLogin import *

def cadastrarUsuario(nome, email, senha):
    erro = 0
    #Validando os dados
    if validarDados(nome, email, senha) == 1:
        pass
    else:
        print('Não foi possível fazer o cadastro!')
        return 0
    #Conectando no Banco de Dados
    try:
        db = sqlite3.connect('dataUser.db')
        command = db.cursor()
        #Cria Banco de Dados Caso Ainda Não Exista Um
        command.execute("CREATE TABLE IF NOT EXISTS dataUser (nome text, email text, senha text)")
        command.execute(f"INSERT INTO dataUser VALUES ('{nome}', '{email}', '{senha}')")
        db.commit()
        db.close()
        print('Novo usuário cadastrado!')
        return 1
    except sqlite3.Error as error:
        print(error)
        return 0

def telaCadastro():
    app = Tk()
    app.title('Cadastrar Usuário')
    app.geometry('490x560+610+153')
    app.resizable(width=0, height=0)

    #imagens
    background = PhotoImage(file="img/screen/teladecadastro.png")
    botaoIMG = PhotoImage(file="img/button/botaoteladecadastro.png")
    botaoIMG2 = PhotoImage(file="img/screen/teladevoltar.png")
    alertBackground = PhotoImage(file="img/alert/erroDeCadastro.png")

    #funções
    def cadastrar():
        nonlocal alertBackground
        if cadastrarUsuario(inNome.get(), inEmail.get(), inSenha.get()) != 0:
            inNome.delete(0,"end")
            inEmail.delete(0,"end")
            inSenha.delete(0,"end")
            alertBackground = PhotoImage(file="img/alert/usuarioCadastrado.png")
            alert = Label(app, image = alertBackground)
            alert.pack()
            alert.place(x=69, y=72)
        else:
            alert = Label(app, image = alertBackground)
            alert.pack()
            alert.place(x=69, y=72)
    def telaLogin():
        app.destroy()
        os.system("python main.py")

    #labels
    labelBackground = Label(app, image=background)
    labelBackground.pack()

    #inputs
    inNome = Entry(app, bd=2, font=("Calibri",15), justify=CENTER)
    inNome.place(width=347, height=64, x=70, y=147)
    inEmail = Entry(app, bd=2, font=("Calibri",15), justify=CENTER)
    inEmail.place(width=347, height=64, x=72, y=252)

    escondaSenha = StringVar()

    inSenha = Entry(app, textvariable=escondaSenha, show='*', bd=2, font=("Calibri",15), justify=CENTER)
    inSenha.place(width=347, height=64, x=72, y=354)

    #botao
    botaoCadastro = Button(app, bd=0, image=botaoIMG, command=cadastrar)
    botaoCadastro.place(width=158, height=63, x=257, y=463)
    botaoTelaLogin = Button(app, bd=0, image=botaoIMG2, command=telaLogin)
    botaoTelaLogin.place(width=158,height=65,x=73,y=463)

    app.mainloop()