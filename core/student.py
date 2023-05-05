from interface import common_interface,student_interface
from lib import common
student_info={
    'name':None
}

def student_register():
    print('学生注册')
    if student_info['name']:
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        conf_password = input('请确认密码：').strip()
        if password == conf_password:
            flg, msg = student_interface.student_register_interface(name, password)
            if flg:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def student_login():
    print('学生登陆')
    if student_info['name']:
        return
    while True:
        name = input('请输入名字').strip()
        password = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(name, password, 'student')
        if flag:
            print(msg)
            student_info['name'] = name
            break
        else:
            print(msg)

@common.logn_auth('student')
def choose_school():
    print('选择学校')
    school_list=common_interface.check_all_schools()
    if not school_list:
        print('请联系管理员创建学校')
        return
    for i,school in enumerate(school_list):
        print('%s : %s'%(i,school))
    choice = input('请选择学校：')
    if choice.isdigit():
        choice = int(choice)
        if choice < len(school_list):
            flg,msg = student_interface.choose_school_interface(student_info['name'],school_list[choice])
            print(msg)

@common.logn_auth('student')
def choose_course():
    print('选择课程')
    flag,course_list =student_interface.get_can_choose_course_interface(student_info['name'])
    if not flag :
        print(course_list)
        return
    for i ,course in enumerate(course_list):
        print('%s : %s'%(i,course))
    choice = input('请选择课程：')
    if choice.isdigit():
        choice = int(choice)
        if choice < len(course_list):
            _ ,msg=student_interface.choose_course_interface(student_info['name'],course_list[choice])
            print(msg)
        else:
            print('必须选择存在的课程')
    else:
        print('必须输入数字')

@common.logn_auth('student')
def check_score():
    scores = student_interface.check_score_interface(student_info['name'])
    print(scores)


func_dic = {
    '1': student_register,
    '2': student_login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score
}


def student_view():
    while True:
        print('''
        1 注册
        2 登陆
        3 选择学校
        4 选择课程
        5 查看成绩
        ''')
        choice = input('请选择功能:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue
        func_dic[choice]()
