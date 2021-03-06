'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # record the count
    count = 0

    # break case
    if len(word) < 2:
        return 0
    else:
        if word[0] == 't' and word[1] == 'h':
            count = count + 1
    return count + count_th(word[1:])
