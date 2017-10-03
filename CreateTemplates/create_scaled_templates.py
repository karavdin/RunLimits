from ROOT import *
import sys
import numpy
#ct = '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_btag)*(weight_sfmu_HLT)*(weight_sfmu_ID)'
ct = '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_btag)'
systematic_direction_ttbar={'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                             
                            'btag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_up)*(weight_sfelec_Gsf)',                                                    
                            'btag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_down)*(weight_sfelec_Gsf)',                                                 
                            'misbtag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_up)*(weight_sfelec_Gsf)',                                               
                            'misbtag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_down)*(weight_sfelec_Gsf)',                                            
                            'pileup__plus':'(weight_sfelec_ID)*(weight_pu_up)*(weight_btag)*(weight_sfelec_Gsf)',                                                     
                            'pileup__minus':'(weight_sfelec_ID)*(weight_pu_down)*(weight_btag)*(weight_sfelec_Gsf)',                                                  
                            'elecID__plus':'(weight_sfelec_ID_up)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                     
                            'elecID__minus':'(weight_sfelec_ID_down)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                  
                            'elecTRK__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_up)',                                                    
                            'elecTRK__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_down)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                    
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                   
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
                            # 'q2ttbar__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',                
                            # 'q2ttbar__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)'
}
systematic_direction_wjets={'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                             
                            'btag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_up)*(weight_sfelec_Gsf)',                                                    
                            'btag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_down)*(weight_sfelec_Gsf)',                                                 
                            'misbtag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_up)*(weight_sfelec_Gsf)',                                               
                            'misbtag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_down)*(weight_sfelec_Gsf)',                                            
                            'pileup__plus':'(weight_sfelec_ID)*(weight_pu_up)*(weight_btag)*(weight_sfelec_Gsf)',                                                     
                            'pileup__minus':'(weight_sfelec_ID)*(weight_pu_down)*(weight_btag)*(weight_sfelec_Gsf)',                                                  
                            'elecID__plus':'(weight_sfelec_ID_up)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                     
                            'elecID__minus':'(weight_sfelec_ID_down)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                  
                            'elecTRK__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_up)',                                                    
                            'elecTRK__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_down)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                    
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                   
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
                            # 'q2wjets__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                            # 'q2wjets__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                  
}          
systematic_direction_otherbkgs = {'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                       
                            'btag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_up)*(weight_sfelec_Gsf)',                                                    
                            'btag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_down)*(weight_sfelec_Gsf)',                                                 
                            'misbtag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_up)*(weight_sfelec_Gsf)',                                               
                            'misbtag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_down)*(weight_sfelec_Gsf)',                                            
                            'pileup__plus':'(weight_sfelec_ID)*(weight_pu_up)*(weight_btag)*(weight_sfelec_Gsf)',                                                     
                            'pileup__minus':'(weight_sfelec_ID)*(weight_pu_down)*(weight_btag)*(weight_sfelec_Gsf)',                                                  
                            'elecID__plus':'(weight_sfelec_ID_up)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                     
                            'elecID__minus':'(weight_sfelec_ID_down)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                  
                            'elecTRK__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_up)',                                                    
                            'elecTRK__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_down)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                    
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                   
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
}                
systematic_direction_signal= {'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                           
                             'btag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_up)*(weight_sfelec_Gsf)',                                                   
                             'btag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_bc_down)*(weight_sfelec_Gsf)',                                                
                             'misbtag__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_up)*(weight_sfelec_Gsf)',                                              
                             'misbtag__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag_udsg_down)*(weight_sfelec_Gsf)',                                           
                             'pileup__plus':'(weight_sfelec_ID)*(weight_pu_up)*(weight_btag)*(weight_sfelec_Gsf)',                                                    
                             'pileup__minus':'(weight_sfelec_ID)*(weight_pu_down)*(weight_btag)*(weight_sfelec_Gsf)',                                                 
                             'elecID__plus':'(weight_sfelec_ID_up)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                    
                             'elecID__minus':'(weight_sfelec_ID_down)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf)',                                                 
                             'elecTRK__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_up)',                                                   
                             'elecTRK__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_btag)*(weight_sfelec_Gsf_down)',
                             'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                   
                             'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',                                  
                             'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
                             'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_btag)',
                                                 
}         

#systematic_direction_ttbar={'nominal':ct,}
                          # 'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          # 'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          # 'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          # 'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          # 'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',
                          # 'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)',
                          # 'q2ttbar__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'q2ttbar__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)'}
                         
#systematic_direction_wjets={'nominal':ct,}
                          # 'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          # 'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          # 'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          # 'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          # 'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',
                          # 'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)',
                          # 'q2wjets__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'q2wjets__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)'}

#systematic_direction_otherbkgs = {'nominal':ct,}
                          # 'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          # 'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          # 'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          # 'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          # 'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',
                          # 'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)'}
#systematic_direction_signal= {'nominal':ct,}
                          # 'muHLT__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muHLT__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)*(weight_sfmu_ID)*(weight_btag)',
                          # 'muonID__plus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_up)*(weight_btag)',
                          # 'muonID__minus': '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID_down)*(weight_btag)',
                          # 'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__plus':'(weight_pu_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'pileup__minus':'(weight_pu_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag)',
                          # 'btag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_up)',
                          # 'btag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_down)',
                          # 'misbtag__plus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_up)',                           
                          # 'misbtag__minus':'(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)*(weight_btag_udsg_down)'}


samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root',
#'singletop':'uhh2.AnalysisModuleRunner.MC.SingleTop.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root',
#'zjets':'uhh2.AnalysisModuleRunner.MC.DYJets.root',
'diboson':'uhh2.AnalysisModuleRunner.MC.ST_+_DY_+_VV.root',
#'wjets':'uhh2.AnalysisModuleRunner.MC.WJets.root',
'wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets__L.root',
'wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets__B.root',
'wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets__C.root',
'ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root',
'Zprime0500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M0500.root','Zprime4000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M4000.root',
'Zprime1000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M1000.root','Zprime1500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M1500.root',
'Zprime2500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M2500.root', 'Zprime2000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M2000.root',
'Zprime3000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M3000.root' ,
'Zprime3500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M3500.root'}
categories=['T1','T0']
subcategories=['WJetsMVA','antiWJetsMVA']
#categories=['T1_WJetsMVA','T0_WJetsMVA','T1_antiWJetsMVA','T0_antiWJetsMVA']
fout = TFile('ele_theta_bdt0p5_chi30.root', 'recreate')
gROOT.SetBatch(kTRUE)
for cat in categories:
#    cut_string='(eleN==1 & rec_chi2<30 & WJets_TMVA_response>=0.5'
    cut_string_GL='(eleN==1 & rec_chi2<30 & '

    if cat == 'T1':
        h_string_GL='ele_1top_'
        for subcat in subcategories:
            if subcat == 'WJetsMVA':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
                h_string = h_string_GL + 'WJetsMVA_mttbar__' 
            if subcat == 'antiWJetsMVA':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5' 
                h_string = h_string_GL + 'antiWJetsMVA_mttbar__' 

            for key_sample in samplelist:
                myfile = TFile(samplelist[key_sample])
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
        h_string_GL='ele_0top_'
        for subcat in subcategories:
            if subcat == 'WJetsMVA':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
                h_string = h_string_GL + 'WJetsMVA_mttbar__' 
            if subcat == 'antiWJetsMVA':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5' 
                h_string = h_string_GL + 'antiWJetsMVA_mttbar__' 

            for key_sample in samplelist:
                myfile = TFile(samplelist[key_sample])
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

