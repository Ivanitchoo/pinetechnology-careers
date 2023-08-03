from sqlalchemy import create_engine, text
import os

#string *ENCRIPTADA* de conexão á base de dados na cloud
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,

  #certificado ssl para conexão segura com a base de dados. Estes dados são obtidos na plataforma que hospeda a base de dados.
  connect_args={"ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }})


def carregar_vagas_from_db():
  with engine.connect() as conn:
    query = conn.execute(text("SELECT * FROM vagas"))

    #lista criada para armazenar os dicionários da base de dados 'Coluna:'Valor'
    vagas_disponiveis = []

    #neste bloco, cada resultado da query é retornado e convertido em dicionário, e depoois armazeado na lsta de dicionários vagas []
    for linha in query.all():
      vagas_disponiveis.append(linha._asdict())

    return vagas_disponiveis


def carregar_vaga_from_db(id):
  with engine.connect() as conn:
    query = conn.execute(text(f"SELECT * FROM vagas WHERE id = {id}"))

    vaga_disponivel = query.all()

    if len(vaga_disponivel) == 0:
      return None
    else:
      return vaga_disponivel[0]._asdict()
