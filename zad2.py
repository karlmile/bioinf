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

# inicijalizacija centara za k-means++
def initialize(X, K):
    C = [X[random.randint(0, nopt - 1)]]
    for k in range(1, K):
        print(k)
        D = []
        # prvo odredimo najmanje udaljenosti od vec izabranih sredista
        for i in range(nopt):
            cl_point = 0
            cl_dist = sed(X[i], C[0])
            for j in range(len(C)):
                temp_dist = sed(X[i], C[j])
                if temp_dist < cl_dist:
                    cl_dist = temp_dist
                    cl_point = j
            D.append(cl_dist)
        # sad biramo novu tocku na radnom nacin pomocu distribucije proporcionalne s D^2 (u nasem slucaju je to upravo D)
        # prvo nademo sumu da odredimo koji dio vjerojatnosti pripada danim tockama
        # potom idemo po svim tockama i akumuliramo globalnu vjerojatnost dok ne prijedemo danu radnom vrijednost
        sum_dist = sum(D)
        r = random.random()
        cum_prob = 0
        for i in range(nopt):
            # dodamo djelic vjerojatnosti od tocke na vjerojatnost i porvjerimo je li ju presla
            cum_prob += D[i] / sum_dist
            if cum_prob > r:
                C.append(X[i])
                break
    return C

cent = initialize(x, noc)

gid=[]
for i in range(nopt): # punim listu gid (=group indicator), da bih je poslije mogao samo mijenjati
        gid.append(0)

# main loop, repeated "noi" times
# stavi 800 iteracija za mali set
# stavi 50 iteracija za veliki set
for temp in range(50,1,-2):
        # odredjivanje clustera
        for i in range(nopt):
                c=sed(x[i],cent[0])
                suma=tmp_dist=c
                gid[i]=0
                for j in range(1,noc):
                        c=sed(x[i],cent[j])
                        suma=suma+c
                        if c < tmp_dist:
                                gid[i]=j
                                tmp_dist=c
                gid2=random.randint(0,noc-1)
                a=(1.0*temp/200.0)*(1.0*temp/200.0)*(noc*tmp_dist/suma)
                b=random.random()
                if b<a:
                        gid[i]=gid2      
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


                
        
        
        
        




    

