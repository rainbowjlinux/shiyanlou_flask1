from flask import render_template, Flask, make_response, request

app = Flask(__name__)

@app.route('/user/<username>')
def user_index(username):
    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username', username)
    return resp

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'username: {}'.format(username)

if __name__ == '__main__':
    app.run()
