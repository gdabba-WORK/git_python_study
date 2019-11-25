def create_database():
    _list = [[1, "김승영", 91, 91, 91], [2, "정창도", 50, 60, 70], [3, "지재삼", 80, 80, 20],
             [4, "이지혜", 100, 50, 10], [5, "성현기", 100, 100, 100], [6, "김은정", 77, 77, 77],
             [7, "이영섭", 70, 70, 70], [8, "박재성", 90, 80, 70], [9, "김성훈", 100, 70, 90],
             [10, "이정환", 55, 55, 55], [11, "이석훈", 90, 90, 90], [12, "구민수", 95, 95, 95]]
    return _list


def total_avg_insert(_list):
    if type(_list[0]) == list:
        for list_list in _list:
            total = list_list[2] + list_list[3] + list_list[4]
            avg = total / 3
            list_list.extend([total, avg])
    elif type(_list[0]) == int:
        total = _list[2] + _list[3] + _list[4]
        avg = total / 3
        _list.extend([total, avg])
    # print("total_avg_insert() done!\n")


def list_to_dict(_dict, _list):
    if type(_list[0]) == list:
        for list_list in _list:
            _dict[list_list[0]] = list_list[1:]
    elif type(_list[0]) == int:
        _dict[_list[0]] = _list[1:]
    # print("create_dict() done!\n")


def fwrite_dict(filename, _dict):
    with open(filename, "wt") as f:
        for _tuple in _dict.items():
            f.write(f"{_tuple[0]} {_tuple[1][0]} {_tuple[1][1]} {_tuple[1][2]} {_tuple[1][3]}"
                    f" {_tuple[1][4]} {_tuple[1][5]}\n")
    # print("fwrite_dict() done!\n")


def fappend_dict(filename, _dict):
    with open(filename, "at") as f:
        for _tuple in _dict.items():
            f.write(f"{_tuple[0]} {_tuple[1][0]} {_tuple[1][1]} {_tuple[1][2]} {_tuple[1][3]}"
                    f" {_tuple[1][4]} {_tuple[1][5]}\n")
    # print("fappend_dict() done!\n")


def fread_dict(filename, _dict):
    with open(filename, "rt") as f:
        temp_list = []
        for line in f:
            temp_list.extend(line.split())
            _dict[int(temp_list[0])] = [temp_list[1], int(temp_list[2]), int(temp_list[3]),
                                        int(temp_list[4]), int(temp_list[5]), float(temp_list[6])]
            temp_list.clear()
    # print("fread_dict() done!\n")
