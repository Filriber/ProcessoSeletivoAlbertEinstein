#Questao 3 de Web Frameworks, processo seletivo Analista de Sistemas Jr Hospital Albert Einstein (Sem modularização)
from flask import Flask, request, jsonify

app = Flask(__name__)

#Criação do metodo GET para a saudação personalizada
@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Visitante')
    #onde formato a minha mensagem para JSON
    return jsonify({"mensagem": f"Ola, {nome}! Bem-Vindo a nossa API!"})

#Aqui uma requisição POST para gerar a soma do enunciado
@app.route('/soma', methods=['POST'])
def soma():
    dados = request.json
    n1 = dados.get("n1")
    n2 = dados.get("n2")

    #Caso um dos numeros esteja vazios, retorno uma mensagem de erro
    if n1 is None or n2 is None:
        return jsonify({"erro": "Forneça numeros corretamente no JSON"})
    
    #Caso contrario, retorno o resultado da soma
    resultado = n1 + n2
    return jsonify({"O resultado é: ":resultado})

if __name__ == '__main__':
    app.run()
    

