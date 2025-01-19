
import matplotlib.pyplot as plt
import numpy as np

# PLOTTING
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

#plt.plot(xpoints, ypoints ,marker="o",ms=15)
#plt.plot(ypoints, linestyle = 'dashed')
#plt.plot(ypoints, ls = ':')
#plt.plot(ypoints, color = 'r') or (ypoint,c="r")
#plt.plot(ypoints, linewidth = '20.5')

plt.subplot(2, 3, 1)
plt.plot(xpoints,ypoints,'o:r',ms=15,mec="b",mfc="w")

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1,loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)



# BARS
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 2)
plt.bar(x,y ,width=0.5)

plt.subplot(2, 3, 3)
plt.barh(x,y ,color="red")

# HISTOGRAM
x = np.random.normal(170, 10, 250)
plt.subplot(2, 3, 4)
plt.hist(x)

# PIECHART
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.subplot(2, 3, 5)
plt.pie(y, labels = mylabels,startangle=90,explode=myexplode,shadow=True)
plt.legend(title="fruits")

# SCATTERED

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.subplot(2, 3, 6)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()