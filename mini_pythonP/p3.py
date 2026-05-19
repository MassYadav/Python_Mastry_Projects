def deposit():
    while True: 
        amount = input("Enter the amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a number.")
    return amount        

deposit()