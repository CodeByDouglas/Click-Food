from app import db
from app.models import Pedido
from datetime import datetime

def confirmar_pedido(pedido_id):
    """
    Confirma um pedido alterando seu status para 'confirmado' e preenche o campo horario_confirmacao.
    :param pedido_id: ID do pedido a ser confirmado
    :return: Instância do Pedido confirmado ou None se não encontrado
    """
    pedido = Pedido.query.get(pedido_id)
    
    if not pedido:
        return None
    
    pedido.status = "confirmado"
    pedido.horario_confirmacao = datetime.utcnow()
    db.session.commit()
    
    return pedido 