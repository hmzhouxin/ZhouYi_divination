import random

def calculate_iter(num):
    left = random.randint(5, num - 5)
    right = num - left - 1  # right side should be taken away 1
    res_l = left % 4
    res_r = right % 4
    if res_l == 0:
        res_l = 4
    if res_r == 0:
        res_r = 4
    ret = num - 1 - res_l - res_r
    return ret

def calculate_divination(num, result):
    for i in range(0, 3):
        num = calculate_iter(num)
    result.append(num / 4)

def calculate_result(times, num, result):
    for i in range(0, times):
        calculate_divination(num, result)

def print_result(result):
    print("Zhou Yi divination result: ")
    result_str = "" + str(int(result[0]))
    for i in range(1, len(result)):
        result_str += (", " + str(int(result[i])))
    print(result_str)

def zhouyi_divination(initial_num, times):
    result_list = []
    calculate_result(times, initial_num, result_list)
    print_result(result_list)

zhouyi_divination(49, 6)


