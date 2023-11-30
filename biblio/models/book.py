from flask import jsonify, send_file
from sqlalchemy import text
from datetime import date
from biblio.data.db import connect





class Book:
    def __init__(
        self,
        title,
        author,
        pages,
        create_at,
        id_book=None,
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.create_at = create_at
        self.id_book = id_book
    
    def select():
        conn = connect()
        retorno_db = conn.execute(
            text("SELECT * FROM biblio.books")
        ).fetchall()
        conn.close()
        return retorno_db
    
    def select_id(id_book):
        conn = connect()
        retorno_db = conn.execute(
            text(f"SELECT * FROM biblio.books WHERE `id_book` = {id_book}")
        ).fetchall()
        return retorno_db

    def insert(self):
        conn = connect()
        conn.execute(
            text(
                f"INSERT INTO biblio.books (`title`, `author`, `pages`, `creat_at`) VALUES ('{self.title}', '{self.author}', {self.pages}, '{self.create_at}')"   
            )
        )
        conn.commit()
        conn.close()
        return 

    def update(self):
        conn = connect()
        conn.execute(
            text(
                f"UPDATE `biblio`.`books` SET `title` = '{self.title}', `author` = '{self.author}', `pages` = {self.pages}, `creat_at` = '{self.create_at}' WHERE (`id_book` = {self.id_book});"
            )
        )
        conn.commit()
        conn.close()
        return 


    def delete(id_book):
        conn = connect()
        conn.execute(
            text(f"DELETE FROM `biblio`.`books` WHERE (`id_book` = {id_book});")
        )
        conn.commit()
        conn.close()
        return


    # def convert_ret(retorno_db):
    #     taxa = Taxa(
    #         retorno_db[1],
    #         retorno_db[2],
    #         retorno_db[3],
    #         retorno_db[4],
    #         retorno_db[5],
    #         retorno_db[6],
    #         retorno_db[7],
    #         retorno_db[8],
    #         retorno_db[9],
    #         retorno_db[10],
    #         retorno_db[11],
    #         retorno_db[12],
    #         retorno_db[0],
    #     )
       

