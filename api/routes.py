from flask import Blueprint, jsonify
from models import db, Usuario, Tarefa, Avaliacao

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    output = [{'id': usuario.id, 'nome_usuario': usuario.nome_usuario, 'email': usuario.email, 'papel': usuario.papel} for usuario in usuarios]
    return jsonify({'usuarios': output})

@routes_bp.route('/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = Tarefa.query.all()
    output = [{'id': tarefa.id, 'titulo': tarefa.titulo, 'descricao': tarefa.descricao, 'prioridade': tarefa.prioridade, 'prazo': str(tarefa.prazo), 'status': tarefa.status, 'id_criador': tarefa.id_criador, 'id_responsavel': tarefa.id_responsavel} for tarefa in tarefas]
    return jsonify({'tarefas': output})

@routes_bp.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    output = [{'id': avaliacao.id, 'criterios_avaliacao': avaliacao.criterios_avaliacao, 'pontuacao': avaliacao.pontuacao, 'comentarios': avaliacao.comentarios, 'id_tarefa_avaliada': avaliacao.id_tarefa_avaliada, 'id_avaliador': avaliacao.id_avaliador, 'data_avaliacao': str(avaliacao.data_avaliacao)} for avaliacao in avaliacoes]
    return jsonify({'avaliacoes': output})
