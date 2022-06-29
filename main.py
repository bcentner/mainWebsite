from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('index.html')

# favicon loads
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
