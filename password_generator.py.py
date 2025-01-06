#Random Password Calculator

import random
import string

# Main program
print("Random Password Generator!")

while True:
    try:
        # Get password length and ensure the correct length of 4 minimum
        length = int(input("Enter password length (4 minimum): "))
        if length < 4:
            print("Password length must be at least 4 characters")
            
        # Gather the character type preferences
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Build the character sets
        char_sets = []
        if use_uppercase:
            char_sets.append(string.ascii_uppercase)  #adds A-Z
        if use_lowercase:
            char_sets.append(string.ascii_lowercase)  #adds a-z
        if use_numbers:
            char_sets.append(string.digits)  #adds 0-9 
        if use_symbols:
            char_sets.append(string.punctuation)  #adds !@#$ and more
        
        if not char_sets:
            print("At least one character type must be selected")
        
        # Combine the character sets
        all_chars = ''.join(char_sets)
        
        # Generate initial password with one char from each selected set
        password = []
        for char_set in char_sets:
            password.append(random.choice(char_set))
        
        # Fill in the remaining length with random characters
        for _ in range(length - len(password)):
            password.append(random.choice(all_chars))
        
        # Shuffle password
        random.shuffle(password)
        
        # Convert to string and display
        final_password = ''.join(password)
        print("\n Generated Password:", final_password)
        
        # Ask to generate another password
        if input("\n Generate another password? (y/n): ").lower() != 'y':
            print("Thank you for using the Random Password Generator!")
            break
            
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")