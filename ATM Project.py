User_information = {"Name":"Harshita",
                    "Mobile Number": "",
                    "ATM PIN": "1105",
                    "Balance": 50000,
                    "Transaction History": []
                    } #User data
print("Please insert your ATM Card")
remaining_attempts = 3
while remaining_attempts > 0:
    User_pin = input("Pls enter your ATM Pin: ")
    if len(User_pin) == 4:
        if User_pin == User_information['ATM PIN']:
            print("Welcome to the ATM")
            while True:
                print("\n==== ATM MENU ====")
                print("1.Deposit Money")
                print("2.Withdraw Money")
                print("3.Check Balance")
                print("4.Change PIN")
                print("5.Transaction History")
                print("6.Exit")
                choice = int(input("Enter your choice: "))
                if choice == 3:
                    print("Current Balance:",User_information["Balance"])
                elif choice == 1:
                    amount = int(input("Enter amount to deposit: "))
                    User_information["Balance"] += amount
                    User_information["Transaction History"].append(f"Deposited Rs{amount}")
                    print("Money Deposited Successfully")
                elif choice == 2:
                     amount = int(input("Enter amount to deposit: "))
                     if amount <= User_information["Balance"]:
                         User_information["Balance"] -= amount
                         User_information["Transaction History"].append(f"Withdrawn Rs{amount}")
                         print("Please collect your cash")
                     else:
                         print("Insufficient Balance")
                elif choice == 5:
                    if len(User_information["Transaction History"]) == 0:
                        print("No transactions yet")
                    else:
                        for transaction in User_information["Transaction History"]:
                            print(transaction)
                elif choice == 4:
                    old_pin = input("Enter old PIN: ")
                    if old_pin == User_information["ATM PIN"]:
                       new_pin = input("Enter new PIN: ")
                       if len(new_pin) == 4:
                           User_information["ATM PIN"] = new_pin
                           print("PIN changed successfully")
                       else:
                          print("PIN must be 4 digits")
                    else:
                        print("Wrong old PIN")
                elif choice == 6:
                    print("Thank you for using ATM")
                    break
       
        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"Invalid pin entered and you have {remaining_attempts} left")
            else:
                print("Your card is blocked")
    else:
        print("Pls enter 4 digit pin")
    
