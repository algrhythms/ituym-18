"""
    Created by mbenlioglu on 1/20/2018
"""


def get_score(str1, str2):
    result = 0
    len1, len2 = len(str1), len(str2)
    i = 0 if len1 <= len2 else len1-len2
    while i < len1:
        j, temp_count = 0, 0
        if str1[i] == str2[j]:
            while i < len1 and j < len2 and str1[i] == str2[j]:
                temp_count += 1
                i += 1
                j += 1
            if temp_count > result:
                result = temp_count
        else:
            i += 1
    return result


def get_max_concat(words):
    scores = [[0 for _ in xrange(len(words))] for _ in xrange(len(words))]

    # set scores
    for j in xrange(len(words)):
        for k in xrange(j + 1, len(words)):
            scores[j][k] = get_score(words[j], words[k])

    # get max score
    j, k = 0, 0
    max_score = 0
    for j in xrange(len(words)):
        for k in xrange(j + 1, len(words) - 1):
            scores[j + 1][k + 1] += scores[j][k]
        if scores[j][k + 1] > max_score:
            max_score = scores[j][k + 1]
    return max_score


if __name__ == '__main__':
    loop_cnt = int(raw_input())
    strings = []
    for _ in xrange(loop_cnt):
        strings.append(raw_input())
    strings.sort()
    print get_max_concat(strings)
