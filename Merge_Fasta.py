import os           #导入os模块
now_dir = os.getcwd()           #
file_name = os.listdir(path=now_dir)
file_name2 = []
for each_name in file_name:
  if each_name[-6:] == ".fasta":
    file_name2.append(each_name)

result_file = open(now_dir + "/" + "_result.fasta","w")
for each_name in file_name2:
  read_file = open(now_dir + "/" + each_name,"r")
  for each_line in read_file:
    if each_line[0] == ">":
      result_file.write(each_line)
    else:
      result_file.write(each_line + "\n")
  read_file.close()
    
result_file.close()
