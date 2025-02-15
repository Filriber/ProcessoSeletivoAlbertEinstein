from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.security import USERS_DB
from app.limiter import limiter

#Realizada a criação de um Blueprint para organizar as rotas do meu projeto
login_blueprint = Blueprint("login", __name__)

@login_blueprint.route('/login', methods=['POST'])
@limiter.limit("5 per minute")

def login():
    #Utilizo o try para realizar uma possivel prevenção de erro, pois caso aconteça, no nosso except irá notificar que há um problema na execução
    try:
        data = request.json
        usuario = data.get("usuario")
        senha = data.get("senha")

        if not usuario or not senha:
            return jsonify({"erro": "Usuário e senha são obrigatórios"}), 400

        user_hash = USERS_DB.get(usuario)
        if user_hash and check_password_hash(user_hash, senha):
            return jsonify({"mensagem": "Acesso concedido"}), 200

        return jsonify({"erro": "Usuário ou senha inválidos"}), 401

    except Exception:
        return jsonify({"erro": "Erro interno no servidor"}), 500