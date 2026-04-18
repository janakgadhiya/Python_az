from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Addition API is running!"

@app.route('/add')
def add():
    a = int(request.args.get('a', 10))
    b = int(request.args.get('b', 5))
    return {"result": a + b}
    
@app.route('/sub')
def sub():
    a = int(request.args.get('a', 6))
    b = int(request.args.get('b', 3))
    return {"result": a - b}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
