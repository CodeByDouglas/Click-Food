from app.util.QRcode.criar_qrcode import criar_qrcode
from app import create_app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        caminho = criar_qrcode(10)
        print(f"QR code gerado em: {caminho}") 
