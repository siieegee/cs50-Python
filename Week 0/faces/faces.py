def main():
    # Ask user for the message
    message = input("Input the message: ")

    # Call convert on that input
    result = convert(message)

    # Print the result
    print(result)

def convert(message):
    # Replace :) with slightly smiling face
    message = message.replace(":)", "🙂")

    # Replace :( with slightly frowning face
    message = message.replace(":(", "🙁")
                                
    # Return string
    return message

main()