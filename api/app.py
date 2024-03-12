from flask import Flask
# Import SQLAlchemy instance
from database import db
from routes import routes_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@taskevalpro-db/taskevalpro'

# Link the db instance to the current app
db.init_app(app)

# Since models are now imported after db and app have been defined,
# it's safe to import them. Ensure that models are actually used or
# referenced to avoid unused import warnings.
with app.app_context():
    from models.usuario import Usuario
    from models.tarefa import Tarefa
    from models.avaliacao import Avaliacao
    db.create_all()  # Optional: Use only if you want to create tables at startup

# Register blueprints for dependency injection
app.register_blueprint(routes_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)
