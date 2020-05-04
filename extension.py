"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""
"""
This program help to practices addition, subtraction, and multiplication.
First, the user will ask to choose what type he would start with.
Then the three problems will be two and the user will ask to choose between them.
After the second problem, the user will be asked if he wants to continue with the third problem or no.  
"""

import random

MIN_NUM = 1
MAX_NUM = 150
MIN_NUM1 = 1
MAX_NUM1 = 12


def main():
    # description of the program
    print("\n")
    print("                       Instruction \n")
    print("You have three main problems addition, subtraction, multiplication. ")
    print("You can choose what type you want to start.")
    print("After you choose the problem to pass it you should has gotten 3 problems correct in a row \n")
    print("                     So, let's start\n")

    # choose_your_problem: the user can choose the type of problem to start with
    choose_your_problem = str(input("What type of problem  you want to start with? type('add' or 'sub' or 'times'): "))

    # if the user types something error, This will warn it.Then ask him to type the right word.
    while choose_your_problem != 'add' and choose_your_problem != 'sub' and choose_your_problem != 'times':
        correction = input("Please enter 'add' or 'sub' or 'times: ")
        choose_your_problem = correction

    # This is the main  if condition that let the user to choose the problem he wants to start with.
    if choose_your_problem == "add":
        addition()
        print("\n")
        print("Now you can choose your second problem \n")

        # It's time to let the user to choose the second problem
        choose_your_problem = str(input("To choose please, type('sub', 'times'): "))

        # if the user types something error, This will warn it.Then ask him to type the right word.
        while choose_your_problem != 'sub' and choose_your_problem != 'times':
            correction = input("Please enter 'add' or 'sub' or 'times: ")
            choose_your_problem = correction

        # This nested if  let the user to choose the problem he wants to start as a second problem.
        if choose_your_problem == 'sub':
            subtraction()
            print("")
            print("Great job!")
            print("The last problem is multiplication, Are you reedy? ")

            reedy = input("Type 'yes' if you are reedy and 'no' if you aren't: ")

            # if the user types something error, This will warn it.Then ask him to type the right word.
            while reedy != 'yes' and reedy != 'no':
                print("")
                correction = input("Please enter 'yes' if you are reedy and 'no' if you aren't: ")
                reedy = correction
            # The purpose of these conditions to know if the user wants to continue and finish the last problem.
            if reedy == 'yes':
                print("")
                multiplication()
            elif reedy == 'no':
                print("Do you want to stop?")
                stop = input("Type 'yes' if you want to stop and 'no' if you want to continue: ")

                # if the user types something error, This will warn it.Then ask him to type the right word.
                while stop != 'yes' and stop != 'no':
                    correction = input("Please enter 'yes' if you want to stop and 'no' if you want to continue: ")
                    stop = correction

                # The purpose of these conditions to know if the user wants to stop or no
                if stop == 'yes':
                    print("Great, you did nice jop! \n\n")
                elif stop == 'no':
                    print("Ok, lets's start practices multiplication")
                    multiplication()

        # This nested if  let the user to choose the problem he wants to start as a second problem.
        elif choose_your_problem == 'times':
            print("")
            multiplication()
            print("")
            print("Great job!")
            print("The last problem is subtraction, Are you reedy? ")
            reedy = input("Type 'yes' if you are reedy and 'no' if you aren't: ")

            # if the user types something error, This will warn it.Then ask him to type the right word.
            while reedy != 'yes' and reedy != 'no':
                correction = input("Please enter 'yes' if you are reedy and 'no' if you aren't: ")
                reedy = correction

            if reedy == 'yes':
                print("")
                subtraction()
                print("")
            elif reedy == 'no':
                print("Do you want to stop?")
                stop = input("Type 'yes' if you want to stop and 'no' if you want to continue: ")

                # if the user types something error, This will warn it.Then ask him to type the right word.
                while stop != 'yes' and stop != 'no':
                    correction = input("Please enter 'yes' if you want to stop and 'no' if you want to continue: ")
                    stop = correction

                if stop == 'yes':
                    print("Great, you did nice jop! \n\n")
                elif stop == 'no':
                    print("Ok, lets's start practices subtraction")
                    print("")
                    subtraction()
                    print("")

    elif choose_your_problem == "sub":
        subtraction()
        print("\n")
        print("Now you can choose your second problem \n")

        # It's time to let the user to choose the second problem
        choose_your_problem = str(input("To choose please, type('add', 'times'): "))

        # if the user types something error, This will warn it.Then ask him to type the right word.
        while choose_your_problem != 'add' and choose_your_problem != 'times':
            correction = input("Please enter 'add' or 'sub' or 'times: ")
            choose_your_problem = correction

        # This nested 'if' let the user to choose the problem he wants to start as a second problem.
        if choose_your_problem == 'add':
            addition()
            print("Great job!")
            print("The last problem is multiplication, Are you ready? ")
            reedy = input("Type 'yes' if you are reedy and 'no' if you aren't: ")

            # if the user types something error, This will warn it.Then ask him to type the right word.
            while reedy != 'yes' and reedy != 'no':
                correction = input("Please enter 'yes' if you are reedy and 'no' if you aren't: ")
                reedy = correction

            # The purpose of these conditions to know if the user wants to continue and finish the last problem
            if reedy == 'yes':
                print("")
                multiplication()
            elif reedy == 'no':
                print("Do you want to stop?")
                stop = input("Type 'yes' if you want to stop and 'no' if you want to continue:  ")

                # if the user types something error, This will warn it.Then ask him to type the right word.
                while stop != 'yes' and stop != 'no':
                    correction = input("Please enter 'yes' if you want to stop and 'no' if you want to continue: ")
                    stop = correction

                # the purpose of these conditions to know if the user wants to stop or no
                if stop == 'yes':
                    print("Great, you did nice jop!\n \n")
                elif stop == 'no':
                    print("Ok, lets's start practices multiplication")
                    multiplication()
        elif choose_your_problem == 'times':
            print("")
            multiplication()
            print("")
            print("Great job!")
            print("The last problem is addition, Are you reedy? ")
            reedy = input("Type 'yes' if you are reedy and 'no' if you aren't: ")

            # if the user types something error, This will warn it.Then ask him to type the right word.
            while reedy != 'yes' and reedy != 'no':
                correction = input("Please enter 'yes' if you are reedy and 'no' if you aren't: ")
                reedy = correction

            if reedy == 'yes':
                print("")
                addition()
                print("")
            elif reedy == 'no':
                print("Do you want to stop?")
                stop = input("Type 'yes' if you want to stop and 'no' if you want to continue: ")

                # if the user types something error, This will warn it.Then ask him to type the right word.
                while stop != 'yes' and stop != 'no':
                    correction = input("Please enter 'yes' if you want to stop and 'no' if you want to continue: ")
                    stop = correction

                if stop == 'yes':
                    print("Great, you did nice jop! \n\n")
                elif stop == 'no':
                    print("Ok, lets's start practices multiplication")
                    print("")
                    addition()
                    print("")

    elif choose_your_problem == "times":
        multiplication()
        print("\n")
        print("Now you can choose your second problem \n")

        # It's time to let the user to choose the second problem
        choose_your_problem = str(input("To choose please, type('sub', 'add'): "))

        # if the user types something error, This will warn it.Then ask him to type the right word.
        while choose_your_problem != 'add' and choose_your_problem != 'sub':
            correction = input("Please enter 'add' or 'sub': ")
            choose_your_problem = correction

        # This nested if  let the user to choose the problem he wants to start as a second problem.
        if choose_your_problem == 'sub':
            subtraction()
            print("")
            print("Great job!")
            print("The last problem is addition, Are you ready")
            reedy = input("Type 'yes' if you are reedy and 'no' if you aren't: ")

            # if the user types something error, This will warn it.Then ask him to type the right word.
            while reedy != 'yes' and reedy != 'no':
                correction = input("Please enter 'yes' if you are reedy and 'no' if you aren't: ")
                reedy = correction
            if reedy == 'yes':
                addition()
            elif reedy == 'no':
                print("Do you want to stop?")
                stop = input("Type 'yes'  if you want to stop and 'no' if you want to continue: ")

                # if the user types something error, This will warn it.Then ask him to type the right word.
                while stop != 'yes' and stop != 'no':
                    correction = input("Please enter 'yes' if you want to stop and 'no' if you want to continue: ")
                    stop = correction

                if stop == 'yes':
                    print("Great, you did nice jop! \n\n")
                elif stop == 'no':
                    print("Ok, lets's start practices multiplication")
                    addition()

        elif choose_your_problem == 'add':
            print("")
            addition()
            print("Great job!")
            print("The last problem is subtraction, Are you reedy? ")
            reedy = input("Type 'yes' if you are reedy and 'no' if you aren't: ")

            # if the user types something error, This will warn it.Then ask him to type the right word.
            while reedy != 'yes' and reedy != 'no':
                correction = input("Please enter 'yes' if you are reedy and 'no' if you aren't: ")
                reedy = correction

            if reedy == 'yes':
                print("")
                subtraction()
                print("")
            elif reedy == 'no':
                print("Do you want to stop?")
                stop = input("Type 'yes'  if you want to stop and 'no' if you want to continue: ")

                # if the user types something error, This will warn it.Then ask him to type the right word.
                while stop != 'yes' and stop != 'no':
                    correction = input("Please enter 'yes' if you want to stop and 'no' if you want to continue: ")
                    stop = correction

                if stop == 'yes':
                    print("Great, you did nice jop! \n\n")
                elif stop == 'no':
                    print("Ok, lets's start practices multiplication")
                    print("")
                    subtraction()
                    print("")

    print("--------------------------------------------------------------------------------------------------\n")
    print("                        Congratulation! Now your are perfect.\n")
    print("--------------------------------------------------------------------------------------------------\n")

"""
def ready(problem):
    reedy = input("Type 'yes' if you are reedy and 'no' if you aren't: ")

    # if the user types something error, This will warn it.Then ask him to type the right word.
    while reedy != 'yes' and reedy != 'no':
        print("")
        correction = input("Please enter 'yes' if you are reedy and 'no' if you aren't: ")
        reedy = correction
    # The purpose of these conditions to know if the user wants to continue and finish the last problem.
    if reedy == 'yes':
        print("")
        prob = problem
    elif reedy == 'no':
        print("Do you want to stop?")
        stop = input("Type 'yes' if you want to stop and 'no' if you want to continue: ")

        # if the user types something error, This will warn it.Then ask him to type the right word.
        while stop != 'yes' and stop != 'no':
            correction = input("Please enter 'yes' if you want to stop and 'no' if you want to continue: ")
            stop = correction

        # The purpose of these conditions to know if the user wants to stop or no
        if stop == 'yes':
            print("Great, you did nice jop! \n\n")
        elif stop == 'no':
            print("Ok, lets's start practices")
            prob = problem
"""

# This function made addition problem
def addition():
    correct_in_a_row = 1
    while correct_in_a_row <= 3:
        num1 = random.randint(MIN_NUM, MAX_NUM)
        num2 = random.randint(MIN_NUM, MAX_NUM)
        total = num1 + num2
        print("What is " + str(num1) + " + " + str(num2) + ": ")
        ans = int(input("Your answer: "))
        if total == ans:
            print("Correct! You've gotten " + str(correct_in_a_row) + " correct in a row.")
            correct_in_a_row += 1
        else:
            print("Incorrect. The expected answer is " + str(total))
            correct_in_a_row = 1
    print("Congratulations! You mastered addition.")


# This function made subtraction problem
def subtraction():
    correct_in_a_row = 1
    while correct_in_a_row <= 3:
        num1 = random.randint(MIN_NUM, MAX_NUM)
        num2 = random.randint(MIN_NUM, MAX_NUM)
        total = num1 - num2
        print("What is " + str(num1) + " - " + str(num2) + ": ")
        ans = int(input("Your answer: "))
        if total == ans:
            print("Correct! You've gotten " + str(correct_in_a_row) + " correct in a row.")
            correct_in_a_row += 1
        else:
            print("Incorrect. The expected answer is " + str(total))
            correct_in_a_row = 1
    print("Congratulations! You mastered subtraction.")


# This function made multiplication problem
def multiplication():
    num = int(input("Type what number you want in multiplication table: "))
    correct_in_a_row = 1
    while correct_in_a_row <= 3:
        num1 = random.randint(MIN_NUM1, MAX_NUM1)
        total = num * num1
        print("What is " + str(num) + " * " + str(num1) + ": ")
        ans = int(input("Your answer: "))
        if total == ans:
            print("Correct! You've gotten " + str(correct_in_a_row) + " correct in a row.")
            correct_in_a_row += 1
        else:
            print("Incorrect. The expected answer is " + str(total))
            correct_in_a_row = 1
    print("Congratulations! You mastered multiplication.\n")
    print("Do you need more table times practices\n")
    more_times = input("If you need so type 'yes', and if not type 'no': ")
    if more_times == 'yes':
        multiplication()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
