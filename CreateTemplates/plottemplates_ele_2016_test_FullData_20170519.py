#! /usr/bin/env python
from ROOT import *
import sys
import numpy


# systematic_direction_ttbar={'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)' }
# systematic_direction_wjets={'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)'}
# systematic_direction_otherbkgs = {'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)'}
# systematic_direction_signal= {'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)'}



#'nominal'
systematic_direction={'pileup','q2ttbar'}
#systematic_direction={'__btag','__misbtag'}
#systematic_direction={'__pileup','__btag','__misbtag','__toptag','__mistoptag','__elecID','__elecTRK'}
#systematic_direction={'__q2ttbar','__pileup'} #ttbar
#systematic_direction={'__pileup'} #other
#systematic_direction={'__q2wjets'} #wjets
#samplelist = {'DATA','singletop','diboson','ttbar','wjets','ZprimeNarrow0500','zjets'}
#samplelist = {'singletop','diboson','ttbar','wjets','zjets'}
#samplelist = {'ttbar','wjets','other'}
samplelist = {'ttbar'}
#samplelist = {'other'}
#samplelist = {'wjets'}

#categories=['el_0top0btag_mttbar__','el_0top0btag_mttbar_highChi2__','el_1top_mttbar__','el_1top_mttbar_highChi2__','el_0top1btag_mttbar__','el_0top1btag_mttbar_highChi2__']
#categories=['el_0top0btag_mttbar__','el_0top0btag_mttbar_highChi2__','el_0top1btag_mttbar__','el_0top1btag_mttbar_highChi2__']
categories=['ele_1top_WJetsMVA_mttbar__','ele_0top_WJetsMVA_mttbar__','ele_1top_antiWJetsMVA_mttbar__','ele_0top_antiWJetsMVA_mttbar__']
#fin = TFile('el_theta_20170519.root', 'open')
fin = TFile('ele_theta_bdt0p5_chi30_rebinned.root', 'open')
nominalhist = {}
nominalhistDraw = {}
systvarhist = {}
systvarhistDraw = {}
systvarhistRatio = {}
systvarhistRatioDraw = {}
canvas_Bkg = {}
gROOT.SetBatch(kTRUE)
#binning = numpy.arange(0,4100,100)
for samp in samplelist:
    for cat in categories:
        nominalhist[cat+samp] = fin.Get(cat+samp)
        for syst in systematic_direction:
            print 'systematc: ', syst
            canvas_Bkg[samp] = TCanvas("SystVariation_"+cat+samp+syst,"SystVariation_"+cat+samp+syst,800,600)
            legend = TLegend(.54,.70,.99,.95) 
            gStyle.SetOptStat(0)
            gStyle.SetOptTitle(0)
            
            #Upper plot will be in pad1
            pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
            pad1.SetBottomMargin(0); # Upper and lower plot are joined
            pad1.SetGridx();         # Vertical grid
            pad1.Draw();             # Draw the upper pad: pad1
            pad1.cd();               # pad1 becomes the current pad

            nominalhistDraw[cat+samp] = nominalhist[cat+samp].DrawClone('ep')
            nominalhistDraw[cat+samp].GetXaxis().SetTitle("M_{ttbar}, GeV")
            nominalhistDraw[cat+samp].SetMarkerStyle(20)
            nominalhistDraw[cat+samp].SetMarkerSize(1.5)
            nominalhistDraw[cat+samp].SetMarkerColor(kBlack)
            nominalhistDraw[cat+samp].SetLineColor(kBlack)
            legend.AddEntry(nominalhistDraw[cat+samp],cat+samp+' nominal',"lp")
            systvarhist[cat+samp+syst+'__plus'] = fin.Get(cat+samp+syst+'__plus')
            #systvarhist[cat+samp+syst+'__plus'].Add(nominalhist[cat+samp],-1)
            systvarhistDraw[cat+samp+syst+'__plus'] = systvarhist[cat+samp+syst+'__plus'].DrawClone('same')
 #           systvarhistDraw[cat+samp+syst+'__plus'].GetXaxis().SetTitle("M_{ttbar}, GeV")
#            systvarhistDraw[cat+samp+syst+'__plus'].GetYaxis().SetTitle("nominal - variation")
            systvarhistDraw[cat+samp+syst+'__plus'].SetMarkerColor(kRed)
            systvarhistDraw[cat+samp+syst+'__plus'].SetMarkerStyle(21)
            systvarhistDraw[cat+samp+syst+'__plus'].SetLineColor(kRed)
            legend.AddEntry(systvarhistDraw[cat+samp+syst+'__plus'],syst+'__plus','lp')
            systvarhist[cat+samp+syst+'__minus'] = fin.Get(cat+samp+syst+'__minus')
            #systvarhist[cat+samp+syst+'__minus'].Add(nominalhist[cat+samp],-1)
            systvarhistRatio[cat+samp+syst+'__plus']  = systvarhistDraw[cat+samp+syst+'__plus'].Clone(cat+samp+syst+'__plus__ratio')
            systvarhistRatio[cat+samp+syst+'__plus'].Add(nominalhistDraw[cat+samp],-1)
            systvarhistRatio[cat+samp+syst+'__plus'].Divide(nominalhistDraw[cat+samp])
            
            systvarhistDraw[cat+samp+syst+'__minus'] = systvarhist[cat+samp+syst+'__minus'].DrawClone('same')
            systvarhistDraw[cat+samp+syst+'__minus'].SetMarkerStyle(21)
            systvarhistDraw[cat+samp+syst+'__minus'].SetMarkerColor(kBlue)
            systvarhistDraw[cat+samp+syst+'__minus'].SetLineColor(kBlue)
            legend.AddEntry(systvarhistDraw[cat+samp+syst+'__minus'],syst+'__minus','lp')
            legend.Draw()
            # lower plot will be in pad
            canvas_Bkg[samp].cd();          # Go back to the main canvas before defining pad2
            pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
            pad2.SetTopMargin(0);
            pad2.SetBottomMargin(0.2);
            pad2.SetGridx(); # vertical grid
            pad2.Draw();
            pad2.cd();      # pad2 becomes the current pad
            systvarhistRatioDraw[cat+samp+syst+'__plus'] = systvarhistRatio[cat+samp+syst+'__plus'].DrawClone('l')
            systvarhistRatioDraw[cat+samp+syst+'__plus'].GetYaxis().SetRangeUser(-0.5,0.5)
            systvarhistRatioDraw[cat+samp+syst+'__plus'].GetYaxis().SetNdivisions(5,5,0)
            systvarhistRatioDraw[cat+samp+syst+'__plus'].GetYaxis().SetLabelSize(0.05)
            systvarhistRatioDraw[cat+samp+syst+'__plus'].GetXaxis().SetLabelSize(0.05)
            systvarhistRatioDraw[cat+samp+syst+'__plus'].SetMarkerStyle(1)
            
            canvas_Bkg[samp].SaveAs("SystVariation_"+cat+samp+syst+'.pdf')
