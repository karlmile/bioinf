from random import randint
import random

a1=[]
x=10000
l=1000
for i in range(x):
    v=[]
    for j in range(l):
        v.append(randint(0,1))
    a1.append(v)

print(a1[0:10])

jed=[]
for i in range(x):
    c=0
    jed.append(0)
    for j in range(l):
        d=j
        c=0
        while(d<l):
            if(a1[i][d]==1):
                c+=1
                d+=1
            else:
                j=d
                break
        if(c>jed[i]):
            jed[i]=c


f=open("uspjesi.txt", "w")

for i in jed:
    f.write(str(i) + "\n")

f.close()


f1 = open("acids.txt", "r")
ak = f1.readline()
f1.close()

bm = []
f1 = open("blosum50.txt", "r")
for i in range(20):
    line = f1.readline()
    vc = line.split()
    bm.append(vc[:])
for i in range(20):
    for j in range(20):
        bm[i][j] = int(bm[i][j])
f1.close()

b1=[]
for i in range(x):
    v=[]
    for j in range(l):
        v.append(random.choice(ak))
    b1.append(v)

for i in range(x):
    print(b1[i])

y="PAPAHPEWA"
m = l
n = len(y)
mm=[]

for elem in b1:
    
   sm = []
   tmp = []
   for i in range(m + 1):
       tmp.append(0)

   for i in range(n + 1):
       sm.append(tmp[:])

   pom = []
   tmp = []
   for i in range(m + 1):
       tmp.append(" ")

   for i in range(n + 1):
       pom.append(tmp[:])

   for i in range(n + 1):
       sm[i][0] = 0
   for i in range(m + 1):
       sm[0][i] = 0

   for i in range(1, n + 1):
       for j in range(1, m + 1):
        tmp = []
        tmp.append(sm[i - 1][j] - 8)
        tmp.append(sm[i][j - 1] - 8)
        bb = bm[ak.index(y[i - 1])][ak.index(elem[j - 1])]
        tmp.append(sm[i - 1][j - 1] + bb)
        tmp.append(0)
        tmp.sort()
        sm[i][j] = tmp[3]
   maks= max(max(el) for el in sm)
   mm.append(maks)


g=open("scoreovi.txt", "w")
for t in mm:
    g.write("%d" % t + "\n")

g.close()

    






