from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World'

@app.route("/v1/pages/1")
def simple_html():
    return '''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
  </head>
  <body>
    <h1> My First Try Using Flask </h1>
    <p> I returned html script </p>
  </body>
</html>''' 

if __name__ == '__main__':
    print("open http://localhost:8888/v1/pages/1")
    app.run(port=8888)
