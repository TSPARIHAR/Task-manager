from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Task Manager API Running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
