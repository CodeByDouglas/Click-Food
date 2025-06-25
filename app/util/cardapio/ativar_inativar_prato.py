from app import db
from app.models import Prato

def ativar_inativar_prato(prato_id):
    """
    Alterna o status de um prato entre 'ativo' e 'inativo'.
    :param prato_id: ID do prato
    :return: Instância do Prato atualizado ou None se não encontrado
    """
    prato = Prato.query.get(prato_id)
    if not prato:
        return None
    if prato.status == 'ativo':
        prato.status = 'inativo'
    else:
        prato.status = 'ativo'
    db.session.commit()
    return prato
