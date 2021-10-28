class NoParseDataException(Exception):

    def __init__(self, message="Falha ao converter arquivo em json"):
        self.message=message
        super().__init__(self.message)