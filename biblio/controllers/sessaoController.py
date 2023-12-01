
from flask import Blueprint, g, request,  jsonify, session
from ldap3 import SUBTREE, ALL_ATTRIBUTES
import jwt

from biblio.helpers.auth import auth
from biblio.data.ad import connectAD

from  biblio.credentials.credentials import active_directory

bp = Blueprint("sessao", __name__, url_prefix="/sessao")
@bp.route("/login", methods=(["POST"]))
def loginAD():
    g.token = None
    json = request.get_json()

    username = json["username"]
    password = json["password"]

    if not username:
        return jsonify(message = "Username is required."), 400
    elif not password:
        return jsonify(message ="Password is required."), 400

    resp = {"username": "", "token": "", "message": ""}

    connectAD(username, password)

    if not g.ad.bind():
        return jsonify(message =  "Credenciais Invalidas"), 401
    else:
 
        search_filter = f'(sAMAccountname= {username})'
        
        g.ad.search(search_base=f"ou=USUARIOS,dc={active_directory.DOMAIN},dc={active_directory.NAME}", search_filter=search_filter, search_scope=SUBTREE, attributes=ALL_ATTRIBUTES)
        
        entry = g.ad.entries[0] if g.ad.entries else None
        if entry:
            g.token = auth(username)
            resp.update(
                {
                    "username": username,
                    "displayName": entry.entry_attributes_as_dict['displayName'][0],
                    "token":  g.token,
                    "message": "ok-login",
                }
            )
            g.ad.unbind()
            return resp
        else:
            return jsonify(message = "Usuário sem permissão para esse sistema."), 403

    
@bp.route('/sair', methods=(["GET"]))  
def logout():
    g.token = None
    session.clear()
    return jsonify(sair = True), 200 


@bp.route('/auth', methods=(["GET"]))  
def authenticate():
    try:
        token = request.headers['Token']
        g.token = token
        jwt.decode(token, 'dev', algorithms=["HS256"]) 
        return jsonify(token=token)

    except jwt.ExpiredSignatureError:
        return jsonify(message="Token expirado.")
    except jwt.InvalidTokenError:
        return jsonify(message="Token inválido.")
    except:
        return jsonify(message="Usuario não Logado")