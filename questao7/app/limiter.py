from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

#Escolhi usar o limitador de requisições, para evitar ataques de força bruta
limiter = Limiter(get_remote_address, default_limits=["5 por minuto"])