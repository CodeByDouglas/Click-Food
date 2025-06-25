from app.models import Pedido
from datetime import datetime, date

def listar_pedidos_data(data=None):
    """
    Lista todos os pedidos de uma data específica. Se não receber data, lista todos os pedidos.
    :param data: datetime.date ou string no formato 'YYYY-MM-DD' (opcional)
    :return: Lista de instâncias de Pedido
    """
    if data:
        if isinstance(data, str):
            data = datetime.strptime(data, '%Y-%m-%d').date()
        return Pedido.query.filter(
            Pedido.data_criacao >= datetime(data.year, data.month, data.day),
            Pedido.data_criacao < datetime(data.year, data.month, data.day, 23, 59, 59, 999999)
        ).all()
    else:
        return Pedido.query.all()
