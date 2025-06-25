from app import db
from app.models import Bebida

def ativar_inativar_bebida(bebida_id):
    """
    Alterna o status de uma bebida entre 'ativo' e 'inativo'.
    :param bebida_id: ID da bebida
    :return: Instância da Bebida atualizada ou None se não encontrada
    """
    bebida = Bebida.query.get(bebida_id)
    if not bebida:
        return None
    if bebida.status == 'ativo':
        bebida.status = 'inativo'
    else:
        bebida.status = 'ativo'
    db.session.commit()
    return bebida
