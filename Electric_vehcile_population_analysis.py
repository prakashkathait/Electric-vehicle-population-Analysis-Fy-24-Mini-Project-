import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv(r'D:\Python Projects\Electric_Vehicle_Data.csv\Electric_Vehicle_Data.csv')

# Set display options
pd.set_option('display.width', None)          # Automatically adjust the display width to the console size
pd.set_option('display.max_columns', None)    # Display all columns
pd.set_option('display.max_colwidth', None)   # Display full column width

# Display the first few rows
# print(df.head())

# Check for rows and columns
# print(df.info())
# print(df.isnull().sum())  #checking the null values in the dataset
# print(df.shape) #check rows and col.
# print(df['Make'].unique()) # unique makes

# print(df['Make'].value_counts()) #check for value counts

'''Distribution of Makes'''

top_makes = df['Make'].value_counts().head(5)
plt.figure(figsize=(10,6))
top_makes.plot(kind='bar',color=['salmon','pink','lightgreen','gold','darkgreen'])
plt.title('Distribution of make')
# print(plt.show())

'''Distribution by country'''

top_makes = df['County'].value_counts().head(10)
plt.figure(figsize=(10,6))
top_makes.plot(kind='bar',color=['salmon','pink','lightgreen','gold','lightcoral','blue','red','skyblue','yellow','darkgreen'])
plt.title('Distribution by country')
# plt.show()

'''Countrywise distribution of make'''

king_data = df[df['County']=='King']
unique_makes = king_data['Make'].value_counts().head(10)
plt.figure(figsize=(10,5))
unique_makes.plot(kind='bar',color=['salmon','pink','lightgreen','gold','lightcoral','blue','red','skyblue','yellow','darkgreen'])
plt.title('Best selling cars at King')
# plt.show()

'''Distribution by Model'''

makes = df['Model'].value_counts().head(5)
plt.figure(figsize=(10,5))
makes.plot(kind='bar',color=['gold', 'darkgreen','salmon','pink' , 'lightgreen'])
plt.title('Best Selling Electric Car-Models')
# plt.show()

'''Distribution by Clean Alternative Fuel Vehicle (CAFV) Eligibility'''

data = df['Clean Alternative Fuel Vehicle (CAFV) Eligibility']
value_counts = data.value_counts()
colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'lightcoral']
plt.figure(figsize=(10,6))
plt.pie(value_counts,labels=value_counts.index,autopct='%1.1f%%',colors=colors,startangle=140)
plt.title('Number of vehicles eligible for clean alternative fuels')
plt.axis('equal')
plt.show()

'''Distribution of Electric Range Vs. Freequency'''
import seaborn as sns

electric_range_data = df["Electric Range"]
plt.figure(figsize=(10,6))
sns.histplot(data=electric_range_data,bins=15,kde=True,color='skyblue',legend=True)
plt.xlabel('Electric Range')
plt.ylabel('Freequency')
plt.title("Power Reserve")
# plt.show()

'''MSRP Analysis'''

df['Base MSRP'].value_counts().head(10)
