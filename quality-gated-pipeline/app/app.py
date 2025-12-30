from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(status="UP", message="DevOps Pipeline Active")

@app.route('/health')
def health():
    return jsonify(status="Healthy"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)