#!/usr/bin/env python
# coding: utf-8

# In[338]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px


# In[339]:


df=pd.read_csv('BankChurners.csv')


# In[340]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[341]:


df.head()


# In[316]:


df.shape


# In[362]:


Churn=df[df['Attrition_Flag']=='Existing Customer']
Churn.shape


# In[318]:


df.describe()


# In[319]:


df.columns


# In[320]:


df.nunique()


# In[321]:


df['Marital_Status'].unique()


# In[322]:


df.isnull().sum()


# In[323]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[324]:


sns.distplot(df['Credit_Limit'])


# In[325]:


import warnings
warnings.filterwarnings('ignore')


# In[326]:


df.duplicated().sum()


# In[327]:


df.info()


# In[170]:


sns.distplot(df['Credit_Limit']),'bins=5'


# In[224]:


sns.boxplot(x=df['Card_Category'] ,y=df['Total_Trans_Amt'])


# In[ ]:


#customers with Platinum card spend more than rest of the other card category


# In[367]:


mean_amounts = df.groupby("Card_Category")["Total_Trans_Amt"].mean()
print(mean_amounts)


# In[374]:


mean_amounts.plot(kind="bar",color=['Blue','Gold','Purple','Silver'])
# add labels for the mean values on the bars
for i, mean in enumerate(mean_amounts):
    plt.text(i, mean, f"{mean:.2f}", ha="center", va="bottom")
plt.title("Mean Transaction Amounts by Card_Category")
plt.xlabel("Card_Category")
plt.ylabel("Mean Total_Trans_Amt")
plt.show()


# In[381]:


print(df.Attrition_Flag.value_counts())
plt.figure(figsize=(4,2))
df.Attrition_Flag.value_counts().plot(kind = "bar")
plt.style.use("fast")
plt.title("Count Type of Customer")
plt.xlabel("Type of Customer")
plt.ylabel("Count")
#rotate the x-axis labels by 360degree
plt.xticks(rotation=360)
plt.show()
plt.close()


# In[349]:


plt.figure(figsize=(6,4))
df.Credit_Limit.plot(kind = "hist")
plt.style.use("seaborn-muted")
plt.title("Credit Limit Distribution")
plt.xlabel("Credit Limit")
plt.ylabel("Number of Customers")
plt.show()
plt.close()


# In[350]:


print(df['Total_Trans_Amt'].mean())
print(df['Total_Trans_Amt'].median())


# In[351]:


plt.figure(figsize=(10, 5))
sns.histplot(x=df['Total_Trans_Amt'], kde=True)
plt.title("Transaction amount distribution")


# In[ ]:


#Transaction volume chart is right skewed too, most transactions are between  2k−
 5k. considering that fact that more credit limit to customers are within this range.


# In[227]:


plt.figure(figsize=(6,4))
sns.lineplot(data = df, x = 'Customer_Age', y = 'Total_Trans_Ct')
plt.show()
plt.close()


# In[347]:


plt.figure(figsize=(6,4))
sns.barplot(data = df,x = 'Card_Category',y = 'Credit_Limit', hue = 'Gender')
plt.show()
plt.close()


# In[348]:


print(df['Credit_Limit'].mean())
print(df['Credit_Limit'].median())


# In[301]:


plt = px.histogram(df, x="Gender", y="Credit_Limit", color="Marital_Status")
plt.show()


# In[302]:


fig = px.histogram(df , x="Education_Level", y="Months_on_book", color="Income_Category")
fig.show()


# In[303]:


df['Credit_Limit'].value_counts()


# #distribution of credit limits in the dataset, and identifying any patterns or outliers 

# In[310]:


df['Credit_Limit'].describe()


# In[ ]:


# the range and distribution of credit limits in the dataset


# In[382]:


plt.figure(figsize=(6,4))
sns.countplot(x=df['Income_Category'], order=df['Income_Category'].value_counts().sort_values(ascending=False).index)
plt.xticks(rotation=360)


# In[329]:


plt.figure(figsize=(6,4))
sns.histplot(x=df['Customer_Age'], kde=True)
plt.title("Customers Age distribution")


# In[336]:


print(df['Customer_Age'].mean())
print(df['Customer_Age'].median())


# In[332]:


# The customer age is even distributed,almost no outlier.average and median age of customers  46. 
# chart also shows that a large number of our customers are between 40 and 50 years old.


# In[346]:


plt.figure(figsize=(6,4))
sns.countplot(x=df['Marital_Status'],order=df['Marital_Status'].value_counts().sort_values(ascending=False).index)
plt.xticks(rotation=90)


# In[353]:


plt.figure(figsize=(6, 4))
sns.histplot(x=df['Total_Trans_Ct'])


# In[354]:


print(df['Total_Trans_Ct'].mean())
print(df['Total_Trans_Ct'].median())
print(df['Total_Trans_Ct'].std())


# In[355]:


#average customer perform64 transactions in year,large number of customers also performs about 80 transactions.


# In[383]:


plt.figure(figsize=(6,4))
sns.countplot(x=df['Months_Inactive_12_mon'],order=df['Months_Inactive_12_mon'].value_counts().sort_values(ascending=False).index)
plt.title('Months of inactivity in a year')              


# In[359]:


plt.figure(figsize=(4,2))
sns.scatterplot(x=df['Months_Inactive_12_mon'], y=df['Credit_Limit'])


# In[384]:


#inactivity does not directly affect credit limit, transaction amount


# In[ ]:





# In[ ]:




