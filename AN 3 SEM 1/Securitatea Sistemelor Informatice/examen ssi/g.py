from hashlib import sha256

# sha256(string)
# from https://cryptomarketpool.com/convert-a-string-to-sha256-in-python/
# Online convertor: https://emn178.github.io/online-tools/sha256.html
str = 'PAROLA'
result = sha256(str.encode())
hs = result.hexdigest()
print("Hash pe PAROLA: " + hs)

