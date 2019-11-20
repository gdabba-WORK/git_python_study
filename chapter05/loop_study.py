def gugu(value):
    for i in range(1,10):
        print("{} * {} = {}".format(value, i, value*i))


def gugudan():
    for i in range(2, 10):
        print("{}단 시작".format(i))
        for j in range(1, 10):
            print("{} * {} = {}".format(i, j, i*j))


def gugudan_land():
    for i in range(1, 10):
        for j in range(2, 10):
            print("{0} * {1} = {2:2}".format(j, i, j * i), end='\t')
        print()


if __name__ == "__main__":
    for i in [0, 1, 2, 3, 4, 5]:
        print(i, end=' ')

    print()
    for i in range(1, 10):
        print(i, end=' ')

    print()
    for i in range(0, 10, 2):
        print(i, end=' ')

    print()
    print("{} {}".format(range(0, 10), list(range(0, 10))))

    print("----------------------------------")
    # 구구단
    gugu(2)  # 2단

    gugudan()  # 전체의 구구단

    # ex) 2 * 1 = 2   3 * 1 = 3   ... 9 * 1 = 9
    #     2 * 2 = 4   3 * 2 = 6   ... 9 * 2 = 18
    gugudan_land()
