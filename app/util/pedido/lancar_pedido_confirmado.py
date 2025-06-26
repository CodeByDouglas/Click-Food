from app import db
from app.models import Pedido, ItemPedido, Prato, Bebida
from datetime import datetime

def lancar_pedido_confirmado(itens_array, entrega=False, mesa=None):
    """
    Cria um pedido confirmado com os itens fornecidos.
    :param itens_array: Array no formato [[tipo, id, quantidade], [tipo, id, quantidade], ...]
    :param entrega: Boolean indicando se é entrega (True) ou mesa (False)
    :param mesa: Número da mesa (pode ser None se entrega=True)
    :return: Instância do Pedido criado
    """
    # Validação: se não for entrega, mesa deve ser fornecida
    if not entrega and mesa is None:
        raise ValueError("Mesa deve ser fornecida quando não for entrega")
    
    # Criar o pedido
    novo_pedido = Pedido(
        valor_total=0.0,
        status="confirmado",
        entrega=entrega,
        mesa=mesa,
        horario_confirmacao=datetime.utcnow()
    )
    db.session.add(novo_pedido)
    db.session.flush()  # Para obter o ID do pedido
    
    valor_total = 0.0
    
    # Processar cada item do array
    for item_data in itens_array:
        tipo, item_id, quantidade = item_data
        
        # Buscar o item no banco para obter o valor
        if tipo.lower() == 'prato':
            item = Prato.query.get(item_id)
        elif tipo.lower() == 'bebida':
            item = Bebida.query.get(item_id)
        else:
            raise ValueError(f"Tipo inválido: {tipo}. Deve ser 'prato' ou 'bebida'")
        
        if not item:
            raise ValueError(f"Item não encontrado: {tipo} com ID {item_id}")
        
        # Calcular valor do item
        valor_item = item.valor * quantidade
        valor_total += valor_item
        
        # Criar ItemPedido
        item_pedido = ItemPedido(
            pedido_id=novo_pedido.id,
            tipo_item=tipo.lower(),
            item_id=item_id,
            quantidade=quantidade
        )
        db.session.add(item_pedido)
    
    # Atualizar valor total do pedido
    novo_pedido.valor_total = valor_total
    
    db.session.commit()
    return novo_pedido 
