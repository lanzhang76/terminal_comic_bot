import re
import random
import pandas as pd
import os

# the flow when someone tries to create a new model for generation
# 1. preparing the text
# 2. train and generate


def clear():
    os.system('clear')


def addToCorpus(csv_file, name, context, selections):
    file = pd.read_csv(csv_file)
    words = []
    if selections.get(name) is not None:
        context[name] = [file.scripts[i] for i in selections.get(name)]
        print(f"{name} is now part of your comic voice")
        corpus = ""
        for i in context:
            for e in context[i]:
                corpus += e
        corpus = corpus.replace('\', \'', ' ').replace(
            '\']', '').replace('[\'', '').replace('xa0', ' ').replace('\\', '')
        words = corpus.split(" ")
    else:
        print("your selection is incorrect. Try again")
    return words


def delFromCorpus(context, name):
    try:
        context_dict.pop(name)
        print(f"{name} is deleted from the dictionary")
    except:
        print(f"sorry, {name} is not in the dictionary. It cannot be deleted.")
        print(f"{[i for i in context]} are in the dictionary.")


# MARKOV FUNCTION BELOW:

def markovCount(word_list, num):
    markov_dict = {}
    for word in range(len(word_list)-num):
        gram = tuple(word_list[word:word+num])
        next_follow = word_list[word+num]
        if gram not in markov_dict:
            markov_dict[gram] = []
        markov_dict[gram].append(next_follow)
    return markov_dict


def clamp(min_val, value, max_val):
    num = max(min_val, min(value, max_val))
    return num


def nextWord_anyInput(sentence, words):
    sentence = sentence.replace("'", "’")
    og_ngram = markovCount(words, len(sentence.split()))
    key_words = tuple(sentence.split())
    next_word_list = []
    count = 1
    while og_ngram.get(key_words) is None:
        new_pairs = markovCount(words, len(sentence.split()[count:]))
        next_word_list = new_pairs.get(key_words[count:])
        if count > clamp(0, count, len(sentence.split())-2):
            break
        else:
            count += 1
    else:
        next_word_list = og_ngram.get(key_words)
    return next_word_list

# this generates until it reaches the end of a sentence


def generateTillEnd(current_sentence, li):
    sen = current_sentence
    next_word = ''
    word_list = li
    while (re.findall(r"[.?!][]\"')}]?", sen) == []) is True:
        if nextWord_anyInput(sen, word_list) == None:
            print("Sorry, we don't have related content of your input")
            sen = sen + '.'
            break

        elif len(nextWord_anyInput(sen, word_list)) == 0:
            next_word = '.'
            sen += "."
        else:
            next_list = nextWord_anyInput(sen, word_list)
            next_word = next_list[int(random.randrange(len(next_list)))]
            sen = sen + " " + next_word

    return sen
