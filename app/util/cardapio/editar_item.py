from app import db
from app.models import Prato, Bebida

def editar_item(tipo, id_item, **kwargs):
    """
    Edita um item (prato ou bebida) no banco de dados.
    :param tipo: 'prato' ou 'bebida'
    :param id_item: ID do item a ser editado
    :param kwargs: Dados a serem alterados (nome, foto, descricao, valor)
    :return: Instância do item editado ou None se não encontrado
    """
    if tipo.lower() == 'prato':
        item = Prato.query.get(id_item)
    elif tipo.lower() == 'bebida':
        item = Bebida.query.get(id_item)
    else:
        raise ValueError("Tipo deve ser 'prato' ou 'bebida'")
    
    if not item:
        return None
    
    # Atualiza os campos fornecidos
    for campo, valor in kwargs.items():
        if hasattr(item, campo):
            setattr(item, campo, valor)
    
    db.session.commit()
    return item
