from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/encode', methods=['POST'])
def encode():
    #to Draco encode endpoint: ASP
    specs = request.get_json()
    try:

            #tf.keras.backend.set_session(sess)
            z = specs
            #draco
            #z=start_draco(specs)
    except Exception as e:
        raise InvalidUsage(e.message)
    return jsonify(z.tolist())


if __name__ == '__main__':
    rules = []
    port=5500

    app.run(port=port, debug=False)