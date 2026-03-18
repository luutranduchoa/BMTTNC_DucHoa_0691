import rsa, os

# Kiểm tra và tạo thư mục lưu trữ khóa nếu chưa tồn tại
if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo cặp khóa công khai và khóa bí mật (1024 bits)
        (public_key, private_key) = rsa.newkeys(1024)
        
        # Lưu khóa công khai vào file .pem
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
            
        # Lưu khóa bí mật vào file .pem
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        # Tải khóa công khai từ file
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
            
        # Tải khóa bí mật từ file
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
            
        return private_key, public_key

    def encrypt(self, message, key):
        # Mã hóa thông điệp
        return rsa.encrypt(message.encode('ascii'), key)

    def decrypt(self, ciphertext, key):
        # Giải mã thông điệp với xử lý lỗi
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    def sign(self, message, key):
        # Tạo chữ ký số cho thông điệp sử dụng SHA-1
        return rsa.sign(message.encode('ascii'), key, 'SHA-1')

    def verify(self, message, signature, key):
        # Xác thực chữ ký số
        try:
            return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
        except:
            return False