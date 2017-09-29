import copy
import math
import random
Max = 999999999
Min = 0.0000001
#define job
class Job():
    def __init__(self,id,source,bestfrequency):
        self.id = id
        self.resource = source
        self.best = bestfrequency

class Machine():
    def __init__(self,id, source,frequency):
        self.id = id
        self.source = source
        self.initalFrequency = frequency

Joblist =[]

j1 = Job(1,5,1000)
j2 = Job(2,20,2000)
j3 = Job(3,15,3000)
j4 = Job(4,40,2500)
j5 = Job(5,30,1500)
j6 = Job(6,25,1800)
j7 = Job(7,35,1700)
j8 = Job(8,29,1937)
j9 = Job(9,47,1354)
j10= Job(10,35,2119)
#for i in range (0,5):
Joblist.append(j1)
Joblist.append(j2)
Joblist.append(j3)
Joblist.append(j4)
Joblist.append(j5)
Joblist.append(j6)
Joblist.append(j7)
Joblist.append(j8)
Joblist.append(j9)
Joblist.append(j10)
m1 = Machine(0,50,2000)
m2 = Machine(1,60,1500)
m3 = Machine(2,50,1700)
mlist =[m1,m2,m3]
solnum =5
sol = [[0 for i in range(len(Joblist))] for j in range(solnum)]
def Initailzation(Machinelist,Joblist,solnum):

    for i in range(0,solnum):
        for j in range(0,len(Joblist)):
            sol[i][j]=random.randint(1,len(Machinelist))
        print(sol[i])

p=1
#Initailzation(mlist,Joblist,solnum)
# Single point mutation
def Mutation(population,p):
    for i in range (0,len(population)):
        pob=random.uniform(0,1)
        if(pob-p<0.0000001):
                choro = population[i]
                num =  random.randint(0,len(Joblist)-1)
                choro[num] = random.randint(1,len(mlist))
                population[i] = choro
    return population
#Mutation(sol,p)
#print(sol)
def Crossover(population):

    num1 = 0
    num2 = 0
    while(num1==num2):
        num1 = random.randint(0, len(population)-1)
        num2 = random.randint(0,len(population)-1)
    Parent1 = population[num1]
    Parent2 = population[num2]
    offspring = []
    mid = random.randint(0,len(Parent1))
    for i in range (0,len(Parent1)):
        if(i<mid):
            offspring.append(Parent1[i])
        else:
            offspring.append(Parent2[i])
    #print(mid,Parent1,Parent2,offspring)
       # mid = chrosome[num1]
       # chrosome[num1] = chrosome[num2]
       # chrosome[num2] = mid
        #print(chrosome)
    return offspring
#Crossover(sol)

def Selection(population,fitgroup):
  offspring = []

  sumfit =0
  count =0
  bestfit = 0.0
  bestnum = 0
  worstnum = 0
  for i in range(0,len(fitgroup)):
      sumfit = sumfit + fitgroup[i]
      #print(fitgroup[i])

      if(fitgroup[i]-bestfit>Min):
          bestfit = fitgroup[i]
          bestnum = i
  #print(sumfit)
  while(count<len(fitgroup)):
        pob = random.uniform(0, 1)
        curfit = 0.0
        count = count + 1
        minfit = Max
        for i in range(0, len(fitgroup)):
            curfit = curfit+1.0/sumfit*fitgroup[i]
            if (pob-curfit<Min):
                #print(i)
                offspring.append(population[i])
                #print(pob)
                #print(curfit,i)
                if(fitgroup[i]-minfit<Min):
                    minfit = fitgroup[i]
                    worstnum = i
                break

  offspring[worstnum]=population[bestnum]
  return offspring


def transfer(freq,best):
    normal = 1+(freq-best)/100* 0.1
    return normal

def calPcost(freq):
    power = (freq/1000)**3
    return  power

def DVFS(best,curfre):
    if(best>curfre):
        curfre= curfre+1
        return curfre
    elif(best==curfre):
        return curfre
    else:
        curfre = curfre - 1
        return curfre


def Evaulation(chrosome,a,b):
    sol = chrosome
    curmac = []
    curjob = []
    curfre = 0
    time = [0,0]
    t_interval = 1
    p_cost = 0
    for i in range(0,len(sol)):
        curmac = mlist[chrosome[i]-1]
        curfre = curmac.initalFrequency
        curjob = Joblist[i]
        jobSource = Joblist[i].resource
        best = curjob.best
        while(jobSource>0):
         #print(jobSource)
         cur_finish = transfer(best,curfre)
         curfre=DVFS(best,curfre)
         jobSource = jobSource-cur_finish
         time[curmac.id-1]= time[curmac.id-1]+t_interval
         p_cost = calPcost(curfre)
    makespan = 0
    for i  in range(0,len(time)):
        if (time[i]>makespan):
            makespan  = time[i]
    fitness = 0
    fitness = makespan
    #print(fitness)
    return fitness


#Main

Initailzation(mlist,Joblist,solnum)
fitgroup = [0 for i in range(len(sol))]
x=1
y=0
final = []

for a in range(0,5):
    #print(sol)

    Gene = []
    for i in range(0,len(sol)):
        mid = Crossover(sol)
        Gene.append(mid)
        fitgroup[i] = Evaulation(mid, x, y)
        print("fitness",i,fitgroup[i])
    Sol = Selection(Gene,fitgroup)
    Mutation(sol, p)
#print(sol)



