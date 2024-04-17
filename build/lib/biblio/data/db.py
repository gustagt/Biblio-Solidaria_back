import socket
from sqlalchemy import create_engine

from  biblio.credentials.credentials import data_base

pcName = socket.gethostname()

engine = create_engine(f"mysql://{data_base.USER}:{data_base.PASSWORD}@{data_base.IP}:{data_base.PORT}/{data_base.SCHEMA}",
                            pool_recycle=3600, echo=True)

if pcName != "TRANS-E138764":
    engine = create_engine(f"mysql://{data_base.USER_SERVER}:{data_base.PASSWORD_SERVER}@{data_base.IP}:{data_base.PORT}/{data_base.SCHEMA}",
                            pool_recycle=3600, echo=True)
    print(pcName)
else: 
    engine = create_engine(f"mysql://{data_base.USER}:{data_base.PASSWORD}@{data_base.IP}:{data_base.PORT}/{data_base.SCHEMA}",
                            pool_recycle=3600, echo=True)
    print(pcName)


def connect():
    conn = engine.connect()
    return conn

