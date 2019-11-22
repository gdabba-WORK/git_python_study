def avg_insert(_list):
    for list_list in _list:
        avg = (list_list[1] + list_list[2] + list_list[3]) / 3
        list_list.append(avg)


if __name__ == "__main__":
    student_list = [["김승영", 90, 90, 90], ["정창도", 50, 60, 70], ["지재삼", 80, 80, 20]]
    print(student_list)

    avg_insert(student_list)
    print(student_list)
    # student_dict = {"1":["김승영", 90, 90, 90, 270], "2":["정창도"]}


    # with open("student_list", "wt") as f:
    #     pass