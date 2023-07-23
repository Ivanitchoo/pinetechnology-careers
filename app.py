from flask import Flask, render_template, jsonify
from database import carregar_vagas_from_db

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


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
