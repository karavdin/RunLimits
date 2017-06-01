from ROOT import *
import sys
import numpy
ct = '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_btag)*(weight_sfmu_HLT)*(weight_sfmu_ID)'
systematic_direction_ttbar={'nominal':ct}
for i in range(244):
    pdfstring  = '*(wgtMC__PDF['+str(i)+'])'
    systematic_direction_ttbar['wgtMC__PDF_'+str(i)] = ct+pdfstring

samplelist ={'ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root'}
categories=['T1','T0']
fout = TFile('T1_T0_ttbar_pdf.root', 'recreate')
gROOT.SetBatch(kTRUE)
for cat in categories:
    cut_string='(muoN==1 & rec_chi2<30 & WJets_TMVA_response>0.5'
    if cat == 'T1':
        h_string='mu_1top_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
            if 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0 )*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
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
            if 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0 )*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
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

    
