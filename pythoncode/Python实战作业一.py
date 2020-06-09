# -*- coding: utf-8 -*-
# 有参数,但未给参数赋值,无需返回,需要传参才有参数值

def login(manual_login):
    # return manual_login  无需返回值
    print(manual_login)


# 有参数，且给参数赋值,有返回值，返回所赋值配合表达式公式

def login2(name='Daniel', password='123456'):
    return name, password


method0 = login2()


# 无参数，有返回值,返回值为表达式

def login3():
    return 'kb' + 'auto_input', '=', ['ID', 'Daniel'], ['password', (1 + 2) / 3 - 4 * 5 + 6 * 100000]


method = login3()


# 无参数, 无返回值,打印结果为none

def login4():
    pass


method2 = login4()

if __name__ == '__main__':
    login('Keyboard input')
    print(method0)
    print(method)
    print(method2)
