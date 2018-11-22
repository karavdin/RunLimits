#! /usr/bin/env python
from ROOT import *
import sys
import numpy


#'nominal'
#systematic_direction={'__pileup','__toptag','__mistoptag','__muID','__muTRK','__muHLT','__csv_cferr1','__csv_cferr2','__csv_hf','__csv_hfstats1','__csv_hfstats2','__csv_jes','__csv_lf','__csv_lfstats1','__csv_lfstats2','__PDF','__q2ttbar','__q2wjets','__jer','__jec'}
#systematic_direction={'__jec'}
#systematic_direction={'__csv_cferr1','__csv_cferr2','__csv_hf','__csv_hfstats1','__csv_hfstats2','__csv_jes','__csv_lf','__csv_lfstats1','__csv_lfstats2'}
#systematic_direction={'__q2ttbar'} #ttbar
#systematic_direction={'__jer','__jec'}
systematic_direction={'__PDF'}
#systematic_direction={'__q2wjets'} #wjets
#systematic_direction={'__toppt_reweight'}

#samplelist = {'ttbar','wjets_c','wjets_b','wjets_l','diboson','ST','DY','VV'}
samplelist = {'ttbar','wjets_c','wjets_b','wjets_l','ST','DY'}
#samplelist = {'ST','DY'}
#samplelist = {'ttbar'}
#samplelist = {'ttbar','wjets_l'}
#samplelist = {'wjets_l'}
#samplelist = {'qcd_mu'}

#categories=['mu_1top_WJetsMVA_chi2_mttbar__','mu_0top_WJetsMVA_chi2_mttbar__','mu_0top_antiWJetsMVA3_antichi2_mttbar__','mu_0top_antiWJetsMVA2_antichi2_mttbar__']
# categories=['ele_1top_WJetsMVA_chi2_mttbar__','ele_0top_WJetsMVA_chi2_mttbar__','ele_0top_antiWJetsMVA2_antichi2_mttbar__','ele_0top_antiWJetsMVA3_antichi2_mttbar__','ele_0top_antiWJetsMVA2_chi2_mttbar__','ele_0top_antiWJetsMVA3_chi2_mttbar__']
# fin = TFile('ele_theta_wFlatShapeSyst_min200_allPDF_onlyEleStream_rebinned10_addedPDF_addedQ2.root', 'open')

categories=['ele_1top_WJetsMVA_chi2_mttbar__','ele_0top_WJetsMVA_chi2_mttbar__','ele_0top_antiWJetsMVA2_chi2_mttbar__','ele_0top_antiWJetsMVA3_chi2_mttbar__']
#fin = TFile('ele_theta_wFlatShapeSyst_min200_20bins_wTopPtrewSymSyst_rebinned_addedPDF_addedQ2.root', 'open')
#fin = TFile('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF_addedQ2.root', 'open')
fin = TFile('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_25bins_rebinned_addedPDF_addedQ2.root', 'open')

nominalhist = {}
nominalhistDraw = {}
nominalhistUncerDraw = {}
nominalhistUncer = {}
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
        print "Work with ", cat+samp
        print "Number of events ", nominalhist[cat+samp].GetEntries()
        if(nominalhist[cat+samp].GetEntries()>0):
            canvas_Bkg[cat+samp] = TCanvas("Uncert_"+cat+samp,"Uncert_"+cat+samp,800,600)
            legend = TLegend(.35,.90,.99,.99) 
            gStyle.SetOptStat(0)
            gStyle.SetOptTitle(0)
                
            # #Upper plot will be in pad1
            # pad1[cat+samp+syst] = TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
            # pad1[cat+samp+syst].SetBottomMargin(5); # Upper and lower plot are not joined
            # pad1[cat+samp+syst].SetGridx();         # Vertical grid
            # pad1[cat+samp+syst].Draw();             # Draw the upper pad: pad1
            # pad1[cat+samp+syst].cd();               # pad1 becomes the current pad
                
            nominalhistUncer[cat+samp] = nominalhist[cat+samp].Clone()
            for i in range(1,nominalhist[cat+samp].GetNbinsX()+1):
                value = 0
                if nominalhist[cat+samp].GetBinContent(i)>0: 
                    value = 100.*(nominalhist[cat+samp].GetBinError(i)/nominalhist[cat+samp].GetBinContent(i))
                nominalhistUncer[cat+samp].SetBinContent(i,value)         

            nominalhistUncerDraw[cat+samp] = nominalhistUncer[cat+samp].DrawClone('hist')
            nominalhistUncerDraw[cat+samp].GetYaxis().SetRangeUser(0,110.)
            nominalhistUncerDraw[cat+samp].GetYaxis().SetTitle("stat. uncertainty, %")
            nominalhistUncerDraw[cat+samp].GetXaxis().SetTitle("M_{ttbar}, GeV")
            nominalhistUncerDraw[cat+samp].SetMarkerStyle(20)
            nominalhistUncerDraw[cat+samp].SetMarkerSize(1.5)
            nominalhistUncerDraw[cat+samp].SetMarkerColor(kBlack)
            nominalhistUncerDraw[cat+samp].SetFillColor(kBlack)
            nominalhistUncerDraw[cat+samp].SetLineColor(kBlack)

            legend.AddEntry(nominalhistUncerDraw[cat+samp],cat+samp,"f")
            legend.Draw()
            #lower plot will be in pad
                
                    
#             canvas_Bkg[cat+samp+syst].cd();          # Go back to the main canvas before defining pad2
#             pad2[cat+samp+syst] = TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
#             pad2[cat+samp+syst].SetTopMargin(5);
#             pad2[cat+samp+syst].SetBottomMargin(5);
#             pad2[cat+samp+syst].SetGridx(); # vertical grid
#             pad2[cat+samp+syst].Draw();
#             pad2[cat+samp+syst].cd();      # pad2 becomes the current pad
#             systvarhistRatio[cat+samp+syst+'__plus__ratio']  = systvarhistDraw[cat+samp+syst+'__plus'].Clone(cat+samp+syst+'__plus__ratio')
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].Divide(nominalhistDraw[cat+samp])
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.6,1.4)
# #                    systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.89,1.11)
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetNdivisions(5,5,0)
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetLabelSize(0.12)
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetXaxis().SetLabelSize(0.12)
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetYaxis().SetTitle("Variation/Nominal")
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].GetXaxis().SetTitle("M$_{ttbar}$, GeV")
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].SetMarkerStyle(1)
#             systvarhistRatio[cat+samp+syst+'__plus__ratio'].Draw('l')
            
#             systvarhistRatio[cat+samp+syst+'__minus__ratio']  = systvarhistDraw[cat+samp+syst+'__minus'].Clone(cat+samp+syst+'__minus__ratio')
#             systvarhistRatio[cat+samp+syst+'__minus__ratio'].Divide(nominalhistDraw[cat+samp])
#             systvarhistRatio[cat+samp+syst+'__minus__ratio'].SetMarkerStyle(1)
#             systvarhistRatio[cat+samp+syst+'__minus__ratio'].Draw('same')
            canvas_Bkg[cat+samp].SaveAs("Uncert_"+cat+samp+'.pdf')
