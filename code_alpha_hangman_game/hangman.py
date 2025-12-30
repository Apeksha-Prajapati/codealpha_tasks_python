import random

HANGMAN_PICS = [
    "",
    "O",
    "O\n|",
    "O\n/|",
    "O\n/|\\",
    "O\n/|\\\n/",
    "O\n/|\\\n/ \\"
]

def choose_word():
    categories = {
        "fruits": ["apple", "banana", "orange", "grapes", "mango"],
        "animals": ["tiger", "lion", "zebra", "monkey", "elephant"]
    }

    print("\nCategories:", ", ".join(categories.keys()))
    cat = input("Choose category: ").lower()

    if cat not in categories:
        cat = "fruits"

    return random.choice(categories[cat])

def choose_difficulty():
    print("\nDifficulty Levels:")
    print("Easy (8 attempts)")
    print("Medium (6 attempts)")
    print("Hard (4 attempts)")

    level = input("Choose difficulty: ").lower()

    if level == "easy":
        return 8
    elif level == "hard":
        return 4
    else:
        return 6

def play_game():
    word = choose_word()
    attempts = choose_difficulty()

    display = ["_"] * len(word)
    wrong_letters = []
    used_letters = []
    hint_used = False

    print("\n🎮 Welcome to Advanced Hangman Game")

    while attempts > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        print("Wrong letters:", " ".join(wrong_letters))
        print("Attempts left:", attempts)
        print(HANGMAN_PICS[len(wrong_letters)])

        guess = input("Enter a letter (or type 'hint'): ").lower()

        if guess == "hint":
            if not hint_used:
                display[0] = word[0]
                hint_used = True
                print("💡 Hint used! First letter revealed.")
            else:
                print("⚠ Hint already used.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Enter only one alphabet.")
            continue

        if guess in used_letters:
            print("⚠ Letter already tried.")
            continue

        used_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("❌ Wrong!")
            wrong_letters.append(guess)
            attempts -= 1

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over!")
        print("Correct word was:", word)

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing 😊")
            break

main()

