import cld2


class CipherCaesar():

    def cipher_ru(self, string, key):
        alphabet_ru = ord('я')
        new_stirng = ''
        for symbol in string:
            old_symbol = ord(symbol)
            new_symbol = (old_symbol + key) % 32
            new_chr = chr(new_symbol)
            new_stirng += new_chr
        return new_stirng

    def cipher_en(self, string, key):
        alphabet_en = ord('z')
        new_stirng = ''
        for symbol in string:
            old_symbol = ord(symbol)
            new_symbol = (old_symbol + key) % alphabet_en
            new_chr = chr(new_symbol)
            new_stirng += new_chr
        return new_stirng


cipher = CipherCaesar()
string = "это"
key = 5
print(cipher.cipher_ru(string, key))
# details = cld2.detect(string)
# if details.details[0][0] == 'RUSSIAN':
#     print(cipher.cipher_ru(string, key))
# elif details.details[0][0] == 'ENGLISH':
#     print(cipher.cipher_en(string, key))