import os
import qrcode
from app.models.QRcode import MesaQR
from app import db

def criar_qrcode(numero_mesa, base_url="http://localhost:5000/mesa/"):
    """
    Cria um QR code para a URL da mesa e salva na pasta de imagens.
    :param numero_mesa: Número da mesa
    :param base_url: URL base para o QR code
    :return: Caminho do arquivo do QR code gerado
    """
    # Montar a URL
    url = f"{base_url}{numero_mesa}"
    
    # Gerar QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Pasta de destino
    pasta_destino = os.path.join(os.path.dirname(__file__), '../../static/image/QRcode')
    pasta_destino = os.path.abspath(pasta_destino)
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_destino, f"mesa_{numero_mesa}.png")
    img.save(caminho_arquivo)

    # Salvar no banco (ou atualizar)
    mesa_qr = MesaQR.query.filter_by(numero=numero_mesa).first()
    if not mesa_qr:
        mesa_qr = MesaQR(numero=numero_mesa, qrcode=caminho_arquivo)
        db.session.add(mesa_qr)
    else:
        mesa_qr.qrcode = caminho_arquivo
    db.session.commit()

    return caminho_arquivo
