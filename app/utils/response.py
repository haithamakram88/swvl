class Response:
    def __init__(self):
        self.status = True
        self.data = {}

    def add_data(self, key, value):
        self.data[key] = value
