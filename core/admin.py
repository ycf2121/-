from interface import student_interface, teacher_interface, admin_interface, common_interface
from lib import common

admin_info = {
    'name': None
}


def admin_register():
    print('管理员注册')
    if admin_info['name']:
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        conf_password = input('请确认密码：').strip()
        if password == conf_password:
            flg, msg = admin_interface.admin_register_interface(name, password)
            if flg:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def admin_login():
    print('管理员登陆')
    if admin_info['name']:
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(name, password, 'admin')
        if flag:
            admin_info['name'] = name
            print(msg)
            break
        else:
            print(msg)


@common.logn_auth(user_type='admin')
def create_school():
    print('创建学校')
    school_name=input('请输入学校名字：').strip()
    address =input('请输入学校地址').strip()
    flag,msg=admin_interface.create_school_interface(admin_info['name'],school_name,address)
    if flag:
        print(msg)
    else:
        print(msg)


@common.logn_auth(user_type='admin')
def create_teacher():
    print('创建老师')
    name = input('请输入老师名字：').strip()
    flag, msg = admin_interface.create_teacher_interface(admin_info['name'], name)
    if flag:
        print(msg)
    else:
        print(msg)


@common.logn_auth(user_type='admin')
def create_course():
    print('创建课程')
    while True:
        school_list=common_interface.check_all_schools()
        if school_list:
            for i ,school in enumerate(school_list):
                print('%s : %s'%(i,school))

            choice = input('请选择学校：').strip()
            if choice.isdigit():
                choice =int(choice)
                if choice>=len(school_list):continue
                name = input('请输入课程名称：').strip()
                flag, msg = admin_interface.create_course_interface(admin_info['name'], name,school_list[choice])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)



func_dic = {
    '1': admin_register,
    '2': admin_login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course
}


def admin_view():
    while True:
        print('''
        1 注册
        2 登陆
        3 创建学校
        4 创建老师
        5 创建课程
        ''')
        choice = input('请选择功能:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue
        func_dic[choice]()
