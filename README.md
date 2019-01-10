# chloroplast_genome_alignment
该项目包含一系列脚本，脚本可结合Geneious软件对基因结构出现变化的叶绿体基因组编码区进行精确排序。

该脚本为作者自用脚本，尚未进行任何的兼容性测试，出现任何bug请联系作者解决。

The project includes a series of scripts that work with geneious software to alignment sequence of coding regions when the chloroplast genome gene structure has changed.

## 使用前准备

1.脚本需运行于windows平台

2.脚本需要python3环境
https://www.python.org/downloads/

3.脚本需要安装numpy模块
http://www.numpy.org/

4.亦可直接安装Anaconda使用,若安装此软件，前两个步骤可省略。
https://www.anaconda.com/

5.脚本需要Geneious软件配合，作者使用geneious版本为Geneious R11，其他版本Geneious并未进行测试。
https://www.geneious.com/


## 使用步骤

1. 在Geneious R11软件中安装MAFFT插件，并将export_annotation.geneiousWorkfolw; extract_annotation.geneiousWorkfolw; extract_annotation.geneiousWorkfolw; 三个workfolw导入Geneious软件中.

2. 将所有叶绿体基因组的gb文件导入Geneious中。

3. 在Geneious中选中所有文件，Workflows中点击extract。该步骤会将叶绿体中所有的功能区提取出来，每个生成的文件中包含一个叶绿体的所有功能基因，并分行显示。

4. 选中所有生成的文件，Workflows中点击export。该步骤会将这些刚刚生成的文件导出到桌面的Batch Export文件夹中（文件夹会自动建立）。

5. 将Batch Export文件夹中的所有文件拷入本脚本所在的文件夹。

6. 运行脚本Formatting_Annotation.py 该脚本会将大多数的rRNA注释修改为普通的rRNA注释，并且会删掉所有的tRNA，因为tRNA注释信息不同的序列注释方法差异很大，难以统一，强行排序会引入很多的非同源错误。并且tRNA总长度只有两到三千，长度较短，删除后对最终结果影响很小。

7. 运行脚本Combine_Uniform_Gene.py 该脚本会将同名基因中的一个基因删掉，因为叶绿体中存在反向重复区，反向重复区基因序列完全一样，重复计算会加权该区域的比重。

8. 运行脚本Transform.py 该脚本会将所有文件中相同名称的基因序列提取出来，形成一个以基因名称命名的文件。需要注意，该脚本还会生成一个response.txt文件，该文件中包含有各个基因文件中包含有哪些物种的基因情况。

9. 将这些结果导入Geneious软件中，选中所有文件，Workflows中点击Mafft。软件会自动将所有基因文件进行排序。之后再用export Workflows将排序产生的结果导出。并将导出的结果拷回到本脚本所在的目录中。（注意此时脚本目录中还存有未进行排序的基因文件，需要先将这些文件删除）

10. 运行Get_Homology.py 该脚本会自动分析整个矩阵，如果一列矩阵中空缺的物种超过了一定比例则将这列直接删除（gap占比过多的地方可认为是排序不成功的地方，属于非同源位点）。删除的比例默认为10%，可自行修改该脚本的第81行中的数字。改数字为1则表示当gap占比达到10%便删除该列。

11. 运行Append_Missing_Data.py 该脚本会检测每个基因文件中均包含所有物种，如果物种缺少，则会给这个物种加入missing_data("?")。

12. 运行Connect_Gene.py 该脚本将每个基因文件中的序列按照物种名称提取出来，形成各自物种文件。脚本还会形成一个名为result.txt的文件，该文件中的内容可作为partitionfinder软件https://github.com/brettc/partitionfinder/releases/tag/v2.1.1的输入文件使用。

13. 运行Merge_Fasta.py 该脚本可将多个fasta文件合并为一个fasta文件。该文件即是最后的排序完成的文件
