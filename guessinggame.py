import random

# Define a dictionary of popular mobile games with their descriptions
mobile_games = {
    "Among Us": "An online multiplayer social deduction game where players work together to complete tasks while one or more impostors attempt to sabotage and kill everyone.",
    "Clash Royale": "A real-time strategy game where players collect cards of various troops and spells, and deploy them to destroy their opponent's towers.",
    "Pokemon Gop": "An augmented reality mobile game where players capture virtual creatures called Pokémon, which appear as if they are in the player's real-world location.",
    "Candy Crush ": "A match-three puzzle game where players swap colored candies on a game board to make a match of three or more of the same color, causing them to disappear.",
    "Subway Surfers": "An endless runner mobile game where players control characters who surf on hoverboards, avoiding obstacles and collecting coins."
}

def guess_game():
    # Choose a random game from the dictionary
    game_name = random.choice(list(mobile_games.keys()))
    game_description = mobile_games[game_name]
    
    print("Welcome to the Popular Mobile Game Guessing Game!")
    print("I am thinking of a popular mobile game. Can you guess what it is?")
    print(f"Description: {game_description}")
    
    attempts = 3
    while attempts > 0:
        guess = input("\nYour guess: ").strip().title()  # Convert the guess to title case for uniformity
        if guess == game_name:
            print("\nCongratulations! You guessed correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\nIncorrect guess. You have {attempts} attempts left.")
            else:
                print("\nSorry, you ran out of attempts.")
                print(f"The correct answer was: {game_name}")

# Run the game
guess_game()
