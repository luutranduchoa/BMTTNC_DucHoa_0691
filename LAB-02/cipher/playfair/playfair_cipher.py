class PlayFairCipher:
    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        matrix_str = ""
        for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char.isalpha() and char not in matrix_str:
                matrix_str += char
        return [list(matrix_str[i:i+5]) for i in range(0, 25, 5)]

    def find_position(self, matrix, char):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return -1, -1

    def prepare_text(self, text):
        text = text.upper().replace("J", "I")
        text = "".join([c for c in text if c.isalpha()])
        prepared = ""
        i = 0
        while i < len(text):
            prepared += text[i]
            if i + 1 < len(text):
                if text[i] == text[i+1]:
                    prepared += "X"
                else:
                    prepared += text[i+1]
                    i += 1
            i += 1
        if len(prepared) % 2 != 0:
            prepared += "X"
        return prepared

    def playfair_encrypt(self, text, matrix):
        text = self.prepare_text(text)
        encrypted = ""
        for i in range(0, len(text), 2):
            r1, c1 = self.find_position(matrix, text[i])
            r2, c2 = self.find_position(matrix, text[i+1])
            if r1 == r2:
                encrypted += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                encrypted += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:
                encrypted += matrix[r1][c2] + matrix[r2][c1]
        return encrypted

    def playfair_decrypt(self, text, matrix):
        decrypted = ""
        for i in range(0, len(text), 2):
            r1, c1 = self.find_position(matrix, text[i])
            r2, c2 = self.find_position(matrix, text[i+1])
            if r1 == r2:
                decrypted += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                decrypted += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
            else:
                decrypted += matrix[r1][c2] + matrix[r2][c1]
                
            decrypted = decrypted.replace("X","")
        return decrypted