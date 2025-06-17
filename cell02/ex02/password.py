password = "python is awesome"
user_input = input("Enter password: ").strip()
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")