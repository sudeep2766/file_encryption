from cryptography import fernet
import os

image_list = list()
for item in os.listdir():
    if os.path.isfile(item):
        image_list.append(item)

to_encrypt = list()
for image in image_list:
    if image == 'main.py' or image == 'decrypt.py' or image == 'thekey.key' or image == 'requirements.txt' or image == 'README.txt':
        continue
    else:
        to_encrypt.append(image)

key = fernet.Fernet.generate_key()

if os.path.exists('thekey.key'):
    opt = input("Password file already exists. Are you sure on encrypting? (Y/n)")
    if opt.lower() == 'y':
        opt2 = input("Are you sure about that? If already encrypted the password will be overwritten and cannot be recovered (Y/n)")
        if opt2.lower() == 'y':
            with open ('thekey.key', 'wb') as thekey1:
                thekey1.write(key)

            for file in to_encrypt:
                with open(file, 'rb')as encrypting:
                    contents = encrypting.read()
        
                encrypted = fernet.Fernet(key).encrypt(contents)

                with open(file, 'wb') as just_encrypting:
                    just_encrypting.write(encrypted)
    print("Encryption successful!")
    print(to_encrypt)

else:
    with open ('thekey.key', 'wb') as thekey1:
        thekey1.write(key)

    for file in to_encrypt:
        with open(file, 'rb')as encrypting:
            contents = encrypting.read()

        encrypted = fernet.Fernet(key).encrypt(contents)

        with open(file, 'wb') as just_encrypting:
            just_encrypting.write(encrypted)
    print("Encryption successful!")
    print(to_encrypt)

