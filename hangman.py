

import random

words = ["apple", "tiger", "python", "robot", "music"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman Game 🎮")

while wrong_guesses < max_wrong and "_" in display_word:

    print("\nWord:", " ".join(display_word))

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:

        print("✅ Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1

        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong - wrong_guesses)

if "_" not in display_word:

    print("\n🎉 Congratulations! You Won 🎉")
    print("The Word Was:", word)

else:

    print("\n💀 Game Over 💀")
    print("The Word Was:", word)