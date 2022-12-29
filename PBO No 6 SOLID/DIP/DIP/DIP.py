class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

class NodeHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

class MockHttpService(Connection):
    def request(self, url: str, options:dict):
        pass