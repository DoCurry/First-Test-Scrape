from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import main

app = Flask(__name__)
CORS(app)

@app.route('/')
def frontend():
    return render_template("chat.html")


@app.route('/getchoices', methods=['POST'])
def getchoices():
    data = request.get_json()
    sys= data.get('sys')
    return jsonify({
        'choices':main.getchoices(str(sys))
        })

@app.route('/respond', methods=['POST'])
def respond():
    data = request.get_json()
    sys = data.get('sys')
    user = data.get('user')
    return jsonify({
        'respon':main.respond(sys,user)
    })


if __name__ == '__main__':
    app.run(debug=True)