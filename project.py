from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'Name': 'Siddhant',
        'Contact': '+91 9224242424',
        'status': False
    },
    {
        'id': 2,
        'Name': 'Avi',
        'Contact': '+91 9876543210',
        'status': False
    },
    {
        'id': 3,
        'Name': 'Tanay',
        'Contact': '+91 9874340218',
        'status': False
    }
]


@app.route('/data')
def get_data():
    return jsonify({'data': data})


if(__name__ == "__main__"):
    app.run(debug=True)
