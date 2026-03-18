import ecdsa, os

# Kiểm tra và tạo thư mục lưu trữ khóa nếu chưa tồn tại
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo khóa riêng tư (SigningKey)
        sk = ecdsa.SigningKey.generate()
        # Lấy khóa công khai (VerifyingKey) từ khóa riêng tư
        vk = sk.get_verifying_key()
        
        # Lưu khóa riêng tư vào file .pem
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
            
        # Lưu khóa công khai vào file .pem
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Tải khóa riêng tư từ file
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
            
        # Tải khóa công khai từ file
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
            
        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        # Tải khóa công khai (vk) để xác thực
        _, vk = self.load_keys()
        try:
            # Xác thực chữ ký số
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False