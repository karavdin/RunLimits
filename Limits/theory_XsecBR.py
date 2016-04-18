#!/usr/bin/env python
from ROOT import TGraph

def get_theory_XsecBR_graph(signal_):

    th = list()

    if signal_ == 'n':
        kNLO = 1.0
        #th.append([ 400., 35.77])
        th.append([ 500., 56.27])
        #th.append([ 600., 10.08])
        #th.append([ 700., 5.74])
        th.append([ 750., 12.99])
        #th.append([ 800., 3.32])
        #th.append([ 900., 1.98])
        th.append([1000., 4.25])
        th.append([1250., 1.67])
        th.append([1500., 0.74])
        #th.append([1700., 7.99E-02])
        th.append([2000., 0.18])
        th.append([2500., 5.17E-02])
        th.append([3000., 1.66E-02])
        th.append([3500., 5.66E-03])
        th.append([4000., 2.03E-03])
    elif signal_ == 'w':
        kNLO = 1.0
        #th.append([ 400., 271.98])  
        th.append([ 500., 517.74])  
        #th.append([ 600., 77.71])   
        #th.append([ 700., 43.59])   
        th.append([ 750., 126.05])   
        #th.append([ 800., 25.67])   
        #th.append([ 900., 15.63])   
        th.append([1000., 42.24])    
        th.append([1250., 17.04])    
        th.append([1500., 7.74])    
        #th.append([1700., 0.616])   
        th.append([2000., 2.000])   
        th.append([2500., 0.63])
        th.append([3000., 0.23])
        th.append([3500., 0.093])
        th.append([4000., 0.0425])
    elif signal_ == 'r':
        kNLO = 1.0
        th.append([500., 275.9])
        th.append([750., 62.41])
        th.append([1000., 20.05])
        th.append([1500., 3.519])
        th.append([2000., 0.95])
        th.append([2500., 0.313])
        th.append([3000., 0.1289])
        th.append([3500., 0.0545])

    else:
        print '\n@@@ FATAL -- undefined signal model. stopping script.\n'
        raise SystemExit

    g = TGraph()
    for a in range(0,len(th)):
        g.SetPoint(a,th[a][0]/1000.,th[a][1]*kNLO)

    return g

