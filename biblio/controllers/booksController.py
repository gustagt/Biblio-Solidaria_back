import os
from pathlib import Path
from flask import Blueprint, request, send_from_directory
import pandas as pd

from biblio.helpers.auth import login_required
from biblio.models.book import Book
from biblio.models.assessments import Assessments
from biblio.models.protocol import Protocol
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
        book = Book.select_id(id)
        if book:
            assessments = Assessments.select_id_book(id)
            
            
            
            df_assessments = pd.DataFrame(assessments, columns=['id_assessment', 'overall', 'romantic', 'fun', 'sad','shocking','comments','id_book','protocol'])
            
            assessments_json = df_assessments.to_json(orient='records', date_format='iso', force_ascii=False, indent=3)
            
            df = pd.DataFrame(book, columns=['id', 'title', 'author', 'pages', 'date'])
            
            json_result = df.to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
            book_json = json.loads(json_result)[0]
            book_json['assessments'] = json.loads(assessments_json)
            
            count = 0
            
            if assessments:
                for assessment in assessments:
                    protocol = Protocol.select_id(assessment[-1])
                    protocol_str = pd.DataFrame(protocol, columns=['id', 'user_possession', 'remove_at', 'returned_at', 'id_book']).to_json(orient='records', date_format='iso', force_ascii=False, indent=2)
                    prtocol_json = json.loads(protocol_str)
                    if book_json['assessments'][count]['protocol'] == assessment[-1]:
                        book_json['assessments'][count]['protocol'] = prtocol_json[0]
                    count +=1

        
            return book_json
        else:
            return {'error': 'Error B-001: Livro não encontrado'}

        
       
      
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

