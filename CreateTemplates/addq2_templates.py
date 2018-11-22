#! /usr/bin/env python
# add "envelope" of q2 variations for ttbar and w+jets
# input: root file with rebinned Mttbar templates 
# output: root file with rebinned Mttbar templates + q2ttbar and q2w+jets variations with name "input name"+_addedQ2.root
# created on 02.11.2017

import sys
sys.argv.append('-b')

import ROOT
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(000000000)
ROOT.gStyle.SetOptTitle(0)

from ROOT import TCanvas, TFile, TH1, THStack, TLegend

class hinfo:
  def __init__(self, name):
    fields = name.split('__')
    self.channel = fields[0]
    self.process = fields[1]
    self.systematic = None
    self.shift = None
    if len(fields) > 2:
      self.systematic = fields[2]
      self.shift = fields[3]


def name(channel, process, systematic = None, shift = None):
  if not systematic:
    return '__'.join([channel, process])
  return '__'.join([channel, process, systematic, shift])



def addq2File(filename, xtitle, backgrounds):
  file = TFile(filename)
  keys = file.GetListOfKeys()
  h_bkg = {}
  system_q2ttbar_list={"q2ttbarMuRdnMuFdn","q2ttbarMuRupMuFup","q2ttbarMuRdnMuFct","q2ttbarMuRupMuFct","q2ttbarMuRctMuFdn","q2ttbarMuRctMuFup"}
  h_tmp_q2syst_q2ttbar = {}
  h_q2syst_q2ttbar = {} # final "q2ttbar__plus","q2ttbar__minus" hists
  
  system_q2wjets_list={"q2wjetsMuRdnMuFdn","q2wjetsMuRupMuFup","q2wjetsMuRdnMuFct","q2wjetsMuRupMuFct","q2wjetsMuRctMuFdn","q2wjetsMuRctMuFup"}
  h_tmp_q2syst_q2wjets = {}
  h_q2syst_q2wjets = {} # final "q2wjets__plus","q2wjets__minus" hists
  
  # load all the background histograms and create tmp hists to store q2 variations
  for key in keys:
    key = key.GetName()
    info = hinfo(key)
    if not info.systematic:
      h_bkg[info.channel+info.process] = file.Get(key).Clone()
      for i in range(1,h_bkg[info.channel+info.process].GetNbinsX()+1):
        h_tmp_q2syst_q2ttbar[info.channel+info.process+str(i)] = ROOT.TH1F(info.channel+info.process+"_"+str(i)+"_q2ttbar",info.channel+info.process+"_"+str(i)+"_q2ttbar", 80000, 0., 40000.)
        h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)] = ROOT.TH1F(info.channel+info.process+"_"+str(i)+"_q2wjets",info.channel+info.process+"_"+str(i)+"_q2wjets", 80000, 0., 40000.)

        # h_tmp_q2syst_q2ttbar[info.channel+info.process+str(i)] = ROOT.TH1F(info.channel+info.process+"_"+str(i)+"_q2ttbar",info.channel+info.process+"_"+str(i)+"_q2ttbar", 20000, 1., 10000.)
        # h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)] = ROOT.TH1F(info.channel+info.process+"_"+str(i)+"_q2wjets",info.channel+info.process+"_"+str(i)+"_q2wjets", 20000, 1., 10000.)
        
  #read 6 variations for q2ttbar and store them in a histogram. One histtogram per Mttbar bin        
  for key in keys:
    key = key.GetName()
    info = hinfo(key)
    if info.systematic:
      if info.shift == "plus": # plus and minus are identical
        if info.process in backgrounds:
          for key_q2syst_q2ttbar in system_q2ttbar_list:
            if key_q2syst_q2ttbar == info.systematic:
              h_bkg[info.channel+info.process+key_q2syst_q2ttbar] = file.Get(key).Clone()
              for i in range(1,h_bkg[info.channel+info.process+key_q2syst_q2ttbar].GetNbinsX()+1):
                value = h_bkg[info.channel+info.process+key_q2syst_q2ttbar].GetBinContent(i)
                h_tmp_q2syst_q2ttbar[info.channel+info.process+str(i)].Fill(value)

  #read 6 variations for q2wjets and store them in a histogram. One histtogram per Mttbar bin        
  for key in keys:
    key = key.GetName()
    info = hinfo(key)
    if info.systematic:
      if info.shift == "plus": # plus and minus are identical
        if info.process in backgrounds:
          for key_q2syst_q2wjets in system_q2wjets_list:
            if key_q2syst_q2wjets == info.systematic:
              h_bkg[info.channel+info.process+key_q2syst_q2wjets] = file.Get(key).Clone()
              for i in range(1,h_bkg[info.channel+info.process+key_q2syst_q2wjets].GetNbinsX()+1):
                value = h_bkg[info.channel+info.process+key_q2syst_q2wjets].GetBinContent(i)
                h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].Fill(value)

  #store hists in a root file
  output = TFile(filename.split('.')[0]+'_addedQ2.root', 'RECREATE')

  #In each Mttbar bin store Mean-Sigma (minus) and Mean+Sigma(plus) of histogram with 6 q2ttbar variation.
  #This gives "envelope" of q2 variations for ttbar
  #Draw tmp hist for a sanity check and store it in the output root file
  for key in keys:
    key = key.GetName()
    info = hinfo(key)
    if info.systematic:
      if info.process in backgrounds:
        if info.systematic == "q2ttbarMuRdnMuFdn":
#          print "create q2ttbar"       
          if info.shift == "plus":
            h_q2syst_q2ttbar["q2ttbar__plus"+info.channel] = h_bkg[info.channel+info.process+info.systematic].Clone()
            h_q2syst_q2ttbar["q2ttbar__plus"+info.channel].SetName(info.channel+"__ttbar"+"__q2ttbar__plus")
            h_q2syst_q2ttbar["q2ttbar__plus"+info.channel].SetTitle(info.channel+"__ttbar"+"__q2ttbar__plus")
            h_q2syst_q2ttbar["q2ttbar__minus"+info.channel] = h_bkg[info.channel+info.process+info.systematic].Clone()
            h_q2syst_q2ttbar["q2ttbar__minus"+info.channel].SetName(info.channel+"__ttbar"+"__q2ttbar__minus")
            h_q2syst_q2ttbar["q2ttbar__minus"+info.channel].SetTitle(info.channel+"__ttbar"+"__q2ttbar__minus")

            canvas = TCanvas()
            for i in range(1,h_bkg[info.channel+info.process+info.systematic].GetNbinsX()+1):
              h_q2syst_q2ttbar["q2ttbar__plus"+info.channel].SetBinContent(i,h_tmp_q2syst_q2ttbar[info.channel+info.process+str(i)].GetMean()+h_tmp_q2syst_q2ttbar[info.channel+info.process+str(i)].GetRMS())
              h_q2syst_q2ttbar["q2ttbar__minus"+info.channel].SetBinContent(i,h_tmp_q2syst_q2ttbar[info.channel+info.process+str(i)].GetMean()-h_tmp_q2syst_q2ttbar[info.channel+info.process+str(i)].GetRMS())
               
            #plots hists for canity check  
            h_q2syst_q2ttbar["q2ttbar__plus"+info.channel].SetLineColor(2)
            h_q2syst_q2ttbar["q2ttbar__minus"+info.channel].SetLineColor(3)                  
            h_q2syst_q2ttbar["q2ttbar__plus"+info.channel].Draw('hist')
            h_q2syst_q2ttbar["q2ttbar__minus"+info.channel].Draw('samehist')
            canvas.SaveAs(info.channel+'__'+info.process+'__q2ttbar.pdf')
            output.cd()
            h_q2syst_q2ttbar["q2ttbar__minus"+info.channel].Write()
            h_q2syst_q2ttbar["q2ttbar__plus"+info.channel].Write()

  #In each Mttbar bin store Mean-Sigma (minus) and Mean+Sigma(plus) of histogram with 6 q2wjets variation.
  #This gives "envelope" of q2 variations for w+jets
  #Draw tmp hist for a sanity check and store it in the output root file
  for key in keys:
    key = key.GetName()
    info = hinfo(key)
    if info.systematic:
      if info.process in backgrounds:
        if info.systematic == "q2wjetsMuRdnMuFdn":
          if info.shift == "plus":
            #print info.process
            h_q2syst_q2wjets["q2wjets__plus"+info.channel] = h_bkg[info.channel+info.process+info.systematic].Clone()
            h_q2syst_q2wjets["q2wjets__plus"+info.channel].SetName(info.channel+"__"+info.process+"__q2wjets__plus")
            h_q2syst_q2wjets["q2wjets__plus"+info.channel].SetTitle(info.channel+"__"+info.process+"__q2wjets__plus")
            h_q2syst_q2wjets["q2wjets__minus"+info.channel] = h_bkg[info.channel+info.process+info.systematic].Clone()
            h_q2syst_q2wjets["q2wjets__minus"+info.channel].SetName(info.channel+"__"+info.process+"__q2wjets__minus")
            h_q2syst_q2wjets["q2wjets__minus"+info.channel].SetTitle(info.channel+"__"+info.process+"__q2wjets__minus")
            canvas = TCanvas()
            for i in range(1,h_bkg[info.channel+info.process+info.systematic].GetNbinsX()+1):
#              print i, h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].GetMean(), h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].GetRMS()
              h_q2syst_q2wjets["q2wjets__plus"+info.channel].SetBinContent(i,h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].GetMean()+h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].GetRMS())
              h_q2syst_q2wjets["q2wjets__minus"+info.channel].SetBinContent(i,h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].GetMean()-h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].GetRMS())
              # canvasTMP = TCanvas()
              # h_tmp_q2syst_q2wjets[info.channel+info.process+str(i)].Draw('hist')
              # canvasTMP.SaveAs(info.channel+info.process+str(i)+'.pdf')
                            
            #plots hists for canity check  
            h_q2syst_q2wjets["q2wjets__plus"+info.channel].SetLineColor(2)
            h_q2syst_q2wjets["q2wjets__minus"+info.channel].SetLineColor(3)                  
            h_q2syst_q2wjets["q2wjets__plus"+info.channel].Draw('hist')
            h_q2syst_q2wjets["q2wjets__minus"+info.channel].Draw('samehist')
            canvas.SaveAs(info.channel+'__'+info.process+'__q2wjets.pdf')
                                    
            output.cd()
            h_q2syst_q2wjets["q2wjets__minus"+info.channel].Write()
            h_q2syst_q2wjets["q2wjets__plus"+info.channel].Write()

  #Add the rest of systematic to the new root file
  system_q2_list = system_q2ttbar_list
  system_q2_list.update(system_q2wjets_list)
  h_all_system = {}
  for key in keys:
    key = key.GetName()
    #print key
    info = hinfo(key)
    if not info.systematic:
      h_all_system[info.channel+"__"+info.process] = file.Get(key).Clone()
      output.cd()
      h_all_system[info.channel+"__"+info.process].Write()
       
    if info.systematic:
      isStore = True
      for key_q2_q2wjets in system_q2_list:
        if info.systematic == key_q2_q2wjets:
          isStore = False
      if isStore:
        h_all_system[info.channel+"__"+info.process+"__"+info.systematic+"__"+info.shift] = file.Get(key).Clone()
        output.cd()
        h_all_system[info.channel+"__"+info.process+"__"+info.systematic+"__"+info.shift].Write()
       
#print "Hello!"
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_min250_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_widerBins_min250_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_narrowBins_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_chi2.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_min200.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])



#addq2File(0.30,  'mu_theta_wFlatShapeSyst_widerBins_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
#addq2File(0.30,  'ele_theta_wFlatShapeSyst_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])

# addq2File(0.30,  'mu_theta_wFlatShapeSyst_METcut_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
# 
# addq2File(0.30,  'mu_theta_wFlatShapeSyst_Limits_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
# addq2File(0.30,  'ele_theta_wFlatShapeSyst_Limits_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])

#addq2File(0.30,  'ele_theta_bdt0p5_chi30_1MttbarBin.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File(0.30,  'mu_theta_bdt0p5_chi30_1MttbarBin.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File(0.30,  'mu_theta_wFlatShapeSyst_min200_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# #addq2File(0.30,  'ele_theta_bdt0p5_chi30_rebinned.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','diboson','qcd','wjets_b','wjets_c'])
# addq2File(0.30,  'ele_theta_wFlatShapeSyst_rebinned.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
# addq2File(0.30,  'ele_theta_wFlatShapeSyst_Limits_rebinned.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
# addq2File(0.30,  'mu_theta_wFlatShapeSyst_rebinned.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
# addq2File(0.30,  'mu_theta_wFlatShapeSyst_Limits_rebinned.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l'])
# addq2File(0.30,  'ele_theta_bdt0p5_chi30.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File(0.30,  'mu_theta_bdt0p5_chi30.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File(0.30,  'ele_theta_bdt0p5_chi30_1MttbarBin.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File(0.30,  'mu_theta_bdt0p5_chi30_1MttbarBin.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# #addq2File(0.30,  'ele_theta_bdt0p5_chi30.root','M_{t#bar{t}} [GeV/c^{2}]',['wjets_c','wjets_b'])

#addq2File(0.30,  'ele_theta_wFlatShapeSyst_min200_allPDF_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_min200_allPDF_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File(0.30,  'mu_theta_wFlatShapeSyst_min200_allPDF_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File(0.30,  'ele_theta_wFlatShapeSyst_min200_allPDF_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File(0.30,  'ele_theta_wFlatShapeSyst_min200_allPDF_onlyEleStream_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('mu_theta_wFlatShapeSyst_min200_allPDF_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_min200_PDFttbarAndWjetsL_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('ele_theta_wFlatShapeSyst_min200_PDFttbarAndWjetsL_onlyEleStream_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('mu_theta_wFlatShapeSyst_min200_allPDF_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('ele_theta_wFlatShapeSyst_min200_allPDF_onlyEleStream_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_min200_QCDHT_allPDF_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_rebinnedSmallBkg_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCDt0only_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_MET120_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCD_SR_CR4_only_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCD_SR_CR4_only_rebinnedSmallBkg_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('ele_theta_wFlatShapeSyst_min200_allPDF_onlyEleStream_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('ele_theta_wFlatShapeSyst_onlyEleStream_allSyst_LIMITS_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_allSyst_LIMITS_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('ele_theta_wFlatShapeSyst_onlyEleStream_allSyst_LIMITS_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# #addq2File('ele_theta_wFlatShapeSyst_min200_20bins_wTopPtrewSymSyst_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# #addq2File('mu_theta_wFlatShapeSyst_min200_20bins_wTopPtrewSymSyst_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T01_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T1_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T0_SR_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T0_CR1_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T0_CR2_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T01_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T0_CR1_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T0_SR_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T1_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T0_CR2_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# #addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_T01_VV_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])


# addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_ZprimeNarrow4000_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b','ZprimeNarrow4000'])
#addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_ZprimeNarrow4000_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b','ZprimeNarrow4000'])
#addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_25bins_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_woJERJECsignal_LIMITS_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# # #addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinnedSmallBkg_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('mu_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# # #addq2File('mu_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# # #addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# #addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])


#addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

# addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_highMasses_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('mu_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_highMasses_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
# addq2File('mu_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('mu_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_woTopPtCT_LIMITS.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_CHI2_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
#addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_CHI2_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])

#addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_woPDF_BkgZPrime4000.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
addq2File('mu_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF_BkgZPrime4000_addedPDF.root','M_{t#bar{t}} [GeV/c^{2}]',['ttbar','wjets_l','wjets_c','wjets_b'])
