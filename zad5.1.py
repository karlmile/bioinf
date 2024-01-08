import math
ak='ARNDCQEGHILKMFPSTWYV'

#### model building function
def mobu(a):
    al=len(a) ## length of alignment
    m=[] #### alignment list
    for i in range(al):
        b=a[i].rstrip()
        m.append(b)
    aw=len(m[0]) ## alignment width
    moma=[] ## model matrix
    ### reading alignment, building model
    for i in range(aw):
        tmp=[]
        for k in range(20):
            tmp.append(1)
        for j in range(al):
            aa=m[j][i]
            bb=ak.index(aa)
            tmp[bb]=tmp[bb]+1
        moma.append(tmp[:])
        for j in range(len(moma[i])):
            moma[i][j]=moma[i][j]/len(moma[i])
            moma[i][j]=math.log(moma[i][j])-math.log(1/20)
    return(moma)



#####still need normalization????, and log (oduzmi log(1/20))
######### model evaluation function: takes a string and a model, evaluates at
######### every position, and returns the value, the evaluated substring, and
######### its position; the model should be in the llr-format

def moev(str,mo,indeks):
    topsc=-1000 ## top score
    topst=[] ## top string
    topp=0 ## top position
    m=len(mo) ## model length
    n=len(str) ## string length
    for i in range(n-m+1):
        tmpsc=0
        for j in range(m):
            a=str[i+j]
            b=ak.index(a)
            tmpsc=tmpsc+mo[j][b]
        if tmpsc>topsc:
            topsc=tmpsc
            topp=i

    if topsc>-1000:
        for i in range(m):
            topst.append(str[topp+i])
    return topsc, topp, topst, indeks

#prvi korak
upit=['FVFGDSLSDA'] 
f1=open("AT.fasta","r")       
bb=mobu(upit)

cc=[]
for i in range(2*33409):
    x=f1.readline()
    x=x.rstrip()
    if(i%2==1):
        cc.append(moev(x,bb,-1))

dd=sorted(cc, key=lambda x: x[0])[::-1]

#drugi korak
for j in range(10):
    cc=[]
    top=100
    mo=[]
    

    novi=[]
    for i in range(top):
        new=''
        for x in dd[i][2]:
            new+=x
        p=[]
        p.append(new)
        novi.append(new)
    mo=mobu(novi)

    f1.seek(0)
    k=0
    for i in range(2*33409):
        x=f1.readline()
        x=x.rstrip()
        if(i%2==1):
            cc.append(moev(x,mo,k))
            k+=1
            

        


    dd=sorted(cc, key=lambda x: x[0])[::-1]

g=open("score.txt","w")  
for i in range(100):
    print(dd[i])
    g.write(str(dd[i][0]))
    g.write('\n')

h=open("sviscore.txt","w")
for i in range(33409):
    h.write(str(dd[i][0]))
    h.write('\n')


g2 = open("ATBioPositives.txt","r") 
g1 = open("AT_imena.txt","r")

pozitivni_indeksi=[]
for i in range(2*33409):
    g2.seek(0)
    a=g1.readline()
    a=a[1:10]
    if(len(pozitivni_indeksi)==104):
        break
    for j in range(104):
        b=g2.readline()
        b=b.rstrip()
        if(a==b):
            pozitivni_indeksi.append(i)
            g2.seek(0)
            break
tp=0
for i in range(104):
    for j in range(100):
        if(dd[j][3]==pozitivni_indeksi[i]):
            tp+=1

print(tp)

h.close()
g.close()
g1.close()
g2.close()



