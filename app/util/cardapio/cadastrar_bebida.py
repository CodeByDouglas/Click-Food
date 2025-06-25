from app import db
from app.models import Bebida

def cadastrar_bebida(nome, foto=None, descricao=None, valor=0.0):
    """
    Cadastra uma nova bebida no banco de dados.
    :param nome: Nome da bebida
    :param foto: URL ou caminho da foto
    :param descricao: Descrição da bebida
    :param valor: Valor da bebida
    :return: Instância da Bebida cadastrada
    """
    nova_bebida = Bebida(
        nome=nome,
        foto=foto,
        descricao=descricao,
        valor=valor
    )
    db.session.add(nova_bebida)
    db.session.commit()
    return nova_bebida
