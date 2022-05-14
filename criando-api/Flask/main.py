from flask import Flask, request

app = Flask("API Python")

@app.route("/", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()

    if("nome" not in body): return gerarResponse(400,"O parâmetro nome é obrigatório!")
    if("email" not in body): return gerarResponse(400,"O parâmetro email é obrigatório!")
    if("senha" not in body): return gerarResponse(400,"O parâmetro senha é obrigatório!")

    usuario = insereUsuario(body["nome"],body["email"],body["senha"])

    return gerarResponse(200, "Usuário criado!", "user", usuario)

def insereUsuario(nome, email, senha):
    return {"nome": nome , "email": email}

def gerarResponse(status, mensagem, nome_do_conteudo = False, conteudo = False):
    response = {}
    response["mensagem"] = mensagem
    response["status"] = status
    
    if(nome_do_conteudo and conteudo): response[nome_do_conteudo] = conteudo

    return response

app.run()