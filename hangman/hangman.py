import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(tries)

    while not guessed and tries > 0:
        guess = input("take a guess: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("try again", guess)
            elif guess not in word:
                print(guess, "is wrong.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is right!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("try again", guess)
            elif guess != word:
                print(guess, "is a no from me.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        else:
            print("Not a valid guess.")
        print(tries)
        print(word_complete)
        print("\n")
    if guessed:
        print("Congrats, You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()