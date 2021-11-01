import os

from formula import formula


path = os.environ.get("RIT_INPUT_PATH")
port = os.environ.get("RIT_INPUT_PORT")
route = os.environ.get("RIT_INPUT_ROUTE")
formula.Run(path, port, route)
