from app import db
from app.models import Pedido
from datetime import datetime

def concluir_pedido(pedido_id):
    """
    Conclui um pedido alterando seu status para 'concluido' e preenche o campo horario_conclusao.
    :param pedido_id: ID do pedido a ser concluído
    :return: Instância do Pedido concluído ou None se não encontrado
    """
    pedido = Pedido.query.get(pedido_id)
    
    if not pedido:
        return None
    
    pedido.status = "concluido"
    pedido.horario_conclusao = datetime.utcnow()
    db.session.commit()
    
    return pedido 
