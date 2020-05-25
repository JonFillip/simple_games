import random

"""
Magic 8 ball is a small ball that when shaken by a user after asking a question
it returns an answer ranging from positive certainty or very doubtful.
"""


def magic8ball(answer_number):
    """Gets a random number and returns an answer"""
    if answer_number == 1:
        return "That is affirmative."
    elif answer_number == 2:
        return "It is what it is"
    elif answer_number == 3:
        return "Sure!"
    elif answer_number == 4:
        return "Its hazy in here. Try again!"
    elif answer_number == 5:
        return "Not sure right now. Ask me later."
    elif answer_number == 6:
        return "Proceed with caution"
    elif answer_number == 7:
        return "This doesn't look good"
    elif answer_number == 8:
        return "Definitely NO!"


guessed_number = random.randint(1, 9)
fortune = magic8ball(guessed_number)
print(fortune)
