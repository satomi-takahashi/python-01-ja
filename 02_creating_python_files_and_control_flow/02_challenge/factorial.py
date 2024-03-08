def compute_factorial():
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    number = int(input("please enter a number >= 0:")) #5
    if number == 0:
        return 1
    if number < 0:
        return "Error: negative numbers are invalid" 
    for x in range (1, number):
        number = number * x
# result変数を編集し、最終的な計算結果を保存します
    result = number
    return result


compute_factorial()
