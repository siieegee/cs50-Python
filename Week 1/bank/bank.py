user_greeting = input("Greeting: ").strip().lower()

if user_greeting.startswith("hello"):
    print("$0")
elif user_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
