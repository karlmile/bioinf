import matplotlib.pyplot as plt
from matplotlib import style
import sklearn
from sklearn.cluster import KMeans

f=open("podaci005.txt","r")
noc=int(f.readline())
nop=int(f.readline())
dim=int(f.readline())


nv=[]
for i in range(nop):
    a=f.readline()
    x=a.split()
    nv.append(x)
f.close()

for i in range(nop):
    for j in range(dim):
        nv[i][j]=float(nv[i][j])

wcss=[]
for i in range(1,35):
    kmeans=KMeans(n_clusters=i, init="k-means++", random_state=40, n_init="auto")
    kmeans.fit(nv)
    wcss.append(kmeans.inertia_)

x=[]
for i in range(34):
    x.append(i+1)


from scipy import stats
y=x[:]

for i in range(34):
    y[i]=wcss[i]*x[i]*x[i]


MNK=stats.linregress(x,y)
a=MNK.slope
b=MNK.intercept
linereg=x[:]
for i in range(1,35):
    linereg[i-1]=a/i + b/(i*i)

plt.plot(range(10,35), wcss[9:], color="g", linewidth="3")
plt.plot(range(10,35), linereg[9:], color="r", linewidth="3")
plt.xlabel("K - broj clustera")
plt.ylabel("WCSS")
plt.show()

