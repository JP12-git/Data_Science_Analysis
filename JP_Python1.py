###########################   Data Collection   ##########################
                             
###Used Required Library
import pandas as pd
import sqlite3    # For Database Connection
import openpyxl   # For Excel File Handling

# pd.set_option('display.max_rows',None)     # Show All Rows
# pd.set_option('display.max_columns',None)  # Show All Columns
# pd.set_option('display.width',None)       # Show All Column in one row


### Read csv & Excel File

# data=pd.read_csv("D:/JP PROGRAMING/DATA/DATA.csv")
# data=pd.read_excel("D:/JP PROGRAMING/DATA/DATA.xlsx")
# print(data)


### Read Database Table

# JP=sqlite3.connect("D:/JP PROGRAMING/DATA/JP.db")
# data=pd.read_sql_query("select * from DATA",JP)
# print(data)
# print(data.sample(5))    # Extract Random Five Records


#########################   Data Inspection   ##############################


# Display Columns DataTypes & Shape

# JP=data.info()      # Display Columns DataType
# JP=data.shape       # Display How Many Rows & Columns
# print(JP)


# Listout Of All Columns

# print(data.columns)


#  Display Records Using Index

# print(data.head())    #Show First Five Records
# print(data.tail())    #Show Last Five Records

# JP=data.iloc[14:27]   # Show Records in Specific Range
# print(JP)
# print(data.iloc[23,[2,4,6]])


# print(data.loc[6])    # Show only one Records
# print(data.loc[35,'NAME'])    # show one Records with Specific Columns
# print(data.loc[25,['NAME','AGE','Salary','CITY','DATE']])


# Display Largest & Smallest values 

# print(data.nlargest(3,'Salary'))
# print(data.nsmallest(2,'AGE'))


# Show Particular Columns

# JP=data[['ID','NAME','DATE','Gender','Salary']]
# print(JP)


#########################   Data Cleaning   ##############################


###1 Identify Duplicates

# JP=data[data.duplicated()]
# print(JP)

# Remove duplicate rows

# data = data.drop_duplicates()
# print(data)

# Unique Values Per Columns

# print(data.nunique())

###2 Identify missing values

# print(data.isnull().sum())

# Identify Missing Values only in specific columns

# JP=data[['NAME','AGE','Salary','CITY','Gender']].isna().sum()
# print(JP)

# Remove  missing value

# data=data.dropna()
# print(data)

# Remove Missing Values only in specific columns

# Single Column

# data = data.dropna(subset=['CITY'])
# print(data)

# Multiple Column

# data = data.dropna(subset=['Salary','AGE','Gender'])
# print(data)

# Fill Missing Values

# Fill Single Values

# data["AGE"]=data["AGE"].fillna(data["AGE"].mean())   
# print(data)

# Fill Multiple Values

# data[["NAME","CITY","Salary"]]=data[["NAME","CITY","Salary"]].fillna({"NAME":"Unknown","AGE":data["AGE"].mean(),"Salary":data['Salary'].sum()})

# data[["COURSE","EMAIL","Gender"]]=data[["COURSE","EMAIL","Gender"]].fillna({"COURSE":"IT","EMAIL":"JP","Gender":"Other"})

# print(data)

# Fill Missing Values Using Forward Fill & Backward Fill

# data=data.ffill()         # Fill Missing Values With Above Row Values (Forward)
# data[['Salary','EMAIL']]=data[['Salary','EMAIL']].bfill()     # Fill Missing Values With Below Row Values (Backward)
# print(data)


###3 Convert Columns Strings into Lower & Upper Case

# data['EMAIL']=data['EMAIL'].str.upper()   # Convert Full String 
# data['EMAIL']=data['EMAIL'].str.title()   # Convert Only First Character of Each Words in Uppercase
# print(data)

# Text to Columns

# data[['First_Name','Last_Name']]=data['NAME'].str.split(" ",expand=True)  # Split Full Name into First & Last Name 
# print(data)

# Frequency Distribution of Values in a Column 

# print(data['AGE'].value_counts())


###4 Datatype Conversion

# data[['AGE','Salary']]=data[['AGE','Salary']].astype(int)   # Before Convert Datatype Must Handle Missing Values
# print(data)


## Save cleaned data to a new CSV & new Table

# data.to_csv('Cleaned_data.csv', index=False)
# data.to_sql("Cleaned_data",JP,if_exists="replace",index=False)


#########################   Data Wrangling   ###################################


###5 Remove Column & Rows

# Single Column

# data=data.drop("AGE",axis=1)  # Axis=1 -> Working in Columns (Remove Column)
# print(data)

# Multiple Column

# data=data.drop(["Gender","COURSE"],axis=1) 
# print(data)


# Single Rows

# data=data.drop(5)    # Axis=0 -> Working in Rows (Remove Rows)
# print(data)

# Multiple Rows

# data=data.drop(data.index[5:8])    
# print(data)


###6 Replace Values 

# Single Values

# data=data.replace("Mumbai","India")
# print(data)

# Multiple Values

# data=data.replace(["Hyderabad",22,"Male"],["India","XYZ","Other"])
# print(data)


###7 Rename Columns

# Single Columns 

# data=data.rename(columns={'COURSE':'Course'})
# print(data)

# Multiple Columns 

# data=data.rename(columns={'CITY':'City','AGE':'Age','DATE':'Date'})
# print(data)


###8 Reshaping Data

# Using Pivot

# data=data.pivot(index='ID',columns='Gender',values='CITY')   # Must Remove Duplicates
# print(data)

# Using Pivot Table

# data=data.pivot_table(columns='Gender',values='AGE').mean()
# print(data)


###9 Filtering Data

# Simple Method

# Single Values

# JP=data[data['CITY']=='Chennai']
# print(JP)

# Multiple Values

# JP=data[(data['AGE']>=18) & (data['Gender']=='Male') & (data['COURSE']=='BBA') & (data['Salary']>=45000)]
# print(JP)


# Using Query Function

# Single Values

# data=data.query("CITY =='Surat'")
# print(data)

# Multiple Values

# data=data.query(" AGE >= 18 and Gender =='Male' and CITY =='Pune' and Salary <= 45000 ")
# print(data)


# Using Filter Function

#  Filter Specific Columns

# JP=data.filter(items=['NAME','Gender','AGE','ID','Salary'])     
# print(JP)

#  Label Matching

# JP=data.filter(like='C',axis=1)      #Label Matching Only Work In Columns Name & Rows Index
# JP=data.filter(like='2',axis=0)
# print(JP)

# Using Where Function

# Single Values

# JP=data.where(data['Salary']>=50000).dropna()     # Before Using Where Function Must Handle Missing Values
# print(JP)

# Multiple Values

# JP=data.where((data['Gender']=="Female") & (data['Salary']>=20000) & (data['AGE']>=19)).dropna()   
# print(JP)


###10 Sorting Data

# Column Values (Sort By Value)

# data=data.sort_values(by=['Salary'])   # Sort columns Values in Ascending Order       ## By defult ascending=True then descending=False
# print(data)                                                                                #  When ascending=False then descending=True

# Rows or Columns (Sort By Index)

# data=data.sort_index(ascending=False)   #Sort Rows in Decending Order
# data=data.sort_index(axis=1,ascending=False)   #Sort Columns in Descending Order 
# print(data)


###11 Grouping Data

# Single Column

# JP=data.groupby('Gender').size()           # Aggregate funcation = size(),first(),mean(),median(),sum(),count() 
# print(JP)      

# Multiple Column

# JP=data.groupby('Gender')['AGE'].count()      
# print(JP)


###14 Combining Data

# Example With DataFrame

# data1={
#    'ID':[1,2,3,4,5],
#    'Name':('ABC','PQR','XYZ','DEF','MNO'),
#    'Department':('HR','Account','IT','HR','Sales')
#     }
# data2={
#        'ID':[1,2,3,4,5],
#        'Department':('HR','Account','IT','HR','Sales'),
#        'Salary':(20000,25000,50000,43000,76000)
#    }                                                                     
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)


# Using Concat Function

# JP=pd.concat([df1,df2],axis=1)     # axis=1 -> Concate Columns  ; axis=0 -> Concate Rows

# Using Merge Function

# JP=pd.merge(df1,df2)

# Using Join Function

# data3={
#        'Number':[11,22,33,44,55,66,77,88,99],
#        'Percantage':(202,75,558,43,87,852,93,54,94),
#        'Fees':(6000,6500,2000,4653020,22800,1750,30000,12000,5343453)
#    }

# df3=pd.DataFrame(data3)
# JP=df3.join(df1)   
# print(JP)


###12 Summary Statistics of Numeric Columns

# JP=data.describe()
# print(JP)


###13 Statistics Calculation

# JP=data['Salary'].mean()
# JP=data['Salary'].median()
# JP=data['Salary'].mode()
# JP=data['Salary'].std()
# JP=data['Salary'].var()
# JP=data['Salary'].skew()

# print(JP)


###15 DateTime Feature

# from datetime import datetime   #Used Required Library

# Extract Date Time Components in CSV File & DataBase

# data['DATE']=pd.to_datetime(data['DATE'],dayfirst=True)
# data['Date']=data['DATE'].dt.day
# data['Month']=data['DATE'].dt.month
# data['Year']=data['DATE'].dt.year
# data['Month Name']=data['DATE'].dt.month_name()
# data['Day Name']=data['DATE'].dt.day_name()

# print(data)


##16 Correlation Co-efficients 

# JP=(data['AGE']).corr(data['Salary'])
# print(JP)


###17 Outliners Detection Using  IQR Method  &  Kurtosis

# JP=df3['Fees'].kurt()  ## kurt[ = 0 (NearAbout)-> Normal Distribution ; > 0 (graterthen)-> high chance of Outliners ; < 0 (lessthen)-> Low Chance Of Outliners ]

# Q1=df3['Fees'].quantile(0.25)     #Quartile One (25%)
# Q3=df3['Fees'].quantile(0.75)     #Quartile three(75%)

# IQR=Q3-Q1   # IQR(Inter Quartile Range)

# JP=df3[(df3['Fees'] < (Q1 - 1.5 * IQR)) | (df3['Fees'] > (Q3 + 1.5 * IQR))] # Lower & Upper Bound ( Any Value Below to Q1 or Above to Q3 is Outliners )
 
# print(JP)


###18 Feature Enginerring 

# Create Columns 

# data['Tax (25%)']=data['Salary'] * 0.25
# data['Salary_After_Tax']=data['Salary'] - data['Tax (25%)']
# print(data)

# Modified Columns

# data['AGE']=pd.cut(data['AGE'],bins=[0,18,22,25,30],labels=["Teen","Young","Mature","Exprienced"])
# print(data)


###19 Encoding Columns  

# One Hot Encoding Columns 

# JP=pd.get_dummies(data,columns=['Gender'],dtype=int)         # Convert Categorical Columns into Numeric Columns [ When categories do NOT have any order ]
# print(JP)

# Label Encoding Columns

# from sklearn.preprocessing import LabelEncoder    #Used Required Library

# Example With Dataframe

# JP={
#     'ID':[1,2,3,4,5,6,7,8,9,10],
#     'Course':['BCA','BBA','MBA','BCA','MBA','BBA','BCA','MBA','BBA','BCA'],
#     'Grade':['A','B','A','C','B','A','C','B','A','C']
# }
# data=pd.DataFrame(JP)

# data['Grade']=LabelEncoder().fit_transform(data['Grade'])     #   When categories have order or Multiple categories ; Which is repited 
# data['Course']=LabelEncoder().fit_transform(data['Course'])   
# print(data)

# Example With CSV file or DataBase

# data['CITY_Label_EnCoding']=LabelEncoder().fit_transform(data['CITY'])
# print(data)


###20 Feature Scaling 

## Min Max scaling

# from sklearn.preprocessing import MinMaxScaler     #Used Required Library

# data[['Salary_MinMax','AGE_MinMax']]=MinMaxScaler().fit_transform(data[['Salary','AGE']])  # Scale Numeric Columns Between 0 to 1 (0 is Minimum Value & 1 is Maximum Value)
# print(data)

## Z-Score Scaling 

# from sklearn.preprocessing import StandardScaler    #Used Required Library
 
# data[['Salary_Z-Score','AGE_Z-Score']]=StandardScaler().fit_transform(data[['Salary','AGE']])    # Scale Numeric Columns with Mean=0 & Standard Deviation=1 
# print(data)


#######################   Data Visualization   ############################


#Used Required Library
# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.style.use('ggplot')
# plt.grid(True)

# plt.xlabel('AGE')   # X-Asix Name
# plt.ylabel('Salary')     # Y-Asix Name
# plt.title('Data Visualization',fontsize=30,fontweight="bold",color='Purple')   # Figure Name
 

##1 Line Chart
# plt.fill_between(data['AGE'],data['Salary'],color='skyblue')   #Area Chart
# plt.plot(data['AGE'],data['Salary'],color='orange',linestyle='--',linewidth=1,marker='o',label='My Graph')


##2 Scatter Chart
# plt.scatter(data['AGE'],data['Salary'],color='Purple',marker='*',s=300,label='My Graph')  # s=Size of Marker


##3 Bar Chart
# plt.bar(data['AGE'],data['Salary'],color='Green',label='My Graph')  #Vartical Bar chart
# plt.barh(data['AGE'],data['Salary'],color='Green',label='My Graph')  #Horizontal Bar chart


##4 Histogram Chart
# plt.hist(data['Salary'],bins=20,color='Red',edgecolor='Black',label='My Graph')


##5 Pie Chart

# plt.pie(data['Salary'],autopct='%1.2f%%')
# plt.legend(data['AGE'],loc='lower right')  # Give Name of Graph Using Legend

# Donut Pie Chart

# plt.pie(data['AGE'],wedgeprops=dict(width=0.5),autopct='%1.2f%%',startangle=10)
# plt.legend(data['Salary'],loc='lower right')


##6 Box Chart
# plt.boxplot(df3['Percantage'],label='My Graph') 


#7 Subplot Chart             #Syntax: plt.subplot(nrows,ncolumns,index)     #nrows= Number OF the Rows in figure  
                                                                    
# plt.subplot(3,3,1)                                                         #ncolumn= Number OF the Columns in figure    
# plt.bar(data['AGE'],data['Salary'],color='Green')                          #index= Position OF the Graph
                                                                   
# plt.subplot(3,3,3)                                                 
# plt.hist(data['AGE'],bins=9,color='Red',edgecolor='Black')

# plt.subplot(3,3,7)
# plt.scatter(data['AGE'],data['Salary'],color='Purple')

# plt.subplot(3,3,9) 
# plt.plot(data['AGE'],data['Salary'],color='Green',linestyle='--',marker='o')

# plt.subplot(3,3,5)         
# plt.pie(data['AGE'],labels=data['Gender'],wedgeprops=dict(width=0.5),autopct='%1.1f%%')

#Give Name of Graph Using Legend
# plt.legend(loc='upper right')

#Show Graph
# plt.show()  

