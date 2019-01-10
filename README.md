# chloroplast_genome_alignment
该项目包含一系列脚本，脚本可结合geneious软件对基因结构出现变化的叶绿体基因组编码区进行精确排序。

The project includes a series of scripts that work with geneious software to alignment sequence of coding regions when the chloroplast genome gene structure has changed.

## 使用前准备




## 使用步骤

1. 在Geneious R11软件中安装MAFFT插件，并将export_annotation.geneiousWorkfolw; extract_annotation.geneiousWorkfolw; extract_annotation.geneiousWorkfolw; 三个workfolw导入Geneious软件中.

2. 将所有叶绿体基因组的gb文件导入Geneious中。

3. 在Geneious中选中所有文件，Workflows中点击extract。该步骤会将叶绿体中所有的功能区提取出来，每个生成的文件中包含一个叶绿体的所有功能基因，并分行显示。

4. 选中所有生成的文件，后再Workflows中点击export。该步骤会将这些刚刚生成的文件导出到桌面的Batch Export文件夹中（文件夹会自动建立）。

5. 将Batch Export文件夹中的所有文件考入本脚本所在的文件夹。

6. 运行脚本Formatting_Annotation.py 该脚本运行会
