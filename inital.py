import copy
import math
import random
Max = 999999999
Min = 0.0000001
excuc = [92.79,85.20,78.99,74.57,69.65,65.59,61.80,58.73,56.15,53.58,51.26,49.19,100.40,110.60]
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
        self.initalFrequency = frequency


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

        num1 = 0
        num2 = 0
        while(num1==num2):
            num1 = random.randint(0, len(Joblist) - 1)
            num2 = random.randint(0,len(Joblist)-1)
        mid = chrosome[num1]
        chrosome[num1] = chrosome[num2]
        chrosome[num2] = mid
        print(chrosome)
for a in range(0,5):
    print(a)
    Crossover(sol[a],p)
fitgroup=[]
def Selection(population,fitgroup):

  pob = random.uniform(0,1)
  sumfit =0
  count =0
  for i in range(0,len(fitgroup)):
      sumfit = sumfit + fitgroup(i)
  while(count<len(population)):
        curfit = 0
        count = count + 1
        for i in range(0, len(fitgroup)):
            curfit = curfit+1.0/sumfit*fitgroup[i]
            if (pob-curfit<0.0000001):
                print(population[i])

def corr(freq):
    excucal = 0
    if freq == 1200:
        excucal = excuc[0]
    elif freq == 1300:
        excucal = excuc[1]
    elif freq == 1400:
        excucal = excuc[2]
    elif freq == 1500:
        excucal = excuc[3]
    elif freq == 1600:
        excucal = excuc[4]
    elif freq == 1700:
        excucal = excuc[5]
    elif freq == 1800:
        excucal = excuc[6]
    elif freq == 1900:
        excucal = excuc[7]
    elif freq == 2000:
        excucal = excuc[8]
    elif freq == 2100:
        excucal = excuc[9]
    elif freq == 2200:
        excucal = excuc[10]
    elif freq == 2300:
        excucal = excuc[11]
    elif freq == 1100:
        excucal = excuc[12]
    elif freq == 1000:
        excucal = excuc[13]
    return excucal


def Evaulation(chrosome,a,b,m1,m2):
    sol = chrosome
    curmac = []
    curjob = []
    curfre = 0
    for i in range(0,len(sol)):
        curmac = mlist.index(i)
        curfre = curmac.initalFrequency

        curjob = Joblist.index(i)
        JobSource = curjob.source
        bestcurjobf =  curjob.best
        







