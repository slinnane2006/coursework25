import pandas as pd

#Set file path
file_path = 'raw_data.csv'

#Read the file using Python data
data = pd.read_csv(file_path, na_values=['no data'])

#Remove special characters like €
data= data.replace({r'\*':''}, regex= True)

#Save cleaned data to a new file
cleaned_file_path = 'cleandata.csv'
data.to_csv(cleaned_file_path, index=False)

print("the file has been cleaned", cleaned_file_path)


import matplotlib.pyplot as plt
import pandas as pd


file_path = 'cleandata.csv'
data = pd.read_csv(file_path, na_values=['no data'], encoding= 'utf-8')

df = pd.DataFrame(data)

X = list(df.iloc[:,2])
Y = list(df.iloc[:,3])

width = 0.05

#create the bar chart
plt.bar(X, Y, color='b', width=width) # set width of bars
plt.title("Sleep hours in relation to attendance ") 
plt.xlabel("Sleep hours") 
plt.ylabel("Attendance(%)")
plt.savefig('bar_chart.png')

# Show the plot 
plt.show()



X = list(df.iloc[:,1])
Y = list(df.iloc[:,4])

plt.scatter(X, Y, color='g') 
plt.title("Study hours in relation to grades") 
plt.xlabel("Study hours") 
plt.ylabel("Grades")
plt.savefig('scatter_chart.png')

plt.show()
