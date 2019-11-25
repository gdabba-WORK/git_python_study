if __name__ == "__main__":
    mySquare = lambda x: x ** 2
    print(mySquare(9))

    list1 = [1, 2, 3, 4, 5]


    for i in list1:
        print(i ** 2)

    [print(i ** 2, end=' ') for i in list1 if i % 2 == 1]

    (1, 2, 3, 4)