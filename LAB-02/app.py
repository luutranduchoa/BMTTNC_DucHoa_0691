from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# --- CAESAR ---

# router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    # Gọi class xử lý thuật toán
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    
    # Thay vì return text thô, ta render lại template và truyền biến result_enc
    return render_template('caesar.html', result_enc=encrypted_text)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    # Gọi class xử lý thuật toán
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    
    # Trả về template và truyền biến result_dec để hiển thị ở phần Giải mã
    return render_template('caesar.html', result_dec=decrypted_text)

# --- VIGENERE ROUTES ---
@app.route("/vigenere", methods=["GET","POST"])
def vigenere():

    encrypted_result = None
    decrypted_result = None

    vigenere = VigenereCipher()

    if request.method == "POST":

        if "plainText" in request.form:
            text = request.form["plainText"]
            key = request.form["keyEncrypt"]
            encrypted_result = vigenere.vigenere_encrypt(text, key)

        elif "cipherText" in request.form:
            text = request.form["cipherText"]
            key = request.form["keyDecrypt"]
            decrypted_result = vigenere.vigenere_decrypt(text, key)

    return render_template(
        "vigenere.html",
        encrypted_result=encrypted_result,
        decrypted_result=decrypted_result
    )

##--- RAILFENCE ---
@app.route("/railfence", methods=["GET","POST"])
def railfence():

    encrypted_result = None
    decrypted_result = None

    railfence = RailFenceCipher()

    if request.method == "POST":

        if "plainText" in request.form:
            text = request.form["plainText"]
            key = int(request.form["keyEncrypt"])
            encrypted_result = railfence.rail_fence_encrypt(text, key)

        elif "cipherText" in request.form:
            text = request.form["cipherText"]
            key = int(request.form["keyDecrypt"])
            decrypted_result = railfence.rail_fence_decrypt(text, key)

    return render_template(
        "railfence.html",
        encrypted_result=encrypted_result,
        decrypted_result=decrypted_result
    )
##playfair
@app.route("/playfair", methods=["GET","POST"])
def playfair():

    encrypted_result = None
    decrypted_result = None
    matrix = None

    playfair = PlayFairCipher()

    if request.method == "POST":

        # CREATE MATRIX
        if "createMatrix" in request.form:
            key = request.form["matrixKey"]
            matrix = playfair.create_playfair_matrix(key)

        # ENCRYPT
        elif "plainText" in request.form:
            text = request.form["plainText"]
            key = request.form["keyEncrypt"]

            matrix = playfair.create_playfair_matrix(key)
            encrypted_result = playfair.playfair_encrypt(text, matrix)

        # DECRYPT
        elif "cipherText" in request.form:
            text = request.form["cipherText"]
            key = request.form["keyDecrypt"]

            matrix = playfair.create_playfair_matrix(key)
            decrypted_result = playfair.playfair_decrypt(text, matrix)

    return render_template(
        "playfair.html",
        encrypted_result=encrypted_result,
        decrypted_result=decrypted_result,
        matrix=matrix
    )

##transposition
@app.route("/transposition", methods=["GET","POST"])
def transposition():

    encrypted_result = None
    decrypted_result = None

    transposition = TranspositionCipher()

    if request.method == "POST":

        if "plainText" in request.form:
            text = request.form["plainText"]
            key = int(request.form["keyEncrypt"])
            encrypted_result = transposition.encrypt(text, key)

        elif "cipherText" in request.form:
            text = request.form["cipherText"]
            key = int(request.form["keyDecrypt"])
            decrypted_result = transposition.decrypt(text, key)

    return render_template(
        "transposition.html",
        encrypted_result=encrypted_result,
        decrypted_result=decrypted_result
    )
# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)