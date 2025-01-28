from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    tipo = request.form['tipo']
    if tipo == 'fisica':
        cpf = request.form['cpf']
        return f"Cadastro de pessoa física: {nome}, CPF: {cpf}"
    else:
        cnpj = request.form['cnpj']
        return f"Cadastro de pessoa jurídica: {nome}, CNPJ: {cnpj}"


if __name__ == '__main__':
    app.run(debug=True)
