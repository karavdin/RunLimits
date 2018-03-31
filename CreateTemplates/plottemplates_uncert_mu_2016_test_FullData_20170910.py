#! /usr/bin/env python
from ROOT import *
import sys
import numpy


#'nominal'
samplelist = {'ttbar','wjets_c','wjets_b','wjets_l','qcd_mu','ST','DY','VV'}
samplesumlist = {'wjets_c','wjets_b','DY'} #qcd_mu added by default


#categories=['mu_1top_WJetsMVA_chi2_mttbar__','mu_0top_WJetsMVA_chi2_mttbar__','mu_0top_antiWJetsMVA3_antichi2_mttbar__','mu_0top_antiWJetsMVA2_antichi2_mttbar__']
#categories=['mu_1top_WJetsMVA_chi2_mttbar__','mu_0top_WJetsMVA_chi2_mttbar__','mu_0top_antiWJetsMVA3_antichi2_mttbar__','mu_0top_antiWJetsMVA2_antichi2_mttbar__','mu_0top_antiWJetsMVA3_chi2_mttbar__','mu_0top_antiWJetsMVA2_chi2_mttbar__']
categories=['mu_1top_WJetsMVA_chi2_mttbar__','mu_0top_WJetsMVA_chi2_mttbar__','mu_0top_antiWJetsMVA3_chi2_mttbar__','mu_0top_antiWJetsMVA2_chi2_mttbar__']
#fin = TFile('mu_theta_wFlatShapeSyst_min200_allPDF_rebinned10_addedPDF_addedQ2.root', 'open')
#fin = TFile('mu_theta_wFlatShapeSyst_min200_allPDF_rebinned01_addedPDF_addedQ2.root', 'open')
#fin = TFile('mu_theta_wFlatShapeSyst_min200_QCDHT_allPDF_rebinned_addedPDF_addedQ2.root', 'open')
#fin = TFile('mu_theta_wFlatShapeSyst_min200_PDFttbarAndWjetsL_rebinned_addedPDF_addedQ2.root', 'open')
#fin = TFile('mu_theta_wFlatShapeSyst_min200_100bins_allPDF_rebinnedSmallBkg_rebinned_addedPDF_addedQ2.root', 'open')
#fin = TFile('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCDt0only_rebinned_addedPDF_addedQ2.root', 'open')
#fin = TFile('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCD_SR_CR4_only_rebinned_addedPDF_addedQ2.root', 'open')
#fin = TFile('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCD_SR_CR4_only_rebinnedSmallBkg_rebinned_addedPDF_addedQ2.root', 'open')
fin = TFile('mu_theta_wFlatShapeSyst_min200_20bins_wTopPtrewSymSyst_rebinned_addedPDF_addedQ2.root', 'open')

nominalhist = {}
nominalhistsum = {}
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
for samp in samplelist:
    for cat in categories:
        nominalhist[cat+samp] = fin.Get(cat+samp)
        if ('qcd_mu' in samp):
            nominalhistsum[cat] = nominalhist[cat+samp]

        print "Work with ", cat+samp
        print "Number of events ", nominalhist[cat+samp].GetEntries()
        if(nominalhist[cat+samp].GetEntries()>0):
            canvas_Bkg[cat+samp] = TCanvas("Uncert_"+cat+samp,"Uncert_"+cat+samp,800,600)
            legend = TLegend(.35,.90,.99,.99) 
            gStyle.SetOptStat(0)
            gStyle.SetOptTitle(0)
                
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
            canvas_Bkg[cat+samp].SaveAs("Uncert_"+cat+samp+'.pdf')

contribution = ' qcd_mu '
for cat in categories:
    for samp in samplesumlist:
        nominalhist[cat+samp] = fin.Get(cat+samp)
        nominalhistsum[cat].Add(nominalhist[cat+samp])
        if('1top_WJetsMVA_chi2' in cat):
            contribution = contribution+' '+samp
    nominalhistsum[cat].Print()

    print "Work with ", cat
    print "Number of events ", nominalhistsum[cat].GetEntries()
    if(nominalhistsum[cat].GetEntries()>0):
        canvas_Bkg[cat] = TCanvas("Uncert_"+cat+"_other","Uncert_"+cat+"_other",800,600)
        legend = TLegend(.15,.90,.99,.99) 
        gStyle.SetOptStat(0)
        gStyle.SetOptTitle(0)
                
        nominalhistUncer[cat] = nominalhistsum[cat].Clone()
        for i in range(1,nominalhistsum[cat].GetNbinsX()+1):
            value = 0
            if nominalhistsum[cat].GetBinContent(i)>0: 
                value = 100.*(nominalhistsum[cat].GetBinError(i)/nominalhistsum[cat].GetBinContent(i))
                nominalhistUncer[cat].SetBinContent(i,value)         
                
        nominalhistUncerDraw[cat] = nominalhistUncer[cat].DrawClone('hist')
        nominalhistUncerDraw[cat].GetYaxis().SetRangeUser(0,110.)
        nominalhistUncerDraw[cat].GetYaxis().SetTitle("stat. uncertainty, %")
        nominalhistUncerDraw[cat].GetXaxis().SetTitle("M_{ttbar}, GeV")
        nominalhistUncerDraw[cat].SetMarkerStyle(20)
        nominalhistUncerDraw[cat].SetMarkerSize(1.5)
        nominalhistUncerDraw[cat].SetMarkerColor(kBlack)
        nominalhistUncerDraw[cat].SetFillColor(kBlack)
        nominalhistUncerDraw[cat].SetLineColor(kBlack)
        
        legend.AddEntry(nominalhistUncerDraw[cat],cat+contribution,"f")
        legend.Draw()
        canvas_Bkg[cat].SaveAs("Uncert_"+cat+"other.pdf")
