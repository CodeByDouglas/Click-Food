from app import db

class MesaQR(db.Model):
    __tablename__ = 'mesas_qr'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    qrcode = db.Column(db.String(512), nullable=False)  # Pode ser caminho do arquivo ou base64

    def __repr__(self):
        return f'<MesaQR {self.numero}>'
