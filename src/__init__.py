from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from logging import FileHandler,WARNING

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

spec = FlaskPydanticSpec("API-Biscuit", title="API-Biscuit")
spec.register(app)