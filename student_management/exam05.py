def avg_insert(_list):
    for list_list in _list:
        avg = (list_list[1] + list_list[2] + list_list[3]) / 3
        list_list.append(avg)


def create_dict(_dict, _list):
    i = 1
    for list_list in _list:
        _dict[i] = list_list
        i += 1


def fwrite_dict(filename, _dict):
    with open(filename, "wt") as f:
        for _tuple in _dict.items():
            f.write("{} {}\n".format(_tuple[0], _tuple[1]))


if __name__ == "__main__":
    student_list = [["김승영", 90, 90, 90], ["정창도", 50, 60, 70], ["지재삼", 80, 80, 20]]
    print(student_list)

    avg_insert(student_list)
    print(student_list)

    student_dict = {}
    create_dict(student_dict, student_list)
    print(type(student_dict))
    print(student_dict)

    fwrite_dict("student_list.txt", student_dict)

