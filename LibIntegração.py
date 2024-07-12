import requests
import json
from LibProdutos import Produto

def JSON2Produto(dadosJSON):
    p = Produto(dadosJSON['nome'],dadosJSON['quantidade'],dadosJSON['preco'])
    p.id = dadosJSON['id']
    return p

class ProdutoNet:
    def __init__(self):
        self.baseURL = 'http://127.0.0.1:5000/api/doc'