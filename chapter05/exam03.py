import random as rnd
from chapter04.exam02 import bubble_sort


def binary_search(key, _list):
    left, right = 0, len(_list) - 1
    mid = (left + right) // 2

    while left < right:
        if _list[left] == key:
            print("찾는 값의 위치(index) = {} 입니다".format(left))
            return
        elif _list[right] == key:
            print("찾는 값의 위치(index) = {} 입니다".format(right))
            return

        elif _list[mid] == key:
            print("찾는 값의 위치(index) = {} 입니다".format(mid))
            return

        if _list[mid] < key:
            left = left + 1

        elif key < _list[mid]:
            right = right - 1

    print("찾는 값이 존재하지 않습니다")
    return


if __name__ == "__main__":
    rnd.seed(4)
    sorted_list = bubble_sort([rnd.randint(1, 50) for i in range(10)])
    key = 47
    print("찾을 list = {}\n찾는 값 = {}".format(sorted_list, key))


    binary_search(key, sorted_list)
