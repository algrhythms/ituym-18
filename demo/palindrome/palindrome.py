"""
    Created by mbenlioglu on 1/19/2018
"""


def is_palindrome(text):
    print 'YES' if text == text[::-1] else 'NO'


if __name__ == '__main__':
    inp = raw_input()
    is_palindrome(inp)
