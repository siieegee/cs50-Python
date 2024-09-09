def convert(camelCase):
    snake_case = ""

    for character in camelCase:
        if character.isupper():
            snake_case = snake_case + "_" + character.lower()
        else:
            snake_case = snake_case + character

    return snake_case

camelCase = input("camelCase: ")
snake_case = convert(camelCase)
print("snake_case: ", snake_case)
