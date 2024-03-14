def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:  # 3と5の両方の倍数の場合は 'FizzBuzz'
            print("FizzBuzz")
        elif i % 3 == 0:  # 3の倍数の場合は 'Fizz'
            print("Fizz")
        elif i % 5 == 0:  # 5の倍数の場合は 'Buzz'
            print("Buzz")
        else:
            print(i)
fizzbuzz()
