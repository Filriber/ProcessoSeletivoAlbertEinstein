from flask import Blueprint, request, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Visitante')
    return jsonify({"mensagem": f"Ola, {nome}! Seja muito bem-vindo a nossa API!"})

@bp.route('/soma', methods=['POST'])
def soma():
    dados = request.json
    n1 = dados.get("n1")
    n2 = dados.get("n2")

    if n1 is None or n2 is None:
        return jsonify({"erro": "Forneça números corretamente no JSON"}), 400
    
    resultado = n1 + n2
    return jsonify({"O resultado é": resultado})




