import random as rnd


def swap(list, curr, next):
    temp = list[curr]
    list[curr] = list[next]
    list[next] = temp


def bubble_sort(list):
    count = False      # count == False는 swap이 일어나지 않았음을 의미. 따라서 바깥 for문 다 돌기 전 return 될 수 있음
    last = len(list)
    for i in range(0, last-1):
        for j in range(0, last-1-i):
            if list[j] > list[j+1]:
                swap(list, j, j+1)
                count = True
        if not count:
            return list
        else:
            count = False
    return list


if __name__ == "__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0, 10):
        random_list.append(rnd.randint(1, 46))

    print(random_list)

    sorted_list = bubble_sort(random_list)
    print(sorted_list)
