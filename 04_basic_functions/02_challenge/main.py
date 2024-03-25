def encode():
    user_input = input("文字を入力してください：")
    unicode_value = ord(user_input[0])
    return chr(unicode_value).encode()

def decode(encoded_data):
    decoded_user_input = encoded_data.decode()
    print(decoded_user_input)

encoded_data = encode()
decode(encoded_data)

