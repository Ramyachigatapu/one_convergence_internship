from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
@app.route("/pages/<number>")
def pages(number):
    return "<h1>Page #%s</h1>" % number


if __name__ == '__main__':
    app.run(port=8888)
