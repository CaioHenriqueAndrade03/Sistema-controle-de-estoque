from flask import jsonify
from marshmallow import ValidationError
from utils.ma import ma
from Db.db import db
from controllers.produto import ProdutoComId,ProdutoSemId
from servidor.iniciar import servidor

api = servidor.api
app = servidor.app


#gera as routes do codigo, e da as funcionalidades de uma restAPI
api.add_resource(ProdutoComId,"/produto/<int:id>")
api.add_resource(ProdutoSemId,"/produto")

#se for a primeira vez do codigo rodando ele gera a tabela no banco de dados
@app.before_first_request
def create_tables():
    db.create_all()

#instancia o servidor e inicia o banco de dados
if __name__ == "__main__":
    ma.init_app(app)
    db.init_app(app)
    servidor.run()
