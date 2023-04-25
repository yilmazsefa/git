from flask import Flask
app = Flask(__name__)

@app.route('/')
def ays():
    return 'hello, Simple flask appliction'