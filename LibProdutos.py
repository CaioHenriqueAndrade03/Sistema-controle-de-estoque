class Produto:
    def __init__(self,nome,quantidade,preco):
        self.id = ""
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        
    def __str__(self):
        return 'f{self.nome}::{self.quantidade}::{self.preco}'
    
    def exibir(self):
         print(f'{self.nome} tem {self.quantidade} no estoque e cada unidade custa {self.preco} R$')
         
    def serialize(self):
        return{
            "id":self.id,
            "nome":self.nome,
            "quantidade":self.quantidade,
            "preco":self.preco
        }
         