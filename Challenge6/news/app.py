from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def filelist():
    directory = os.path.join(os.path.abspath(os.path.dirname(__name__)), '..', 'files')
    lists = {}
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        with open(filepath, 'r') as f:
            lists[file[:-5]] = json.load(f)
    return lists

@app.route('/')
def index():
    return render_template('index.html', title_list=[item['title'] for item in filelist().values()])

@app.route('/files/<filename>')
def showfile(filename):
    if filename not in filelist():
        abort(404)
    return render_template('file.html', file_content=filelist()[filename])

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

def main():
    app.run()

if __name__ == '__main__':
    main()
