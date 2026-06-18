Pin = "1234"
pin = input("Please enter your PIN: ")
balance = 20000
if pin == "1234":
    print("Access granted.") 

    print("Welcome to your account!")
    print ("1. Check Balance")
    print ("2. Withdraw Money")
    print ("3. Deposit Money")
    print ("4. Exit")
    choice = input("Please select an option (1-4): ")
    if choice == "1":
        print(f"Your current balance is: ${balance}")
    elif choice == "2":
        enter_amount = float(input("Enter the amount to withdraw: "))
        balance = balance-enter_amount
        print(f"Transaction successful. Your new balance is: {balance}")
    if choice == "3":
        enter_amount = float(input("Enter the amount to deposit: "))
        balance=balance+enter_amount
        print(f"Transaction successful. Your new balance is: {balance}")
    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
else:
    print("Access denied. Please try again.")
    pin = input("Please enter your PIN: ")
    if pin == "1234":
        print("Access granted.")
    


