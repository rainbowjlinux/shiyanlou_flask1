from flask import render_template, Flask

app = Flask(__name__)

@app.route('/usr/<usrname>')
def usr_index(usrname):
    return render_template('usr_index.html', usrname=usrname)

if __name__ == '__main__':
    app.run()
