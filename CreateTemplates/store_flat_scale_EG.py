#! /usr/bin/env python
#Print minus and plus variation for systematics to use as scale for flat "shape" systematics for the channels/categories with limited statistic
#copy of plottemplates_ele_2016_test_FullData_20170910.py
from ROOT import *
import sys
import numpy


#samplelist = {'wjets_c','wjets_b','wjets_l','diboson','qcd'}

#systematic_direction={'__csv_cferr1','__csv_cferr2','__csv_hf','__csv_hfstats1','__csv_hfstats2','__csv_jes','__csv_lf','__csv_lfstats1','__csv_lfstats2','__pileup','__toptag','__mistoptag','__elecID','__elecTRK','__elecHLT','__jer','__jec','__PDF','__q2wjets'}
#samplelist = {'wjets_c','wjets_b','wjets_l','diboson','qcd'}
systematic_direction={'__PDF'}
samplelist = {'ttbar','wjets_l'}
#samplelist = {'wjets_c','wjets_b','wjets_l','diboson','qcd','ttbar'}


# systematic_direction={'__PDF','__q2wjets'}
# samplelist = {'wjets_c','wjets_b','wjets_l'}

categories=['ele_1top_WJetsMVA_chi2_mttbar__','ele_0top_WJetsMVA_chi2_mttbar__','ele_0top_antiWJetsMVA2_antichi2_mttbar__','ele_0top_antiWJetsMVA3_antichi2_mttbar__']
fin = TFile('ele_theta_bdt0p5_chi30_1MttbarBin_addedQ2_addedPDF.root', 'open')
#fin = TFile('ele_theta_bdt0p5_chi30_1MttbarBin_addedQ2.root', 'open')

nominalhist = {}
nominalhistDraw = {}
systvarhist = {}
systvarhistDraw = {}
systvarhistRatio = {}
systvarhistRatioDraw = {}
canvas_Bkg = {}
pad1 = {}
pad2 = {}
gROOT.SetBatch(kTRUE)
#binning = numpy.arange(0,4100,100)
for samp in samplelist:
    for cat in categories:
        nominalhist[cat+samp] = fin.Get(cat+samp)
#        print "Work with ", cat+samp
#        print "Number of events ", nominalhist[cat+samp].GetEntries()
        if(nominalhist[cat+samp].GetEntries()>0):
            for syst in systematic_direction:
                #print 'systematc: ', syst
                canvas_Bkg[cat+samp+syst] = TCanvas("SystVariation_"+cat+samp+syst,"SystVariation_"+cat+samp+syst,800,600)
            #            legend = TLegend(.54,.70,.99,.95) 
#                legend = TLegend(.34,.70,.99,.99) 
                legend = TLegend(.50,.70,.99,.99) 
                gStyle.SetOptStat(0)
                gStyle.SetOptTitle(0)
                
            #Upper plot will be in pad1
                pad1[cat+samp+syst] = TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
            #            pad1.SetBottomMargin(0); # Upper and lower plot are joined
                pad1[cat+samp+syst].SetBottomMargin(5); # Upper and lower plot are not joined
                pad1[cat+samp+syst].SetGridx();         # Vertical grid
                pad1[cat+samp+syst].Draw();             # Draw the upper pad: pad1
                pad1[cat+samp+syst].cd();               # pad1 becomes the current pad
                
                if fin.Get(cat+samp+syst+'__plus') and fin.Get(cat+samp+syst+'__minus'):
                    systvarhist[cat+samp+syst+'__plus'] = fin.Get(cat+samp+syst+'__plus')
                    systvarhist[cat+samp+syst+'__minus'] = fin.Get(cat+samp+syst+'__minus')

#                    systvarhist[cat+samp+syst+'__plus'].Print()
#                    systvarhist[cat+samp+syst+'__minus'].Print()

                    systvarhistDraw[cat+samp+syst+'__plus'] = systvarhist[cat+samp+syst+'__plus'].DrawClone('ep')
                    systvarhistDraw[cat+samp+syst+'__plus'].GetXaxis().SetTitle("M_{ttbar}, GeV")
                    systvarhistDraw[cat+samp+syst+'__plus'].GetXaxis().SetRangeUser(100,2000)
                    systvarhistDraw[cat+samp+syst+'__plus'].SetMarkerColor(kRed)
                    systvarhistDraw[cat+samp+syst+'__plus'].SetMarkerStyle(21)
                    systvarhistDraw[cat+samp+syst+'__plus'].SetLineColor(kRed)
                    systvarhistDraw[cat+samp+syst+'__plus'].SetLineWidth(3)
                
                    systvarhistDraw[cat+samp+syst+'__minus'] = systvarhist[cat+samp+syst+'__minus'].DrawClone('same')
                    systvarhistDraw[cat+samp+syst+'__minus'].SetMarkerColor(kBlue)
                    systvarhistDraw[cat+samp+syst+'__minus'].SetMarkerStyle(21)
                    systvarhistDraw[cat+samp+syst+'__minus'].SetLineColor(kBlue)
                    
                    nominalhistDraw[cat+samp] = nominalhist[cat+samp].DrawClone('same')
                    nominalhistDraw[cat+samp].GetXaxis().SetTitle("M_{ttbar}, GeV")
                    nominalhistDraw[cat+samp].SetMarkerStyle(20)
                    nominalhistDraw[cat+samp].SetMarkerSize(1.5)
                    nominalhistDraw[cat+samp].SetMarkerColor(kBlack)
                    nominalhistDraw[cat+samp].SetLineColor(kBlack)
                    
                    legend.AddEntry(nominalhistDraw[cat+samp],cat+samp+' nominal',"lp")
                    legend.AddEntry(systvarhistDraw[cat+samp+syst+'__plus'],syst+'__plus','lp')
                    legend.AddEntry(systvarhistDraw[cat+samp+syst+'__minus'],syst+'__minus','lp')
                    legend.Draw()
                    #lower plot will be in pad
                    canvas_Bkg[cat+samp+syst].cd();          # Go back to the main canvas before defining pad2
                    pad2[cat+samp+syst] = TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
                    pad2[cat+samp+syst].SetTopMargin(5);
                    pad2[cat+samp+syst].SetBottomMargin(5);
                    pad2[cat+samp+syst].SetGridx(); # vertical grid
                    pad2[cat+samp+syst].Draw();
                    pad2[cat+samp+syst].cd();      # pad2 becomes the current pad
                    systvarhistRatio[cat+samp+syst+'__plus__ratio']  = systvarhistDraw[cat+samp+syst+'__plus'].Clone(cat+samp+syst+'__plus__ratio')
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].Divide(nominalhistDraw[cat+samp])
                    #systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.89,1.11) #flat "shape" systematics
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.8,1.20) #flat "shape" systematics
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetNdivisions(5,5,0)
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetLabelSize(0.12)
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetXaxis().SetLabelSize(0.12)
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetTitle("Variation/Nominal")
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetXaxis().SetTitle("M$_{ttbar}$, GeV")
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].SetMarkerStyle(1)
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].Draw('l')
                    
                    systvarhistRatio[cat+samp+syst+'__minus__ratio']  = systvarhistDraw[cat+samp+syst+'__minus'].Clone(cat+samp+syst+'__minus__ratio')
                    systvarhistRatio[cat+samp+syst+'__minus__ratio'].Divide(nominalhistDraw[cat+samp])
                    systvarhistRatio[cat+samp+syst+'__minus__ratio'].SetMarkerStyle(1)
                    systvarhistRatio[cat+samp+syst+'__minus__ratio'].Draw('same')

                    print '"'+'scale_'+cat+samp+syst+'__plus'+'"'+': '+str(systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetBinContent(1))+", "
                    print '"'+'scale_'+cat+samp+syst+'__minus'+'"'+': '+str(systvarhistRatio[cat+samp+syst+'__minus__ratio'].GetBinContent(1))+", "
                    canvas_Bkg[cat+samp+syst].SaveAs("SystVariation_"+cat+samp+syst+'.pdf')
                else:
                    print '"'+'scale_'+cat+samp+syst+'__plus'+'"'+': '+str(1)+", "
                    print '"'+'scale_'+cat+samp+syst+'__minus'+'"'+': '+str(1)+", "
