from app import db

class Prato(db.Model):
    __tablename__ = 'pratos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    valor = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Prato {self.nome}>'
