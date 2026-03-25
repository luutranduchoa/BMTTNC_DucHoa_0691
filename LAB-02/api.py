from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

# Khởi tạo các đối tượng Cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()

# Hàm hỗ trợ kiểm tra dữ liệu đầu vào (Helper function)
def get_data_field(data, field_name):
    if not data or field_name not in data:
        return None
    return data[field_name]

## --- CAESAR ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    try:
        plain_text = data['plain_text']
        key = int(data['key'])
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Thiếu hoặc sai định dạng plain_text/key'}), 400

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    try:
        cipher_text = data['cipher_text']
        key = int(data['key'])
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Thiếu hoặc sai định dạng cipher_text/key'}), 400

## --- VIGENERE ---
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    try:
        plain_text = data['plain_text']
        key = data['key']
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except KeyError:
        return jsonify({'error': 'Thiếu plain_text hoặc key'}), 400

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    try:
        cipher_text = data['cipher_text']
        key = data['key']
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except KeyError:
        return jsonify({'error': 'Thiếu cipher_text hoặc key'}), 400

## --- RAILFENCE ---
@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    # Lấy dữ liệu từ JSON gửi lên
    plain_text = data.get('plain_text')
    key_val = data.get('key')

    # Chuyển đổi key sang kiểu int vì Postman đang gửi dạng chuỗi "3"
    try:
        key = int(key_val)
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        # Trả về đúng key 'encrypted_text' như trong hình của bạn
        return jsonify({'encrypted_text': encrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': 'Yêu cầu cần có plain_text (string) và key (int)'}), 400

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key_val = data.get('key')

    try:
        key = int(key_val)
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': 'Yêu cầu cần có cipher_text (string) và key (int)'}), 400
    
## playfair
playfair_cipher =PlayFairCipher()
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data.get('key')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

## transposition
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
## --- MAIN ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)