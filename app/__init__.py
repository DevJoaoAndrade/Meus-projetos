from flask import Flask
# importando o Blueprint criado na pasta app/routes/main
from app.routes.main import main_bp

# Essa função cria e retorna uma instancia do flask


def create_app():
    # Inicializa a aplicação flask. O argumento __name__ indica o módulo atual
    app = Flask(__name__)
    # Adiciona as rotas ao aplicativo flask
    app.register_blueprint(main_bp)
    return app
