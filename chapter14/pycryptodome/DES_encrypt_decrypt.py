from Crypto.Cipher import DES

# Fill with spaces the user until 8 characters
user =  "user    ".encode("utf8")
password = "password".encode("utf8")

key='mycipher'

# we create the cipher with DES
cipher = DES.new(key.encode("utf8"),DES.MODE_ECB)

# encrypt username and password
cipher_user = cipher.encrypt(user)
cipher_password = cipher.encrypt(password)

print("Cipher User: " + str(cipher_user))
print("Cipher Password: " + str(cipher_password))

# We simulate the server where the messages arrive encrypted
cipher = DES.new(key.encode("utf8"),DES.MODE_ECB)
decipher_user = cipher.decrypt(cipher_user)
decipher_password = cipher.decrypt(cipher_password)

print("Decipher user: " + str(decipher_user.decode()))
print("Decipher Password: " + str(decipher_password.decode()))
