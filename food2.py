#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv("Food_Establishment_Inspection_Data.csv" , low_memory=False)
df.head()


# In[93]:


df["City"] = df["City"].apply(lambda x : x.lower().title() )
df.head()


# In[94]:


sns.catplot(data= df, x="Inspection Closed Business", y="Inspection Score", hue="Grade", kind="point")


#                    شود True آن Inspection Closed Business رستوران هایی که امتیاز بالا کسب میکنند یعنی مرتکب تخلفات بیشتری شده اند که منجر میشود  

# In[4]:


sns.catplot(
    data=df,
    x="Grade", y="Inspection Score", kind="boxen",
)


# In[ ]:


یک دارند با وجود تعداد زیاد ولی از لحاظ امتیاز در وضعیت بهتری هستند Grade به طور کلی رستوران هایی که


# In[95]:


sns.scatterplot(x='Longitude',y='Latitude',hue=(df['Description']=='Seating 0-12 - Risk Category III') ,data= df, legend= False)
#ax[1,1].set_title("The distribution of inspections by risk",size=20)
#ax[1,1].set_xlabel('Longitude')
#ax[1,1].set_ylabel('LATITUDE')
#, ax=ax[1,1]


# In[40]:


df['Inspection Date']=pd.to_datetime(df['Inspection Date'])

df['year']=pd.DatetimeIndex(df['Inspection Date']).year
df.head()


# In[106]:


fig,ax=plt.subplots(figsize=(20,20))
x=df.year.value_counts().index
y=df.year.value_counts()
sns.barplot(x=x,y=y,ax=ax)
ax.set_title("The counts of inspection by year",size=20)
ax.set_ylabel('counts',size=18)
ax.set_xlabel('')


# In[ ]:


تعداد بازرسی ها در هر سال نشان داده شده است 


# In[155]:


dfgrade=df.groupby(['Grade','year'])['Inspection Date'].agg('count').unstack('Grade')
dfgrade


# In[156]:


fig,ax=plt.subplots(figsize=(20,16))
dfgrade.plot(kind='bar',ax=ax)
ax.tick_params(axis='x',labelrotation=360)
ax.legend(loc=0, ncol=1, fontsize=14,bbox_to_anchor=(1.15,0.75))
ax.set_title("The counts of Grade of Inspection Date by year ",size=20)
ax.set_ylabel('counts',size=18)


#     تعداد بازرسی های انجام شده برای هر گرید در سال را نشان میدهد که با توجه به تعداد گریدهای یک تعداد بازرسی های بیشتری هم دارند 

# In[157]:


dfv=df.groupby(['Violation Type','year'])['Inspection Date'].agg('count').unstack('Violation Type')
dfv


# In[159]:


fig,ax=plt.subplots(figsize=(20,16))
dfv.plot(kind='bar',ax=ax)
ax.tick_params(axis='x',labelrotation=360)
ax.legend(loc=0, ncol=1, fontsize=14,bbox_to_anchor=(1.15,0.75))
ax.set_title("The counts of Violation Type  of Inspection Date by year ",size=20)
ax.set_ylabel('counts',size=18)


#    در هر سال را نشان میدهد که با توجه به نمودار در سال های 2014 و 2015 و 2016 تفاوت چشمگیری دارند Violation Type تعداد 

# In[26]:


df1 =df.groupby(['Grade','Inspection Result']).count().reset_index()
df1


# In[35]:


df2 =df.groupby(['Grade','Business_ID','Inspection Type']).count().reset_index()
df2


# In[ ]:





# In[28]:


df3=df.groupby(['Business_ID','Grade'])['Inspection Result'].nunique()

df3.head()


# In[142]:


fig,ax=plt.subplots(1,1,figsize=(20,10))
x=df['Inspection Result'].value_counts().index
y=df['Inspection Result'].value_counts()
sns.barplot(x=x,y=y,ax=ax)

ax.tick_params(axis='x', rotation=90)

#fig, ax = plt.subplots(1,1, figsize = (10,5))
#ax = sns.scatterplot(data = df,x = "Inspection Result" , y = "Inspection Score")
plt.draw()

#ax.set_xticks(range(len(ax.get_xticks())));
#ax.set_xticklabels(ax.get_xticklabels() , rotation = 90 );





# سه نتیجه پرتکرار بازرسی ها مشاهده میشود

# In[146]:


fig,ax=plt.subplots(1,1,figsize=(10,7))
sns.scatterplot(x='Longitude',y='Latitude',hue='Violation Type',hue_order=['BLUE','RED'] ,data= df[df['Inspection Result']=='Unsatisfactory'], ax=ax)
ax.set_title("The distribution of Violation Type for Unsatisfactory",size=10)
ax.set_xlabel('Longitude')
ax.set_ylabel('LATITUDE')

plt.draw()




# با توجه به نوع تخلف نشان داده شده که تقریبا در همه موارد نوع آن  است   Unsatisfactory نتیجه بازرسی 

# In[148]:


fig,ax=plt.subplots(1,1,figsize=(10,7))
sns.scatterplot(x='Longitude',y='Latitude',hue='Violation Type',hue_order=['BLUE','RED'] ,data= df[df['Inspection Result']=='Satisfactory'], ax=ax)
ax.set_title("The distribution of Violation Type for satisfactory",size=10)
ax.set_xlabel('Longitude')
ax.set_ylabel('LATITUDE')
plt.draw()


# توزیع نتیجه بازرسی  برای آن نشان داده شده است که نوع تخلف آن نیز با توجه به رنگ آن قابل مشاهده است :Satisfactory 

# In[150]:


fig,ax=plt.subplots(1,1,figsize=(10,7))
sns.scatterplot(x='Longitude',y='Latitude',hue='Violation Type',hue_order=['BLUE','RED'] ,data= df[df['Inspection Result']=='Complete'], ax=ax)
ax.set_title("The distribution of Violation Type for Complete ",size=10)
ax.set_xlabel('Longitude')
ax.set_ylabel('LATITUDE')
plt.draw()


#  توزیع این نتیجه نشان میدهد مقدارآن نسبت به دو نتیجه دیگر بسیار اندک است : Complete

# In[152]:


fig,ax=plt.subplots(1,1,figsize=(5,3))
x=df['Inspection Type'].value_counts().index
y=df['Inspection Type'].value_counts()
#ax= sns.barplot(x=x,y=y)
                
ax = sns.barplot(data=df , x = x , y= y)
ax.tick_params(axis='x', rotation=90)


#  تعداد آن در هر حالت نشان داده شده است : Inspection Type

# In[57]:


dfdf = df.groupby(['year','Inspection Type'])["City"].agg('count').unstack('Inspection Type')
dfdf


# In[65]:


fig,ax=plt.subplots(figsize=(15,16))
dfdf.plot(ax=ax,color=['red','yellow','green'])
ax.legend(loc=0, ncol=1, fontsize=14,bbox_to_anchor=(1.15,0.75))
ax.set_title("The counts of Inspection Type by year",size=20)
ax.set_ylabel('counts',size=18)


# بررسی هر سه حالت آن برای سال های مختلف نشان داده شده است: Inspection Type

# In[12]:


df.groupby(['Inspection Type','Inspection Date'])['Inspection_Serial_Num'].agg('count')


# In[123]:


df.groupby(['Inspection Type','Inspection Date'])['Inspection_Serial_Num'].value_counts()


# In[124]:


df.groupby(['Inspection Result'])['Grade'].value_counts()


# In[34]:


df1=df.groupby("Business_ID").nunique().loc[df[df["Latitude"].isna()]["Business_ID"].unique()].sum()
df1


# In[ ]:





# In[76]:


df[['capacity','Risk_category']]= df['Description'].str.split(" - ",expand=True)

df.head()


# In[45]:


df["Risk_category"].unique()


# In[71]:


df_risk1=df[df['Risk_category']=='Risk Category I']
df_risk1.head(1)


# در سه نمودار زیر   10 شهر که بیشترین تعداد ریسک ها را براساس نوع آن داشته اند میبینیم  

# In[75]:


fig, ax = plt.subplots(figsize = ( 5 , 3 ))
sns.barplot(ax = ax ,x=df_risk1['City'].value_counts()[:10],y=df_risk1['City'].value_counts()[:10].index)

ax.set_xlabel( "count " , size = 12 )
ax.set_ylabel( "City" , size = 12 )
ax.set_title( "Top 10 City Type by the counts of risk 1" , size = 11)


# In[ ]:





# In[72]:


df_risk2=df[df['Risk_category']=='Risk Category II']


# In[74]:


fig, ax = plt.subplots(figsize = ( 5 , 3 ))
sns.barplot(ax = ax ,x=df_risk2['City'].value_counts()[:10],y=df_risk2['City'].value_counts()[:10].index)

ax.set_xlabel( "count " , size = 12 )
ax.set_ylabel( "City" , size = 12 )
ax.set_title( "Top 10 City  by the counts of risk 2" , size = 11 )
plt.show()


# In[76]:


df_risk3=df[df['Risk_category']=='Risk Category III']


# In[77]:


fig, ax = plt.subplots(figsize = ( 5 , 3 ))
sns.barplot(ax = ax ,x=df_risk3['City'].value_counts()[:10],y=df_risk3['City'].value_counts()[:10].index)

ax.set_xlabel( "count " , size = 12 )
ax.set_ylabel( "City" , size = 12 )
ax.set_title( "Top 10 City  by the counts of risk 3" , size = 11 )
plt.show()


# In[78]:


df["City"].unique()


# In[72]:


fig,ax=plt.subplots(figsize=(15,10))
y=df['Violation Description'].value_counts()[:10].index
x=df['Violation Description'].value_counts()[:10]
sns.barplot(x=x,y=y,ax=ax)
ax.set_title("Top 10 Violation Description by the counts of inspection ",size=20)
ax.set_xlabel('counts',size=18)
ax.set_ylabel('', size = 51)
plt.show()


#  ده تای پرتکرار:Violation Description

# In[77]:


data1 = df[df["City"]=='Seattle']
data1


# In[91]:


data1=data1.dropna(subset=['Latitude','Longitude','Risk_category'])
data1.isnull().sum()


# In[92]:


fig,ax=plt.subplots(figsize=(9,7))
sns.scatterplot(x='Longitude',y='Latitude',hue='Risk_category',hue_order=['Risk Category I','Risk Category II','Risk Category III'] ,data=data1, ax=ax)
ax.set_title("The distribution of Risk_category for Seattle ",size=9)
ax.set_xlabel('Longitude')
ax.set_ylabel('LATITUDE')


# توزیع ریسک  برای شهر سیاتل 

# In[160]:


fig,ax=plt.subplots(figsize=(9,7))
sns.scatterplot(x='Longitude',y='Latitude',hue='Violation Type',hue_order=['BLUE','RED'] ,data=data1, ax=ax)
ax.set_title("The distribution of Violation Type  ",size=9)
ax.set_xlabel('Longitude')
ax.set_ylabel('LATITUDE')


# توزیع نوع تخلف نشان داده شده است

# In[154]:


df5= df.groupby(["Violation Description","Violation Type"])["City"].agg('count').unstack('Violation Type')
df5


# In[ ]:




