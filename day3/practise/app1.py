from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return {"app1": "success"}
 
if __name__ == '__main__':
    print("http://localhost:8888/")
    app.run(port=8888)
