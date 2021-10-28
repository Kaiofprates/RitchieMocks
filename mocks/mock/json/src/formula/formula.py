from colored import fg
from server.jsonServer import JsonServer


def Run(path, port, route):

    print(f"{fg(9)}  Application Running in {route}/{port}")
    jsonServer = JsonServer()
    jsonServer.run_server(path, int(port), route)

