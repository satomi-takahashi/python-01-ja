def encode(message):
    encoded = []
    for c in message : 
        encoded.append(str(ord(c)))
    return  " ".join(encoded)

print (encode("Hello world"))

def decode(message):
    unicode_list = message.split()
    result = ""
    
    for i in unicode_list:
        result += chr(int(i))
    return result

print(decode("72 101 108 108 111 32 119 111 114 108 100"))  # Hello world
