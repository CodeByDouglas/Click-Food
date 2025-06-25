from app import db
from app.models import Pedido

def cancelar_pedido(pedido_id):
    """
    Cancela um pedido alterando seu status para 'cancelado'.
    :param pedido_id: ID do pedido a ser cancelado
    :return: Instância do Pedido cancelado ou None se não encontrado
    """
    pedido = Pedido.query.get(pedido_id)
    
    if not pedido:
        return None
    
    pedido.status = "cancelado"
    db.session.commit()
    
    return pedido
