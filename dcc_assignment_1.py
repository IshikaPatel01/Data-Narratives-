# -*- coding: utf-8 -*-
"""dcc_assignment_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mJCCboplBI61NbVoU2E0ceu0xMeZd3Dv
"""

import pandas as pd
import numpy as np

df=pd.read_csv("/content/dcc-assignment_1.xlsx - main.csv")
print(df)

"""Q1"""

femaledf= df[df['Gender'] == 'Female']
mathsavg=femaledf['Mathematics'].mean()
scienceavg=femaledf['Science'].mean()
engavg=femaledf['English'].mean()
dict1=pd.DataFrame({"average":[mathsavg, scienceavg, engavg]})
ans=dict1.mean()
print(ans)
# print((mathsavg+scienceavg+engavg)/3)

"""Q2"""

df1=df['Mathematics']>df['Mathematics'].median()
count=(df1==True).sum()
count

"""Q3"""

print(df['Science'].mode()[1])

"""Q4"""

maledf = df[df['Gender'] == 'Male']
df1=maledf['English']<maledf['English'].mean()
count=(df1==True).sum()
print(count)

"""Q5"""

age15=df[df['Age']==15]
mathematics=age15['Mathematics'].sum()
science=age15['Science'].sum()
eng=age15['English'].sum()
ans=mathematics+science+eng
print(ans)

"""Q6"""

femaledf=df[df['Gender']=="Female"]
ans=femaledf[((femaledf['Mathematics']>=85) & (femaledf['Mathematics']<=90)) |
             (femaledf['Science']>=85) & (femaledf['Science']<=90) |
              (femaledf['English']>=85) & (femaledf['English']<=90)]
ans.shape[0] #counting

"""Q7"""

a=df[df['Name'].str.startswith('A')]
mathsavg=a['Mathematics'].mean()
scienceavg=a['Science'].mean()
engavg=a['English'].mean()
avg=(mathsavg+scienceavg+engavg)/3
print(avg)

"""Q8"""

df1=df["English"]
df2=df["Science"]
df3=df["Mathematics"]
count1=(df1==88).sum()
count2=(df2==88).sum()
count3=(df3==88).sum()
print(count1+count2+count3)

"""Q9"""

maledf=df[df['Gender']=="Male"]
mathsmedian=maledf['Mathematics'].median()
sciencemedian=maledf['Science'].median()
engmedian=maledf['English'].median()
dict1=pd.DataFrame({"median":[mathsmedian,sciencemedian,engmedian ]})
print(dict1.median())

"""Q10"""

femaledf=df[df['Gender']=='Female']
df1=femaledf["Mathematics"]>femaledf["Mathematics"].mean()
count=(df1==True).sum()
print(count)

"""PLOTS:

Gender
"""

import pandas as pd
malecount=(df["Gender"]=="Male").sum()
malecount
femalecount=(df["Gender"]=="Female").sum()
femalecount

dict1={"count" : [malecount,femalecount]}
df1 = pd.DataFrame(dict1,index= [ "Male", "Female"])
df1.plot.pie(y='count')

"""female maths marks hist"""

femaledf=df[df['Gender']=='Female']
mathsmarks=femaledf['Mathematics'].plot(kind='hist', edgecolor='black', color='pink')

"""male english marks hist"""

maledata=df[df['Gender']=="Male"]
maledata['English'].plot(kind='hist',edgecolor='black')

"""mean of all 3 subjects of females"""

femaledf= df[df['Gender'] == 'Female']
mathsavg=femaledf['Mathematics'].mean()
scienceavg=femaledf['Science'].mean()
engavg=femaledf['English'].mean()

dict1=pd.DataFrame({'subject':['maths', 'science', 'eng'],
                    'value':[mathsavg,scienceavg,engavg]})
dict1.plot(kind='bar', x= 'subject',y='value',legend=False, color=['yellow','blue','red'],edgecolor='black')

"""graph of male english marks"""

maledata=df[df['Gender']=="Male"]
maledata.plot(kind='bar',x='Student-ID',y=['English'],legend=False)

"""mean marks of male & female in all subjects"""

df1=df[['Mathematics','Science','English','Gender']].groupby('Gender').mean()
df1.plot(kind='bar')

