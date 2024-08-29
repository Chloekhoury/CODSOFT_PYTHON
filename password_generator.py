import random
import string

while True:
    while True:
        length=int(input ("Welcome back!\nPlease enter the length of your password: "))
        if (length>4&length<30):break
        
    # Initialize an empty string
    result = ""
        
    for i in range(1, length+1): 
         # Generate a random character
        random_char = random.choice(string.ascii_letters)  # This chooses a random letter (uppercase or lowercase)
        # Concatenate the random character to the result string
        result += random_char
        
    print(f"Your password is: {result}.")
        
          
    r=input("Press 'C' to continue using the app and 'E' to exit: ")
    if (r=='E'):break
    elif r == 'C':
        continue
    else:
        print("Invalid option. Please press 'C' to continue or 'E' to exit.")

