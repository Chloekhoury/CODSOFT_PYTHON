while True:
    while True:
        op = input("Welcome to Codsoft calculator!\nPlease choose the operation you want:\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n")
        
        if op in ['1', '2', '3', '4']:
        #if (op!=1 and op!=2 and op!=3 and op!=4): #no bcz op is a string
            break
        else:
            print("Invalid choice. Please select a valid operation (1-4).")

    # Asking for two numbers input
    # The input() function always returns the user's input as a string. 
    # If you need the input as another data type (e.g., an integer or float), 
    # you should convert it using int() or float().
    num = float(input("Enter a first number: "))
    num2=float(input("Enter a second number: "))

    if (op=='1'):
        result = num+num2
        print(f"{num}+{num2}={result}.")
    # The f in Python refers to f-strings (formatted string literals), 
    # a way to embed expressions inside string literals using curly braces {}. 

    if (op=='2'):
        result = num-num2
        print(f"{num}-{num2}={result}.")
        
    if (op=='3'):
        result = num*num2
        print(f"{num}*{num2}={result}.")
        
    if (op=='4'):
        result = num/num2
        print(f"{num}/{num2}={result}.")

    r=input("Press 'C' to continue using the app and 'E' to exit")
    if (r=='E'):break
    elif r == 'C':
        # Restart the calculator process if 'C' is pressed
        continue
    else:
        print("Invalid option. Please press 'C' to continue or 'E' to exit.")