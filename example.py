from bottle import route,run,template

@route('/hello/<name>')
def index(name):
    return template('<b>hello {{name}}</b>!', name=name)

@route('/hello')
def index1():
    return ('<b>Hello World!</b>')
run(host='localhost',port=8080)
