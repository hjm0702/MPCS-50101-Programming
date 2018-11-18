plain = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
original = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
message = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
keys = 25
encrypted = []
decrypted = []
decrypted_message = []
encrypted_message = []

# def caesar_encrypt(key, message):
#     for i in range(len(message)):
#         order = plain.index(message[i])
#         new_order = order + int(key)
#         if new_order > 25:
#             new_order = new_order - 25
#         else:
#             new_order = new_order
#         encrypted.append(plain[int(new_order)])
#     encrypted_message = "".join(encrypted)
#     return encrypted_message

# def caesar_decrypt(key, message):
for key in range(keys):
    decrypted_message = " "
    for i in range(len(message)):
        if message[i] != " ":
            order = plain.index(message[i])
            new_order = order - int(key)
            if new_order > 25:
                new_order = new_order - 25
            else:
                new_order = new_order
            decrypted.append(plain[int(new_order)])
        else:
            decrypted.append(" ")
        decrypted_message = "".join(decrypted)
    print decrypted_message, key


print "Key is 11 and message is", "believe you can and you are halfway there"



    # print key, decrypted_message

# print caesar_encrypt(key, message)
# print caesar_decrypt(key, message)
# def caesar_decrypt(key, message):
#   return decrypted_message
#
# print plain
