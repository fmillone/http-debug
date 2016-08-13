import datetime

class Report:
    def __init__(self, request):
        self.request = request
        self.method = request.method
        self._params = request.params
        self.path = request.fullpath
        self._headers = request.headers

        self.date = datetime.datetime.now()

    def __toDictionary(self, item):
        return { x : item[x] for x in item.keys() }

    def params(self):
        return self.__toDictionary(self._params)

    def headers(self):
        return self.__toDictionary(self._headers) 

