from flask import Blueprint, request
import pandas as pd

from biblio.helpers.auth import login_required
from biblio.models.book import Book
from datetime import datetime

bp = Blueprint("books", __name__, url_prefix="/books")


@bp.route("/", methods=(["GET", "POST"]))
# @login_required
def books():
    if request.method == "GET":
        data = Book.select()
        
        df = pd.DataFrame(data, columns=['id', 'title', 'author', 'pages', 'date'])
       
        json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)

        return json_result
    
    if request.method == "POST":
        book = Book(request.form.get('title'),request.form.get('author'),request.form.get('pages'), datetime.now())
        try:
            data = book.insert()
        except:
            # fazer as mensagens de retorno
            return 'not ok'
        return 'ok'



@bp.route("/<int:id>", methods=(["GET", "PUT","DELETE"]))
# @login_required
def book(id):
    if request.method == "GET":
        data = Book.select_id(id)
        
        df = pd.DataFrame(data, columns=['id', 'title', 'author', 'pages', 'date'])
        json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
        
        return json_result
      
    if request.method == "PUT":
        book = Book(request.form.get('title'),request.form.get('author'),request.form.get('pages'),request.form.get('creat_at'), id_book=id)
        try:
            book.update()
            data = Book.select_id(id)
        
            df = pd.DataFrame(data, columns=['id', 'title', 'author', 'pages', 'date'])
            json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
            return json_result 
        
        except:
            # fazer as mensagens de retorno
            return 'not ok'
        
    if request.method == "DELETE":
        try:
            Book.delete(id)
            return 'ok'
        except:
            # fazer as mensagens de retorno
            return 'not ok'
        



