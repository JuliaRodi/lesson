from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
        result_t = first / second
        return result_t

# result_t1 = divide(49, 7)
# result_t2 = divide(15, 0)
#
# print(result_t1)
# print(result_t2)