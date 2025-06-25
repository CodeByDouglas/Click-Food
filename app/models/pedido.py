from app import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    entrega = db.Column(db.Boolean, default=False)
    mesa = db.Column(db.Integer)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    horario_confirmacao = db.Column(db.DateTime, nullable=True)
    horario_conclusao = db.Column(db.DateTime, nullable=True)

    # Relação com itens do pedido
    itens = db.relationship('ItemPedido', backref='pedido', lazy=True)

    def __repr__(self):
        return f'<Pedido {self.id}>'

class ItemPedido(db.Model):
    __tablename__ = 'itens_pedido'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    tipo_item = db.Column(db.String(10), nullable=False)  # 'prato' ou 'bebida'
    item_id = db.Column(db.Integer, nullable=False)  # id do prato ou bebida
    quantidade = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return f'<ItemPedido {self.id} - Pedido {self.pedido_id}>'
