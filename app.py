from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buscar_cep', methods=['GET'])
def buscar_cep():
    cep = request.args.get('cep')
    if not cep:
        return jsonify({"erro": "CEP não informado"}), 400

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            return jsonify({"erro": "Endereço não encontrado"})
        return jsonify({"rua": data.get("logradouro"), "bairro": data.get("bairro")})
    return jsonify({"erro": "Erro ao buscar o CEP"}), 500


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
