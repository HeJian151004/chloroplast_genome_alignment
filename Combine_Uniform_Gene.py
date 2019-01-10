import os           #导入os模块
import re
now_dir = os.getcwd()           #切换至当前目录
file_name = os.listdir(path=now_dir)             #切换至当前目录
file_name2 = []        #储存后缀为.fasta的文件至file_name2
line_list = []        #遍历文件，带有">"的一行不重复的储存在此列表中

def build_gene():     #分别处理问价夹中的每一个文件
  fasta_file = open(now_dir + "/" + fasta_name, "r")       #读取文件夹中的fasa文件
  write_file = open(now_dir + "/" + species_name[0] + ".fasta", "a")       #新建一个文件，文件名为物种名，后缀为".fasta",
  for each_line in fasta_file:      #遍历fasa文件
    if each_line[0] == ">":       #当文件是以>开头时
      if each_line not in line_list:        #当以>开头的这一行字符在line_list列表中找不到时（说明该基因是第一次出现）
        line_list.append(each_line)       #将这行加入line_list
        write_file.write(each_line)       #将这行写入新建的文件write_file中
        code = fasta_file.readline()      #向下读取一行，并将其字符保存到变量code中（将这个基因的序列赋值给code变量）
        write_file.write(code)        #将code写入新建的文件write_file中
      else:       #当以>开头的这一行字符在line_list列表中可以找到时（说明该基因不是第一次出现，应该删除）
        fasta_file.readline()      #直接读取下一行，这一行（带有>的这行）以及下一行字符串（这个基因的序列），均不写入新建的文档中
   

for each in file_name:      #遍历file_name中的每一个字符串
    if ".fasta" in each:        #如果.fasta在字符串中
        file_name2.append(each)         #将该字符串加入列表file_name2中

for fasta_name in file_name2:     #遍历列表file_name2
    species_name = fasta_name.split(" ")        #将该文件名以空格键“ ”进行分割，分割可得到该种的种名
    build_gene()
    os.remove(fasta_name)
