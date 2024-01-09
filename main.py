import random
from logo import hangman_stages, logo
from hangman_words import word_list

print(logo)
# word_list = ["APPMILLERS", "UDEMY"]
secret_word = random.choice(word_list)
word_length =len(secret_word)
guessed_letters = []
blanks = []
lives = 6
for _ in range(word_length):
    blanks.append("_")
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper() 
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)
    
    for position in range(word_length):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose.")
    
    print(" ".join(blanks))
    
    print(hangman_stages[lives])
    if "_" not in blanks:
        end_game = True
        print("You win")
    
    if end_game:
        ask = input("Do you want to play again?(Y/N) ")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            word_length =len(secret_word)
            for _ in range(word_length):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time.")


