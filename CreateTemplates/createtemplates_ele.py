#! /usr/bin/env python
from ROOT import *
import sys
import numpy
systematic_direction_ttbar={'nominal':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'btag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)',
                          'btag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)',
                          'misbtag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)',
                          'misbtag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)',
                          'toptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)',
                          'toptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)',
                          'mistoptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)',
                          'mistoptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)',
                          'pileup__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'pileup__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'q2ttbar__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(wgtMC__muR_dn__muF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'q2ttbar__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(wgtMC__muR_up__muF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'elecID__plus':'(wgtMC__elecIDSF_up)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'elecID__minus':'(wgtMC__elecIDSF_dn)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'elecHLT__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                          'elecHLT__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)'}
                         
systematic_direction_wjets={'nominal':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'btag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)',
                            'btag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)',
                            'misbtag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)',
                            'misbtag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)',
                            'toptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)',
                            'toptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)',
                            'mistoptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)',
                            'mistoptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)',
                            'pileup__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'pileup__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'q2wjets__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(wgtMC__muR_dn__muF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'q2wjets__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(wgtMC__muR_up__muF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                           'elecID__plus':'(wgtMC__elecIDSF_up)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                           'elecID__minus':'(wgtMC__elecIDSF_dn)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                           'elecHLT__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                           'elecHLT__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)'}

systematic_direction_otherbkgs = {'nominal':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'btag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)',
                            'btag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)',
                            'misbtag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)',
                            'misbtag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)',
                            'toptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)',
                            'toptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)',
                            'mistoptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)',
                            'mistoptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)',
                            'pileup__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'pileup__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'elecID__plus':'(wgtMC__elecIDSF_up)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'elecID__minus':'(wgtMC__elecIDSF_dn)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'elecHLT__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                            'elecHLT__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)'}

systematic_direction_signal= {'nominal':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                             'btag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)',
                             'btag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)',
                             'misbtag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)',
                             'misbtag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)',
                             'toptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)',
                             'toptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)',
                             'mistoptag__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)',
                             'mistoptag__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)',
                             'pileup__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)',
                             'pileup__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_ct)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)',
                             'elecID__plus':'(wgtMC__elecIDSF_up)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                             'elecID__minus':'(wgtMC__elecIDSF_dn)*(wgtMC__elecHLTSF_ct)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                             'elecHLT__plus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
                             'elecHLT__minus':'(wgtMC__elecIDSF_ct)*(wgtMC__elecHLTSF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)'}

samplelist = {'Zprime1250':'uhh2.AnalysisModuleRunner.MC.Zp10w1250.root','DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_LO.root', 'wjets':'uhh2.AnalysisModuleRunner.MC.WJetsToLNu.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TT.root','Zprime0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root','Zprime4000':'uhh2.AnalysisModuleRunner.MC.Zp01w4000.root','Zprime1000':'uhh2.AnalysisModuleRunner.MC.Zp01w1000.root','Zprime1500':'uhh2.AnalysisModuleRunner.MC.Zp01w1500.root','Zprime2500':'uhh2.AnalysisModuleRunner.MC.Zp01w2500.root','Zprime750':'uhh2.AnalysisModuleRunner.MC.Zp01w0750.root','Zprime3500':'uhh2.AnalysisModuleRunner.MC.Zp01w3500.root','Zprime3000':'uhh2.AnalysisModuleRunner.MC.Zp01w3000.root','Zprime2000':'uhh2.AnalysisModuleRunner.MC.Zp01w2000.root'}


categories=['T0B0','T1','T0B']
fout = TFile('el_theta_0411_narrow_v1.root', 'recreate')
gROOT.SetBatch(kTRUE)
binning = numpy.arange(0,4100,100)
for cat in categories:
    cut_string='(eleN==1 & rec_chi2<30'
    if cat == 'T1':
        h_string='el_1top_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==1 & ttagevt>=1 & btagN>=0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                tempdata = TH1F("tempdata","tempdata",160,0,8000)
                mytree.Draw("invmass>>tempdata",cut)
                tempdata.SetName(h_string+key_sample)
                fout.WriteObject(tempdata,h_string+key_sample)
                del tempdata
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==1 & ttagevt>=1 &btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",160,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",160,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==1 & ttagevt>=1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",160,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",160,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==1 & ttagevt>=1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",160,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",160,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==1 & ttagevt>=1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",160,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",160,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
    elif cat == 'T0B':
        h_string='el_0top1btag_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==0 & ttagevt>=0 & btagN>=1)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp2data = TH1F("temp2data","temp2data",160,0,8000)
                mytree.Draw("invmass>>temp2data",cut)
                #if(invmass>4000): print invmass
                temp2data.SetName(h_string+key_sample)
                fout.WriteObject(temp2data,h_string+key_sample)
                del temp2data
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0  & btagN>=1)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",160,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",160,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0  & btagN>=1)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",160,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",160,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0 & btagN>=1)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",160,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",160,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0  & btagN>=1)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",160,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",160,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
    elif cat == 'T0B0':
        h_string='el_0top0btag_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==0 & ttagevt>=0 & btagN==0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp3data = TH1F("temp3data","temp3data",160,0,8000)
                mytree.Draw("invmass>>temp3data",cut)
                temp3data.SetName(h_string+key_sample)
                fout.WriteObject(temp3data,h_string+key_sample)
                del temp3data
            elif 'Zprime' in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0 & btagN==0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",160,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",160,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0 & btagN==0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",160,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",160,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0 & btagN==0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",160,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",160,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==0 & ttagevt>=0 & btagN==0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",160,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",160,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys 
