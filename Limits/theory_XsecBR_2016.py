#!/usr/bin/env python
from ROOT import TGraph

def get_theory_XsecBR_graph(signal_):

    th = list()

    if signal_ == 'n':
        kNLO = 1.0
        th.append([ 500., 5.83131e+01])
        th.append([ 750., 1.36051e+01])
        th.append([1000., 4.50540e+00])
        th.append([1250., 1.80866e+00])
        th.append([1500., 8.13716e-01])
        th.append([1750., 3.97420e-01])
        th.append([2000., 2.05510e-01])
        th.append([2250., 1.10890e-01])
        th.append([2500., 6.17038e-02])
        th.append([2750., 3.52336e-02])
        th.append([3000., 2.05665e-02])
        th.append([3250., 1.21935e-02])
        th.append([3500., 7.34662e-03])
        th.append([3750., 4.46826e-03])
        th.append([4000., 2.75870e-03])
        th.append([4250., 1.72335e-03])
        th.append([4500., 1.09115e-03])
        th.append([4750., 6.99838e-04])
        th.append([5000., 4.58135e-04])
        th.append([5250., 3.04742e-04])
        th.append([5500., 2.07506e-04])
        th.append([5750., 1.44911e-04])
        th.append([6000., 1.03407e-04])


    elif signal_ == 'w':
        kNLO = 1.0
        th.append([ 500., 5.36522e+02])  
        th.append([ 750., 1.31954e+02])   
        th.append([1000., 4.48526e+01])    
        th.append([1250., 1.83735e+01])    
        th.append([1500., 8.47610e+00])    
        th.append([1750., 4.24656e+00])    
        th.append([2000., 2.26215e+00])   
        th.append([2250., 1.26395e+00])
        th.append([2500., 7.34314e-01])
        th.append([2750., 4.41032e-01])
        th.append([3000., 2.72788e-01])
        th.append([3250., 1.73249e-01])
        th.append([3500., 1.12874e-01])
        th.append([3750., 7.53710e-02])
        th.append([4000., 5.15542e-02])
        th.append([4250., 3.61230e-02])
        th.append([4500., 2.59114e-02])
        th.append([4750., 1.90265e-02])
        th.append([5000., 1.42839e-02])
        th.append([5250., 1.09496e-02])
        th.append([5500., 8.55804e-03])
        th.append([5750., 6.80722e-03])
        th.append([6000., 5.50276e-03])

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

