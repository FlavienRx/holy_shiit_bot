def average_size_by_char(sentence):

    # Set the big letters of the font
    big_chars = ['m', 'u', 'c', 'w', 'v']
    # Set the little letters of the font
    little_chars = ['l', 'i', 'j']
    # Initialize the weight
    weight = 0

    # Compute the sentence's weight
    for big_char in big_chars:
        weight = weight + sentence.count(big_char)

    for little_char in little_chars:
        weight = weight - sentence.count(little_char)

    # fix an average size by char
    if weight < -2:
        average_size = 13
    elif weight < 0:
        average_size = 15
    elif weight < 2:
        average_size = 17
    elif weight < 4:
        average_size = 18
    else:
        average_size = 20

    return average_size