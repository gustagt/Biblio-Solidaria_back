from sqlalchemy import text
from datetime import date
from biblio.data.db import connect



class Protocol:
    def __init__(
        self,
        user_possession,
        remove_at,
        id_book,
        returned_at=None,
        id_protocol=None,
    ):
        self.id_protocol = id_protocol
        self.user_possession = user_possession
        self.remove_at = remove_at
        self.id_book = id_book
        if returned_at:
            self.returned_at = f"'{returned_at}'" 
        else: 
            self.returned_at= 'NULL'
        
    def select():
        conn = connect()
        retorno_db = conn.execute(
            text("SELECT * FROM biblio.protocols")
        ).fetchall()
        conn.close()
        return retorno_db

    def select_id(id_protocol):
        conn = connect()
        retorno_db = conn.execute(
            text(f"SELECT * FROM biblio.protocols WHERE `id_protocol` = {id_protocol}")
        ).fetchall()
        return retorno_db

    def insert(self):
        conn = connect()
        conn.execute(
            text(
                f"INSERT INTO `biblio`.`protocols` (`user_possession`, `remove_at`, `returned_at`, `book_id_book`) VALUES ('{self.user_possession}', '{self.remove_at}', {self.returned_at}, {self.id_book});"   
            )
        )
        conn.commit()
        conn.close()
        return 

    def update(self):
        conn = connect()
        conn.execute(
            text(
                f"UPDATE `biblio`.`protocols` SET `user_possession` = '{self.user_possession}', `remove_at` = '{self.remove_at}', `returned_at` = {self.returned_at}, `book_id_book` = {self.id_book} WHERE (`id_protocol` = {self.id_protocol});"
            )
        )
        conn.commit()
        conn.close()
        return 


    def delete(id_protocol):
        conn = connect()
        conn.execute(
            text(f"DELETE FROM `biblio`.`protocols` WHERE (`id_protocol` = {id_protocol});")
        )
        conn.commit()
        conn.close()
        return