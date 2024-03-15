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
    for fruit in fruits:
        occurrences[fruit] = occurrences.get(fruit, 0) +1
    return occurrences

print(counter())
