def add(a, b):
    return a+b


def div(a, b):
    return a / b


def mul(a, b):
    return a*b


if  __name__ == "__main__":
    print("{} {} {}" .format("Hello Python", "hi pycharm", "Good Luck"))
    x = 10
    y = 5
    print("add({}, {}) result => {}".format(x, y, add(x,y)))
    print("div({}, {}) result => {}".format(x, y, div(x,y)))
    print("mul({}, {}) result => {}".format(x, y, mul(x,y)))


