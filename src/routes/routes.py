from src import app, spec, Response, Request
from flask import make_response, jsonify, request
from src.models.biscuit import *
from src.services.db import lista_biscuits


@app.get('/')
@spec.validate(query=QueryBiscuit, resp=Response(HTTP_200=Biscuits))
def retornar_biscuits():
    """Retorna todos os Biscuits cadastrados no banco de dados"""
    # query = request.context.query.dict(exclude_none=True)
    # breakpoint()
    return make_response(
        jsonify(
            Biscuits(
                biscuits=lista_biscuits,
                count=len(lista_biscuits)
            ).dict()
        )
    )

@app.get('/<int:id>')
@spec.validate(resp=Response(HTTP_200=Biscuit))
def retornar_biscuit(id):
    """Retorna o Biscuit cadastrado com o ID especificado"""
    try:
        return make_response(
            jsonify(
                lista_biscuits[id]
            )
        )
    except IndexError:
        return {'message': 'Biscuit not found!'}, 404

@app.post('/')
@spec.validate(body=Request(Biscuit), resp=Response(HTTP_201=Biscuit))
def inserir_biscuit():
    """Insere um novo Biscuit no bando de dados"""
    #body = request.context.body.dict()
    body = request.get_json(force=True)
    # breakpoint()
    lista_biscuits.append(body)
    return body


@app.put('/<int:id>')
@spec.validate(body=Request(Biscuit), resp=Response(HTTP_200=Biscuit))
def altera_biscuit(id):
    '''Altera um Biscuit do banco de dados'''
    body = request.get_json(force=True)
    lista_biscuits[0]=body
    return jsonify(body)

@app.delete('/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deleta_biscuit(id):
    '''Remove um Biscuit do banco de dados'''
    global lista_biscuits
    lista_biscuits = lista_biscuits[1:]
    return jsonify({})