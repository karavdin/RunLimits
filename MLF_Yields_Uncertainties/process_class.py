import math
class Process:
    def __init__(self, name):
        self.name = name
        self.typeA = [[]for i in range(3)]
        self.typeB = [[]for i in range(3)]
        self.typeC = [[]for i in range(3)]
        self.rateA = self.typeA[0]        
        self.rateB = self.typeB[0]
        self.rateC = self.typeC[0]
        self.stat_uncA = self.typeA[1]
        self.stat_uncB = self.typeB[1]
        self.stat_uncC = self.typeC[1]
        self.sys_uncA = self.typeA[2]
        self.sys_uncB = self.typeB[2]
        self.sys_uncC = self.typeC[2]
 
    def add_rateA(self,rateA):
        self.typeA[0].insert(0,rateA)

    def add_rateB(self,rateB):
        self.typeB[0].insert(0,rateB)

    def add_rateC(self,rateC):
        self.typeC[0].insert(0,rateC)

    def add_stat_uncA(self,stat_uncA):
        self.typeA[1].insert(0,stat_uncA)
 
    def add_stat_uncB(self,stat_uncB):
        self.typeB[1].insert(0,stat_uncB)
 
    def add_stat_uncC(self,stat_uncC):
        self.typeC[1].insert(0,stat_uncC)

    def add_sys_uncA(self,sys_uncA):
        self.typeA[2].append(sys_uncA)

    def add_sys_uncB(self,sys_uncB):
        self.typeB[2].append(sys_uncB)

    def add_sys_uncC(self,sys_uncC):
        self.typeC[2].append(sys_uncC)

def total_syst_unc(systematics):
    stot =0.
    for sys in systematics:
        s = float(sys)
        stot +=  math.pow(sys,2)
    nsys = math.sqrt(len(systematics))
    sys_unc = math.sqrt(stot)/float(nsys)
    return sys_unc

