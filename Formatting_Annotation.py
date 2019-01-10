import os           #导入os模块
species_list = []
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



#将输出geneious输出的注释文件格式化
def formatting():
    with open (now_dir + "/" + fasta_name[:-2], "a") as write_file:
        with open (now_dir + "/" + fasta_name, "r") as read_file:
            for each_line in read_file:
                if "_-_4.5S_rRNA" in each_line:
                    each_line = each_line.replace("_-_4.5S_rRNA","_-_rrn4.5_rRNA")
                    write_file.write(each_line)
                elif "_-_4.5_rRNA" in each_line:
                    each_line = each_line.replace("_-_4.5_rRNA","_-_rrn4.5_rRNA")
                    write_file.write(each_line)
                elif "_-_5_rRNA" in each_line:
                    each_line = each_line.replace("_-_5_rRNA","_-_rrn5_rRNA")
                    write_file.write(each_line)
                elif "_-_5S_rRNA" in each_line:
                    each_line = each_line.replace("_-_5S_rRNA","_-_rrn5_rRNA")
                    write_file.write(each_line)                    
                elif "_-_rnl_rRNA" in each_line:
                    each_line = each_line.replace("_-_rnl_rRNA","_-_rrn23_rRNA")
                    write_file.write(each_line)           
                elif "_-_rns_rRNA" in each_line:
                    each_line = each_line.replace("_-_rns_rRNA","_-_rrn16_rRNA")
                    write_file.write(each_line) 
                elif "_-_23S_rRNA" in each_line:
                    each_line = each_line.replace("_-_23S_rRNA","_-_rrn23_rRNA")
                    write_file.write(each_line)           
                elif "_-_23_rRNA" in each_line:
                    each_line = each_line.replace("_-_23_rRNA","_-_rrn23_rRNA")
                    write_file.write(each_line) 
                elif "_-_rrn23S_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrn23S_rRNA","_-_rrn23_rRNA")
                    write_file.write(each_line)
                elif "_-_rrn16S_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrn16S_rRNA","_-_rrn16_rRNA")
                    write_file.write(each_line)
                elif "_-_rrn5S_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrn5S_rRNA","_-_rrn5_rRNA")
                    write_file.write(each_line)
                elif "_-_rrn4.5S_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrn4.5S_rRNA","_-_rrn4.5_rRNA")
                    write_file.write(each_line)
                elif "_-_rRNA23" in each_line:
                    each_line = each_line.replace("_-_rRNA23","_-_rrn23_rRNA")
                    write_file.write(each_line)
                elif "_-_rRNA16" in each_line:
                    each_line = each_line.replace("_-_rRNA16","_-_rrn16_rRNA")
                    write_file.write(each_line)
                elif "_-_rRNA5" in each_line:
                    each_line = each_line.replace("_-_rRNA5","_-_rrn5_rRNA")
                    write_file.write(each_line)
                elif "_-_rRNA4.5" in each_line:
                    each_line = each_line.replace("_-_rRNA4.5","_-_rrn4.5_rRNA")
                    write_file.write(each_line)
                elif "_-_rrrn23_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrrn23_rRNA","_-_rrn23_rRNA")
                    write_file.write(each_line)
                elif "_-_rrrn16_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrrn16_rRNA","_-_rrn16_rRNA")
                    write_file.write(each_line)
                elif "_-_rrrn5_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrrn5_rRNA","_-_rrn5_rRNA")
                    write_file.write(each_line)
                elif "_-_rrrn4.5_rRNA" in each_line:
                    each_line = each_line.replace("_-_rrrn4.5_rRNA","_-_rrn4.5_rRNA")
                    write_file.write(each_line)
                elif "trn" in each_line:
                    read_file.readline()
                elif "tRN" in each_line:
                    read_file.readline()                    
                else:
                    write_file.write(each_line)











get_file_list()             #得到当前目录中所有的文件名并存入相关列表中

for fasta_name in file_name:
    formatting()
    os.remove(fasta_name)
    os.rename(fasta_name[:-2],fasta_name)

  
