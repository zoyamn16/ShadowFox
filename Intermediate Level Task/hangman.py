import random

word_hints = {
    "python": "A programming language",
    "developer": "Person who writes code",
    "internship": "Learning job for students",
    "programming": "Writing code",
    "algorithm": "Steps to solve a problem",
    "function": "Small block of code",
    "variable": "Stores a value",
    "printer": "Used to print",
    "website": "Page on the internet",
    "browser": "Used to open websites",
    "scanner": "Used to scan documents",
    "debugging": "Fixing mistakes in code",
    "compiler": "Changes code to computer language",
    "database": "Stores information",
    "software": "Programs in a computer",
    "hardware": "Physical parts of computer",
    "file": "Stores data",
    "folder": "Contains files",
    "email": "Electronic message",
    "internet": "Network used to connect computers",
    "keyboard": "Used for typing"
}

while True:
    word = random.choice(list(word_hints.keys()))
    hint = word_hints[word]

    displayed_word = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("\n🎮 WELCOME TO HANGMAN")
    print("💡 Hint:", hint)

    while attempts > 0 and "_" in displayed_word:
        print("\nWord:", " ".join(displayed_word))
        print("Used letters:", ", ".join(guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter only ONE letter.")
            continue

        if guess in guessed_letters:
            print("⚠ Letter already used.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    displayed_word[i] = guess
        else:
            print("❌ Wrong guess!")
            attempts -= 1

    if "_" not in displayed_word:
        print("\n🎉 Congratulations you guessed the word:", word)
    else:
        print("\n💀 Game over! Word was:", word)

    play_again = input("\nPlay again? (yesn/no): ").lower()
    if play_again not in ["yes", "y"]:
        print("👋 Thanks for playing!")
        break

