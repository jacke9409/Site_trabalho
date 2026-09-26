from app.models import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    status = db.Column(db.String(30), default='pendente')
    total = db.Column(db.Numeric(10, 2), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    itens = db.relationship('ItemPedido', backref='pedido', lazy=True)


class ItemPedido(db.Model):
    __tablename__ = 'itens_pedido'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    variacao_id = db.Column(db.Integer, db.ForeignKey('variacoes.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Numeric(10, 2), nullable=False)

    variacao = db.relationship('Variacao')