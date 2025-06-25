from app import db
from app.models import Pedido, ItemPedido, Prato, Bebida

def atualizar_itens_pedido(pedido_id, novos_itens, mesa=None):
    """
    Atualiza os itens de um pedido, removendo os antigos e inserindo os novos.
    Atualiza também o valor total e, se fornecido, o campo mesa.
    :param pedido_id: ID do pedido a ser atualizado
    :param novos_itens: Array no formato [[tipo, id, quantidade], ...]
    :param mesa: Novo número da mesa (opcional)
    :return: Instância do Pedido atualizado ou None se não encontrado
    """
    pedido = Pedido.query.get(pedido_id)
    if not pedido:
        return None

    # Remover todos os itens antigos do pedido
    ItemPedido.query.filter_by(pedido_id=pedido_id).delete()

    valor_total = 0.0
    # Adicionar os novos itens
    for item_data in novos_itens:
        tipo, item_id, quantidade = item_data
        if tipo.lower() == 'prato':
            item = Prato.query.get(item_id)
        elif tipo.lower() == 'bebida':
            item = Bebida.query.get(item_id)
        else:
            raise ValueError(f"Tipo inválido: {tipo}. Deve ser 'prato' ou 'bebida'")
        if not item:
            raise ValueError(f"Item não encontrado: {tipo} com ID {item_id}")
        valor_item = item.valor * quantidade
        valor_total += valor_item
        novo_item = ItemPedido(
            pedido_id=pedido_id,
            tipo_item=tipo.lower(),
            item_id=item_id,
            quantidade=quantidade
        )
        db.session.add(novo_item)

    # Atualizar valor total
    pedido.valor_total = valor_total
    # Atualizar mesa se fornecido
    if mesa is not None:
        pedido.mesa = mesa

    db.session.commit()
    return pedido 