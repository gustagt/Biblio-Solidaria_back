from flask import Blueprint, request
import pandas as pd

from biblio.helpers.auth import login_required
from biblio.models.protocol import Protocol

from datetime import datetime

bp = Blueprint("protocols", __name__, url_prefix="/protocols")


@bp.route("/", methods=(["GET", "POST"]))
# @login_required
def protocols():
    if request.method == "GET":
        data = Protocol.select()
        
        df = pd.DataFrame(data, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book'])
       
        json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)

        return json_result
    
    if request.method == "POST":
        book = Protocol(request.form.get('user_possession'),datetime.now(),request.form.get('id_book'))
        try:
            data = book.insert()
        except:
            # fazer as mensagens de retorno
            return 'not ok'
        return 'ok'



@bp.route("/<int:id>", methods=(["GET", "PUT","DELETE"]))
# @login_required
def protocol(id):
    if request.method == "GET":
        data = Protocol.select_id(id)
        
        df = pd.DataFrame(data, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book'])
        json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
        
        return json_result
      
    if request.method == "PUT":
        book = Protocol(request.form.get('user_possession'),request.form.get('remove_at'),request.form.get('id_book'), datetime.now(), id_protocol=id)
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
        



