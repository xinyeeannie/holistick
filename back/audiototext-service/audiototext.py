from flask import Flask, jsonify, request

audiototext = Flask(__name__)

if __name__ == "__main__":
    audiototext.run(debug=True, port=16160)
