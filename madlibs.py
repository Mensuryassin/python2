

def mad_libs():
    print("Welcome to the Mad Libs Game1\n")

    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    noun2 = input("Enter another noun: ")
    verb1 = input("enter verb: ")
    adjective2 = input("Enter another adjective: ")
    place = input("Enter a place: ")
    plural_noun = input("Enter a plural noun: ")
    emotion = input("Enter an emotion: ")
    adverb = input("Enter an adverb: ")


    story = f"""
    Once upon a time, there was a {noun1} who was very {adjective1}. Every day, it went to the {place} with its best friend, 
    a {adjective2} {noun2}. Together, they would {verb1} and have the best time.

    One day, while they were at the {place}, they encountered a group of {plural_noun} who were feeling very {emotion}. 
    The {noun1} decided to help them by {adverb} teaching them how to {verb1}, and from that day on, they were all friends.

    The end.
    """

    # Display the final story with user inputs
    print("\nHere is your Mad Libs story:")
    print(story)

mad_libs()