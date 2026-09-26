from flask import Blueprint, render_template
from app.models.produto import Produto

loja_bp = Blueprint('loja', __name__)


@loja_bp.route('/')
def index():
    produtos = Produto.query.filter_by(ativo=True).all()
    categorias = sorted({p.categoria for p in produtos if p.categoria})

    return render_template(
        'base.html',
        produtos=produtos,
        categorias=categorias,
        nome_loja='VESTE'
    )