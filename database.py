from report import Report

class Database:
    _list = []

    def add(self, request):
        self._list.append(Report(request))

    def get0(self):
        return self._list[0]
    
    def getAll(self):
        return self._list
