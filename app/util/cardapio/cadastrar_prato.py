from app import db
from app.models import Prato

def cadastrar_prato(nome, foto=None, descricao=None, valor=0.0):
    """
    Cadastra um novo prato no banco de dados.
    :param nome: Nome do prato
    :param foto: URL ou caminho da foto
    :param descricao: Descrição do prato
    :param valor: Valor do prato
    :return: Instância do Prato cadastrado
    """
    novo_prato = Prato(
        nome=nome,
        foto=foto,
        descricao=descricao,
        valor=valor
    )
    db.session.add(novo_prato)
    db.session.commit()
    return novo_prato
