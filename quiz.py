def user_menu():
    print("Welcome to the Historical Quotes Quiz")
    print("1. Start the quiz")
    print("2. Exit the game")
    option = input("Please select your option > ")
    print("\n")
    return option

def quiz_game():
    score = 0
    question_1 = input("Don't cry because it's over, smile because it happened. \na. Patrick Stewart \nb. JK Rowling \nc. Dr. Seuss \nAnswer > ")
    if question_1 == "c" or question_1 == "Dr. Seuss":
        score += 1
        print("Well Done! That is the correct answer.")
        print("Score > ", score)
        print("\n")
    else:
        print("Sorry that is the incorrect answer! The answer is c. Dr. Seuss ")
        print("Score > ", score)
        print("\n")

    question_2 = input("Be yourself; everyone else is already taken. \na. Oscar Wilde \nb. Walt Disney \nc. Sean Connery \nAnswer > ")
    if question_2 == "a" or question_2 == "Oscar Wilde":
        score += 1
        print("Well Done! That is the correct answer.")
        print("Score > ", score)
        print("\n")
    else:
        print("Sorry that is the incorrect answer! The answer is a. Oscar Wilde")
        print("Score > ", score) 
        print("\n")

    question_3 = input("I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best. \na. Marilyn Monroe \nb. Leonardo DiCaprio \nc. Paris Hilton \nAnswer > ")
    if question_3 == "a" or question_3 == "Marilyn Monroe":
        score += 1
        print("Well Done! That is the correct answer.")
        print("Score > ", score)
        print("\n")
    else:
        print("Sorry that is the incorrect answer! The answer is a. Marilyn Monroe")
        print("Score > ", score)
        print("\n")

    question_4 = input("In three words I can sum up everything I've learned about life: it goes on. \na. Frank Zappa \nb. Robert Frost \nc. David Nesbit \nAnswer > ")
    if question_4 == "b" or question_4 == "Robert Frost":
        score += 1
        print("Well Done! That is the correct answer.")
        print("Score > ", score)
        print("\n")
    else:
        print("Sorry that is the incorrect answer! The answer is a. Marilyn Monroe")
        print("Score > ", score) 
        print("\n")

def while_loop():
    while True:
        option = user_menu()
        if option == "1":
            quiz_game()
        elif option == "2":
            break
        else:
            print("ERROR - Please select an option")
        print("\n")

while_loop()