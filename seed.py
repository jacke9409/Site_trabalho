from app.database import create_app
from app.models import db
from app.models.produto import Produto
from app.models.variacao import Variacao

app = create_app()

with app.app_context():
    # limpa dados antigos (opcional, útil pra rodar o seed várias vezes)
    Variacao.query.delete()
    Produto.query.delete()

    # cria produtos
    camiseta = Produto(
        nome='Camiseta Básica',
        descricao='Camiseta 100% algodão, corte reto',
        preco=59.90,
        imagem_url='https://via.placeholder.com/300',
        categoria='camiseta'
    )

    calca = Produto(
        nome='Calça Jeans',
        descricao='Calça jeans skinny, lavagem escura',
        preco=149.90,
        imagem_url='https://via.placeholder.com/300',
        categoria='calça'
    )

    db.session.add_all([camiseta, calca])
    db.session.flush()  # garante que camiseta.id e calca.id já existem

    # cria variações (tamanho/cor/estoque) pra cada produto
    variacoes = [
        Variacao(produto_id=camiseta.id, tamanho='P', cor='Branco', estoque=10),
        Variacao(produto_id=camiseta.id, tamanho='M', cor='Branco', estoque=15),
        Variacao(produto_id=camiseta.id, tamanho='G', cor='Preto', estoque=8),
        Variacao(produto_id=calca.id, tamanho='38', cor='Azul', estoque=5),
        Variacao(produto_id=calca.id, tamanho='40', cor='Azul', estoque=7),
    ]

    db.session.add_all(variacoes)
    db.session.commit()

    print('Seed concluído! Produtos e variações criados.')