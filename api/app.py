from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routes_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@taskevalpro-db/taskevalpro'
db.init_app(app)

# Registrar blueprints com injeção de dependência
app.register_blueprint(routes_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)
