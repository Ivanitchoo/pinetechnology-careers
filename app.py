from flask import Flask, render_template, jsonify, request
from database import carregar_vagas_from_db, carregar_vaga_from_db

app = Flask(__name__)


@app.route("/")
def index():
  vagas_disponiveis = carregar_vagas_from_db()
  return render_template('home.html', vagas=vagas_disponiveis)


#Este é um API para aceder aos dados das vagas
#para qualquer finalidade
@app.route("/api/vagas")
def listar_emprego():
  vagas_disponiveis = carregar_vagas_from_db()
  return jsonify(vagas_disponiveis)


#rota dinâmica para aceder a página da vaga tendo o ID como o parâmetro
@app.route("/vaga/<id>")
def visualizar_vaga(id):
  vaga_disponivel = carregar_vaga_from_db(id)

  if not vaga_disponivel:
    return "Not Found", 404
  else:
    return render_template('vaga.html', vaga=vaga_disponivel)


@app.route("/vaga/<id>/candidatura_form")
def candidatura_form(id):
  
  vaga_disponivel = carregar_vaga_from_db(id)
  return render_template('candidatura_form.html', vaga=vaga_disponivel)

@app.route("/vaga/<id>/candidatura_form/submit", methods =['post'])
def candidatar_to_job(id):
  data = request.form
  return jsonify(data)
  #Guardar na base de dados
  #Enviar Email

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
