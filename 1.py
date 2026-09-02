import random
word=["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
print("Welcome to the Word Guessing Game!")
print("You have 5 attempts to guess the word.")
print("The word has", len(random.choice(word)), "letters.")
print(" ".join(len(random.choice(word)) * ["_"]))
if __name__ == "__main__":
    attempts = 5
    chosen_word = random.choice(word)
    guessed_letters = []
    while attempts > 0:
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in chosen_word:
            print("Good guess!")
        else:
            print("Wrong guess.")
            attempts -= 1
        display_word = [letter if letter in guessed_letters else "_" for letter in chosen_word]
        print(" ".join(display_word))
        if "_" not in display_word:
            print("Congratulations! You've guessed the word:", chosen_word)
            break
    else:
        print("Sorry, you've run out of attempts. The word was:", chosen_word)