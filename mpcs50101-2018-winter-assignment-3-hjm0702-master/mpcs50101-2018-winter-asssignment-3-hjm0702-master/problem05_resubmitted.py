plain = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
original_file = open("./common_words_100.txt", 'r')
sort = sorted(original_file.read().split(), key=str.lower)

message_origin = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
# print message

# print type(message)

key = 1
encrypted = []
decrypted = []
decrypted_message = []
encrypted_message = []


# def caesar_encrypt(key, message_origin):
#     message = message_origin.upper()
#     for i in range(len(message)):
#         order = plain.index(message[i])
#         new_order = order + int(key)
#         if new_order >= 26:
#             new_order = new_order - 26
#         else:
#             new_order = new_order
#         encrypted.append(plain[int(new_order)])
#     encrypted_message = "".join(encrypted)
#     return encrypted_message

def caesar_decrypt(key, message_origin):
    while key < 26:
        message = message_origin.upper()
        for i in range(len(message)):
            if message[i] != " ":
                order = plain.index(message[i])
                new_order = order - int(key)
                if new_order >= 27:
                    new_order = new_order - 27
                else:
                    new_order = new_order
                decrypted.append(plain[int(new_order)])
            else:
                decrypted.append(" ")
        decrypted_message = "".join(decrypted)
        key = key + 1
        print decrypted_message[-41:].lower()
        for k in decrypted_message[-41:].split():
            if k.lower() in sort:
                print key-1
                break

# print caesar_encrypt(key, message_origin)

print caesar_decrypt(key, message_origin)

'''
The answer is :
Key : 11
Message : believe you can and you are halfway there

My assumption is some of words from the hidden message must match the words from 'common_words_100.txt' '''




# def caesar_decrypt(key, message):
#   return decrypted_message
#
# print plain
