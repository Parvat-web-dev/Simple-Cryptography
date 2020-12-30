class Cryptography:
    def __init__(self, key, text):
        self.en_c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
        self.de_c = []
        self.key = str(key)
        self.text = str(text)

        for a in range(6765, 190897, 379):
            if len(self.de_c) == len(self.en_c):
                break
            self.de_c.append(a)
            
        self.en_k = dict(zip(self.en_c, self.de_c))
        self.de_k = dict(zip(self.de_c, self.en_c))

    def encode(self, Print = False):
        key_list = []
        encoded_text_list = []
        text_to_return = ''
        num = 0

        #Adding the letters of the 'key' in the list at key_list
        for letters in self.key:
            key_list.append(letters)

        #Adding the letters in the text
        for character in self.text:
            encoded_text_list.append(self.en_k[character])

        #Adding the items of list again and again till it is equal to len of the text
        for item in key_list:
            if len(key_list) == len(encoded_text_list):
                break
            key_list.append(item)

        #The text to be returned:
        for a in encoded_text_list:
            text_to_return = text_to_return + str(int(a) + int(self.en_k[key_list[num]])) + ' '
            num += 1

        if Print == True:
            print(text_to_return)

        return text_to_return
        
    def decode(self, Print = False):
        key_list = []
        text_char = []
        text_to_return = ''
        num = 0
        
        #All the key appending in the list:
        for a in self.key:
            key_list.append(a)

        #All the chars in encoded text:
        for a in self.text.split():
            text_char.append(int(a))

        #Adding the key upto its length:
        for a in key_list:
            if len(key_list) == len(text_char):
                break
            key_list.append(a)

        #Adding the decoded text:
        for a in text_char:
            text_to_return = text_to_return + str(self.de_k[int(a) - int(self.en_k[key_list[num]])])
            num += 1

        if Print == True:
            print(text_to_return)

        return text_to_return


if __name__ == '__main__':
    print('Hello from Cryptography Module v1.0, developed on : Dec 12 2020, 17:20')
    print('For any help visit : https://github.com/Parvat-web-dev/Simple-Cryptography')
