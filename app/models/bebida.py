from app import db

class Bebida(db.Model):
    __tablename__ = 'bebidas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='ativo')

    def __repr__(self):
        return f'<Bebida {self.nome}>'
