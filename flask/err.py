from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
