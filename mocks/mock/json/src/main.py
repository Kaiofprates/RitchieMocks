import os

from formula import formula


path = os.environ.get("RIT_INPUT_TEXT")
port = os.environ.get("RIT_INPUT_TEXT")
route = os.environ.get("RIT_INPUT_TEXT")
formula.Run(path, port, route)
