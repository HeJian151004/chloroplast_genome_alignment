gene_list = ["rpl32","accD","atpA","atpB","atpE","atpF","atpH","atpI","ccsA","cemA","clpP","infA","matK","ndha","ndhB","ndhC","ndhD","ndhe","ndhF","ndhG","ndhh","ndhi","ndhJ","ndhK","petA","petB","petD","petG","petL","petN","psaA","psaB","psaC","psaI","psaJ","PsbA","psbB","psbC","psbD","psbE","psbF","psbH","psbi","psbJ","psbK","psbL","psbM","psbN","psbT","psbz","rbcl","rpl14","rpl16","rpl2","rpl20","rpl22","rpl23","rpl33","rpl36","rpoA","rpoB","rpoC1","rpoC2","rps11","rps12","rps14","rps15","rps16","rps18","rps19","rps2","rps3","rps4","rps7","rps8","rrn16","rrn23","rrn4.5","rrn5","trnA-UGC","trnC-GCA","trnD-GUC","trnE-UC","trnF-GAA","trnfM-CAU","trnG-GCC","trnG-UCC","trnH-GUG","trnI-CAU","trnI-GAU","trnK-UUU","trnL-CAA","trnL-UAA","trnL-UAG","trnM-CAU","trnN-GUU","trnP-UGG","trnQ-UUG","trnR-ACG","trnR-UCU","trnS-GCU","trnS-GGA","trnS-UGA","trnT-GGU","trnT-UGU","trnV-GAC","trnV-UAC","trnW-CCA","trnY-GUA","ycf1","ycf2","ycf3","ycf4"]
species_list = []           #储存文件名而形成的list
import os           #导入os模块
import re
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






def del_gene():
    with open (now_dir + "/" + fasta_name[:-2], "a") as write_file:
        with open (now_dir + "/" + fasta_name, "r") as read_file:
            for each_line in read_file:
                if each_line[0] == ">":
                    judge = 0
                    for each_gene in gene_list:
                        if each_gene in each_line:
                            judge = 1
                    if judge == 1:
                        write_file.write(each_line)
                        write_file.write(read_file.readline())
                    














                          


def build_gene():       #将物种文件中的基因分别提取出来，形成新的基因文件，后缀为".fas"
    now_list = []
    fasta_file = open(now_dir + "/" + fasta_name, "r")
    for each_line in fasta_file:
      if each_line[0] == ">":
          name1 = re.split("_-_",each_line)
          name2 = re.split("_| ",name1[1]) 
          gene_name = name2[0]
          now_list.append(gene_name.upper())
          result_file = open(now_dir + "/" + gene_name + ".fas", "a")
          result_file.write(each_line)
          next_line = fasta_file.readline()
          result_file.write(next_line)
          result_file.close()

        

          
          




get_file_list()             #得到当前目录中所有的文件名并存入相关列表中

for fasta_name in file_name:
    del_gene()
    os.remove(fasta_name)
    os.rename(fasta_name[:-2],fasta_name)
    build_gene()
    species_list.append(fasta_name[:-6])










#------------------------------文件已经建立完毕，之后开始检测相关基因缺失情况-------------------------------------------








def get_fas_list():
  global now_dir
  now_dir = os.getcwd()           #得到当前目录   
  file_temp = os.listdir(path=now_dir)    #得到当前目录中的所有文件名
  global fas_name
  fas_name = []         #储存基因文件名称
  for each in file_temp:        #将后缀为.fasta的文件加入列表file_name中
      if each[-4:] == ".fas":
          fas_name.append(each)

def build_test():         #分别打开各个基因文件，检查物种名称是否跟根据物种文件建立的物种list(species_list) 相同    
    now_species_list = []                                        #基因文件中所有的物种名存入这一列表（now_species_list） 
    fas_file = open(now_dir + "/" + fasta_name, "r")             #打开基因文件
    response_file = open(now_dir + "/" + "response.txt", "a")  #建立结果文件
    for each_line in fas_file:                                   #遍历基因文件                                     
      if each_line[0] == ">":                                    #如果一行文件的开头字符为“>”
          name1 = each_line.split("_-_")                         #将第一行文件按照字符串“_-_”进行分割，分割后的结果赋值给name1
          now_species_list.append(name1[0][1:])                  #提取列表name1的第一个元素（也就是这行中的基因名称）              
    for each in species_list:                   #检查各个基因文件，缺少的物种名称在报告中标出
        if each not in now_species_list:
            response_file.write(each + " not in " + fasta_name + "\n")
    response_file.close()

get_fas_list()             #得到当前目录中所有的文件名并存入相关列表中

for fasta_name in fas_name:
    build_test()
