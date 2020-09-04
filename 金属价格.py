import pandas as pd

def number(df,stu):
    df[stu] = df[stu].apply(str)

dataman = []
data = []
fr = open('E:/python数据/bank-additional-full.csv','r')
lines = fr.readlines()
for line in lines:
    line = line.replace('\n', '')
    line = line.replace('"', '')
    t = line.split(";")
    if(len(t)==21):
        dataman.append(t)
for i in  range(len(dataman)):
    if(i>0):
        data.append(dataman[i])

df = pd.DataFrame(data, columns=['age','job','marital','education','default','housing','loan','contact','month','day_of_week','duration','campaign','pdays'
                         ,'previous','poutcome','emp.var.rate','cons.price.idx','cons.conf.idx','euribor3m','nr.employed','y'])

for i in df.columns:
    number(df,i)

df.to_csv('E:/备份/bank-additional-full.csv', index=False, sep=',')