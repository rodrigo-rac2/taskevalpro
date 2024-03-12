from database import db


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
