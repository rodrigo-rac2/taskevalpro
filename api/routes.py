from flask import Blueprint, jsonify, request, abort
from datetime import datetime
from database import db
from models.usuario import Usuario
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    output = [{'id': usuario.id, 'nome_usuario': usuario.nome_usuario, 'email': usuario.email, 'papel': usuario.papel} for usuario in usuarios]
    return jsonify({'usuarios': output})

@routes_bp.route('/usuario/<int:id>', methods=['GET'])
def get_usuario_by_id(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        abort(404, description="Usuário não encontrado")
    
    return jsonify({
        'id': usuario.id,
        'nome_usuario': usuario.nome_usuario,
        'email': usuario.email,
        'papel': usuario.papel
    })

@routes_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nome_usuario = data.get('nome_usuario')
    email = data.get('email')
    senha = data.get('senha')
    papel = data.get('papel')

    if not nome_usuario or not email or not papel:
        return jsonify({'message': 'Faltam dados obrigatórios'}), 400

    # Verificar se o email já está em uso
    if Usuario.query.filter_by(email=email).first():
        return jsonify({'message': 'O email já está em uso'}), 409

    # Criar o usuário
    usuario = Usuario(nome_usuario=nome_usuario, email=email, papel=papel, senha=senha)
    db.session.add(usuario)
    db.session.commit()

    return jsonify({'message': 'Usuário criado com sucesso'}), 201

@routes_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.json
    nome_usuario = data.get('nome_usuario')
    email = data.get('email')
    senha = data.get('senha')
    papel = data.get('papel')

    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    # Atualizar os atributos do usuário
    if nome_usuario:
        usuario.nome_usuario = nome_usuario
    if email:
        usuario.email = email
    if papel:
        usuario.papel = papel
    if senha:
        usuario.senha = senha

    db.session.commit()

    return jsonify({'message': 'Usuário atualizado com sucesso'}), 200

@routes_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({'message': 'Usuário excluído com sucesso'}), 200

## tarefas
@routes_bp.route('/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = Tarefa.query.all()
    output = [{'id': tarefa.id, 'titulo': tarefa.titulo, 'descricao': tarefa.descricao, 'prioridade': tarefa.prioridade, 'prazo': str(tarefa.prazo), 'status': tarefa.status, 'id_criador': tarefa.id_criador, 'id_responsavel': tarefa.id_responsavel} for tarefa in tarefas]
    return jsonify({'tarefas': output})

# Get a specific task by ID using a new endpoint /tarefa/<id>
@routes_bp.route('/tarefa/<int:id>', methods=['GET'])
def get_tarefa_by_id(id):
    tarefa = Tarefa.query.get(id)
    if tarefa is None:
        abort(404, description="Tarefa não encontrada")
    
    return jsonify({
        'id': tarefa.id,
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao,
        'prioridade': tarefa.prioridade,
        'prazo': str(tarefa.prazo),
        'status': tarefa.status,
        'id_criador': tarefa.id_criador,
        'id_responsavel': tarefa.id_responsavel
    })

@routes_bp.route('/tarefas', methods=['POST'])
def create_tarefa():
    data = request.json
    titulo = data.get('titulo')
    descricao = data.get('descricao')
    prioridade = data.get('prioridade')
    prazo = data.get('prazo')
    status = data.get('status')
    id_criador = data.get('id_criador')
    id_responsavel = data.get('id_responsavel')

    if not titulo or not descricao or not prioridade or not prazo or not id_criador or not id_responsavel:
        return jsonify({'message': 'Faltam dados obrigatórios'}), 400

    # Verificar se o criador e o responsável existem
    criador = Usuario.query.get(id_criador)
    if not criador:
        return jsonify({'message': 'Criador não encontrado'}), 404

    responsavel = Usuario.query.get(id_responsavel)
    if not responsavel:
        return jsonify({'message': 'Responsável não encontrado'}), 404

    # Criar a tarefa
    tarefa = Tarefa(titulo=titulo,
                    descricao=descricao,
                    prioridade=prioridade,
                    prazo=datetime.strptime(prazo, '%Y-%m-%d'),
                    status=status,
                    id_criador=id_criador,
                    id_responsavel=id_responsavel)
    
    db.session.add(tarefa)
    db.session.commit()

    return jsonify({'message': 'Tarefa criada com sucesso'}), 201

@routes_bp.route('/tarefas/<int:id>', methods=['PUT'])
def update_tarefa(id):
    data = request.json
    titulo = data.get('titulo')
    descricao = data.get('descricao')
    prioridade = data.get('prioridade')
    prazo = data.get('prazo')
    status = data.get('status')
    id_responsavel = data.get('id_responsavel')

    tarefa = Tarefa.query.get(id)
    if not tarefa:
        return jsonify({'message': 'Tarefa não encontrada'}), 404

    # Atualizar os atributos da tarefa
    if titulo:
        tarefa.titulo = titulo
    if descricao:
        tarefa.descricao = descricao
    if prioridade:
        tarefa.prioridade = prioridade
    if prazo:
        tarefa.prazo = datetime.strptime(prazo, '%Y-%m-%d')
    if status:
        tarefa.status = status
    if id_responsavel:
        tarefa.id_responsavel = id_responsavel

    db.session.commit()

    return jsonify({'message': 'Tarefa atualizada com sucesso'}), 200

@routes_bp.route('/tarefas/<int:id>', methods=['DELETE'])
def delete_tarefa(id):
    tarefa = Tarefa.query.get(id)
    if not tarefa:
        return jsonify({'message': 'Tarefa não encontrada'}), 404

    db.session.delete(tarefa)
    db.session.commit()

    return jsonify({'message': 'Tarefa excluída com sucesso'}), 200


### avaliacoes

@routes_bp.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    output = [{'id': avaliacao.id, 'criterios_avaliacao': avaliacao.criterios_avaliacao, 'pontuacao': avaliacao.pontuacao, 'comentarios': avaliacao.comentarios, 'id_tarefa_avaliada': avaliacao.id_tarefa_avaliada, 'id_avaliador': avaliacao.id_avaliador, 'data_avaliacao': str(avaliacao.data_avaliacao)} for avaliacao in avaliacoes]
    return jsonify({'avaliacoes': output})

# Get a specific evaluation by ID using a new endpoint /avaliacao/<id>
@routes_bp.route('/avaliacao/<int:id>', methods=['GET'])
def get_avaliacao_by_id(id):
    avaliacao = Avaliacao.query.get(id)
    if avaliacao is None:
        abort(404, description="Avaliação não encontrada")
    
    return jsonify({
        'id': avaliacao.id,
        'criterios_avaliacao': avaliacao.criterios_avaliacao,
        'pontuacao': avaliacao.pontuacao,
        'comentarios': avaliacao.comentarios,
        'id_tarefa_avaliada': avaliacao.id_tarefa_avaliada,
        'id_avaliador': avaliacao.id_avaliador,
        'data_avaliacao': str(avaliacao.data_avaliacao)
    })

@routes_bp.route('/avaliacoes', methods=['POST'])
def create_avaliacao():
    data = request.json
    criterios_avaliacao = data.get('criterios_avaliacao')
    pontuacao = data.get('pontuacao')
    comentarios = data.get('comentarios')
    id_tarefa_avaliada = data.get('id_tarefa_avaliada')
    id_avaliador = data.get('id_avaliador')

    if not criterios_avaliacao or not pontuacao or not id_tarefa_avaliada or not id_avaliador:
        return jsonify({'message': 'Faltam dados obrigatórios'}), 400

    # Verificar se a tarefa avaliada e o avaliador existem
    tarefa = Tarefa.query.get(id_tarefa_avaliada)
    if not tarefa:
        return jsonify({'message': 'Tarefa não encontrada'}), 404

    avaliador = Usuario.query.get(id_avaliador)
    if not avaliador:
        return jsonify({'message': 'Avaliador não encontrado'}), 404

    # Criar a avaliação
    avaliacao = Avaliacao(criterios_avaliacao=criterios_avaliacao,
                          pontuacao=pontuacao,
                          comentarios=comentarios,
                          id_tarefa_avaliada=id_tarefa_avaliada,
                          id_avaliador=id_avaliador,
                          data_avaliacao=datetime.now())
    
    db.session.add(avaliacao)
    db.session.commit()

    return jsonify({'message': 'Avaliação criada com sucesso'}), 201

@routes_bp.route('/avaliacoes/<int:id>', methods=['PUT'])
def update_avaliacao(id):
    data = request.json
    criterios_avaliacao = data.get('criterios_avaliacao')
    pontuacao = data.get('pontuacao')
    comentarios = data.get('comentarios')

    avaliacao = Avaliacao.query.get(id)
    if not avaliacao:
        return jsonify({'message': 'Avaliação não encontrada'}), 404

    # Atualizar os atributos da avaliação
    if criterios_avaliacao:
        avaliacao.criterios_avaliacao = criterios_avaliacao
    if pontuacao:
        avaliacao.pontuacao = pontuacao
    if comentarios:
        avaliacao.comentarios = comentarios

    db.session.commit()

    return jsonify({'message': 'Avaliação atualizada com sucesso'}), 200

@routes_bp.route('/avaliacoes/<int:id>', methods=['DELETE'])
def delete_avaliacao(id):
    avaliacao = Avaliacao.query.get(id)
    if not avaliacao:
        return jsonify({'message': 'Avaliação não encontrada'}), 404

    db.session.delete(avaliacao)
    db.session.commit()

    return jsonify({'message': 'Avaliação excluída com sucesso'}), 200
