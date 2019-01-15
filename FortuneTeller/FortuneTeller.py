
print("Think of a yes or no question.")

color = input("Now enter a color; Red, Green, Blue, or Yellow: ")

number = int(input("Now enter a number between 1 and 4: "))

red_answers = ["Yes", "No", "Maybe", "I don't think so"]
green_answers = ["In this economy??", "Not a chance!", "Yeah, sure", "If you believe in yourself, yes", ]
blue_answers = ["Whaaaat?  No way!", "I guess so...", "Not now, but ask later", "Ask your dad"]
yellow_answers = ["Ummmmm... Ok", "If I had to say yes I would.  But I don't, so no", "Heck yeah!!",
                  "Hmmm...  That's an interesting question that I don't have an answer for.  Sorry!"]

if color.lower() == "red":
    answer = red_answers[number - 1]
elif color.lower() == "green":
    answer = green_answers[number - 1]
elif color.lower() == "blue":
    answer = blue_answers[number - 1]
elif color.lower() == "yellow":
    answer = yellow_answers[number - 1]

print("The answer to your question is:", answer)