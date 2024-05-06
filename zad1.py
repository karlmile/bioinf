import random
import math
def sed(x,y): # square of euclidean distance
    dist=0
    for i in range(len(x)):
        dist = dist + (x[i]-y[i])*(x[i]-y[i])
    return dist
def sad(x,y): # simple addition of vectors
        v=[]
        for i in range(len(x)):
                v.append(x[i]+y[i])
        return v
f1=open("podaci005.txt", "r")
f2=open("res005++.txt", "w")
noc=int(f1.readline()) # broj centara
nopt=int(f1.readline()) # broj tocaka
dimpt=int(f1.readline()) # dimenzija tocaka
noi=15 # broj iteracija
x=[]
for i in range(nopt):
    line=f1.readline() # citam jedan redak iz datoteke
    vector=line.split() # splittam redak u listu
    x.append(vector) # appendam listu u matricu
for i in range(nopt):
        for j in range(dimpt):
                x[i][j]=float(x[i][j])



cent=[]
for i in range(noc):
        ind=random.randint(0, nopt-1)
        cent.append(x[ind])


gid=[]
for i in range(nopt): # punim listu gid (=group indicator), da bih je poslije mogao samo mijenjati
        gid.append(0)

# main loop, repeated "noi" times
# stavi 800 iteracija za mali set
# stavi 50 iteracija za veliki set
for temp in range(100
                  ,1,-2):
        print(temp)
        # odredjivanje clustera
        for i in range(nopt):
                c=sed(x[i],cent[0])
                for j in range(1, noc):
                    if(sed(x[i],cent[j])<c):
                        gid[i]=j
                        c=sed(x[i],cent[j])
        # kraj odredjivanja clustera
        # odredjivanje novih centara
        for i in range(noc):
                v=[]
                for j in range(dimpt):
                        v.append(0)
                cl_count=0
                for j in range(nopt):
                        if gid[j]==i:
                                cl_count=cl_count+1
                                v=sad(v,x[j])
                if cl_count>0:
                        for j in range(dimpt):
                                cent[i][j]=v[j]*1.0/cl_count
        # kraj odredjivanja novih centara
        # ispis u file
        obj=0
        for i in range(nopt):
                obj=obj+sed(x[i],cent[gid[i]])        
        f2.write(' %s %3d %20.10f \n' % ('iteration', temp, obj))
        counter=[]
        for i in range(noc):
            cnt = 0
            for j in gid:
                if(j == i):
                    cnt = cnt + 1
            counter.append(cnt)
                    
        print(counter)           
f1.close()
f2.close()
