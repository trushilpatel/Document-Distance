from nltk.stem import PorterStemmer
from math import pi


def transformData(file):
    sentences = sentenceTokenize(file)
    wordTokenize(sentences)
    # Here we are returning sentences because it's directly
    # updated in wordTokenize function
    return sentences


def removeSquareBracket(sentence):
    # input single sentences
    s = sentence
    squre_bracket_index = list()  # list of bracket index
    for i in range(len(s)):
        if s[i] == "[" or s[i] == ']':
            squre_bracket_index.append(i)

    i = int(len(squre_bracket_index)) - 1

    while i >= 0:
        first = squre_bracket_index.pop()
        i = i - 1
        sencond = squre_bracket_index.pop()
        i = i - 1
        s = s[0:sencond] + s[first + 1:]

    return s


def sentenceTokenize(file):
    openFile = open(file, 'rt')
    sentences = openFile.read().split(".")
    resultSentences = list()

    for i in sentences:
        resultSentences.append(removeSquareBracket(i))

    return resultSentences


def wordTokenize(sentences):
    for i in range(len(sentences)):
        sentences[i] = sentences[i].split()
    # here we are directly updating sentences which updates original
    # sentences in calling function


def stemming(sentences):
    ps = PorterStemmer()

    word_set = list()
    for i in sentences:
        word_set.extend(i)

    for i in range(len(word_set)):
        word_set[i] = ps.stem(word_set[i])

    return word_set


def squareVector(vec):
    temp = 0
    for i in range(len(vec)):
        temp += vec[i] ** 2
    return temp




def cosineDistance(first, second):
    # first and second two vectors as an input
    distance = 0
    first_2 = squareVector(first)
    second_2 = squareVector(second)

    for i in range(len(first)):
        distance += first[i] * second[i]

    return distance / ((first_2 ** 0.5) * (second_2 ** 0.5))


def euclideanDistance(first, second):
    # first and second two vectors as an input
    distance = 0

    for i in range(len(first)):
        distance += (first[i] - second[i]) ** 2

    # square root of distance
    return distance ** 0.5


def radianToDegree(radian):
    return radian * (180 / pi)
