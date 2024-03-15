def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]
    fruits_order = ["banana", "apple", "orange", "grape", "melon", "kiwi", "strawberry"]  # 指定された順序
    
    for fruit in fruits_order:
        occurrences[fruit] = fruits.count(fruit)
    
    return occurrences

print(counter())

