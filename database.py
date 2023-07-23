from sqlalchemy import create_engine, text

#string de conexão á base de dados na cloud
db_connection_string = "mysql+pymysql://a25kpo4dly8nnkkdi4y7:pscale_pw_QHMdb7cwUqEDhBtnDxIMqS50cD4Y8rhHycbfrPCAJcv@aws.connect.psdb.cloud/pinetechologycareers?charset=utf8mb4"

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
