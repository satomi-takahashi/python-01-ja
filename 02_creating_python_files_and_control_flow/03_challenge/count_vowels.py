def count_vowels():
    userinput = input("Enter a string: ") # ユーザー入力として文字列を受け取る
    string = userinput.lower() #小文字に変換 hello world!
    a = string.count('a') # a の数　0
    b = string.count('e') # e の数　1
    c = string.count('i') # i の数　0
    d = string.count('o') # o の数　2
    e = string.count('u') # u の数　0
    result = str(a + b + c + d + e)

    print("Enter a string: " + userinput)
    print("Number of vowels: " + result) 
count_vowels()