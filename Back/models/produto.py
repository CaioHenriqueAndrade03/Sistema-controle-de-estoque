from Db.db import db

#definição de como sera a construção da tabela
class ProdutoModel(db.Model):
    __tablename__="Produtos"

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(80),nullable=False,unique=True)
    quantidade = db.Column(db.Integer,nullable=False)
    preco = db.Column(db.Float,nullable=False)

    #o quais campos precisam ser preenchidos para permitir a adição ao banco
    def __init__(self,nome,quantidade,preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __repr(self,):
        return f"ProdutoModel(nome={self.nome},quantidade={self.quantidade},preco={self.preco})"
    
    #Modelo do json que vai ser lido na api
    def json(self,):
        return{
            "nome":self.nome,
            "quantidade":self.quantidade,
            "preco": self.preco,
        }
    
    #definição das querrys e o que elas vão fazer

    
    def salvar_no_banco(self,):
        db.session.add(self)
        db.session.commit()

    def deletar_do_banco(self,):
        db.session.delete(self)
        db.session.commit()
        