import os
import subprocess
import glob
import re
from pathlib import Path

os.chdir('tmp')

print("合并上游拦截规则")
file_list = glob.glob('adblock*.txt')
with open('combined_adblock.txt', 'w') as outfile:
    for file in file_list:
        with open(file, 'r') as infile:
            outfile.write(infile.read())
            outfile.write('\n')
            
with open('combined_adblock.txt', 'r') as f:
    content = f.read()
content = re.sub(r'^[!].*$\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^#(?!\s*#).*\n?', '', content, flags=re.MULTILINE)

with open('cleaned_adblock.txt', 'w') as f:
    f.write(content)
print("拦截规则合并完成")
            
current_dir = os.getcwd()
adblock_file = os.path.join(current_dir, 'cleaned_adblock.txt')
target_dir = os.path.join(current_dir, '.././data/rules/')
Path(target_dir).mkdir(parents=True, exist_ok=True)
adblock_file_new = os.path.join(target_dir, 'adblock.txt')
os.rename(adblock_file, adblock_file_new) 

print("规则去重中")
os.chdir(".././data/rules/")  # 更改当前目录
files = os.listdir()  # 得到文件夹下的所有文件名称
result = []
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        if os.path.splitext(file)[1] == '.txt':
            print('开始去重'+(file))
            f = open(file, encoding="utf8")  # 打开文件
            result = list(set(f.readlines()))
            result.sort()
            fo = open('test' + (file), "w", encoding="utf8")
            fo.writelines(result)
            f.close()
            fo.close()
            os.remove(file)
            os.rename('test' + (file), (file))
            print((file) + '去重完成')
print("规则去重完成")
