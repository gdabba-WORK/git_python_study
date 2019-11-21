# parameter: 1.list 2.tuple, 3.dictionary
def my_student_info_list(listBylist):
    print("my_student_info_list() start!")
    for list_value in listBylist:
        print("------------------------")
        print("학생 이름 : %s" % list_value[0], "학급 번호 : %s" % list_value[1], "전화 번호 : %s" % list_value[2],
              sep='\n')
    print("my_student_info_list() end!\n")


def my_student_info_tuple(tupleBytuple):
    print("my_student_info_tuple() start!")
    for tuple_index in range(len(tupleBytuple)):
        print("------------------------")
        print("학생 이름 : {}\n학급 번호 : {}\n전화 번호 : {}".format(tupleBytuple[tuple_index][0],
                                                     tupleBytuple[tuple_index][1], tupleBytuple[tuple_index][2]))
    print("my_student_info_tuple() end!\n")


def my_student_info_dict1(dictBydict):
    print("my_student_info_dict() start!")
    for dict_key, dict_value in zip(dictBydict.keys(), dictBydict.values()):
        print("번호 {}".format(dict_key))
        for dict_key_in_value in dict_value:
            print("{} : {}".format(dict_key_in_value, dict_value[dict_key_in_value]))
    print("my_student_info_dict() end!\n")


# my_student_info_dict1과 출력결과는 같으나 for 문의 index 및 range 구조를 다른 방식으로 구성
def my_student_info_dict2(dictBydict):
    print("my_student_info_dict2() start!")
    for dict_tuple in dictBydict.items():
        print("번호 {}".format(dict_tuple[0]))
        for dict_tuple_tuple in dict_tuple[1].items():
            print("{} : {}".format(dict_tuple_tuple[0], dict_tuple_tuple[1]))
    print("my_student_info_dict2() end!\n")


if __name__ == "__main__":
    std_list = [["현아", "01", "01-235-6789"], ["진수", "02", "01-987-6543"]]
    my_student_info_list(std_list)

    std_tuple = (("현아", "01", "01-235-6789"), ("진수", "02", "01-987-6543"))
    my_student_info_tuple(std_tuple)

    std_dict = {"01": {"학생 이름": "현아", "학급 번호": "01", "전화 번호": "01-235-6789"},
                "02": {"학생 이름": "진수", "학급 번호": "02", "전화 번호": "01-987-6543"}}
    my_student_info_dict1(std_dict)
    my_student_info_dict2(std_dict)