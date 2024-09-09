# implement a program that prompts the user for a str of text and
# then outputs that same text but with all vowels (A, E, I, O, and U)
# omitted, whether inputted in uppercase or lowercase.

#Function to remove vowels
def isVowel(string):
    newString = string
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    for character in string:
        if character in vowels:
            newString = newString.replace(character, "")
    return newString

userInput = input("Input: ").strip()
output = isVowel(userInput)
print("Output: ", output)
