from app.models import db

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    imagem_url = db.Column(db.String(255))
    categoria = db.Column(db.String(80))
    ativo = db.Column(db.Boolean, default=True)

    variacoes = db.relationship('Variacao', backref='produto', lazy=True)