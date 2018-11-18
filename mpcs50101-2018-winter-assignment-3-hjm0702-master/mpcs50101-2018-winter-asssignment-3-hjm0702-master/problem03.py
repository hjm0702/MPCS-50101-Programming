plain = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

message = "HIHIHI"
key = 24
encrypted = []
decrypted = []
decrypted_message = []
encrypted_message = []


def caesar_encrypt(key, message):
    for i in range(len(message)):
        order = plain.index(message[i])
        new_order = order + int(key)
        if new_order > 25:
            new_order = new_order - 25
        else:
            new_order = new_order
        encrypted.append(plain[int(new_order)])
    encrypted_message = "".join(encrypted)
    return encrypted_message

def caesar_decrypt(key, message):
    for i in range(len(message)):
        order = plain.index(message[i])
        new_order = order - int(key)
        if new_order > 25:
            new_order = new_order - 25
        else:
            new_order = new_order
        decrypted.append(plain[int(new_order)])
    decrypted_message = "".join(decrypted)
    return decrypted_message

print caesar_encrypt(key, message)
print caesar_decrypt(key, message)
# def caesar_decrypt(key, message):
#   return decrypted_message
#
# print plain
