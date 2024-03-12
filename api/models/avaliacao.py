from database import db

class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    id = db.Column(db.Integer, primary_key=True)
    criterios_avaliacao = db.Column(db.String(100), nullable=False)
    pontuacao = db.Column(db.Integer, nullable=False)
    comentarios = db.Column(db.Text)
    id_tarefa_avaliada = db.Column(db.Integer, db.ForeignKey('tarefas.id'), nullable=False)
    id_avaliador = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    data_avaliacao = db.Column(db.Date, nullable=False)