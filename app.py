from flask import Flask, request, send_file, jsonify
from gerador_relatorios import gerar_pdf, gerar_word, gerar_excel
import os

app = Flask(__name__)

@app.route('/')
def raiz():
    return jsonify({"mensagem": "API SENKAS rodando com sucesso!"})

@app.route('/relatorio/pdf', methods=['POST'])
def rota_pdf():
    dados = request.json
    caminho = gerar_pdf(dados)
    return send_file(caminho, as_attachment=True)

@app.route('/relatorio/word', methods=['POST'])
def rota_word():
    dados = request.json
    caminho = gerar_word(dados)
    return send_file(caminho, as_attachment=True)

@app.route('/relatorio/excel', methods=['POST'])
def rota_excel():
    dados = request.json
    caminho = gerar_excel(dados)
    return send_file(caminho, as_attachment=True)

if __name__ == '__main__':
    app.run()
