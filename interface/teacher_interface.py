from db import modles
import os
from conf import settings
from lib import common
def get_all_course():
    path=os.path.join(settings.BASE_DB,'course')
    return common.get_all_dir_obj(path)

def choose_teach_course_interface(teacher_name,course_name):
    teacher_obj= modles.Teacher.get_obj_by_name(teacher_name)
    if course_name not in teacher_obj.course_list:
        teacher_obj.add_course(course_name)
        return True,'选择课程成功'
    else:
        return False,'您已经选择了本门课程'


def check_all_teach_course(teacher_name):
    teacher_obj = modles.Teacher.get_obj_by_name(teacher_name)
    return teacher_obj.course_list


def check_student_in_course(course_name):
    course_obj=modles.Course.get_obj_by_name(course_name)
    return course_obj.student_list


def modify_score(teacher_name,course_name,student_name,score):
    teacher_obj = modles.Teacher.get_obj_by_name(teacher_name)
    student_obj=modles.Student.get_obj_by_name(student_name)
    teacher_obj.modify_score(student_obj,course_name,score)
    return True,'修改分数成功'

