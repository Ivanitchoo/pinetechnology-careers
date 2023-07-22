from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'titulo':'Electricista',
    'localizacao':'Namicopo, Nampula',
    'empresa':'EDM',
    'salario':'12.000,00 MTn'
  },
{
    'id':2,
    'titulo':'Contabilista',
    'localizacao':'Bairro do Aeroporto B, Maputo',
    'empresa':'Recheio',
    'salario':'16.880,00 MTn'
  },
{
    'id':3,
    'titulo':'Padeiro',
    'localizacao':'Pandora, Maputo',
    'empresa':'Lafões',
    'salario':'8.280,00 MTn'
  },
{
    'id':4,
    'titulo':'Especialista em Ciber-Segurança',
    'localizacao':'Bairro Central C, Maputo',
    'empresa':'Ernst&Young',
    'salario':'93.860,00 MTn'
  }
]

@app.route("/")
def index():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def listar_emprego():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
