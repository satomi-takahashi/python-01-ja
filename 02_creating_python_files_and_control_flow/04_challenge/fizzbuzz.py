def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:  # 3と5の両方の倍数の場合は 'FizzBuzz'
            print("FizzBuzz")
        elif num % 3 == 0:  # 3の倍数の場合は 'Fizz'
            print("Fizz")
        elif num % 5 == 0:  # 5の倍数の場合は 'Buzz'
            print("Buzz")
        else:
            print(num)
fizzbuzz()
