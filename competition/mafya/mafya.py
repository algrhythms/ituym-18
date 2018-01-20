"""
    Created by mbenlioglu on 1/20/2018
"""


def select(num_list):
    left, right = 0, len(num_list) - 1
    while right - left + 1 > 2:
        is_popped = False
        for i in xrange(0, len(num_list)/2):
            if num_list[i] == num_list[-(i+1)]:
                continue
            is_popped = True
            if num_list[i] < num_list[-(i+1)]:
                left += 1
            else:
                right -= 1

        if not is_popped:
            return num_list[len(num_list) / 2]

        for i in xrange(0, len(num_list)/2):
            if num_list[i] == num_list[-(i+1)]:
                continue
            if num_list[i] > num_list[-(i+1)]:
                left += 1
            else:
                right -= 1
    return num_list[left] if num_list[left] > num_list[right] else num_list[right]


if __name__ == '__main__':
    n = int(raw_input())
    nums = (int(s) for s in raw_input().split())
    nums = tuple(nums)
    print select(nums)
