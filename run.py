# Aqui fazemos a importação do create app dentro de __init__ que está dentro da pasta app
from app import create_app

# Aqui criamos uma variável que recebe o retorno da função create_app()
app = create_app()

if __name__ == '__main__':
    # Executando o programa com o modo debug ligado
    app.run(debug=True)
