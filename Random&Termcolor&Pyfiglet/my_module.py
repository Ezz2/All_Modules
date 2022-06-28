# By Ezz

def sayHello(name):
    return f"Hello {name}"

def sayHowAreYou(name):

    return f"How Are You {name}"

def cleanword(word):

    if len(word) == 1:

        return word

    if word[0] == word[1]:

        return cleanword(word[1:])

    return word[0] + cleanword(word[1:])
