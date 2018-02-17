# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:06:32 2018

@author: harjas
"""
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing,cross_validation,neighbors,svm,tree
from matplotlib import pyplot as plt

#%%
max=0
for i in range(1250):
    s="fastStorage/2013-8/"
    s+=str(i+1)
    s+='.csv'
    df=pd.read_csv(s,delimiter=';')
    rows=df.shape[0]
    #print(rows)
    if rows>max:
        max=rows

print(max)
#%%
a=np.zeros((1250,max))
for i in range(1250):
    s="fastStorage/2013-8/"
    s+=str(i+1)
    s+='.csv'
    df=pd.read_csv(s,delimiter=';')
    print(i)
    for j in range(df.shape[0]):
        a[i][j]=df['\t'+'CPU usage [MHZ]'][j]

#%%
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5, random_state=0).fit(a)
#print(kmeans.labels_)
#f.write(str(kmeans.labels_))
#f.close()
#%%
d={0:'CPU cores',1:'CPU capacity provisioned [MHZ]',2:'CPU usage [MHZ]',3:'CPU usage [%]',4:'Memory capacity provisioned [KB]',5:'Memory usage [KB]',6:'Disk read throughput [KB/s]',7:'Disk write throughput [KB/s]',8:'Network received throughput [KB/s]',9:'Network transmitted throughput [KB/s]'}
cols=['VM No.']
for i in range(10):
    cols.append(d[i])
clus=np.zeros((1250,11))#dtype=[('no.','i'),('col1','f'),('col2','f'),('col3','f'),('col4','f'),('col5','f'),('col6','f'),('col7','f'),('col8','f'),('col9','f'),('col10','f')])
#clus[0][0]='VM No.'
for j in range(10):
    var1=d[j]
    #clus[0][j+1]=var1
    print(var1)
    a=np.zeros((1250,max))
    for i in range(1250):
        s="fastStorage/2013-8/"
        s+=str(i+1)
        s+='.csv'
        clus[i][0]=i+1
        df=pd.read_csv(s,delimiter=';')
        for k in range(df.shape[0]):
            a[i][k]=df['\t'+var1][k]
    kmeans = KMeans(n_clusters=10, random_state=0).fit(a)
    x=0
    for z in kmeans.labels_:
        clus[x][j+1]=z
        x+=1        
#%%        
data=pd.DataFrame(data=clus[0:,0:],
                  index=clus[0:,0],
                  columns=cols)
data.to_csv('E:/study/sem 6/lop/dataset/clusters/cluster.csv')
#%%
kmeans2 = KMeans(n_clusters=20, random_state=0).fit(clus[2:,1:])
f=open('E:/study/sem 6/lop/dataset/clusters/result.txt','w')
f.write('VM No.\t\tCluster No.\n')
i=1
for k in kmeans2.labels_:
    f.write(str(i)+'\t\t'+str(k)+'\n') 
    i+=1
f.close()    
#%%
X=np.array(df_up.drop(['predict'],1))
Y=np.array(df_up['predict'])
P=np.array(f.drop(['predict'],1))
Q=np.array(f['predict'])
clf=svm.SVC()
#score123=cross_val_score(clf,X,Y,cv=10)
clf.fit(X,Y)
accuracy=clf.score(P,Q)