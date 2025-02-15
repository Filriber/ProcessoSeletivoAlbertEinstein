#Questao 7 de Security Practices, processo seletivo Analista de Sistemas Jr Hospital Albert Einstein (Sem modularização)
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

#Escolhi usar o limitador de requisições, para evitar ataques de força bruta
limitador = Limiter(get_remote_address, app=app, default_limits=["5 por minuto"])


USERS_DB = {
    "admin": os.getenv("ADMIN_PASSWORD_HASH", "pbkdf2:sha256:260000$hashedpassword")
}

@app.route('/login', methods=['POST'])
@limitador.limit("5 por minuto")

def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"erro": "Usuário e senha são obrigatórios"}), 400

        user_hash = USERS_DB.get(username)
        if user_hash and check_password_hash(user_hash, password):
            return jsonify({"mensagem": "Acesso concedido"}), 200
        
        return jsonify({"erro": "Usuário ou senha inválidos"}), 401
    
    except Exception as e:
        return jsonify({"erro": "Erro interno no servidor"}), 500
 
if __name__ == '__main__':
    #Retirado o debug=True com a finalidade de evitar vazamento de informações
    app.run()
