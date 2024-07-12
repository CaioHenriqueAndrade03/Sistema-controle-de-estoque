from flask import request
from flask_restx import Resource,fields

from models.produtoDAO import ProdutoDAO
from Db.produto import ProdutoSchema

from servidor.iniciar import servidor

produto_n = servidor.produto_n

#definição do esquema de rotas do flask restx
schema_produto_com_id = ProdutoSchema()
schema_produto_sem_id = ProdutoSchema(many = True)

PRODUTO_N_LOCALIZADO ="Produto não encontrado"

#modelo que são as "promisses" da requisição
item = produto_n.model("Produto",
    {
        'nome':fields.String(description="Nome do produto"),
        'quantidade':fields.Integer(description="Quantidade de produto"),
        'preco':fields.Float(description="Preco do produto")
})
  
#separação dos metodos que precisam de id e dos que não precisam
class ProdutoComId(Resource):
    def get(self,id):
        produto_data = ProdutoDAO.achar_id(id)
        if produto_data:
            return schema_produto_com_id.dump(produto_data),200
        return{"menssagem":"Não há nenhum produto com este ID"},404
    
    @produto_n.expect(item)
    def put(self, id):
        try:
            produto_json = request.get_json()
            produto_data = ProdutoDAO.alterar_no_banco(id,produto_json)
            return schema_produto_com_id.dump(produto_data), 200
        except:
            return{"menssagem":"Não há nenhum produto com este ID"},404            
           
    def delete(self, id):
        produto_data = ProdutoDAO.achar_id(id)
        if produto_data:
            produto_data.deletar_do_banco()
            return "", 204
        return {"mensagem": PRODUTO_N_LOCALIZADO}, 404
    
   
class ProdutoSemId(Resource):
    @produto_n.expect(item)
    @produto_n.doc("Criar produto")
    def post(self,):
        produto_json = request.get_json()
        produto_data = schema_produto_com_id.load(produto_json)

        produto_data.salvar_no_banco()
        
        return schema_produto_com_id.dump(produto_data),201
    
    def get(self,):
        produto_data = ProdutoDAO.achar_todos()
        if produto_data:
            return schema_produto_sem_id.dump(produto_data),200
        return{"menssagem":""},404
    
  
