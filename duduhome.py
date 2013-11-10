from flask import Flask, render_template, redirect, url_for, request
from service.service import note_service
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='template')
app.register_blueprint(note_service, url_prefix='/note/service')


@app.route('/')
def index():
    return render_template('index.htm')


@app.errorhandler(404)
def unknown_user_icon(err):
    if request.path.startswith('/icon/'):
        return redirect(url_for('static', filename='icon/unknown.jpg'))
    else:
        return 'Page Not Found', 404

if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8080)
    IOLoop.instance().start()