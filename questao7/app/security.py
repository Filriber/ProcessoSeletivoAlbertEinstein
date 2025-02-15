import os
#utilizei a biblioteca werkzeug para auxiliar o Flask nessa operação
from werkzeug.security import generate_password_hash

#Utilizado um banco de dados ficticio para poder testar a aplicação, sendo necessario realizar a troca por um real!
USERS_DB = {
    "admin": os.getenv("ADMIN_PASSWORD_HASH", generate_password_hash("123456"))
}


