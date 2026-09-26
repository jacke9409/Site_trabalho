from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# importa todos os models pra registrar as tabelas no db.create_all()
from app.models.usuario import Usuario
from app.models.produto import Produto
from app.models.variacao import Variacao
from app.models.carrinho import ItemCarrinho
from app.models.pedido import Pedido, ItemPedido