from utils.ma import ma
from models import ProdutoModel
class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProdutoModel
        load_instance = True
