#https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    x = list(string)
    x[position] = character
    string = ''.join(x)
    return string