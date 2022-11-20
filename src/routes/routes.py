from src import app
from flask import make_response, jsonify, request

@app.route('/')
def home():
    return make_response(
        jsonify(
            message="Home",
            data={"Pagina": "Inicial"}
            )
        )