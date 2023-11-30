from flask import jsonify, send_file
from sqlalchemy import text
from datetime import date




class Protocol:
    def __init__(
        self,
        id_book,
        title,
        author,
        pages,
        create_at,
    ):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.pages = pages
        self.create_at = create_at
    
    # def select(id_taxa, conn: Connection):
    #     retorno_db = conn.execute(
    #         text(f"SELECT * FROM sitt.taxas WHERE `id_taxa` = {id_taxa}")
    #     ).fetchone()
    #     if retorno_db:
    #         taxa = Taxa.convert_ret(retorno_db)
    #     else:
    #         return retorno_db
    #     return taxa
    
    # def select_id(id_taxa, conn: Connection):
    #     retorno_db = conn.execute(
    #         text(f"SELECT * FROM sitt.taxas WHERE `id_taxa` = {id_taxa}")
    #     ).fetchone()
    #     if retorno_db:
    #         taxa = Taxa.convert_ret(retorno_db)
    #     else:
    #         return retorno_db
    #     return taxa

    # def insert(self, conn: Connection):
    #     conn.execute(
    #         text(
    #             "INSERT INTO sitt.taxas (`tipo_taxa`, `data_emissao`, `data_vencimento`, `valor`, `estado`, `setor`,`nome_cadastrante`, `contribuintes_id`) "
    #             f"VALUES ('{self.tipo_taxa}','{self.data_emissao}','{self.data_vencimento}',{self.valor},{self.estado},{self.setor},'{self.nome_cadastrante}',{self.id_contribuinte})"
    #         )
    #     )

    # def update(self, conn: Connection):
    #     conn.execute(
    #         text(
    #             f"UPDATE sitt.taxas "
    #             f"SET `tipo_taxa` = '{self.tipo_taxa}', `data_emissao` = '{self.data_emissao}', `data_vencimento` = '{self.data_vencimento}', `valor`={self.valor}, `estado` = {self.estado}, `setor` = {self.setor},`nome_cadastrante`='{self.nome_cadastrante}', `contribuintes_id`={self.id_contribuinte} "
    #             f"WHERE id_taxa = {self.id}"
    #         )
    #     )


    # def delete(id_taxa, conn: Connection):
    #     retorno_db = conn.execute(
    #         text(f"SELECT * FROM sitt.taxas WHERE `id_taxa` = {id_taxa}")
    #     ).fetchone()
    #     if retorno_db:
    #         taxa = Taxa.convert_ret(retorno_db)
    #     else:
    #         return retorno_db
    #     return taxa



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
    #     return taxa

