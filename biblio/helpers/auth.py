
import functools
from flask import Blueprint, g, jsonify, session, request
from datetime import datetime, timedelta
import jwt



bp = Blueprint("auth", __name__)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        try:
            token = request.headers['Token']
            g.token = token
            jwt.decode(token, 'dev', algorithms=["HS256"])  

        except jwt.ExpiredSignatureError:
            return jsonify(message="Token expirado.")
        except jwt.InvalidTokenError:
            return jsonify(message="Token inválido.")
        except:
            return jsonify(message="Usuario não Logado")
        return view(**kwargs)

    return wrapped_view


def auth(nome):
    
    vencimento =datetime.now() + timedelta(hours=12)
    token = jwt.encode({'user': nome,'exp': vencimento}, 'dev', algorithm="HS256")
    return token

