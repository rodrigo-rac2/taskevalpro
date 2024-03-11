from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    papel = db.Column(db.String(50), nullable=False)

class Tarefa(db.Model):
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    prioridade = db.Column(db.Integer, nullable=False)
    prazo = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, default=False)
    id_criador = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_responsavel = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    id = db.Column(db.Integer, primary_key=True)
    criterios_avaliacao = db.Column(db.String(100), nullable=False)
    pontuacao = db.Column(db.Integer, nullable=False)
    comentarios = db.Column(db.Text)
    id_tarefa_avaliada = db.Column(db.Integer, db.ForeignKey('tarefas.id'), nullable=False)
    id_avaliador = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    data_avaliacao = db.Column(db.Date, nullable=False)
