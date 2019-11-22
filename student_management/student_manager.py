from student_management.student_data import create_database
from student_management.student_data import total_avg_insert
from student_management.student_data import create_dict
from student_management.student_data import fwrite_dict
from student_management.student_data import fread_dict


def manager_exe():
    print("<<<<<<<<<<<<<<student_manager를 실행합니다>>>>>>>>>>>>>>>")
    print("")
    student_list = create_database()
    total_avg_insert(student_list)
    student_dict = {}
    create_dict(student_dict, student_list)
    fwrite_dict("student_list.txt", student_dict)


def print_student():
    print("-------------모든 학생 정보----------------")
    student_dict = {}
    fn = "student_list.txt"
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
    print(type(data))
    # todo