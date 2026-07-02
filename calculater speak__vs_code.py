
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main calculator function
def calculator():
    print("Simple Speaking Calculator")
    print("Operations: +  -  *  /")

    while True:
        try:
            # Taking input
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            # Performing calculation
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    print("Cannot divide by zero")
                    speak("Cannot divide by zero")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator")
                speak("Invalid operator")
                continue

            # Output
            print("Result:", result)
            speak(f"The answer is {result}")

        except ValueError:
            print("Invalid input")
            speak("Invalid input")

        # Continue or stop
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            speak("Calculator closed")
            break

# Run program
calculator()


