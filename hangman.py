import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
hint = '-' * len(word)
guessed = set()
tries = 8


print("H A N G M A N")
play = input('Type "play" to play the game, "exit" to quit:')

while True:
    if play == "play":
        pass
    else:
        break
    if tries > 0:
        if hint == word:
            print(hint)
            print("You guessed the word!")
            print("You survived!")
            print("")
            play = input('Type "play" to play the game, "exit" to quit:')
        else:
            print('')
            print(hint)
            guess = input("Input a letter:")
            if len(guess) > 1:
                print("You should input a single letter")
            elif guess.isalpha() is False or guess.islower() is False:
                print("Please enter a lowercase English letter")
            elif guess in guessed:
                print("You've already guessed this letter")
            elif guess in word:
                guessed.add(guess)
                hint = ''.join(letter if letter in guessed else '-' for letter in word)
            else:
                guessed.add(guess)
                print("That letter doesn't appear in the word")
                tries -= 1
    else:
        print("You lost!")
        print("")
        play = input('Type "play" to play the game, "exit" to quit:')
