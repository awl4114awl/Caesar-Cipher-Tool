from flask import Flask, render_template, request, jsonify
from caesar_cipher import caesar_cipher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['text']
    shift = int(request.form['shift'])
    encrypted_text = caesar_cipher(text, shift)
    return jsonify({'result': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form['text']
    shift = int(request.form['shift'])
    decrypted_text = caesar_cipher(text, shift, encrypt=False)
    return jsonify({'result': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
