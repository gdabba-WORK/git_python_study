def create_database():
    _list = [["김승영", 91, 91, 91], ["정창도", 50, 60, 70], ["지재삼", 80, 80, 20],
             ["이지혜", 100, 50, 10], ["성현기", 100, 100, 100], ["김은정", 77, 77, 77],
             ["이영섭", 70, 70, 70], ["박재성", 90, 80, 70], ["김성훈", 100, 70, 90],
             ["이정환", 55, 55, 55], ["이석훈", 90, 90, 90], ["구민수", 95, 95, 95]]
    return _list


def total_avg_insert(_list):
    for list_list in _list:
        total = list_list[1] + list_list[2] + list_list[3]
        avg = total / 3
        list_list.extend([total, avg])
    # print("total_avg_insert() done!\n")


def create_dict(_dict, _list):
    i = 1
    for list_list in _list:
        _dict[i] = list_list
        i += 1
    # print("create_dict() done!\n")


def fwrite_dict(filename, _dict):
    with open(filename, "wt") as f:
        for _tuple in _dict.items():
            f.write(f"{_tuple[0]} {_tuple[1][0]} {_tuple[1][1]} {_tuple[1][2]} {_tuple[1][3]}"
                    f" {_tuple[1][4]} {_tuple[1][5]}\n")
    # print("fwrite_dict() done!\n")


def fread_dict(filename, _dict):
    with open(filename, "rt") as f:
        temp_list = []
        for line in f:
            temp_list.extend(line.split())
            _dict[int(temp_list[0])] = [temp_list[1], int(temp_list[2]), int(temp_list[3]),
                                        int(temp_list[4]), int(temp_list[5]), float(temp_list[6])]
            temp_list.clear()
    # print("fread_dict() done!\n")
