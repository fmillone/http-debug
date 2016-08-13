from bottle import route, run, template, request, response, static_file
from database import Database
import json

database = Database()

def buildTemplate(item):
    return {
        'path': item.path,
        'params': item.params(),
        'method': item.method,
        'time': item.date.isoformat(),
        'headers': item.headers()
    }

@route('/report')
def report():
    return static_file('home.html', root='.')

@route('/jsonreport')
def jsonReport():
    return json.dumps([ buildTemplate(item) for item in database.getAll() ] )

@route('/<path>')
def all(path):
    database.add(request)
    response.status = 200
    return 'recorded'



run(host='localhost', port=8080)
