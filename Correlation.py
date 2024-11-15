# -*- coding: utf-8 -*-
"""-Assignment8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_oSQ7bXFY3riy7P_3V6l23k59fLDfney
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset(name='iris')

data

def mean(array):
  sum=0
  mean=0
  for i in array:
    sum+=i
  mean=sum/len(array)
  return mean

def variance(array):
  s=0
  var=0
  for i in array:
    s+=(i-mean(array))**2
    var=s/len(array)
  return var

df=pd.DataFrame(data)

sepallength=df['sepal_length']
sepalwidth=df['sepal_width']
petallength=df['petal_length']
petalwidth=df['petal_width']

print(mean(sepallength))
print(variance(sepallength))

print(mean(sepalwidth))
print(variance(sepalwidth))

print(mean(petallength))
print(variance(petallength))

print(mean(petalwidth))
print(variance(petalwidth))

sepal_length_mean= data['sepal_length'].mean()
sepal_length_mean

sepal_length_variance = data['sepal_length'].var()
sepal_length_variance

sepal_width_mean= data['sepal_width'].mean()
sepal_width_mean

sepal_width_variance= data['sepal_width'].var()
sepal_width_variance

petal_length_mean= data['petal_length'].mean()
petal_length_mean

petal_length_variance= data['petal_length'].var()
petal_length_variance

petal_width_mean= data['petal_width'].mean()
petal_width_mean

petal_width_variance= data['petal_width'].var()
petal_width_variance

dict_data={}

covariance = np.sum((sepallength - mean(sepallength)) * (sepalwidth - mean(sepalwidth))) / 150
correlation = covariance / (np.sqrt(variance(sepallength)) * np.sqrt(variance(sepalwidth)))
correlation
dict_data["sepallength & sepalwidth"] = correlation
print(correlation)




covariance = np.sum((sepallength - mean(sepallength)) * (petallength - mean(petallength))) / 150
correlation = covariance / (np.sqrt(variance(sepallength)) * np.sqrt(variance(petallength)))
correlation
dict_data["sepallength & petallength"] = correlation
print(correlation)


covariance = np.sum((sepallength - mean(sepallength)) * (petalwidth - mean(petalwidth))) / 150
correlation = covariance / (np.sqrt(variance(sepallength)) * np.sqrt(variance(petalwidth)))
correlation
dict_data["sepallength & petalwidth"] = correlation
print(correlation)



covariance = np.sum((petallength - mean(petallength)) * (sepalwidth - mean(sepalwidth))) / 150
correlation = covariance / (np.sqrt(variance(petallength)) * np.sqrt(variance(sepalwidth)))
correlation
dict_data["petallength & sepalwidth"] = correlation





covariance = np.sum((petalwidth - mean(petalwidth)) * (sepalwidth - mean(sepalwidth))) / 150
correlation = covariance / (np.sqrt(variance(petalwidth)) * np.sqrt(variance(sepalwidth)))
correlation
dict_data["petalwidth & sepalwidth"] = correlation
print(correlation)



covariance = np.sum((petalwidth - mean(petalwidth)) * (sepalwidth - mean(sepalwidth))) / 150
correlation = covariance / (np.sqrt(variance(petalwidth)) * np.sqrt(variance(sepalwidth)))
correlation
dict_data["petalwidth & sepalwidth"] = correlation
print(correlation)


covariance = np.sum((petalwidth - mean(petalwidth)) * (petallength - mean(petallength))) / 150
correlation = covariance / (np.sqrt(variance(petalwidth)) * np.sqrt(variance(petallength)))
correlation
dict_data["petalwidth & petallength"] = correlation
print(correlation)

# import pandas as pd


# correlation = data.corr()


# sortedcorrelation = correlation.unstack().sort_values(ascending=False)


# sortedcorrelation = sortedcorrelation[sortedcorrelation != 1]


# for pair, correlation_coefficient in sortedcorrelation.items():
#     print(f"Attributes: {pair}, Correlation: {correlation_coefficient}")

"""Q3

i. setosa
"""

setosadata = data.iloc[:, 4] == "setosa"
data_setosa = data[setosadata]

sepal_length=np.array(data_setosa.iloc[:, 0])
mean_sepal_length=mean(sepal_length)
var_sepal_length = variance(sepal_length)


sepal_width=np.array(data_setosa.iloc[:,1])
mean_sepal_width=mean(sepal_width)
var_sepal_width = variance(sepal_width)


petal_length=np.array(data_setosa.iloc[:,2])
mean_petal_length=mean(petal_length)
var_petal_length = variance(petal_length)


petal_width=np.array(data_setosa.iloc[:,3])
mean_petal_width=mean(petal_width)
var_petal_width = variance(petal_width)

dictsetosa={}

covariance = np.sum((sepal_length - mean_sepal_length) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_sepal_width))
correlation
dictsetosa["Sepal_length & sepal_width"] = correlation



covariance = np.sum((sepal_length - mean_sepal_length) * (petal_length - mean_petal_length)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_petal_length))
correlation
dictsetosa["Sepal_length & petal_length"] = correlation


covariance = np.sum((sepal_length - mean_sepal_length) * (petal_width - mean_petal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_petal_width))
correlation
dictsetosa["Sepal_length & petal_width"] = correlation


covariance = np.sum((petal_length - mean_petal_length) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_length) * np.sqrt(var_sepal_width))
correlation
dictsetosa["petal_length & sepal_width"] = correlation


covariance = np.sum((petal_width - mean_petal_width) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_width) * np.sqrt(var_sepal_width))
correlation
dictsetosa["petal_width & sepal_width"] = correlation


covariance = np.sum((petal_width - mean_petal_width) * (petal_length - mean_petal_length)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_width) * np.sqrt(var_petal_length))
correlation
dictsetosa["petal_width & petal_length"] = correlation

sorteddatasetosa=sorted(dictsetosa.items(),key=lambda x:x[1],reverse=True)
sorteddatasetosa

"""virginica"""

virginicadata = data.iloc[:, 4] == "virginica"
virginicadata = data[virginicadata]

sepal_length=np.array(virginicadata.iloc[:, 0])
mean_sepal_length=mean(sepal_length)
var_sepal_length = variance(sepal_length)

sepal_width=np.array(virginicadata.iloc[:,1])
mean_sepal_width=mean(sepal_width)
var_sepal_width = variance(sepal_width)


petal_length=np.array(virginicadata.iloc[:,2])
mean_petal_length=mean(petal_length)
var_petal_length = variance(petal_length)


petal_width=np.array(virginicadata.iloc[:,3])
mean_petal_width=mean(petal_width)
var_petal_width = variance(petal_width)

dictvirginica={}

covariance = np.sum((sepal_length - mean_sepal_length) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_sepal_width))
correlation
dictvirginica["Sepal_length & sepal_width"] = correlation


covariance = np.sum((sepal_length - mean_sepal_length) * (petal_length - mean_petal_length)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_petal_length))
correlation
dictvirginica["Sepal_length & petal_length"] = correlation

covariance = np.sum((sepal_length - mean_sepal_length) * (petal_width - mean_petal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_petal_width))
correlation
dictvirginica["Sepal_length & petal_width"] = correlation


covariance = np.sum((petal_length - mean_petal_length) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_length) * np.sqrt(var_sepal_width))
correlation
dictvirginica["petal_length & sepal_width"] = correlation


covariance = np.sum((petal_width - mean_petal_width) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_width) * np.sqrt(var_sepal_width))
correlation
dictvirginica["petal_width & sepal_width"] = correlation


covariance = np.sum((petal_width - mean_petal_width) * (petal_length - mean_petal_length)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_width) * np.sqrt(var_petal_length))
correlation
dictvirginica["petal_width & petal_length"] = correlation

sorted_dict_data_virginica=sorted(dictvirginica.items(),key=lambda x:x[1],reverse=True)
sorted_dict_data_virginica

"""versicolor"""

versicolordata = data.iloc[:, 4] == "versicolor"
dataversicolor = data[versicolordata]

sepal_length=np.array(dataversicolor.iloc[:, 0])
mean_sepal_length=mean(sepal_length)
var_sepal_length = variance(sepal_length)

sepal_width=np.array(dataversicolor.iloc[:,1])
mean_sepal_width=mean(sepal_width)
var_sepal_width = variance(sepal_width)

petal_length=np.array(dataversicolor.iloc[:,2])
mean_petal_length=mean(petal_length)
var_petal_length = variance(petal_length)



petal_width=np.array(dataversicolor.iloc[:,3])
mean_petal_width=mean(petal_width)
var_petal_width = variance(petal_width)

dictversicolor={}

covariance = np.sum((sepal_length - mean_sepal_length) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_sepal_width))
correlation
dictversicolor["Sepal_length & sepal_width"] = correlation


covariance = np.sum((sepal_length - mean_sepal_length) * (petal_length - mean_petal_length)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_petal_length))
correlation
dictversicolor["Sepal_length & petal_length"] = correlation


covariance = np.sum((sepal_length - mean_sepal_length) * (petal_width - mean_petal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_sepal_length) * np.sqrt(var_petal_width))
correlation
dictversicolor["Sepal_length & petal_width"] = correlation


covariance = np.sum((petal_length - mean_petal_length) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_length) * np.sqrt(var_sepal_width))
correlation
dictversicolor["petal_length & sepal_width"] = correlation

covariance = np.sum((petal_width - mean_petal_width) * (sepal_width - mean_sepal_width)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_width) * np.sqrt(var_sepal_width))
correlation
dictversicolor["petal_width & sepal_width"] = correlation


covariance = np.sum((petal_width - mean_petal_width) * (petal_length - mean_petal_length)) / len(sepal_length)
correlation = covariance / (np.sqrt(var_petal_width) * np.sqrt(var_petal_length))
correlation
dictversicolor["petal_width & petal_length"] = correlation

sortedversicolor=sorted(dictversicolor.items(),key=lambda x:x[1],reverse=True)
sortedversicolor

# import pandas as pd


# grouped_data = data.groupby('species')

# for species, group in grouped_data:
#     print(f"Correlation coefficients for {species}:")


#     correlation = group.corr()


#     sorted_correlation = correlation.unstack().sort_values(ascending=False)
#     sorted_correlation = sorted_correlation[sorted_correlation != 1]


#     for pair, correlation_coefficient in sorted_correlation.items():
#         print(f"Attributes: {pair}, Correlation: {correlation_coefficient}")

#     print("\n")

"""plots"""

import matplotlib.pyplot as plt


X = df
X = np.array(X)


plt.figure(figsize=(18, 4))

plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], c='r', s=60, alpha=0.4)
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')


plt.subplot(1, 3, 2)
plt.scatter(X[:, 0], X[:, 2], c='b', s=60, alpha=0.4)
plt.xlabel('sepal_length')
plt.ylabel('petal_length')


plt.subplot(1, 3, 3)
plt.scatter(X[:, 0], X[:, 3], c='g', s=60, alpha=0.4)
plt.xlabel('sepal_length')
plt.ylabel('petal_width')

plt.show()