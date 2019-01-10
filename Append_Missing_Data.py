species_list = []           #储存文件名而形成的list

import os           #导入os模块
import re
now_dir = os.getcwd()           #
file_name = os.listdir(path=now_dir)
file_name2 = []
for each in file_name:
    if ".fas" in each:
        file_name2.append(each)

def get_species_list():           #遍历所有基因文件，获得其中的种名，添加入species_list中
  gene_file = open(now_dir + "/" + fasta_name, "r")
  for each_line in gene_file:
    if each_line[0] == ">":
      result = re.match(">([A-Za-z0-9]*_*-*[A-Za-z0-9]*)",each_line)
      species_name = result.group(1)
      if species_name not in species_list:
        species_list.append(species_name)
  gene_file.close()



def append_missing():           #将missing_data 加入到文件中
    use_need_list = []          #基因文件中缺少的物种名
    
    gene_file = open(now_dir + "/" + fasta_name, "r")
    while True:                     #获取该基因的长度
        line = gene_file.readline()
        if line[0] != ">":
            gene_line = len(line)
            break             
    gene_file.close()
    
    gene_file = open(now_dir + "/" + fasta_name, "r")
    while True:                     #获取该基因的名称以及后边的内容
        line = gene_file.readline()
        if line[0] == ">":
            gene_name = line.split("_-_")
            break
    gene_file.close()

    gene_file = open(now_dir + "/" + fasta_name, "r")
    now_species_list = []
    for each_line in gene_file:             #将该基因文件中的物种名称加入到临时的列表“now_species_list中”
        if each_line[0] == ">":
            result = re.match(">([A-Za-z0-9]*_*-*[A-Za-z0-9]*)",each_line)
            species_name = result.group(1)
            now_species_list.append(species_name) 

    for each_species in species_list:           #删选该基因文件没有的物种，加入到列表use_need_list中
        if each_species not in now_species_list:
            use_need_list.append(each_species)
    
            
    gene_file.close()


    write_file = open(now_dir + "/" + fasta_name, "a")
    for each in use_need_list:
        write_file.write(">" + each + "_-_" + gene_name[1])
        for each_num in range(1,gene_line):
            write_file.write("?")
        write_file.write("\n")



for fasta_name in file_name2:     
  get_species_list()            #遍历所有基因文件，获得其中的种名


for fasta_name in file_name2:  
  append_missing()              #将missing_data加入到文件中
