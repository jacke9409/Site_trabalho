from app.models import db

class ItemCarrinho(db.Model):
    __tablename__ = 'itens_carrinho'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    variacao_id = db.Column(db.Integer, db.ForeignKey('variacoes.id'), nullable=False)
    quantidade = db.Column(db.Integer, default=1)

    variacao = db.relationship('Variacao')