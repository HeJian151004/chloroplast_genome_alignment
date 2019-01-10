#!/usr/bin/python3
import os           #导入os模块                            
import re
now_dir = os.getcwd()           #得到工作目录
file_name = os.listdir(path=now_dir)
species_list = []       #从文件中得到物种列表
file_name2 = []         #储存基因文件名称
mrbayes_list = []
modle_dict = {}
speed_dict = {}
protein_list = []
a = 1
b = 1
n = 1
def build_species_list():           #建立一个含有所有单个基因文件的所有物种的列表
  fasta_file = open(now_dir + "/" + fasta_name, "r")
  for each in fasta_file:
    if each[0] == ">":
      result = re.match(">([A-Za-z0-9]*_[A-Za-z0-9]*)",each)
      species_name = result.group(1)
      if species_name not in species_list:
        species_list.append(species_name)
      
def build_protein_list():       #建立一个只含有编码蛋白基因的列表"protein_list"
  for each in file_name2:
    if each[0:3] != "rrn":
      if each[0:3] != "trn":
        if each[0:3] != "IGS":
          if each[0:3] != "Int":
            if each[0:3] != "INT":
              if each[0:3] != "int":
                if each[0:-6] not in protein_list:
                  protein_list.append(each[0:-6])

def build_dict():
  fasta_file = open(now_dir + "/" + fasta_name ,"r")
  for each_line in fasta_file:
    if each_line[0] == ">":
      result = re.match(">([A-Za-z0-9]*_[A-Za-z0-9]*)",each_line)
      species_name = result.group(1)
      code = fasta_file.readline()
      result_file = open(now_dir + "/" + species_name + ".fasta","a")
      result_file.write(code[:-1])
      result_file.close()
      read_file = open(now_dir + "/" + species_name + ".fasta","r")
      if species_name == "Eschscholzia_californica":
        mrbayes_file = open(now_dir + "/" +  "result.txt","a")
        read_file.readline()
        code_long = read_file.readline()
        global a
        global b
        global n
        b = len(code_long)
        if fasta_name[0:-6] in protein_list:
          if a == 1:
            mrbayes_file.write(str(n) + "_pos1 = " + str(a) + "-" + str(b) + r"\3;" + "\n")
            mrbayes_file.write(str(n+1) + "_pos2 = " + str(a+1) + "-" + str(b) + r"\3;" + "\n")
            mrbayes_file.write(str(n+2) + "_pos3 = " + str(a+2) + "-" + str(b) + r"\3;" + "\n")
            a = b
          else:
            mrbayes_file.write(str(n) + "_pos1 = " + str(a+1) + "-" + str(b) + r"\3;" + "\n")
            mrbayes_file.write(str(n+1) + "_pos2 = " + str(a+2) + "-" + str(b) + r"\3;" + "\n")
            mrbayes_file.write(str(n+2) + "_pos3 = " + str(a+3) + "-" + str(b) + r"\3;" + "\n")
            a = b
            read_file.close()
        else:  
          if a == 1:
            mrbayes_file.write(str(n) + "utr = " + str(a) + "-" + str(b) + ";\n")
            a = b
          else:
            mrbayes_file.write(str(n) + "utr = " + str(a+1) + "-" + str(b) + ";\n")
            a = b
            mrbayes_list.append(fasta_name)
            read_file.close()
      n = n + 1 
        
for each in file_name:
    if ".fas" in each:
        file_name2.append(each)

for fasta_name in file_name2:
    build_species_list()
    build_protein_list()
    

for each_species in species_list:         #建立分物种的文件，并将第一行带有“>”的字符串写入
  result_file = open(now_dir + "/" + each_species + ".fasta","a")
  result_file.write(">" + each_species + "\n")
  result_file.close()


for fasta_name in file_name2:
    build_dict()

