def mad_libs_generator():
    story = """
    Once upon a time, there was a {adjective} {noun} who loved to {verb} in the {place}.
    One day, the {noun} found a {adjective} {noun} and decided to {verb} it all day long.
    The {noun} was so happy that it {verb}ed with joy.
    """

    print("Welcome to Mad Libs Generator!")
    print("Please provide the following words:\n")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    mad_libs_story = story.format(adjective=adjective, noun=noun, verb=verb, place=place)

    print("\nHere's your Mad Libs story:\n")
    print(mad_libs_story)

if __name__ == "__main__":
    mad_libs_generator()
