from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return '<h1>appB</h1>'
@app.route('/about')
def about(): return 'testing'
app.run(host='0.0.0.0', port=80)
