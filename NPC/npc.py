

"""
--- Dialog Options ---

Names follow patterns.  For example, option_412 is called by option_41 which is called by option_4 which is one of the
first set of options.
"""

# -- Option tree 1 --



def option_1():
    print("I will tell you how to find the grail- but only if you answer me this riddle.  Will you hear my riddle?\n")
    answer = get_answer(["Yes", "No"])
    if answer == 1:
        option_11()
    else:
        option_12()


def option_11():
    print("Here is the riddle: White is my castle, but doors have I none.  My treasure is hidden between not four "
          "walls... but one.  What am I?")
    answer = get_answer(["A white rock!", "An egg!", "A castle without doors and only one wall.", "That riddle SUCKS!"])
    if answer == 1:
        option_111()
    elif answer == 2:
        option_112()
    elif answer == 3:
        option_113()
    else:
        option_114()


def option_111():
    print("That is incorrect.  I will not tell you the location of the grail!\n")


def option_112():
    print("That is correct!\n  *Bartamaeus pulls something out of his pocket and hands it to you.*\n  The grail was "
          "in my back pocket the whole time!\n  Since you answered my riddle correctly, I will give it to you!\n")
    print("Congratulations on finishing your quest!")


def option_113():
    print("I don't think you understand how riddles work...  Let's try that again!\n")
    option_11()


def option_114():
    print("If you do not answer my riddle now you will never find the grail!\n Will you answer it or not!?\n")
    answer = get_answer(["Fine, I guess...", "No way, LOSER!"])
    if answer == 1:
        option_11()
    else:
        print("*Bartamaeus becomes enraged, conjures up a spell of some sort and fires it at you.*\n"
              "*You black out and when you wake up, you have turned into a frog.*\n"
              "Ribbit!")

def option_12():
    print("Very well.  I wish you good fortune on your quest.")


"""
--- Other functions ---
"""


def get_answer(option_list):
    """Returns the user's answer choice to the NPC's question/statement as an integer"""
    # Print the options
    print("Options:")
    for i in range(len(option_list)):
        print(f"{i + 1}. {option_list[i]}")

    # Return the selected option from the user
    while True:
        try:
            selection = int(input(">>>"))
            if 1 <= selection <= len(option_list):
                print()
                return selection
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid option: Must be a number between 1 and {len(option_list)}")


"""
--- Start the Conversation ---
Start out with some sort of introction on how our conversation with the NPC starts.
"""

print("Greetings traveler.  My name is Bartamaeus.  \n\nWhat do you seek?\n")

answer = get_answer(["I seek the holy grail!", "I seek the wisdom.", "I just want a sandwich...",
                     "I want all of your money!", ])

if answer == 1:
    option_1()
elif answer == 2:
    # option_2()
    pass
elif answer == 3:
    # option_3()
    pass
else:
    # option_4()
    pass
