import sys
from process_class import Process, total_syst_unc
import math


f = open(sys.argv[1],'r')
all_lines = f.readlines()
#print all_lines

#finding pin-points 
for line in all_lines:
    if '4. Rate Summary' in line:
        idx_1 = all_lines.index(line)
    elif 'DATA' in line: 
        idx_2 = all_lines.index(line)

#saving the info of the data entries

data=[]
datavals = all_lines[idx_2].split('</td><td>')
print datavals
data.insert(0, datavals[1])
data.insert(1,datavals[2])
data.insert(2,datavals[3].replace('</td></tr>',''))

yield_stats = all_lines[idx_1:idx_2]
ctgs = []
ctgsvals = yield_stats[3].split('</th><th>')
ctgs.insert(0, ctgsvals[1])
ctgs.insert(1,ctgsvals[2])
ctgs.insert(2,ctgsvals[3].replace('</th></tr>',''))


samples = []
sample_classes = []
'''
yields_0 = []
yields_1 = []
yields_2 = []
'''


for i in range(4,len(yield_stats)):
    if 'total background' not in yield_stats[i]:
        sample = yield_stats[i].split('</td><td>')[0].replace('<tr><td>','')
        #process = Process(sample)
        samples.append(sample)
for sample in samples:
    print sample
    for i in range(4,len(yield_stats)):
       if sample in yield_stats[i]:
           print yield_stats[i]    
           s = Process(sample)
           s.add_rateA(float(yield_stats[i].split('</td><td>')[1].split('+/-')[0]))
           s.add_stat_uncA(float(yield_stats[i].split('</td><td>')[1].split('+/-')[1]))
           s.add_rateB(float(yield_stats[i].split('</td><td>')[2].split('+/-')[0]))
           s.add_stat_uncB(float(yield_stats[i].split('</td><td>')[2].split('+/-')[1]))
           s.add_rateC(float(yield_stats[i].split('</td><td>')[3].replace('</td></tr>','').split('+/-')[0]))
           s.add_stat_uncC(float(yield_stats[i].split('</td><td>')[3].replace('</td></tr>','').split('+/-')[1]))
           sample_classes.append(s)
    
for s in sample_classes:
    print s.name, s.rateA, s.rateB, s.rateC

for line in all_lines:
    if "<h2>Observable '"+ctgs[0]+ "'</h2>" in line:
        idx_3 = all_lines.index(line)
        print line
    elif "<h2>Observable '"+ctgs[1]+ "'</h2>" in line:
        idx_4 = all_lines.index(line)
        print line 
    elif "<h2>Observable '"+"el_1top_mttbar"+ "'</h2>" in line:
        idx_5 = all_lines.index(line)
        print line
    elif '6. Nuisance Parameter Priors' in line:
        idx_6 = all_lines.index(line)
        print line 
    elif 'Observable' in line:
        print line
systematics0 = all_lines[idx_3:idx_4]
systematics1 = all_lines[idx_4:idx_5]
systematics2 = all_lines[idx_5:idx_6]


for line in systematics0:
    for sample in samples:
        if '<tr><td>'+sample+'</td><td>'in line:
            words = line.split('</td><td>')
            for i in range(len(words)): 
                if '</sup><sub>' in words[i]:
                    start1 = words[i].index('<sup>')+len('<sup>')
                    end1 = words[i].index('</sup>')
                    sup = float(words[i][start1:end1])
                    start2 = words[i].index('<sub>')+len('<sub>')
                    end2 = words[i].index('</sub>') 
                    sub = float(words[i][start2:end2])
                    syst = max(abs(sub),abs(sup))
                    #here append syst of the bkg in this category
                    for s in sample_classes:
                        if s.name in sample and syst<50:
                             s.add_sys_uncA(syst)

'''
for s in sample_classes:
    print s.name, s.rateA + s.sys_uncA
'''
for line in systematics1:
#   sample_classes
   
    for sample in samples:
        if '<tr><td>'+sample+'</td><td>'in line:
            words = line.split('</td><td>')
            for word in words:
                if '</sup><sub>' in word:
                    start1 = word.index('<sup>')+len('<sup>')
                    end1 = word.index('</sup>')
                    sup = float(word[start1:end1])
                    start2 = word.index('<sub>')+len('<sub>')
                    end2 = word.index('</sub>')
                    sub = float(word[start2:end2])
                    syst = max(abs(sub),abs(sup))
                    #here append syst of the bkg in this category
                    for s in sample_classes:
                        if s.name in sample and syst<50:
                             s.add_sys_uncB(syst)

for line in systematics2:
    for sample in samples:
        if '<tr><td>'+sample+'</td><td>'in line:
            words = line.split('</td><td>')
            for word in words:
                if '</sup><sub>' in word:
                    start1 = word.index('<sup>')+len('<sup>')
                    end1 = word.index('</sup>')
                    sup = float(word[start1:end1])
                    start2 = word.index('<sub>')+len('<sub>')
                    end2 = word.index('</sub>')
                    sub = float(word[start2:end2])
                    syst = max(abs(sub),abs(sup))
                    #here append syst of the bkg in this category
                    for s in sample_classes:
                        if s.name in sample and syst<50:
                             s.add_sys_uncC(syst)
'''
for s in sample_classes:
    print s.name, s.rateA, s.sys_uncA, s.sys_uncB, s.sys_uncC
'''
for s in sample_classes:
    sys_uncA = 0.01*s.rateA[0]*total_syst_unc(s.sys_uncA)
    tot_uncA = sys_uncA + s.stat_uncA[0]
    sys_uncB = 0.01*s.rateB[0]*total_syst_unc(s.sys_uncB)
    tot_uncB = sys_uncB + s.stat_uncB[0]
    sys_uncC = 0.01*s.rateC[0]*total_syst_unc(s.sys_uncC)
    tot_uncC = sys_uncC + s.stat_uncC[0]
    print str(s.name) + '& ' + str("%.2f" % s.rateA[0]) + ' \pm '+ str("%.2f" % tot_uncA)  + ' & ' + str("%.2f" % s.rateB[0]) + ' \pm '+ str("%.2f" % tot_uncB) + ' & ' + str("%.2f" % s.rateC[0]) + ' \pm '+ str("%.2f" % tot_uncC) +' \\'  + ' \hline'


print 'DATA &'+ str( data[0]) + ' & '+ str(data[1]) + ' & ' + data[2] + '\\ \hline'
