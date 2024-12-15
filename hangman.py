import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

placeholder = ""
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"*****************{lives}/6 LIVES LEFT******************")
    guess = input("Guess a letter:").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "
            
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        
        if lives == 0:
            game_over = True
            print(f"******************IT WAS {chosen_word} YOU LOSE! :(********************")
    
    if display == chosen_word:
        game_over = True
        print("******************YOU WIN! :D*********************")
    
    print("Word to guess:",display)
    print(stages[lives])
