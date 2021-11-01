import json
from flask import Flask
from colored import fg


def Run(path, port, route):
    print(f"{fg(9)}  Application Running in {route}/{port}")
    print(f' port { port} path {path} route {route}')
    jsonServer = JsonServer()
    jsonServer.run_server(path, int(port), route)


def load_json(path):
    file = open(path, )
    try:
        data = json.load(file)
        file.close()
        return data
    except Exception as e:
        raise NoParseDataException(str(e))


class JsonServer:
    def __init__(self, app=Flask('app')):
        self.app = app

    def run_server(self, file, port=8080, route='/'):
        @self.app.route(route)
        def run():
            return str(load_json(file))

        self.app.run(host='localhost', port=port)


class NoParseDataException(Exception):
    def __init__(self, message="Falha ao converter arquivo em json"):
        self.message = message
        super().__init__(self.message)
