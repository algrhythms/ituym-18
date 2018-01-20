"""
    Created by mbenlioglu on 1/20/2018
"""


def get_score(str1, str2):
    return 0


def get_max_concat(words):
    scores = [[0 for _ in xrange(len(words))] for _ in xrange(len(words))]

    # set scores
    for j in xrange(len(words)):
        for k in xrange(j + 1, len(words)):
            scores[j][k] = get_score(words[j], words[k])

    # get max score
    max_score = 0


if __name__ == '__main__':
    loop_cnt = int(raw_input())
    strings = []
    for i in xrange(loop_cnt):
        strings.append(raw_input())
    strings.sort()
    get_max_concat(strings)
