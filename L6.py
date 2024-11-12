import csv
import random

def load_countries_from_csv(file_path):
    """Load a list of country names from a CSV file."""
    countries = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            # Assuming the country names are in the first column of the CSV
            for row in reader:
                if row:
                    countries.append(row[0].strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return countries

def get_random_country(countries):
    """Select a random country from the list."""
    return random.choice(countries).upper()

def display_current_progress(country, guessed_letters):
    """Display the current progress of guessed letters in the country name."""
    display = ""
    for letter in country:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display

def play_game(country):
    """Main game logic for guessing the country."""
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 5

    print("Welcome to the Country Guessing Game!")
    print(f"Try to guess the country name. You can make {max_wrong_guesses} wrong guesses.\n")

    # Game loop
    while True:
        # Show the current progress
        current_progress = display_current_progress(country, guessed_letters)
        print(f"Current word: {current_progress}")

        # Check if the player has guessed the whole word
        if "-" not in current_progress:
            print("\nCongratulations! You've guessed the country correctly!")
            break

        # Get the player's guess
        guess = input("Guess a letter: ").upper()

        # Validate the guess (only single letters are allowed)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in country:
            print(f"Good guess! '{guess}' is in the country name.")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the country name.")
            print(f"You have {max_wrong_guesses - wrong_guesses} wrong guesses left.")

        # Check if the player has reached the maximum number of wrong guesses
        if wrong_guesses >= max_wrong_guesses:
            print("\nYou've used all your guesses. Game over!")
            print(f"The correct country was: {country}")
            break

def main():
    # Load countries from the CSV file
    file_path = 'countries.csv'  # Replace with the path to your CSV file
    countries = load_countries_from_csv(file_path)

    if not countries:
        print("No countries available to play. Please check your CSV file.")
        return

    # Pick a random country
    country = get_random_country(countries)

    # Start the game
    play_game(country)

if __name__ == "__main__":
    main()
