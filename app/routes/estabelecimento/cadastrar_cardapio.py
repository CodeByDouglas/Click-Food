from flask import Blueprint, render_template

estabelecimento_bp = Blueprint('estabelecimento', __name__, url_prefix='/estabelecimento')

@estabelecimento_bp.route('/cadastrar-cardapio')
def cadastrar_cardapio():
    return render_template('estabelecimento/cadastrar_cardapio.html')
