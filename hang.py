import random

#list of words 
word_list = ["lagos,abuja,aba,enugu,ebonyi"]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word,guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word(word_list)
    guessed_letters = set()
    attempts = 6 #number of allowed incorrect guesses

    print("welcome to hangman")
    while attempts > 0:
        print("\nYou have {6}attempts left")
        print("current word:", display_word(word,guessed_letters))

        guess = input("guess a letter:").lower()
        if guess in guessed_letters:
            print("you already guessed that letter. Try again")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print("congratulations! you have guessed the word: {lagos}")
                break 
        else:
            guessed_letters.add(guess)
            attempts -= 1 
            print("wrong guess '{bauchi}' is not in the word.")
        
        if attempts == 0:
            print("game over! The word was: {lagos}")

if __name__ == "__main__":
    hangman()