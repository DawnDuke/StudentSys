filename = 'student.txt'


def menu():
    print('==================学生信息系统=======================')
    print('------------功能菜单------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除入学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出系统')
    print('------------------------------------')


def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n：')
                if answer == 'y':
                    print('退出成功')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def insert():
    student_list = []
    while True:
        id = input('请输入ID（如：201800001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        student = {'id': id, 'name': name, 'english': english}
        student_list.append(student)
        answer = input('是否继续添加？y/n：')
        if answer == 'y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕')


def save(student_list):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in student_list:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()
