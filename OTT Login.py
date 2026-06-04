username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))
plan = input("Enter your plan (Basic / Premium / VIP)")
if username == "Harshi" and password == "1105":
             print("Login successful")
else:
    print("wrong credentials,access denied")
    exit()
    
if plan not in ["Basic", "Premium", "VIP"]:
    print("Invalid plan,Choose Basic,PRemium or VIP")
if age < 13:
    category = "Kids"
elif age < 18:
    category = "Teen"
else:
    category = "Adult"
    
hd = "yes" if plan == "Premium" or plan == "VIP" else "no"

match plan:
    case "Basic":
        screens = 1
        price = 99
    case "Premium":
        screens = 3
        price = 299
    case "VIP":
        screens = 5
        price = 599

print(f"Welcome {username}")
print(f"plan: {plan.upper()} | {price}/month")
print(f"screens: {screens} | HD: {hd}")
print(f"Content category: {category}")
