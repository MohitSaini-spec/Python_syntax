import pandas as pd
print("Version :", pd.__version__)

# Series
a =[1,2,3,4,5,6,7,8,9,0]
my=pd.Series(a,index=[1,2,3,4,5,6,7,8,9,0])
print("Series :\n",my)


# dataFrame
print(f'{" Dataframe ":~^50}')

data={

    "key1":[420,380,390],
    "key2":[50,40,45],
    "Key3":[100,105,107]
}
my_var=pd.DataFrame(data)
print("Using DataFrames :\n",my_var)

# Locate Row
print("Selected row:\n",my_var.loc[0])

# df = pd.read_csv("data.csv")    #same fro json
# print( df.to_string())

# max rows
print("Default max row : ",pd.options.display.max_rows)
pd.options.display.max_rows=200         #changing max row to display without tostring

# Analysing DAta Frames
print(f'{" Analysing data :":~^50}')
print("Starting 5 element :\n",my_var.head())                    # default 5
print("Ending 5 element :\n",my_var.tail())                    # default 5
print("Info :",my_var.info())

# Cleaning Data
print(f'{" Cleaning Data :":~^50}')

df = pd.read_csv('C:/Users/user/Desktop/Program/Code/python/W3school/20. Ex Modules/Panda/data.csv')
print(df.to_string())
newdf = df.dropna()                     # remove null row
print(newdf)

df.fillna(930,inplace=True)             # replace nulll with 980
print(df)

df["Calories"].fillna(130,inplace=True)
print(df)


xmean =df["Calories"].mean()
xmedian = df["Calories"].median()
xmode = df["Calories"].mode()


ymean = df["Calories"].fillna(xmean)
ymedian = df["Calories"].fillna(xmedian)
ymode = df["Calories"].fillna(xmode)

# Wrong data
hi = pd.read_csv("C:/Users/user/Desktop/Program/Code/python/W3school/20. Ex Modules/Panda/hi.csv")
print("odhofhohfouhfhsohfgd",hi.info())
hi["Date"] = pd.to_datetime(hi["Date"])
# removw wrong data
hi.dropna(subset=['Date'], inplace = True)
print(hi.to_string())

# WRONG DATA
df.loc[7,"Duratoion"] = 45

# Changing data
for x in df.index:
    if df.loc[x,"Duration"] > 120:
        df.loc[x,"Duration"]=120

# Remove row
for x in df.index:
    if df.loc[x,"Duration"]>120:
        df.drop(x,inplace=True)

# DISCOVERY DUPLICATE
print(df.duplicated())
df.drop_duplicates(inplace=True)

# data correlation
df.corr()

# PLOTTING
import matplotlib.pyplot as plt
df.plot(kind="scatter",x = "Duration",y = "Pulse")
df.plot(kind="hist")
plt.show()

