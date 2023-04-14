# from faker import Faker
import csv
import random
import time

num=input('请输入需要创建多少条数据:')
start=time.time()
#fake = Faker(locale='zh_CN') # 设置造的数据是中文的
title=['x_a','x_b','x_c','y']
data=[[random.randint(0,1),
       random.randint(0,2),
       random.randint(0,2),
       random.randint(0,1)] for x in range(int(num))] # 随机数据生成
#print(data)
#print(data[1][0])

path = '随机数据.csv'
try:                                                            # 解码器encoding='utf-8-sig' 不加的话用pandas读取中文会变成乱码
   with open(path, 'w', newline='',encoding='utf-8-sig') as t:  # numline是来控制空的行数的
    writer = csv.writer(t)  # 这一步是创建一个csv的写入器
    writer.writerow(title)  # 写入标签
    writer.writerows(data)  # 写入样本数据
except:
   pass
end=time.time()
print('完成,总用时为:',end-start)
