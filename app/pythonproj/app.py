import os
from flask import Flask,jsonify,request
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY","dev-default-key")
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            'message': 'Hello, World!',
            'status' : 'secure'
            })
    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({
            'status': 'healthy'
            }),200
    @app.route('/echo', methods=['POST'])
    def echo():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400
        message = data.get('message', "")
        if len(message) > 200:
            return jsonify({'error': 'Message too long'}), 400
        return jsonify({'echo': message})
    return app
app=create_app()
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)