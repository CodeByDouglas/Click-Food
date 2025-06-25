from app.models import Pedido
from datetime import datetime

def listar_pedidos_confirmados_concluidos():
    """
    Retorna todos os pedidos com status 'confirmado' ou 'concluido' e data igual à data atual.
    :return: Lista de instâncias de Pedido
    """
    hoje = datetime.utcnow().date()
    return Pedido.query.filter(
        Pedido.status.in_(["confirmado", "concluido"]),
        Pedido.data_criacao >= datetime(hoje.year, hoje.month, hoje.day),
        Pedido.data_criacao < datetime(hoje.year, hoje.month, hoje.day, 23, 59, 59, 999999)
    ).all() 