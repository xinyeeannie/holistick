from flask import Flask, jsonify, request

mindmap = Flask(__name__)

if __name__ == "__main__":
    mindmap.run(debug=True, port=16461)
