from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calc', methods=['POST'])
def calc():
    data = request.get_json()
    valor1 = data.get('valor1')
    valor2 = data.get('valor2')
    operacao = data.get('operacao')

    if valor1 is None or valor2 is None or operacao is None:
        return jsonify({'error': 'Parâmetros inválidos'}), 400

    if operacao == '+':
        resultado = int(valor1) + int(valor2)
    elif operacao == '-':
        resultado = int(valor1) - int(valor2)
    elif operacao == '*':
        resultado = int(valor1) * int(valor2)
    elif operacao == '/':
        if int(valor2) == 0:
            return jsonify({'resultado': 'Divisor não pode ser 0.'}), 400
        resultado = int(valor1) / int(valor2)
    else:
        return jsonify({'resultado': 'Operação inválida.'}), 400

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=False)
