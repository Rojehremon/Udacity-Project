# it imports the time module
import time
# it imports the random module
import random
# it imports the sys module
import sys
# the score variable
global total_score
total_score = 0
# the user name variable
global User_name
User_name = None
# this is the score of the questions in evil forest
questions_score = 0
# this variable is for the chances in the carrot mission in healthy forest
global chance
chance = 0
# this is for the 3 answers of the three missions
global answer1
answer1 = None
global answer2
answer2 = None
global answer3
answer3 = None
# number of carrrot opened times in goodness forest orders
global number_of_carrot_opened_times
number_of_carrot_opened_times = 0


def hello_user():
    # This function greet the user asks the user for his input
    # and uses this name in upcoming functions
    global User_name
    # take the user name as input
    User_name = input("Hello! Can you tell us your name:  ")

    while User_name == "" or User_name == " ":
        print("invalid input")
        User_name = input("Hello! Can you tell us your name:  ")

    while True:
        if User_name[-1] == " ":
            User_name = User_name[:-1]

        elif User_name[-1] != " ":
            break

    print_pause(f"Hello {User_name} this an adventure game made by rojeh")
    print_pause("in this game you communicates with the game using the text")
    print_pause("")


def print_pause(text):
    # this is a function to print text with a delay 1 second
    print(text)
    time.sleep(1)


def start():
    # this function starts the game
    if User_name is None:
        hello_user()
    else:
        pass

    kitchen()


def scene(scene, scene2, scene3, scene4, scene5, scene6, choice1, choice2):
    """
    this function manages what is happening to avoid writing alot
    of code in the scene like saying to the user what is happening
    at that time and telling him the choices he can choose
    """
    # here it prints what is happening
    # but it makes sure that what is printed isn't none
    print_pause(f"{User_name} {scene}")

    try:
        sys.stdout.write(scene2)
        time.sleep(1)
    except TypeError:
        pass

    try:
        sys.stdout.write("\n" + scene3)
        time.sleep(1)
    except TypeError:
        pass

    try:
        sys.stdout.write("\n" + scene4)
        time.sleep(1)
    except TypeError:
        pass

    try:
        sys.stdout.write("\n" + scene5)
        time.sleep(1)
    except TypeError:
        pass

    try:
        sys.stdout.write("\n" + scene6)
        time.sleep(1)
    except TypeError:
        pass

    # an empty line that makes the output looks better
    print("")
    # it prints the first choice
    print_pause("Enter 1 " + choice1)
    # here it prints the second choice
    print_pause("Enter 2 " + choice2)
    # and it asks the user for his input
    print_pause("what would you do ?")


def choices_and_input():
    """
    this function handles the input of the user in the choices
    between scenarios and the in the scene itself when it asks
    the user what does he want to do
    """
    while True:
        # this also handles the invalid input from the user
        try:
            # here it make sure that the input is 1 or 2 only
            User_input = int(input("please enter 1,2: "))
            if User_input >= 3 or User_input <= 0:
                print("invalid input")
            else:
                break
        # and here it make sure that the input is integer
        except ValueError:
            print("invalid input")

    return User_input


def score(operation, num, reason):

    """
    this function handles the increasing and the decreasing in score
    and tells you the score
    """
    if operation == "+":
        global total_score
        total_score += num
    else:
        total_score -= num

    print_pause(f"Your Score is: {total_score}" + "\n")

    if total_score <= 0:
        lose(reason)


def lose(reason):
    """
    this funtion tells you that you lost the game
    and tells you why
    """
    print_pause(f"YOU HAVE LOST THE GAME {User_name}")
    print_pause(f"Because {reason} and you died")
    play_again()


def end_game(num, you_win, why, why2, why3, why4):
    """
    this funtion tells you that you that the game
    has ended and the number of ending and tells you why
    """
    if you_win is True:
        print_pause("when you went to mr broccoli he made his medicine")
        print_pause("and took it then he came fresh again he gave you a piece")
        print_pause("of special broccoli when you ate it you found yourself")
        print_pause("in your kitchen again and the simulation ended")
        print_pause(f"Congratulations {User_name} Horrayyyy.")
        print_pause("but wait a minute ")
        print_pause("you were dreaming all that time :)")
        print_pause("when you got up you found a new oven ")
        print_pause("as a gift from your family because of your birthday")
        print_pause("you was very happy and you win congrats")
        print_pause("game end 1 (main)")
        play_again()
    else:
        pass

    try:
        sys.stdout.write(why)
    except TypeError:
        pass

    try:
        sys.stdout.write("\n" + why2)
    except TypeError:
        pass

    try:
        sys.stdout.write("\n" + why3)
    except TypeError:
        pass

    try:
        sys.stdout.write("\n" + why4)
    except TypeError:
        pass

    print_pause(f"the game has ended{User_name} end game {num}")

    if num == 3:
        print_pause("(but your score is very low)")

    play_again()


def play_again():
    """
    this function tells you your score
    and asks you if you want to play again
    if yes it repeats the game
    if no it quits
    """
    global total_score
    total_score = 0

    global questions_score
    questions_score = 0

    global chance
    chance = 0

    global answer1
    answer1 = None
    global answer2
    answer2 = None
    global answer3
    answer3 = None

    global number_of_carrot_opened_times
    number_of_carrot_opened_times = 0

    want_to_play_again = input("Do you want to play again? (y/n)  ")

    while True:
        if want_to_play_again.lower() == "y":
            start()

        elif want_to_play_again.lower() == "n":
            quit()

        else:
            print("invalid input")
            want_to_play_again = input("Do you want to play again? (y/n)  ")


def randoming(list, num_of_random_num):
    """
    this function handles the randomness when you give it a list
    it chooses randomly from it
    """
    randomized_list = []
    randomized_string = None
    index = [1, 2, 3, 4, 5, 6, 7]

    if int(num_of_random_num) > 1:
        random.shuffle(index)
        for i in range(num_of_random_num):
            randomized_list.append(index[i])
        return randomized_list
    else:
        randomized_string = random.choice(list)
        return randomized_string


def kitchen():
    """
    this function handles the start of the first scenario
    with saying what is happening and taking input from the user
    """
    scene("you find your self in old kitchen with old equipment",
          "of your grandma and you love cooking very much ",
          None,
          None,
          None,
          None,
          "to try to make some food with the equipment you have ",
          "to make inventory of the equipment you have ")

    choice_input = choices_and_input()

    if choice_input == 1:
        score("-", 1, "while making the food the oven exploded")

    else:
        score("+", 2, None)

    scene("you found that the oven isn't working and damaged",
          "you opened your phone and searched about ovens",
          "and found a good oven but in a pop up ad with ",
          "special capabillities you found a special oven",
          None,
          None,
          "buy the special oven ",
          "buy a basic new oven ")

    choice_input = choices_and_input()

    if choice_input == 1:
        score("+", 2, None)

    else:
        score("+", 1, None)
        end_game(3,
                 False,
                 "the oven was working and every thing was good",
                 "but what is this boring life",
                 None,
                 None)

    scene("when you turn it on you found a button",
          "that says start simulation. When you pressed the button",
          "it took you to the food world",
          "you found a big world and you discovered that there is two forests",
          "( The evil forest and The goodness forest)",
          None,
          "Enter the goodness and healthy forest",
          "Enter the unhealthy and evil forest")

    choice_input = choices_and_input()

    if choice_input == 1:
        score("+", 2, None)
        goodness_forest()
    else:
        score("+", 2, None)
        evil_forest()


def goodness_forest():
    """
    this function is the for the goodness forest to not repeat
    the code many times
    """
    scene("when you entered the forest you discovered that it is like",
          "the normal forest but healthier. you was very lost but you found",
          "someone that bought the same oven like you but when he knew how",
          "to escape it was too late because you have chance to escape",
          "till evening so he was trapped in it forever he told you that",
          "he would tell you the way to escape",
          "to dont trust him and search for another way to esape",
          "to trust the man and do what he will say to you")

    choice_input = choices_and_input()

    if choice_input == 1:
        score("+", 2, None)

    else:
        score("-", 1, None)
        end_game(2,
                 False,
                 "you went to do what he told you and you came",
                 "near the evening to told him that you did what he said",
                 "but you didn't escape he told you that he lied",
                 "and it wasn't a way to escape so you are stuck forever")

    global mr_goodness
    mr_goodness = randoming(["Mr Broccoli", "Mr WaterMelon", "Mr Mango"], 1)

    print_pause(f"while you was walking in the forest you found")
    print_pause(f"{mr_goodness} he was very old man")
    print_pause("and he told you that if you give him specific somethings")
    print_pause("before evening to make his medicine he would return you home")
    print_pause("")
    bomb = randoming(["cheese", "ketchep", "mayonaize", "mustard"], 1)
    print_pause(f"This area was hit by a {bomb} bomb by the evil forest")
    print_pause("so the fruit and vegetables, water in rivers a lot of them")
    print_pause("became toxic and only a few are not toxic and can be used")

    goodness_forest_orders()


def goodness_forest_orders():
    """
    this function is for the orders of {mr_goodness}
    to you to make his medicine
    it is made to not repeat the code many times
    because its code is repeated many times
    """
    global answer1
    global answer2
    global answer3

    print_pause("choose from three things :")
    print_pause("enter 1 to get the best apple from the trees")
    print_pause("enter 2 to get a good carrot from the two fields of carrots")
    print_pause("enter 3 to get a pure bucket of water from the three rivers")
    print_pause(f"enter 4 : to go to {mr_goodness} and give him the 3 things")

    while True:
        # this also handles the invalid input from the user
        try:
            # here it make sure that the input is 1 or 2 only
            User_input = int(input("please enter 1, 2, 3, 4: "))
            if User_input > 4 or User_input <= 0:
                print("invalid input")
            else:
                break
        # and here it make sure that the input is intger
        except ValueError:
            print("invalid input")

    # this code is for the first order
    if User_input == 1:
        print_pause("You found that there are ten apple trees")
        print_pause("One of them has good apples")
        print_pause("you found on a tree a math equation")
        print_pause("The answer of this equation is the number of the tree")
        print_pause("which have good apples.\nThe equation is :")
        print_pause("( 3X^2 - 4X - 12 ), then X = ?")
        print_pause("while X belongs to natural numbers (positive number)")
        print_pause("Hint : Factorize it")

        while True:
            # make sure that you entered a number as an answer
            try:
                answer1 = int(input("Enter the answer of the equation:  "))
                break

            except ValueError:
                print_pause("invalid input")
                print("please enter a number")

        # if your answer is correct it makes the variable = true
        # if your answer is inorrect it makes the variable = false
        if answer1 == 3:
            answer1 = True

        else:
            answer1 = False

        goodness_forest_orders()

    # this code is for the second order
    elif User_input == 2:
        global number_of_carrot_opened_times
        number_of_carrot_opened_times += 1
        answer2 = carrot()

    # this code is for the third order
    elif User_input == 3:
        print_pause("there are three rivers in this place")
        print_pause("one of them has pure water")
        print_pause("Choose one of them and get from it a bucket of water")

        while True:
            # make sure that you entered a number as an answer
            try:
                answer3 = int(input("Enter the number of the river:  "))
                break

            except ValueError:
                print_pause("invalid input")
                print("please enter a number")

        # if your answer is correct it makes the variable = true
        # if your answer is inorrect it makes the variable = false
        if answer3 == 2:
            answer3 = True

        else:
            answer3 = False

        goodness_forest_orders()

    # this code is for going back to Mr {mr_goodness}
    else:
        print_pause(f"when you went back to {mr_goodness}")
        print_pause("you gave him the three things")
        print_pause("he checked them and told you: ")

        if answer3 is True and answer2 is True and answer1 is True:
            score("+", 5, None)
            end_game(1, True, None, None, None, None)

        if answer1 is not True:
            print_pause("the apple wasn't good go and get other one")

        if answer2 is not True:
            print_pause("the carrot was very bad go and get other one")

        if answer3 is not True:
            print_pause("the water was polluted go and get other one")

        goodness_forest_orders()


def carrot():
    """
    this function is for the second order the carrot
    because it is repeated
    """
    global number_of_carrot_opened_times

    global answer2

    if number_of_carrot_opened_times > 1:
        # here the user chooses one of the carrots
        while True:
            # this also handles the invalid input from the user
            try:
                # here it make sure that the input is from 1 to 10 only
                User_input = int(input("Enter a number from 1 to 10:  "))
                if User_input > 10 or User_input <= 0:
                    print("invalid input")
                else:
                    break
            # and here it make sure that the input is intger
            except ValueError:
                print("invalid input")

        # if the user answers in the first time wrongly
        # it chooses another 4 randomly
        good_carrots = randoming(range(1, 11), 4)

        if User_input in good_carrots:
            answer2 = True
            goodness_forest_orders()

        else:
            answer2 = False
            goodness_forest_orders()

        return answer2

    global chance

    if chance == 1:
        print_pause("Which is the main vitamin in the carrots")

    elif chance == 2:
        print_pause("When you told him that you want a good carrot")
        print_pause("He told you that he would ask you a question")
        print_pause("if you answer it correctly he would tell you which field")
        print_pause("that has good carrots.\nThe question is :")
        print_pause("Which is the main vitamin in the carrots")
    else:
        print_pause("you found that there are two fields of carrots")
        print_pause("in every field there are ten carrots")
        print_pause("one of the fields have four good carrots")
        print_pause("When you went there you found Mr Carrot")
        print_pause("When you told him that you want a good carrot")
        print_pause("He told you that he would ask you a question")
        print_pause("if you answer it correctly he would tell you which field")
        print_pause("that has good carrots.\nThe question is :")
        print_pause("Which is the main vitamin in the carrots")

    while True:
        # make sure that you entered a letter as an answer
        field_answer = input("Enter the answer : Vitamin ")
        try:
            field_answer = int(field_answer)
            print("invalid input")
            print("please enter a letter")

        except ValueError:
            if len(field_answer) == 1:
                field_answer = field_answer.upper()
                chance += 1
                break

            else:
                print("invalid input")
                print("please enter a letter")

    # if the answer is correct it will tell him which field
    # that has good carrots

    if field_answer == "A":
        print_pause("your answer is correct Mr Carrot told you that")
        if chance == 1:
            score("+", 2, None)

        elif chance == 2:
            score("+", 1, None)

        print_pause("the field that have good carrots is the second field")
        print_pause("when you went there you found the ten carrots")
        print_pause("4 of them are good")
        print_pause("Choose one of the carrots")

        # here the user chooses one of the carrots
        while True:
            # this also handles the invalid input from the user
            try:
                # here it make sure that the input is from 1 to 10 only
                User_input = int(input("Enter a number from 1 to 10:  "))
                if User_input > 10 or User_input <= 0:
                    print("invalid input")
                else:
                    break
            # and here it make sure that the input is intger
            except ValueError:
                print("invalid input")

        good_carrots = [2, 5, 9, 7]

        if User_input in good_carrots:
            answer2 = True
            goodness_forest_orders()

        else:
            answer2 = False
            goodness_forest_orders()

        return answer2

    else:
        if chance == 1:
            print_pause("your answer is incorrect")
            print_pause("Mr Carrot gave you another chance but")
            print_pause("it is the last chance if you dont answer correctly")
            print_pause("he will kick you out")
            carrot()

        elif chance == 2:
            print_pause("your answer is incorrect")
            print_pause("Mr Carrot kicked you out of the field")
            print_pause("but after a bit of time you found that")
            print_pause("Mr Carrot left and his brother came")
            carrot()
        elif chance == 3:
            print_pause("your answer is incorrect")
            print_pause("Mr carrot's brother was very angry")
            print_pause("because you couldn't answer")
            print_pause("so he called his friends the burger boys")
            print_pause("and they killed you")
            print_pause("YOU LOST")
            print_pause("Do you want to start from the checkpoint")
            print_pause("or from the beginning")

            chance = 0

            choices_input = choices_and_input()

            if choices_input == 1:
                goodness_forest()
            else:
                kitchen()


def evil_forest():
    """
    this function is the for the evil forest to not repeat
    the code many times
    """

    # these variables are for rivers and the trees of the evil forest
    river = randoming(["pepsi", "sprite", "red bull", "mirinda", "sapthis"], 1)
    tree = randoming(["hamburger", "hotdog", "french fries", "chocolat"], 1)

    scene(
        "When you entered the forest you found strange things like",
        f"river of {river} and {tree} tree you was very amazed ",
        "and you have two choices",
        None,
        None,
        None,
        f"to take from the {tree} tree and from the other things",
        "to don't take or eat from the rivers and the trees"
    )

    choices_input = choices_and_input()

    if choices_input == 1:
        score("-", 1, None)
        time.sleep(3)
        print_pause("After a few minutes")
        print_pause("when you took from them")
        print_pause(f"a big {tree} boss came and was very angry")
        print_pause("because you took from them and he wanted to eat you")
        print_pause("so you ran and he followed you")

        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("....")
        time.sleep(1)

        if randoming([1, 2], 1) == 1:
            print_pause("while you were running from the boss")
            print_pause("you fell into his trap")
            print_pause("and the boss caught you")
            lose("he ate you")
        else:
            print_pause(f"you successfully escaped from the {tree} boss")
            print_pause("without falling into his traps")
            print_pause("and while you were running you found a small house")
            print_pause("while you were looking at it ")
            the_kidnapping_evil_forest()

    else:
        print_pause("so you continued walking to find anything in this forest")
        print_pause("while you were walking you found a small house")
        print_pause("while you were looking at it")
        time.sleep(1)
        the_kidnapping_evil_forest()


def the_kidnapping_evil_forest():
    """
    this function handles the part which the user is kidnapped in it
    """
    print_pause("you were kidnapped!!")
    print_pause("by an old wise man that told you that")
    print_pause("he would help you to escape but he will ask you 7 questions!")
    print_pause("you must at least answer 5 or ")
    print_pause("he would kill you")
    print_pause("...")
    time.sleep(2)

    # here it chooses the 7 questions with randomized organization

    index = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(index)

    # the seventh question is in an independent variable because it is writen
    # normaly the line of the code will be too long
    question7 = "what is the fast food chain serves the Whopper sandwich ?"

    for i in range(7):

        if index[i] == 1:
            question("what is the most famous food in Egypt ?",
                     "kochari",
                     "kabsa",
                     "pizza",
                     1)

        elif index[i] == 2:
            question("What is the most eaten food in the world ?",
                     "Rice",
                     "sushi",
                     "pizza",
                     1)

        elif index[i] == 3:
            question("The KFC secret recipe uses how many herbs and spices ?",
                     "15",
                     "11",
                     "5",
                     2)

        elif index[i] == 4:
            question("When did the first McDonald's store open ?",
                     "2010",
                     "1920",
                     "1940",
                     3)

        elif index[i] == 5:
            question("Does Salt Expire ?",
                     "that salt does not expire",
                     "that salt expire",
                     "that it is depending on the temperature it is placed in",
                     1)

        elif index[i] == 6:
            question("Which food can never expire ?",
                     "Meat",
                     "Vinegar",
                     "bread",
                     2)

        else:
            question(question7,
                     "KFC",
                     "Buffalo burger",
                     "Burger king",
                     3)

    if questions_score == 7:
        # here when you answers all the questions right it gives you
        # a big score increase
        score("+", 6, None)
        print_pause("Congrats")
        print_pause("You answered all the questions correctly")
        print_pause("The old man cast a spell")
        print_pause("and you found yourself in the goodness forest")
        print_pause("......")
        time.sleep(2)
        goodness_forest()

    elif questions_score >= 5:
        score("+", 3, None)
        print_pause("Congrats")
        print_pause(f"you answered {questions_score} of the questions right ")
        print_pause("The old man cast a spell")
        print_pause("and you found yourself in the goodness forest")
        print_pause("......")
        goodness_forest()

    else:
        score("-", 2, None)
        print_pause("Unfortunately")
        print_pause("you couldn't answer the questions correctly")
        print(f"you only answered {questions_score} of the questions right")
        lose("The wise man called his bad people and killed you")


def question(question, choice1, choice2, choice3, correct_answer):
    # here it prints the question itself
    print(question)
    # an empty line that makes the output looks better
    print("")
    # it prints the first choice
    print("Enter 1 to choose " + choice1)
    # here it prints the second choice
    print("Enter 2 to choose " + choice2)
    # here it prints the third choice
    print("Enter 3 to choose " + choice3)

    # and it asks the user for his input
    while True:
        # this also handles the invalid input from the user
        try:
            # here it make sure that the input is 1 or 2 only
            User_input = int(input("please enter 1, 2, 3: "))
            if User_input >= 4 or User_input <= 0:
                print("invalid input")
            else:
                break
        # and here it make sure that the input is integer
        except ValueError:
            print("invalid input")

    if User_input == correct_answer:
        score("+", 2, None)
        global questions_score
        questions_score += 1


# start the game
start()
