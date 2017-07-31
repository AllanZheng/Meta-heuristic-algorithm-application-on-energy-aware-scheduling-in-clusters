import copy
import math
import random
Max = 999999999
Min = 0.0000001
#define job
class Job():
    def __init__(self,id, bestfrequency, source):
        self.id = id
        self.source = source
        self.best = bestfrequency

class Machine():
    def __init__(self,id, frequency, source):
        self.id = id
        self.source = source
        self.initalfrequecy = frequency


j1 = Job(1,50,1000)
j2 = Job(2,200,2000)
j3 = Job(3,150,3000)
j4 = Job(4,400,2500)
j5 = Job(5,300,1500)
Joblist =[]
#for i in range (0,5):
Joblist.append(j1)
Joblist.append(j2)
Joblist.append(j3)
Joblist.append(j4)
Joblist.append(j5)
m1 = Machine(1,500,2000)
m2 = Machine(2,600,1500)
mlist =[]
mlist.append(m1)
mlist.append(m2)
solnum =5
sol = [[0 for i in range(solnum)] for j in range(len(Joblist))]
def Initailzation(Machinelist,Joblist,solnum):

    for i in range(0,solnum):
        for j in range(0,len(Joblist)):
            sol[i][j]=random.randint(1,len(Machinelist))
        print(sol[i])
Initailzation(mlist,Joblist,solnum)
p=1
def Mutation(chrosome,p):
    pob=random.uniform(0,1)
    if(pob-p<0.0000001):
        num =  random.randint(0,len(Joblist)-1)
        chrosome[num] = random.randint(1,len(mlist))
        print(chrosome)


def Crossover(chrosome,p):
    pob = random.uniform(0, 1)
    if (pob - p < 0.0000001):
        num = random.randint(0, len(Joblist) - 1)
        chrosome[num] = random.randint(1, len(mlist))
        print(chrosome)
for a in range(0,5):
    print(a)
    Mutation(sol[a],p)
#def Evaulation():

#def Selection():
