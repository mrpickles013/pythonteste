from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API Flask no Heroku funcionando!"

@app.route('/soma')
def soma():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'resultado': a + b})

@app.route('/mensagem', methods=['POST'])
def mensagem():
    data = request.get_json()
    texto = data.get('texto', '')
    return jsonify({'texto_maiusculo': texto.upper()})

if __name__ == '__main__':
    app.run()
