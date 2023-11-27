def two_sum(list, target):
    prevMap = {}

    for i, n in enumerate(list):
        diff = target - n
        if diff in prevMap:
            return [prevMap[n], i]
        prevMap[n] = i
    return


# my_list = [2,7,11,15]
# target = 9
# print(two_sum(my_list, target))