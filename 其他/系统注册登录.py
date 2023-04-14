import time

print("用户注册")
print("用户名:")
username = input()
print("密码:")
password = input()
print("登录")
for i in range(10):
    print("请输入用户名:")
    inputname = input()
    print("请输入密码:")
    inputpassword = input()
    if username == inputname and password == inputpassword:
        print("登陆成功")
        break
    else:
        if i < 3:
            print("密码错误，还有 {} 次机会".format(2 - i))
        else:
            print("输入密码超过 3 次，请稍后登录")
            time.sleep(30)
