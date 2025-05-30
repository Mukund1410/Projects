import random  # Importing Random module to generate random numbers
import math  # Importing Math module to do mathematical calculations

# Function to check if the user input is a valid integer
def is_valid_integer(value):
    try:
        int(value)                              #converts the value into a int value
        return True                             #if succesfull return true(value can be converted into integer)
    except:
        return False                            #if int(value) gives a error return false(value can't be converted into integer)
    
#Function to keep asking user until a input is valid and greater than 0
def valid_input(value):
    #Check if value is a digit and greater than 0
    if value.isdigit() != 1 or int(value) <= 0:
            while(True):
                # If the input is not a valid integer, keep asking for input
                if is_valid_integer(value) != 1:
                    value = input("Invalid Input! Please enter a digit: ")
                    while(True):
                        # Check if the input is a valid integer and greater than 0
                        if is_valid_integer(value) == 1:
                            if int(value) > 0:
                                break  # Exit the loop if the input is valid
                            else:
                                value = input("Please enter a number greater than 0: ")
                        elif is_valid_integer(value) != 1:
                            value = input("Invalid Input! Please enter a digit: ")
                        elif int(value) <= 0:
                            value = input("Please enter a number greater than 0: ")
                
                # If the input is a valid integer but less than or equal to 0, ask again
                elif int(value) <= 0:
                    value = input("Please enter a number greater than 0: ")
                    while(True):
                        #The same process is repeated
                        if is_valid_integer(value) == 1:
                            if int(value) > 0:
                                break
                            else:
                                value = input("Please enter a number greater than 0: ")
                        elif is_valid_integer(value) != 1:
                            value = input("Invalid Input! Please enter a digit: ")
                        elif int(value) <= 0:
                            value = input("Please enter a number greater than 0: ")
                break
            return int(value)
    else:
        return int(value)


#Main Program

# Ask the user if they want to play the game
playing = input("Do you wanna play the guessing game?(yes/no) ")

# Main loop for the game that will keep asking the user to play until they exit
while(True):
    # Check if the user wants to play
    if (playing == 'yes' or playing == 'Yes'):
        print("\n")
        print("Well! I guessed it right that you want to play :)")
        print("Let's Play :) ")
        print("\n")

        # Ask for the upper range limit for the guessing number
        upper_bound = input("Now Enter the upper range till which you want to guess the number: ")
        
        #check for valid input
        upper_bound=valid_input(upper_bound)

        # Convert the valid upper bound input to an integer
        upper_bound = int(upper_bound)

        # Calculate the ideal number of guesses
        ideal_count = math.log(upper_bound, 2) if upper_bound != 1 else 1

        # Generate a random number within the given range
        random_num = random.randint(1, upper_bound)

        print("\n")
        print("OK! I have got a number under ", upper_bound)
        print("Can you guess it right? Let's see :) ")
        print("\n")

        # Ask the user to enter their guess
        user_in = input("Enter the number: ")
        user_in=valid_input(user_in)
        
        # Number of guesses the user takes to guess the number 
        choices_count = 0

        # Check if the user guessed correctly on the first try
        if user_in == random_num:
            print("Congratulations!! You guessed it right on your first guess!")
            print("You took 1 Guess to guess the correct answer")
            print("\n")
            print("Thank you for playing our game :) ")
            exit()  # Exit the game

        # Keep asking until the user guesses correctly
        while user_in != random_num:
            # If the guess is too low, ask user to guess higher
            if user_in < random_num:
                print("Try a greater number")
                print("\n")
                user_in = input("Enter the number: ")
                choices_count += 1
                # Check if the user input is a valid digit
                user_in=valid_input(user_in)
            # If the guess is too high, ask user to guess lower
            elif user_in > random_num:
                print("Try a smaller number")
                print("\n")
                user_in = input("Enter the number: ")
                choices_count += 1
                # Check if the user input is a valid digit
                user_in=valid_input(user_in)
                

        # If the user guessed correctly, congratulate them and show the number of guesses
        print("Congratulations!! You have guessed it right")
        print("You took ", choices_count, " Guesses to guess the correct answer")

        # Ask if the user wants to play again
        playing = input("Do you want to play again(yes/no): ")

        # If the user says no, exit the game
        if playing == 'No' or playing == 'no':
            print("OK!! I guess I will see you soon :) ")
            print("Thank you for playing :)")
            exit()

    # If the user does not want to play, exit the game
    elif playing == "No" or playing == "no":
        print("OK!! See you next time :) ")
        exit()

    # If the user enters an invalid input, ask again
    else:
        playing = input("Please enter a valid choice(yes/no): ")
