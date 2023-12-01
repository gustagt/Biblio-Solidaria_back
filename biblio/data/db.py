import socket
from sqlalchemy import create_engine

from  biblio.credentials.credentials import data_base

pcName = socket.gethostname()

engine = create_engine(f"mysql://{data_base.USER}:{data_base.PASSWORD}@{data_base.IP}:{data_base.PORT}/{data_base.SCHEMA}",
                            pool_recycle=3600, echo=True)



def connect():
    conn = engine.connect()
    return conn

