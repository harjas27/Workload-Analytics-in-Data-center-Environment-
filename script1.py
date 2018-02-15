import pandas as pd
from matplotlib import pyplot as plt

#df=pd.read_csv("fastStorage/2013-8/1.csv",delimiter=';',dtype={'CPU cores':float})
#df['CPU cores']=df.CPU cores.astype(float)


#print (df.info())

#pcc=df.drop(['Timestamp [ms]'],axis=1).corr(method='pearson')
#print (pcc)
#print (pcc['\tCPU usage [%]'][5])

d={0:'CPU cores',1:'CPU capacity provisioned [MHZ]',2:'CPU usage [MHZ]',3:'CPU usage [%]',4:'Memory capacity provisioned [KB]',5:'Memory usage [KB]',6:'Disk read throughput [KB/s]',7:'Disk write throughput [KB/s]',8:'Network received throughput [KB/s]',9:'Network transmitted throughput [KB/s]'}
f = open('E:/study/sem 6/lop/dataset/pcc.txt', 'w')  

for j in range(10):
    k=j+1
    while k != 9 :
        var1=d[j]
        var2=d[k]
        name='plts/pcc/'+str(j)+'_'+str(k)+'.png'
        x=[]
        y=[]
        summ=0
        mean=0
        print (var1,var2)
        for i in range(1250):
            s="fastStorage/2013-8/"
            s+=str(i+1)
            s+='.csv'
            df=pd.read_csv(s,delimiter=';')
            pcc=df.drop(['Timestamp [ms]'],axis=1).corr(method='pearson')
            x.append(i+1)
            y.append(pcc['\t'+var1][k])
            summ+=pcc['\t'+var1][k]
        k+=1
        mean=summ/1250
        f.write(var1+'_'+var2+' : '+str(mean))
        print(mean)
        print('\n')
        plt.plot(x,y)
        plt.title('PCC of '+ var1+' and '+var2)
        plt.ylabel('PCC')
        plt.xlabel('VM no.')
        plt.savefig(name)
        plt.close()

f.close()