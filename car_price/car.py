from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'g ml'

app.run(debug=True)


