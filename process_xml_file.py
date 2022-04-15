# 找出xml文件中的四个坐标值
import re
import os
x_min = []
y_min = []
x_max = []
y_max = []
file_pos = './job1'
def mean_pos(pos):
    with open(pos, 'r') as file:
        f = file.readlines()
        for line in f:
            if re.findall(r'<xmin>(.*)</xmin>', line):
                x_min.append(int(re.findall(r'<xmin>(.*)</xmin>', line)[0]))
            if re.findall(r'<ymin>(.*)</ymin>', line):
                y_min.append(int(re.findall(r'<ymin>(.*)</ymin>', line)[0]))
            if re.findall(r'<xmax>(.*)</xmax>', line):
                x_max.append(int(re.findall(r'<xmax>(.*)</xmax>', line)[0]))
            if re.findall(r'<ymax>(.*)</ymax>', line):
                y_max.append(int(re.findall(r'<ymax>(.*)</ymax>', line)[0]))
for file in os.listdir(file_pos):
    mean_pos('./job1/'+file)
print(x_min, y_min, x_max, y_max)