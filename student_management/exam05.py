from student_management.student_data import create_list
from student_management.student_data import avg_insert
from student_management.student_data import create_dict
from student_management.student_data import fwrite_dict
from student_management.student_data import fread_dict

if __name__ == "__main__":
    student_list = create_list()
    print("print(student_list)", student_list, sep='\n', end='\n\n')

    avg_insert(student_list)
    print("print(student_list)", student_list, sep='\n', end='\n\n')

    student_dict = {}
    create_dict(student_dict, student_list)
    print("print(student_dict)", student_dict, sep='\n', end='\n\n')

    fwrite_dict("student_list.txt", student_dict)

    empty_dict = {}
    print("print(empty_dict)", empty_dict, sep='\n', end='\n\n')

    fread_dict("student_list.txt", empty_dict)
    print("print(empty_dict)", empty_dict, sep='\n', end='\n\n')
