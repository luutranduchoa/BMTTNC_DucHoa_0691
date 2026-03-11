class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Khởi tạo các danh sách trống cho mỗi thanh ray
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: đi xuống, -1: đi lên

        for char in plain_text:
            rails[rail_index].append(char)
            
            # Đảo chiều khi chạm thanh ray trên cùng hoặc dưới cùng
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            
            rail_index += direction

        # Nối các hàng lại để tạo thành chuỗi mã hóa
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Bước 1: Tính toán số lượng ký tự trên mỗi thanh ray
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Bước 2: Chia chuỗi bản mã vào các thanh ray theo độ dài đã tính
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        # Bước 3: Đọc các ký tự theo hình zic-zac để khôi phục văn bản gốc
        plain_text = ""
        rail_index = 0
        direction = 1
        
        # Biến rails hiện tại chứa các chuỗi, ta chuyển thành list để dễ xử lý cắt ký tự
        rails = [list(r) for r in rails]

        for _ in range(len(cipher_text)):
            # Lấy ký tự đầu tiên của thanh ray hiện tại
            plain_text += rails[rail_index].pop(0)
            
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
              
        return plain_text
