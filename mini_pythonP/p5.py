HISTORY_FILE = "history.txt"

def save_history(question,answer):
    try:
        file = open(HISTORY_FILE,"a")
        file.write(f"{question} = {answer}\n")
        file.close()
    except Exception as e:
        print(f"Error saving history: {e}")

def show_history():
    try:
        file = open(HISTORY_FILE,"r")
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found.")
            return
        else:
            for line in reversed(lines):
                print(line.strip())
    except Exception as e:
        print(f"Error showing history: {e}")
    finally:
        file.close()

def clear_history():
    try:
        file = open(HISTORY_FILE,"w")
        file.close()
        print("History cleared.")
    except Exception as e:
        print(f"Error clearing history: {e}")
    finally:
        file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number")
        return None

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero.")
            return None
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return None

def main():
    
    print("welcome the calculator!")
    while True:
        user_input = input("Enter a calculation (e.g., 2 + 2) or 'history' to view past calculations, 'clear' to clear history, or 'quit' to exit: ").strip().lower()
        if user_input == "quit":
            print("Goodbye!")
            return
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        elif user_input:
            result = calculate(user_input)
            if result is not None:
                print(f"Result: {result}")
                save_history(user_input, result)
            


main()

