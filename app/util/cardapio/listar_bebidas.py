from app.models import Bebida

def listar_bebidas():
    """
    Retorna todas as bebidas cadastradas com status 'ativo'.
    :return: Lista de instâncias de Bebida
    """
    return Bebida.query.filter_by(status='ativo').all() 