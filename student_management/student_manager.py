from student_management.student_data import create_database
from student_management.student_data import total_avg_insert
from student_management.student_data import list_to_dict
from student_management.student_data import fwrite_dict
from student_management.student_data import fappend_dict
from student_management.student_data import fread_dict


def manager_exe():
    print("<<<<<<<<<<<<<<student_manager를 실행합니다>>>>>>>>>>>>>>>", end='')
    fn = "student_list.txt"
    student_list = create_database()
    total_avg_insert(student_list)
    student_dict = {}
    list_to_dict(student_dict, student_list)
    fwrite_dict(fn, student_dict)

    while True:
        try:
            choice = int(input("\n\n원하는 메뉴 번호를 입력하세요\n1. 학생목록, 2. 학생 추가, 3. 학생 수정, 4. 학생 삭제, 5. 종료\n"
                               "input>>>"))
        except ValueError as e:
            print("숫자 [1-5]값만 가능")
            exit(0)

        print()
        if choice == 1:
            print_student()
        elif choice == 2:
            add_student()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            break
    print("<<<<<<<<<<<<<<student_manager를 종료합니다>>>>>>>>>>>>>>>")
    return


def print_student():
    print("-------------모든 학생 정보----------------")
    fn = "student_list.txt"
    student_dict = {}
    fread_dict(fn, student_dict)

    for dict_key, dict_value in student_dict.items():
        print(dict_key, end=' ')
        for list_value in dict_value:
            print(list_value, end=' ')
        print()
    print("----------------------------------------")
    return


def add_student():
    data = input("학생번호, 학생명, 국어점수, 영어점수, 수학점수를 공백으로 구분하여 입력하세요\n"
                 "ex)15 김민수 50 60 70\ninput>>>")
    fn = "student_list.txt"
    student_dict = {}
    fread_dict(fn, student_dict)
    data_split = data.split()

    if int(data_split[0]) in student_dict.keys():
        print("학생번호({})가 이미 존재합니다".format(data_split[0]))
        return
    else:
        _list = []
        _dict = {}

        for _string in data_split[0:1]:
            _list.append(int(_string))
        for _string in data_split[1:2]:
            _list.append(_string)
        for _string in data_split[2:]:
            _list.append(int(_string))

        total_avg_insert(_list)
        list_to_dict(_dict, _list)
        fappend_dict(fn, _dict)
        print("추가되었습니다.")
        return


def update_student():
    _key = int(input("수정할 학생번호를 입력하세요\ninput>>>"))
    fn = "student_list.txt"
    student_dict = {}
    fread_dict(fn, student_dict)

    if _key in student_dict.keys():
        data = input("학생명, 국어점수, 영어점수, 수학점수를 공백으로 구분하여 입력하세요\n"
                     "ex)김민수 50 60 70\ninput>>>")
        data_split = data.split()
        student_dict[_key][0] = data_split[0]
        student_dict[_key][1] = int(data_split[1])
        student_dict[_key][2] = int(data_split[2])
        student_dict[_key][3] = int(data_split[3])
        student_dict[_key][4] = int(data_split[1]) + int(data_split[2]) + int(data_split[3])
        student_dict[_key][5] = (int(data_split[1]) + int(data_split[2]) + int(data_split[3])) / 3
        fwrite_dict(fn, student_dict)
        print()
        return
    else:
        print("일치하는 학생번호({})가 없습니다".format(_key))
        return


def delete_student():
    _key = int(input("삭제할 학생번호를 입력하세요\ninput>>>"))
    fn = "student_list.txt"
    student_dict = {}
    fread_dict(fn, student_dict)

    if _key in student_dict.keys():
        student_dict.pop(_key)
        fwrite_dict(fn, student_dict)
        return
    else:
        print("일치하는 학생번호({})가 없습니다".format(_key))
        return
