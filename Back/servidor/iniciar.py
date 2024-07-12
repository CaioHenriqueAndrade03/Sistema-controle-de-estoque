from flask import Flask,Blueprint
from flask_restx import Api
from flask_cors import CORS

#Classe que iniciará o servidor
class Servidor():
    def __init__(self):
        #instancia do flask
        self.app = Flask(__name__) 
        CORS(self.app,origins= "*")
        
        #permite que a api seja acessada pela URL
        self.blueprint = Blueprint('api',__name__,url_prefix='/api')
        
        #permite que o blue print gere a documentação automatica
        self.api = Api(self.blueprint,doc='/doc',title="Controle de estoque")
        self.app.register_blueprint(self.blueprint)
        
        #Definições do banco de dados
        self.app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
        self.app.config["PROPAGATE_EXCEPTIONS"] = True

        self.produtos_n = self.produto_n

    @property
    def produto_n(self, ):
        return self.api.namespace(name="Produtos",description="Produtos relacionados a operação",path='/')
    
    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host="0.0.0.0"
        )

servidor = Servidor()
