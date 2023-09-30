# Using what we know so far do the following:
# - Have a variable with a number between 1 and 20 for the user to guess. (you can research random package if you are feeling frisky).
# - Using a loop, ask your user for a number between 1 and 20 (with exception handling in case they enter a string).
# - Check user input against the number you have stored.
# - When they get it correctly show a success message and end the program.
# BONUS
# - If you are feeling extra confident:
# - Track how many times the user has guessed.
# - Limit the number of guesses and end the program after the user has guessed too many times.
# - Display how many guesses the user took to get the correct answer.

secret_number = 12
player_guess = 0
try_count = 0

while player_guess != secret_number and try_count < 5:
    try_count += 1

    player_guess = input(f'Guess #{try_count} - Enter an integer from 1 to 20: ')

    try:
        player_guess = int(player_guess)

        if player_guess < 1 or player_guess > 20:
            print(f'\t {player_guess} is not an integer between 1 and 20.')

        elif player_guess != secret_number:
            print(f"\t {player_guess} is not the secret number.")

    except (ValueError):
        print(f'\t {player_guess} does not seem to be an integer.')
    
    if player_guess != secret_number:
        print(f"\tYou have {5 - try_count} guesses left. Try again...")        
    
if secret_number == player_guess:
    print(f'\tCongrats! You guessed it in {try_count} guesses!')
else:
    print("** Sorry. Only 5 tries allowed. **")

print(">>> GAME OVER <<<")