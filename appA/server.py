from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return '<h1>appA</h1>'
@app.route('/about')
def about(): return 'asdf'
app.run(host='0.0.0.0', port=80)
