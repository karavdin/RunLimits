from ROOT import *
import sys
import numpy
ct = '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_btag)*(weight_sfmu_HLT)*(weight_sfmu_ID)'
systematic_direction_ttbar={'nominal':ct,
                          'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',
                          'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)',
                          'q2ttbar__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'q2ttbar__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)'}
                         
systematic_direction_wjets={'nominal':ct,
                          'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',
                          'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)',
                          'q2wjets__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'q2wjets__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)'}

systematic_direction_otherbkgs = {'nominal':ct,
                          'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',
                          'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)'}
systematic_direction_signal= {'nominal':ct,
                          'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',                           
                          'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)'}


samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.SingleMU.root','singletop':'uhh2.AnalysisModuleRunner.MC.SingleTop.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root',
'zjets':'uhh2.AnalysisModuleRunner.MC.DYJets.root','wjets':'uhh2.AnalysisModuleRunner.MC.WJets.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root',
'Zprime0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500_0.root','Zprime4000':'uhh2.AnalysisModuleRunner.MC.Zp01w4000_0.root',
'Zprime1000':'uhh2.AnalysisModuleRunner.MC.Zp01w1000_0.root','Zprime1500':'uhh2.AnalysisModuleRunner.MC.Zp01w1500_0.root',
'Zprime2500':'uhh2.AnalysisModuleRunner.MC.Zp01w2500_0.root', 'Zprime2000':'uhh2.AnalysisModuleRunner.MC.Zp01w2000_0.root',
'Zprime3000':'uhh2.AnalysisModuleRunner.MC.Zp01w3000_0.root' ,
'Zprime3500':'uhh2.AnalysisModuleRunner.MC.Zp01w3500_0.root'}
categories=['T1','T0']
fout = TFile('mu_theta_bdt0p5_chi30.root', 'recreate')
gROOT.SetBatch(kTRUE)
for cat in categories:
    cut_string='(muoN==1 & rec_chi2<30 & WJets_TMVA_response>=0.5'
    if cat == 'T1':
        h_string='mu_1top_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==1   & btagN>=0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                tempdata = TH1F("tempdata","tempdata",30,100,2000)
                mytree.Draw("invmass>>tempdata",cut)
                tempdata.SetName(h_string+key_sample)
                fout.WriteObject(tempdata,h_string+key_sample)
                del tempdata
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",30,100,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",30,100,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*0.72*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",30,100,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",30,100,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & wgtMC__GEN>=0 &  ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",30,100,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",30,100,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'zjets' or 'diboson' or 'others'  in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",30,100,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",30,100,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
    elif cat == 'T0':
        h_string='mu_0top_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==0 & btagN>=0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp2data = TH1F("temp2data","temp2data",30,100,2000)
                mytree.Draw("invmass>>temp2data",cut)
                temp2data.SetName(h_string+key_sample)
                fout.WriteObject(temp2data,h_string+key_sample)
                del temp2data
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",30,100,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",30,100,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",30,100,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",30,100,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",30,100,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",30,100,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'zjets' or 'diboson' or 'others' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",30,100,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",30,100,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys

