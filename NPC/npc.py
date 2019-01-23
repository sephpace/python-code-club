

"""
--- Dialog Options ---

Names follow patterns.  For example, option_412 is called by option_41 which is called by option_4 which is one of the
first set of options.
"""


def option_1():
    print("I will tell you how to find the grail- but only if you answer me this riddle.  Will you hear my riddle?")


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
                return selection
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid option: Must be a number between 1 and {len(option_list)}")


"""
--- Start the Conversation ---
Start out with some sort of introction on how our conversation with the NPC starts.
"""

print("Greetings traveler.  My name is Bartamaeus.  Wht do you seek?")

answer = get_answer(["I seek the wisdom.", "I seek the holy grail!", "I just want a sandwich...",
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