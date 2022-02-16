import base64
def stringingToBinary(string):
    new = ''.join(format(ord(i), '08b') for i in string)

    l = []
    for x in new:
             l.append(int(x))
    return l

def base64ToBinary(string):
    decodedText = base64.decodebytes(string)
    bytes = "".join(["{:08b}".format(x) for x in decodedText])
    bytes = [int(x) for x in bytes]
    return bytes

def binaryToHex(array):
    array = ''.join([str(x) for x in array])
    return hex(int(array, 2))[2:]

def returnKey(text, encryptedText):
    bytes = stringingToBinary(text)
    encryptedbytes = base64ToBinary(encryptedText)

    # XOR 
    keyInBytes = []
    for i in range(len(bytes)):
      keyInBytes.append(bytes[i] ^ encryptedbytes[i])

    return binaryToHex(keyInBytes)

encryptedText = '''o9/khC3Pf3/9CyNCbdzHPy5oorccEawZSFt3mgCicRnihDSM8Obhlp3vviAVuBbiOtCSz6husBWqhfF0Q/8EZ+6iI9KygD3hAfFgnzyv9w=='''.encode('ascii')
key = '''ecb181a479a6121add5b42264db9b44b4b48d7d93c62c56a3c3e1aba64c7517a90ed44f8919484b6ed8acc4670db62c249b9f5bada4ed474c9e4d111308b614788cd4fbdc1e949c1629e12fa5fdbd9'''.encode('ascii')
decryptedText = 'Orice text clar poate obtinut dintr-un text criptat cu OTP dar cu o alta charactereie.'
key2 = returnKey(decryptedText, encryptedText)

print(f"Mesaj 2: {decryptedText}")
print(f"Cheia pentru a obtine mesaj 2: {key2}")
