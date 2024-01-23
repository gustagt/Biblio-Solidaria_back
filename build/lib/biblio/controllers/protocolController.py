from flask import Blueprint, request, jsonify
import jwt
import pandas as pd

from biblio.helpers.auth import login_required
from biblio.models.protocol import Protocol

from datetime import datetime

bp = Blueprint("protocols", __name__, url_prefix="/protocols")


@bp.route("", methods=(["GET", "POST"]))
@login_required
def protocols():
    if request.method == "GET":
        data = Protocol.select()
        
        df = pd.DataFrame(data, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book'])
       
        json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)

        return json_result
    
    if request.method == "POST":
        json = request.get_json()
        
        protocol = Protocol(json['user_possession'],datetime.now(),json['id_book'])
        try:
            protocol.insert()
            data = Protocol.select_last_protocol()
            
            df = pd.DataFrame(data, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book'])
            json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
            return json_result
        except:
            # fazer as mensagens de retorno
            return jsonify(message =  "NOT ok"), 401




@bp.route("/<int:id>", methods=(["GET", "PUT","DELETE"]))
@login_required
def protocol(id):
    if request.method == "GET":
    
        data = Protocol.select_id(id)
        df = pd.DataFrame(data, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book'])
    
        json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
        return json_result
        

      
    if request.method == "PUT":
        json = request.get_json()
        book = Protocol(json['user_possession'],json['remove_at'],json['id_book'], datetime.now(), id_protocol=id)

        try:
            book.update()
            data = Protocol.select_id(id)
        
            df = pd.DataFrame(data, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book'])
            json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
            return json_result 
        
        except:
            # fazer as mensagens de retorno
            return 'not ok'
        
    if request.method == "DELETE":
        try:
            Protocol.delete(id)
            return 'ok'
        except:
            # fazer as mensagens de retorno
            return 'not ok'
        
@bp.route("/id-book/<int:id>", methods=(["GET", "POST"]))
@login_required
def protocol_book(id):
    if request.method == "GET":
        
         
        token = jwt.decode(request.headers['Token'], 'dev', algorithms=["HS256"]) 
        
        data = Protocol.select_last_protocol_id_book(id)
        
        
      
        df = pd.DataFrame(data, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book'])
        
        if not data or not df['returned_at'][0] is None: 
            json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=3)
            return json_result
        
        if token['user'] == df['user_possession'][0]:
            json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=3)
            return json_result
        
        else:
            return jsonify(message = ' A posse do livro está anexada atualmente com outro usuario. Favor comunicar o Setor GEINF.')
      



        
        
       
        



