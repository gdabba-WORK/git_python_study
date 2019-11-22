from student_management.student_data import create_database
from student_management.student_data import total_avg_insert
from student_management.student_data import list_to_dict
from student_management.student_data import fwrite_dict
from student_management.student_data import fappend_dict
from student_management.student_data import fread_dict


def manager_exe():
    print("<<<<<<<<<<<<<<student_manager를 실행합니다>>>>>>>>>>>>>>>")
    fn = "student_list.txt"
    student_list = create_database()
    total_avg_insert(student_list)
    student_dict = {}
    list_to_dict(student_dict, student_list)
    fwrite_dict(fn, student_dict)
    print_student()
    add_student()
    print("<<<<<<<<<<<<<<student_manager를 종료합니다>>>>>>>>>>>>>>>")

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


def add_student():
    data = input("학생번호, 학생명, 국어점수, 영어점수, 수학점수를 공백으로 구분하여 입력하세요\n"
                 "ex)15 김민수 50 60 70\n<<<input>>>\n")
    fn = "student_list.txt"
    student_dict = {}
    fread_dict(fn, student_dict)

    if int(data.split()[0]) in student_dict.keys():
        print("학생번호({})가 이미 존재합니다".format(data.split()[0]))
        return
    else:
        _list = []
        _dict = {}

        print(data.split())
        print(data.split())
        print(data.split())
        for _string in data.split()[0:1]:
            _list.append(int(_string))
        for _string in data.split()[1:2]:
            _list.append(_string)
        for _string in data.split()[2:]:
            _list.append(int(_string))

        total_avg_insert(_list)
        list_to_dict(_dict, _list)
        fappend_dict(fn, _dict)