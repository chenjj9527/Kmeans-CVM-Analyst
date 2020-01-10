#-*- coding: utf-8 -*-
#K-Means聚类算法

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法

inputfile = '../tmp/zscoreddata.xls' #待聚类的数据文件
outputfile = '../tmp/data.xls' #聚类后的结果数据
outputfile1 = '../tmp/data1.xls' #聚类后的结果数据
k = 5                       #需要进行的聚类类别数

#读取数据并进行聚类分析
data = pd.read_excel(inputfile) #读取数据

#调用k-means算法，进行聚类分析
kmodel = KMeans(n_clusters = k, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data) #训练模型
# kmodel.cluster_centers_ #查看聚类中心
# kmodel.labels_ #查看各样本对应的类别

r1 = pd.Series(kmodel.labels_).value_counts()  #统计各个类别的数目

r2 = pd.DataFrame(kmodel.cluster_centers_)     #找出聚类中心

r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目'] #重命名表头
r.to_excel(outputfile1) #保存分类结果
print (r)

r = pd.concat([data, pd.Series(kmodel.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别'] #重命名表头
r.to_excel(outputfile) #保存分类结果
