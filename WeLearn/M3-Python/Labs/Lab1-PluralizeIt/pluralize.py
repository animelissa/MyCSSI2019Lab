# word = 'computerz'
# print(word[:5])
# print(word[:-1])
# print(word[4:])
# print(word[-3:])


def plural(number, word):
    if number > 1:
        if word[-3:] == "ife":
            return number, word[:-3] + "ives"
        elif(word[-2:]) == "sh" or (word[-2:]) == "ch":
            return number, word + "es"
        elif(word[-2:]) == "us":
            return number, word[:-2] + "i"
        elif(word[-2:]) == "ay" or (word[-2:]) == "oy" or (word[-2:]) == "ey" or (word[-2:]) == "uy":
            return number, word + "s"
        elif(word[-1:]) == "y":
            return number, word[:-1] + "ies"
        else:
            return number, word+'s'
    else:
            print number, word

name = str(raw_input('Enter a word: '))
number = int(raw_input('Enter a number: '))

plural(number, name)
