# By Adam Michalowski (c) 2015

#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        'id': 1,
        'username': 'user1'
    },
    {
        'id': 2,
        'username': 'user2',
    }
]

servers = [
    {
        'id': 1,
        'ip': '127.0.0.1:88'
    }
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/servers', methods=['GET'])
def get_servers():
    return jsonify({'servers': servers})

if __name__ == '__main__':
    app.run(debug=True)
