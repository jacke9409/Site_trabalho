from app.models import db

class Variacao(db.Model):
    __tablename__ = 'variacoes'

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    tamanho = db.Column(db.String(10), nullable=False)
    cor = db.Column(db.String(40), nullable=False)
    estoque = db.Column(db.Integer, default=0)