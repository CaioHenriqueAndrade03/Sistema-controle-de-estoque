# dao.py
from Db.db import db
from models import ProdutoModel

class ProdutoDAO:
    @staticmethod
    def achar_nome(nome):
        return ProdutoModel.query.filter_by(nome=nome).first()
    
    @staticmethod
    def achar_id(id):
        return ProdutoModel.query.filter_by(id=id).first()
    
    @staticmethod
    def achar_todos():
        return ProdutoModel.query.all()
    
    @staticmethod
    def salvar_no_banco(produto):
        db.session.add(produto)
        db.session.commit()
        
    @staticmethod
    def alterar_no_banco(id,produto_json):
        produto_data = ProdutoDAO.achar_id(id)
        produto_data.nome = produto_json['nome']
        produto_data.quantidade = produto_json['quantidade']
        produto_data.preco = produto_json['preco']
        db.session.add(produto_data)
        db.session.commit()
        return produto_data
    
    @staticmethod
    def deletar_do_banco(produto):
        db.session.delete(produto)
        db.session.commit()
