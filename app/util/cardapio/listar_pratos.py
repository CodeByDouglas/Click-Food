from app.models import Prato

def listar_pratos():
    """
    Retorna todos os pratos cadastrados com status 'ativo'.
    :return: Lista de instâncias de Prato
    """
    return Prato.query.filter_by(status='ativo').all() 
