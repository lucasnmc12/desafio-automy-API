from flask import Flask, request, render_template
from auth import obter_token
from query import buscar_baterias
from mensagens import gerar_mensagem
from flask import request
from flask_cors import CORS
from flask import jsonify
from datetime import datetime






app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/baterias", methods = ["GET"])
def baterias():
    email = request.args.get("email") 
    print("email recebido", email)
    if not email:
        return "Email não fornecido", 400
    
    token = obter_token()
    if not token:
        return "Erro na autenticação", 401
    
    dados = buscar_baterias(token, email)
    print("dados retornados:", dados)
    
    #separar as baterias anteriores e as próximas
    hoje = datetime.now().date()
    agendadas = []
    passadas = []


    for b in dados:
        try:
            data = datetime.strptime(b["data_agendamento"], "%d/%m/%Y").date()
            print(f"Data processada: {data} | Hoje: {hoje}")

            if data>= hoje:
                agendadas.append(b)
            else:
                passadas.append(b)
        except Exception as e:
            print("erro ao converter data:{b['data_agendamento]} -{e}")
    

    return jsonify({"agendadas": agendadas, "passadas": passadas})




if __name__ =="__main__":
   app.run(debug=True)




