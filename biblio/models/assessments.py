from sqlalchemy import text
from biblio.data.db import connect

class Assessments:
    def __init__(
        self,
        id_book,
        id_protocol,
        id_assessment=None,
        overall=None,
        romantic=None,
        fun=None,
        sad=None,
        shocking=None,
        comments=None,
    ):
        
        self.id_book = id_book
        self.id_protocol = id_protocol
        self.id_assessment = id_assessment
        if overall:
            self.overall = overall
        else:
            self.overall ='NULL'
        if romantic:
            self.romantic = romantic
        else:
            self.romantic ='NULL'
        if fun:
            self.fun = fun
        else:
            self.fun ='NULL'
        if sad:
            self.sad = sad
        else:
            self.sad ='NULL'
        if shocking:
            self.shocking = shocking
        else:
            self.shocking ='NULL'
        if comments:
            self.comments = f"'{comments}'" 
        else: 
            self.comments= 'NULL'
    
    def select():
        conn = connect()
        retorno_db = conn.execute(
            text("SELECT * FROM biblio.assessments")
        ).fetchall()
        conn.close()
        return retorno_db
    
    def select_id_book(id_book):
        conn = connect()
        retorno_db = conn.execute(
            text(f"SELECT * FROM biblio.assessments WHERE `books_id_book` = {id_book}")
        ).fetchall()
        conn.close()
        return retorno_db
    
    def select_id_protocol(id_protocol):
        conn = connect()
        retorno_db = conn.execute(
            text(f"SELECT * FROM biblio.assessments WHERE `protocols_id_protocol` = {id_protocol}")
        ).fetchall()
        conn.close()
        return retorno_db

    def insert(self):
        conn = connect()
        conn.execute(
      
            text(
                f"INSERT INTO `biblio`.`assessments` (`overall`, `romantic`, `fun`, `sad`, `shocking`, `comments`, `books_id_book`, `protocols_id_protocol`) VALUES ({self.overall }, {self.romantic}, {self.fun}, {self.sad}, {self.shocking}, {self.comments}, {self.id_book}, {self.id_protocol});"   
            )
        )
        conn.commit()
        conn.close()
        return 

    def update(self):
        conn = connect()
        conn.execute(
            text(
                f"UPDATE `biblio`.`assessments` SET `overall` = '{self.title}', `romantic` = '{self.author}', `fun` = {self.pages}, `sad` = '{self.create_at}', `shocking`, `comments`, `books_id_book`, `protocols_id_protocol`, WHERE (`id_assessment` = {self.id_assessment});"
            )
        )
        conn.commit()
        conn.close()
        return 


    def delete(id_assessment):
        conn = connect()
        conn.execute(
            text(f"DELETE FROM `biblio`.`assessments` WHERE (`id_assessment` = {id_assessment});")
        )
        conn.commit()
        conn.close()
        return
    
    def select_last_book():
        conn = connect()
        retorno_db = conn.execute(
            text(f"SELECT * FROM `biblio`.`assessments` ORDER BY id_assessment DESC LIMIT 1")
        ).fetchall()
        conn.close()
        return retorno_db