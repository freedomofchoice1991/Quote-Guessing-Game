from randomQuote import displayRandomQuote

def start_game():
    wannaplay = "y"  # repetitive game
    while wannaplay.lower() in ('y', 'yes', 'yess', 'yesss', 'yeah', 'yep'):
        correct_author = displayRandomQuote()[1]
        # split author name to 2 parts and get the second part
        correct_author_last_name = correct_author.split(' ')[1]
        correct_author_dateOfBirth = displayRandomQuote()[2]
        correct_author_placeOfBirth = displayRandomQuote()[3]
        quote_category = displayRandomQuote()[4]

        hint = [f"4οΈβ£  Author last name is {correct_author_last_name}", f"3οΈβ£  Author date of birth: {correct_author_dateOfBirth} π",
                f"2οΈβ£  Author was born {correct_author_placeOfBirth} π", f"1οΈβ£  Quote category: {quote_category} "]

        print("\n\n\n.\n.\n.\n.\n.\n.\n", displayRandomQuote()
              [0], "\n.\n.\n.\n.\n.\n.")  # Random Quote

        # print(correct_author.lower())  # hint for programming

        guess = input('\n\n\nGuess who said that quote:  ').lower()

        if guess == correct_author.lower():  # first guess
            print("β­οΈπππππππππππππππππβ­οΈ\n")
            print("Wow, you are really good at guessingπ±π²!\n")
            print(f"The correct answer is: ππ» {correct_author.upper()} ππ»")
            print("\nβ­οΈπππππππππππππππππβ­οΈ")
            wannaplay = input('Do you want to keep playing?π (y/n) ')
        else:  # next 3 guess
            remainginGuesses = 4
            while (remainginGuesses > 0 and guess != correct_author.lower()):
                print("\n_____________________________________________")
                print("\nUnfortunately you were wrong!\n")
                print("Hintπ‘: ", hint[remainginGuesses-1])
                print("Please use the given hint aboveππ»\n\nremaining guesses: ",
                      remainginGuesses * "β€οΈ ")
                guess = input('\nTake another guess: ').lower()
                remainginGuesses -= 1

                if (guess == correct_author.lower()):
                    print("\n==========================================")
                    print("Cngrats!π Finally your guess was correct!!!ππ₯³π€©")
                    print(
                        f"The correct answer is: ππ» {correct_author.upper()} ππ»")
                    print("==========================================")
                    wannaplay = input(
                        '\nDo you want to keep playing?π (y/n) ')
                    break
            else:
                print("\n\n\n\n_____________________________________________")
                print("_____________________________________________")
                print(
                    f"\nUnfortunately you could not guess the right answerπ\n\nThe correct answer β was:  {correct_author.upper()}\n")
                print("_____________________________________________")
                print("_____________________________________________")
                wannaplay = input('\nDo you want to keep playing?π (y/n) ')
