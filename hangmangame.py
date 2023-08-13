# *BY Osama Abdo Modhish*
import random

word_list = ["ghamdan", "osama",  "mohammed"]  # List of potential words
chosen_word = random.choice(word_list)  # Randomly select a word from the list
try_chose = 6   # Number of tries or guesses allowed
blanks_letters = []   # List to store the guessed letterss

print("******* Welcome to Hang man game  *********")
print("_ " * len(chosen_word))  # Display the initial blanks for the word

while True:
    guess = input("Enter a single letter You guess : ").lower()

    if guess.isalpha() and len(guess) == 1:  # Check if the input is a single alphabetical character
        if guess in blanks_letters:  # Check if the letter has already been guessed
            print("We have this letter. Try again.")
            continue
        blanks_letters.append(guess)  # Add the guessed letter to the list

        if guess in chosen_word:   # Check if the guessed letter is in the word
            print("Good ... Correct guessed.")
        else:
            try_chose -= 1
            print(f"Wrooooong guessed. You have {try_chose} try left.")

        word_display = ""

        # length = len(guess)
        # if guess in chosen_word :
        #    for letter in range(length):
        #       if chosen_word[letter]==guess:
        #         blanks_letters[letter]=guess
        #         word_display += letter + " "
        #       else:
        #         word_display += "_ "

        for letter in chosen_word:
            if letter in blanks_letters:
                word_display += letter + " "
            else:
                word_display += "_ "

        print(word_display)

        if "_" not in word_display:  # Check if all letters have been guessed
            print("Congratulations You are winner +_+")
            break

        if try_chose == 0:  # Check if the player has run out of tries
            print("Game over. You tries Doooone.")
            break
    else:
        print("Error input. Please Enter a single letter.")
