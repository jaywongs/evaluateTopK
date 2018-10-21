import os
import random


if __name__== "__main__":
    file = open('C:/Users/wangs/Desktop/南大软院课程/云计算/云计算python/' + '10million' + '.txt', 'w')
    for i in range(1,10000000):
        file.write(str(random.uniform(1,10000)) + '\n')
    file.close()