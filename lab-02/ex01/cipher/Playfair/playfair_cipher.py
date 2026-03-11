class PlayfairCipher:
    def __init__(self) -> None:
        pass
    
    def __init__(self):
        pass
    
    def create_playfar_matrix(self, key):
        key = key.replace("J", "I") #chuyen J thanh I
        key = key.upper()
        key_set = set(key)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set]
        matrix = list(key)
        
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break
            
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range (len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
    def playfair_encrypt(self, plain_text, key):
        plain_text = plain_text.replace("J", "I")
        