from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializar extensões
db = SQLAlchemy()

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Configurações básicas
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'
    
    # Configurar o banco de dados na pasta instance (padrão Flask)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'instance', 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensões com a app
    db.init_app(app)
    
    # Importar modelos para que sejam registrados com o SQLAlchemy
    from app.models import prato, bebida, pedido

    # Registrar blueprint de estabelecimento
    from app.routes.estabelecimento.cadastrar_cardapio import estabelecimento_bp
    app.register_blueprint(estabelecimento_bp)
    
    # Registrar outros blueprints aqui se necessário
    # from app.routes.cliente import cliente_bp
    # app.register_blueprint(cliente_bp)
    
    return app 