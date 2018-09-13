import random
import re
import turtle


# Function to draw hangman
def draw(l):
    import turtle

    turtle.pensize(3)
    turtle.speed(10)

    # Head
    if l == 9:
        # (-100, 225)
        turtle.circle(-25, 540)

    # Torso
    if l == 8:
        # (-100, 175)
        turtle.sety(100)

    # Right leg
    if l == 7:
        # (-100, 100)
        turtle.setpos(-125, 50)

    # Left leg
    if l == 6:
        # (-125, 50)
        turtle.up()
        turtle.setpos(-100, 100)
        turtle.down()
        turtle.setpos(-75, 50)

    # Right arm
    if l == 5:
        turtle.up()
        turtle.setpos(-100, 150)
        turtle.down()
        turtle.setpos(-125, 120)

    # Left arm
    if l == 4:
        turtle.up()
        turtle.setpos(-100, 150)
        turtle.down()
        turtle.setpos(-75, 120)

    # Right eye
    if l == 3:
        turtle.up()
        turtle.setpos(-110, 210)
        turtle.down()
        turtle.circle(5)

    # Left eye
    if l == 2:
        turtle.up()
        turtle.setpos(-90, 210)
        turtle.down()
        turtle.circle(5)

    # Mouth
    if l == 1:
        turtle.up()
        turtle.setpos(-105, 185)
        turtle.down()
        turtle.setx(-95)

    # Rope
    if l == 0:
        turtle.up()
        turtle.setpos(-100, 170)
        turtle.down()
        turtle.circle(5)


# function to create random word to guess in 1 player mode
def create_word():
    with open("./dictionary.txt", "r") as text:
        word_list = [t.strip() for t in text]

    return random.choice(word_list).lower()


# function to add guesses to already_guessed
def add_to_already_guessed(g, l):
    g_list = list(g)

    for letter in g_list:
        l.append(letter)


def main():

    # set playing states
    play = True
    win = False

    while play:
        prompt = input("\nWelcome to Hangman!\n1 or 2 players? ")

        # Draw hangman canvas
        turtle.title("Hangman")
        turtle.speed(10)
        turtle.ht()
        turtle.up()
        turtle.pensize(3)
        turtle.setx(-300)
        turtle.down()
        turtle.setx(-150)
        turtle.up()
        turtle.setx(-225)
        turtle.down()
        turtle.sety(250)
        turtle.setx(-100)
        turtle.sety(225)

        try:
            while eval(prompt) not in [1, 2]:
                prompt = input("Invalid input.\n1 or 2 players? ")

        except (SyntaxError, NameError):
            while prompt not in ["1", "2"]:
                prompt = input("Invalid input.\n1 or 2 players? ")

        if eval(prompt) == 1:
            target_word = create_word()

        elif eval(prompt) == 2:
            target_word = turtle.textinput(
                "Text Box", "Insert text for player to guess!"
            )
            # target_word = input('Create word for player to guess: ')
            # print('\n' * 50)

        # set number of lives
        lives = 10

        # variable used to present to player; filled in as player guesses correctly
        if target_word.count(" "):
            space_indices = [i for i, x in enumerate(list(target_word)) if x == " "]

            fill_word = list(len(target_word) * "_")

            for i in space_indices:
                fill_word[i] = " "
        else:
            fill_word = list(len(target_word) * "_")

        # maintain list of already guessed letters and phrases
        already_guessed = []

        while lives > 0:
            print("\n\t" + "".join(fill_word) + "\n")

            display_guessed = " ".join(already_guessed)

            print(f"Already guessed letters: {display_guessed}")

            guess = input("Enter guess (type exit() to quit game) :\n-->\t").strip()

            # exit game
            if guess == "exit()":
                win = True
                break

            while not guess.isalnum() or guess == "":
                guess = input("Enter guess (type exit() to quit game) :\n-->\t").strip()

            # if player already guessed letter or phrase
            while guess in already_guessed:
                print("Already guessed that. Try something else!")
                guess = input("Enter guess (type exit() to quit game) :\n-->\t").strip()

            # if player's guess is a match
            if re.search(guess, target_word):
                add_to_already_guessed(guess, already_guessed)

                # for letter in guess_list:
                for letter in list(guess):
                    index_match = re.finditer(letter, target_word)
                    match_list = [m.start(0) for m in index_match]

                    for i in match_list:
                        fill_word[i] = letter

                print(f"\nMatch found! {lives} lives remaining.")

            # if player's guess does not match
            elif not re.search(guess, target_word):
                if len(guess) == 1:
                    add_to_already_guessed(guess, already_guessed)
                    lives -= 1
                    draw(lives)

                    print(f"No match. Lose a life. {lives} lives remaining.")

                else:
                    print(f"No match. {lives} lives remaining.")

            # if player guesses target correctly
            if "".join(fill_word) == target_word:
                win = True
                print("\n\t" + "".join(fill_word) + "\n")
                print("Congrats! You win!")
                break

        if win is False:
            print(f"\nSorry, you lost. The correct answer was:\n\n\t{target_word}")

        play_again = input("\nPlay again (yes/no)? ")

        if play_again == "yes":
            turtle.reset()
            turtle.ht()
            win = False
            continue
        else:
            play = False

    print("\nThanks for playing!\n")
    turtle.bye()


main()


# Bugs:
# account for punctuation and case
# multiword guess for 1 player mode
