import os

from flask import Flask
from waitress import serve
from flask_cors import CORS
import secrets



app = Flask(__name__, instance_relative_config=True)



app.config.from_mapping(
    SECRET_KEY=secrets.token_hex(32),
)

try:
    print(app.instance_path)
    os.makedirs(app.instance_path)
except OSError:
    pass

from biblio.helpers import auth

app.register_blueprint(auth.bp)

from biblio.controllers import sessaoController, protocolController, booksController

app.register_blueprint(sessaoController.bp)

app.register_blueprint(protocolController.bp)

app.register_blueprint(booksController.bp)

    

  


CORS(app)

if __name__ == "__main__":
    serve(app)


