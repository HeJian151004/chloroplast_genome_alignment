import os           #导入os模块
import numpy as np

#函数 get_file_list()，得到当前目录中所有的文件名并存入相关列表中
def get_file_list():
  global now_dir
  now_dir = os.getcwd()           #得到当前目录   
  file_temp = os.listdir(path=now_dir)    #得到当前目录中的所有文件名
  global file_name
  file_name = []         #储存基因文件名称
  for each in file_temp:        #将后缀为.fasta的文件加入列表file_name中
      if ".fasta" in each:
          file_name.append(each)
  



#函数get_row_column()，得到矩阵的行数还有列数
def get_row_column():
  temp_list = []
  fasta_file = open(now_dir + "/" + fasta_name, "r")
  judge = True
  for each_line in fasta_file:
    if each_line[0] == ">":
      temp_list.append(">")
    elif judge == True:
      global column
      column = len(each_line[0:-1])
      judge = False
    else:
      pass
  global row
  row = len(temp_list)
  fasta_file.close()



#函数get_matrix(),建立一个只含有序列信息的文本文档
def get_matrix():
  matrix_file = open(now_dir + "/" + fasta_name[0:-6] + ".txt", "a")
  fasta_file = open(now_dir + "/" + fasta_name, "r")
  for each_line in fasta_file:              #将所有的碱基对以数字的形式存入列表中
    if each_line[0] != ">":
      code_line = each_line
      intab = "ATCG-QWERYUIOPSDFHJKLZXVBNM?"
      outtab = "1234000000000000000000000000"
      trantab = str.maketrans(intab,outtab)         #建立字符映射表
      new_line = code_line.translate(trantab)            #经过映射的字符串赋值给变量new_line
      for each in new_line:                         #每行中的字符后面加一个空格
          if each != "\n":
              matrix_file.write(each + " ")
          else:
              matrix_file.write(each)
  matrix_file.close()
  fasta_file.close()



#函数get_temp_matrix()，根据上一个函数生成的文本文档，建立一个numpy矩阵
def get_temp_matrix():
  global matrix
  matrix = np.zeros((row,column),dtype=np.int)            #创建一个row*column的空白方阵
  matrix_file = open(now_dir + "/" + fasta_name[0:-6] + ".txt", "r")         #打开之前创建好的_temp.txt文件
  matrix_row = 0                                                #matrix_row表示矩阵的行，从0行开始
  for each_line in matrix_file:                                 #遍历_temp.txt文件中的所有行，并将每行存入刚刚建好的矩阵中
    line_list = each_line.strip(" \n").split(" ")               #首先将每行文件头尾中的字符" \n"去掉，之后再用" "将每个字符分割出来存入列表中
    matrix[matrix_row:] = line_list                             #将列表中的所有字符赋值给矩阵的第一行
    matrix_row += 1                                             #开始处理第二行



#函数delete_code()，将numpy矩阵中非同源的列删掉
def delete_code():
  need_delete_list = []
  for i in range(column):
    num_row_list = list(matrix[:,i])                     #将矩阵的每一列都存储到列表num_row_list中
    number1 = num_row_list.count(0)                       #统计每列中的gap个数
    number2 = num_row_list.count(5)
    number3 = number1 + number2
    hold = number3/row                              #计算gap占整列数据的比例
    if hold > 0.4:                                       #如果该比例大于50%
      need_delete_list.append(i)                         #则将该列的索引号加入到列表need_delete_list中
  global matrix_new
  matrix_new = np.delete(matrix,need_delete_list,axis=1)      #在矩阵中将这些索引号所对应的列删掉，并将新的矩阵赋值给一个新的变量matrix_new



#函数write_file()，将得到的
def write_file():
  name_list = []
  code_list = []
  np.savetxt(now_dir + "/" + fasta_name[0:-2],matrix_new,fmt="%d")
  os.remove(now_dir + "/" + fasta_name[0:-6] + ".txt")
  fas_file = open(now_dir + "/" + fasta_name[0:-2],"r")
  tem_file = open(now_dir + "/" + fasta_name[0:-6],"a")
  for each_line in fas_file:
    code_line = each_line
    intab = "123405"
    outtab = "ATCG-?"
    trantab = str.maketrans(intab,outtab)         #建立字符映射表
    new_line = code_line.translate(trantab)            #经过映射的字符串赋值给变量new_line
    for each in new_line:                         #每行中的字符后面的空格删掉
        if each != " ":
            tem_file.write(each)                  #将字符写入文件tem_file中
  tem_file.close()

  fasta_file = open(now_dir + "/" + fasta_name, "r")         #打开fasta_name文件
  for each_fasta_line in fasta_file:                          #读取每一行
    if each_fasta_line[0] == ">":                             #如果该行第一个字符为">"
      name_list.append(each_fasta_line)                       #将该行填入列表name_list中
  fasta_file.close()                      

  tem_file = open(now_dir + "/" + fasta_name[0:-6],"r")      #打开temp文件
  for each_tem_line in tem_file:                              #读取该文件中的每一行
    if each_tem_line[0] != " ":                               #如果该行的第一个字符不为" "
      code_list.append(each_tem_line)                         #将该行加入到列表code_list中
      
  fas_file = open(now_dir + "/" + fasta_name[0:-2],"w")      #建立最终的fas文件
  for num in range(0,len(name_list)):                         #得到之前建立的两个列表的长度，遍历这一数字当做列表的索引
    fas_file.write(name_list[num])                            #将带有">"的一行字符串写入fas_file
    fas_file.write(code_list[num])                            #将序列写入fas_file
  fas_file.close()
  tem_file.close()
  os.remove(now_dir + "/" + fasta_name[0:-6])                #将刚刚建立的tem_file删除
  

      



  

get_file_list()             #得到当前目录中所有的文件名并存入相关列表中

for fasta_name in file_name:            
  get_row_column()            #调用函数get_row_column()
  get_matrix()                #调用函数get_matrix()
  get_temp_matrix()           #调用函数get_temp_matrix()
  delete_code()               #调用函数delete_code()
  write_file()                #调用函数write_file()



