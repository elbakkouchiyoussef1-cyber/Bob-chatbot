bot_name = "Bob"
print(f"Hello! I am {bot_name}. What can I do for you?")

while True:
    user_input = input("you: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print(f"{bot_name}: Hi there! How can I help you?")

    elif user_input in ["bye", "goodbye"]:
        print(f"{bot_name}: Goodbye! Have a nice day :)")
        break  # Exit the loop

    elif user_input in ["+", "add", "-", "subtract", "*", "multiply", "/", "divide"]:
        print(f"{bot_name}: Sure! Let's do some math!")

        while True:  # Retry loop for invalid input
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))

                if user_input in ["+", "add"]:
                    result = num1 + num2
                elif user_input in ["-", "subtract"]:
                    result = num1 - num2
                elif user_input in ["*", "multiply"]:
                    result = num1 * num2
                elif user_input in ["/", "divide"]:
                    if num2 == 0:
                        print(f"{bot_name}: Cannot divide by zero. Try again.")
                        continue
                    result = num1 / num2

                print(f"{bot_name}: The result is = {result}")
                break  # Exit retry loop
            except ValueError:
                print(f"{bot_name}: Oops! Please enter valid numbers.")

    else:
        print(f"{bot_name}: Sorry, I don't understand. Please try again.")
