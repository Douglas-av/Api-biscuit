from src import app, spec, Response, Request
from flask import make_response, jsonify, request
from src.models.biscuit import Biscuit

@app.get('/')
# @spec.validate(resp=Response(HTTP_200=Biscuit))
def retornar_biscuit():
    """Retorna todos os Biscuits cadastrados no banco de dados"""
    return make_response(
        jsonify(
            message="Biscuit",
            data={"Pagina": "Biscuit"}
            )
        )

@app.post('/')
@spec.validate(body=Request(Biscuit), resp=Response(HTTP_200=Biscuit))
def inserir_biscuit():
    """Insere um novo Biscuit no bando de dados"""
    body = request.context.body.dict()
    return body