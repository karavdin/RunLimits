#! /usr/bin/env python
from ROOT import *
import sys
import numpy


#'nominal'
systematic_direction={'__csv_cferr1','__csv_cferr2','__csv_hf','__csv_hfstats1','__csv_hfstats2','__csv_jes','__csv_lf','__csv_lfstats1','__csv_lfstats2','__pileup','__toptag','__mistoptag','__elecID','__elecTRK','__elecHLT','__jer','__jec','__PDF','__q2ttbar','__q2wjets'}
#systematic_direction={'__toppt_reweight'}
#systematic_direction={'__PDF'}

#systematic_direction={'__jer','__jec'}
#systematic_direction={'__PDF','__q2ttbar'}
#systematic_direction={'__PDF','__q2wjets'}
#systematic_direction={'__PDF'}
#systematic_direction={'__csv_cferr1','__csv_cferr2','__csv_hf','__csv_hfstats1','__csv_hfstats2','__csv_jes','__csv_lf','__csv_lfstats1','__csv_lfstats2'}
#systematic_direction={'__pileup','__toptag','__mistoptag','__elecID','__elecTRK','__elecHLT'}
#systematic_direction={'__jer','__jec'}
#systematic_direction={'__PDF'}
#systematic_direction={'__q2ttbar'} #ttbar
#systematic_direction={'__q2wjets'} #wjets
samplelist = {'ttbar','wjets_c','wjets_b','wjets_l','diboson','ST','DY','VV'}
#samplelist = {'wjets_c','wjets_b','wjets_l'}
#samplelist = {'wjets_b','qcd'}
#samplelist = {'ttbar'}
#samplelist = {'wjets_l'}
#samplelist = {'wjets_b'}

#categories=['ele_1top_WJetsMVA_chi2_mttbar__','ele_0top_WJetsMVA_chi2_mttbar__','ele_0top_antiWJetsMVA2_antichi2_mttbar__','ele_0top_antiWJetsMVA3_antichi2_mttbar__']
categories=['ele_1top_WJetsMVA_chi2_mttbar__','ele_0top_WJetsMVA_chi2_mttbar__','ele_0top_antiWJetsMVA2_antichi2_mttbar__','ele_0top_antiWJetsMVA3_antichi2_mttbar__','ele_0top_antiWJetsMVA2_chi2_mttbar__','ele_0top_antiWJetsMVA3_chi2_mttbar__']
#categories=['ele_0top_antiWJetsMVA2_antichi2_mttbar__','ele_0top_antiWJetsMVA3_antichi2_mttbar__'] #CR
#fin = TFile('ele_theta_bdt0p5_chi30_rebinned.root', 'open')
#fin = TFile('ele_theta_bdt0p5_chi30_rebinned_addedQ2.root', 'open')
#fin = TFile('ele_theta_wFlatShapeSyst_rebinned_addedQ2_addedPDF.root', 'open')
#fin = TFile('ele_theta_wFlatShapeSyst_addedPDF_addedQ2_rebinned.root', 'open')
#fin = TFile('ele_theta_wFlatShapeSyst_min200_allPDF_addedPDF_addedQ2_rebinned30.root', 'open')
fin = TFile('ele_theta_wFlatShapeSyst_min200_allPDF_rebinned30_addedPDF_addedQ2.root', 'open')

#fin = TFile('ele_theta_bdt0p5_chi30_addedQ2_addedPDF.root', 'open')

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
        #print "Work with ", cat+samp
        #print "Number of events ", nominalhist[cat+samp].GetEntries()
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
                    systvarhistDraw[cat+samp+syst+'__plus'] = systvarhist[cat+samp+syst+'__plus'].DrawClone('ep')
                    systvarhistDraw[cat+samp+syst+'__plus'].GetXaxis().SetTitle("M_{ttbar}, GeV")
                    systvarhistDraw[cat+samp+syst+'__plus'].GetXaxis().SetRangeUser(100,2000)
                    systvarhistDraw[cat+samp+syst+'__plus'].SetMarkerColor(kRed)
                    systvarhistDraw[cat+samp+syst+'__plus'].SetMarkerStyle(21)
                    systvarhistDraw[cat+samp+syst+'__plus'].SetLineColor(kRed)
                    
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
                   # systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.6,1.4)
                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.89,1.11)
                    #systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.50,1.50) #flat "shape" systematics JEC/JER
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
                    canvas_Bkg[cat+samp+syst].SaveAs("SystVariation_"+cat+samp+syst+'.pdf')
