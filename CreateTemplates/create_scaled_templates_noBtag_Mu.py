from ROOT import *
import sys
import numpy
#ct = '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)'
ct = '(weight_pu)*(wgtMC__ttagSF_ct)'
systematic_direction_ttbar={'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',              
                            'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)',                           
                            'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',      
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'q2ttbar__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)',
                            'q2ttbar__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)'
}
systematic_direction_wjets={'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)',
                            'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'q2wjets__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)',
                            'q2wjets__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)',
}          
systematic_direction_otherbkgs = {'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                           'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                           'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                            'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                            'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                            'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                            'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                            'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)',
                            'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)',
#                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
#                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
}                
systematic_direction_signal= {'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',    
                             'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                             'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                             'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)', 
                             'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                             'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)', 
                             'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                             'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)',
                             'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)',
                             'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)', 
                             'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',   
                             'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
                             'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)',
}         

inputdir="/uscms_data/d2/drberry/ZPrimeSemiLeptonic_2016/CMSSW_8_0_24_patch1/test/UHH2/ZprimeSemiLeptonic/config/TTbarLJAnalysisLiteResults/"
samplelist = {'DATA':'TTbarLJAnalysis.DATA_SingleMuon.root',
#'singletop':'TTbarLJAnalysis.SingleTop.root','diboson':'TTbarLJAnalysis.Diboson.root',
#'zjets':'TTbarLJAnalysis.DYJets.root',
#'diboson':'TTbarLJAnalysis.Others.root',
#'wjets':'TTbarLJAnalysis.WJets.root',
'wjets_l':'TTbarLJAnalysis.WJets__L.root',
'wjets_b':'TTbarLJAnalysis.WJets__B.root',
'wjets_c':'TTbarLJAnalysis.WJets__C.root',
'ttbar':'TTbarLJAnalysis.TTbar.root',
'Zprime0500':'TTbarLJAnalysis.ZprimeToTT_01w_M0500.root','Zprime4000':'TTbarLJAnalysis.ZprimeToTT_01w_M4000.root',
'Zprime1000':'TTbarLJAnalysis.ZprimeToTT_01w_M1000.root','Zprime1500':'TTbarLJAnalysis.ZprimeToTT_01w_M1500.root',
'Zprime2500':'TTbarLJAnalysis.ZprimeToTT_01w_M2500.root', 'Zprime2000':'TTbarLJAnalysis.ZprimeToTT_01w_M2000.root',
'Zprime3000':'TTbarLJAnalysis.ZprimeToTT_01w_M3000.root' ,
'Zprime3500':'TTbarLJAnalysis.ZprimeToTT_01w_M3500.root'}
#categories=['T1','T0','T01']
categories=['T1','T0']
#subcategories=['WJetsMVA','antiWJetsMVA']
subcategories=['WJetsMVA_chi2','antiWJetsMVA_chi2']
subcategories2=['WJetsMVA_antichi2','antiWJetsMVA_antichi2']
#categories=['T1_WJetsMVA','T0_WJetsMVA','T1_antiWJetsMVA','T0_antiWJetsMVA']
fout = TFile('mu_theta_bdt0p5_chi30.root', 'recreate')
gROOT.SetBatch(kTRUE)
for cat in categories:
#    cut_string='(muoN==1 & H_Rec_chi2<30 & WJets_TMVA_response>=0.5'
    cut_string_GL='(muoN==1 & '
    if cat == 'T01':
        h_string_GL='mu_01top_'
        for subcat in subcategories2:
            # if subcat == 'WJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
            #     h_string = h_string_GL + 'WJetsMVA_mttbar__' 
            # if subcat == 'antiWJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response<0.5' 
            #     h_string = h_string_GL + 'antiWJetsMVA_mttbar__' 
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & H_Rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__' 
            if subcat == 'antiWJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & H_Rec_chi2<30 ' 
                h_string = h_string_GL + 'antiWJetsMVA_chi2_mttbar__' 
            if subcat == 'WJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & H_Rec_chi2>=30 '
                h_string = h_string_GL + 'WJetsMVA_antichi2_mttbar__' 
            if subcat == 'antiWJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & H_Rec_chi2>=30 ' 
                h_string = h_string_GL + 'antiWJetsMVA_antichi2_mttbar__' 

            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
        #        mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
                mytree.SetAlias("invmass","Mttbar")
                if key_sample == 'DATA':
                    cut = str(cut_string+' & ttagN>=0   & btagN>=0)')
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    tempdata = TH1F("tempdata","tempdata",30,100,2000)
                    mytree.Draw("invmass>>tempdata",cut)
                    tempdata.SetName(h_string+key_sample)
                    fout.WriteObject(tempdata,h_string+key_sample)
                    del tempdata
                elif 'Zprime'in key_sample:
                    for syst in systematic_direction_signal:
                        cut = str(cut_string+' & ttagN>=0 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
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
#                        cut = str(cut_string+' & ttagN==1 & btagN>=0)*0.75*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        cut = str(cut_string+' & ttagN>=0 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
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
                elif 'wjets_l' in key_sample:
                    for syst in systematic_direction_wjets:
                        cut = str(cut_string+' &  ttagN>=0 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
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
                elif 'zjets' or 'diboson' or 'others' or 'wjets_b' or 'wjets_c' in key_sample:
                    for syst in systematic_direction_otherbkgs:
                        cut = str(cut_string+' & ttagN>=0 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
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

    if cat == 'T1':
        h_string_GL='mu_1top_'
        for subcat in subcategories:
            # if subcat == 'WJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
            #     h_string = h_string_GL + 'WJetsMVA_mttbar__' 
            # if subcat == 'antiWJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response<0.5' 
            #     h_string = h_string_GL + 'antiWJetsMVA_mttbar__' 
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & H_Rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__' 
            if subcat == 'antiWJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & H_Rec_chi2<30 ' 
                h_string = h_string_GL + 'antiWJetsMVA_chi2_mttbar__' 
            if subcat == 'WJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & H_Rec_chi2>=30 '
                h_string = h_string_GL + 'WJetsMVA_antichi2_mttbar__' 
            if subcat == 'antiWJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & H_Rec_chi2>=30 ' 
                h_string = h_string_GL + 'antiWJetsMVA_antichi2_mttbar__' 

            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
        #        mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
                mytree.SetAlias("invmass","Mttbar")
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
#                        cut = str(cut_string+' & ttagN==1 & btagN>=0)*0.75*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        cut = str(cut_string+' & ttagN==1 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
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
                elif 'wjets_l' in key_sample:
                    for syst in systematic_direction_wjets:
                        cut = str(cut_string+' &  ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
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
                elif 'zjets' or 'diboson' or 'others' or 'wjets_b' or 'wjets_c' in key_sample:
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
        h_string_GL='mu_0top_'
        for subcat in subcategories:
            # if subcat == 'WJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
            #     h_string = h_string_GL + 'WJetsMVA_mttbar__' 
            # if subcat == 'antiWJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response<0.5' 
            #     h_string = h_string_GL + 'antiWJetsMVA_mttbar__' 
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & H_Rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__' 
            if subcat == 'antiWJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & H_Rec_chi2<30 ' 
                h_string = h_string_GL + 'antiWJetsMVA_chi2_mttbar__' 
            if subcat == 'WJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & H_Rec_chi2>=30 '
                h_string = h_string_GL + 'WJetsMVA_antichi2_mttbar__' 
            if subcat == 'antiWJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & H_Rec_chi2>=30 ' 
                h_string = h_string_GL + 'antiWJetsMVA_antichi2_mttbar__' 


            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
                mytree.SetAlias("invmass","Mttbar")
#                mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
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
#                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*0.75*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
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
                elif 'wjets_l' in key_sample:
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
                elif 'zjets' or 'diboson' or 'others' or 'wjets_b' or 'wjets_c' in key_sample:
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
                            temp2sys.Print()
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys

