import os
from pathlib import Path
from flask import Blueprint, request, send_from_directory
import pandas as pd

from biblio.helpers.auth import login_required
from biblio.models.book import Book
from datetime import datetime
from werkzeug.utils import secure_filename
import json

bp = Blueprint("books", __name__, url_prefix="/books")


@bp.route("", methods=(["GET", "POST"]))
@login_required
def books():
    if request.method == "GET":
        data = Book.select()
        
        df = pd.DataFrame(data, columns=['id', 'title', 'author', 'pages', 'date'])
       
        json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)

        return json_result
    
    if request.method == "POST":
        data = request.form['book']
        convert_json = json.loads(data)
        book = Book(convert_json['title'],convert_json['author'],convert_json['pages'], datetime.now())
        
        img_book = request.files['img_book']
        caminho = Path().absolute()/  'biblio' / 'static' / 'books' 
        
        try:
            book.insert()
            
            data = Book.select_last_book()
            df = pd.DataFrame(data, columns=['id', 'title', 'author', 'pages', 'date'])
            
         
            img_book.save(os.path.join(caminho, secure_filename('cover-'+str(df['id'][0])+'.jpg')))
            
            json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
            return json_result
        except:
            # fazer as mensagens de retorno
            return 'not ok'
       



@bp.route("/<int:id>", methods=(["GET", "PUT","DELETE"]))
@login_required
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
        

@bp.route('/images/<path:filename>', methods=(["GET", "POST"]))
def images(filename):
    if request.method == "GET":
        caminho = Path().absolute()/  'biblio' / 'static' / 'books' 
        return send_from_directory(caminho ,filename)

