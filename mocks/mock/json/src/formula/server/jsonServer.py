import json

from src.formula.server.server import Server
from flask import Flask
from src.formula.exceptions.noparsedata import NoParseDataException

class JsonServer(Server):
    def __init__(self, app=Flask('app')):
        self.app=app

    def run_server(self, file, port=8080, route='/'):
        @self.app.route(route)
        def run():
            return str(self.load_json(file))
        self.app.run(host='localhost', port=port)

    def load_json(self, path):
        file = open(path, )
        try:
            data = json.load(file)
            file.close()
            return data
        except Exception as e:
            raise NoParseDataException(e)





