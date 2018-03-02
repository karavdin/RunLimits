from ROOT import *
import sys
import numpy
ct = '(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)'
addPDF = True
#addPDF = False

systematic_direction_ttbar={'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__plus':'(weight_sfelec_ID)*(weight_pu_up)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__minus':'(weight_sfelec_ID)*(weight_pu_down)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecID__plus':'(weight_sfelec_ID_up)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecID__minus':'(weight_sfelec_ID_down)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecTRK__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_up)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',              
                            'elecTRK__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_down)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecHLT__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*1.02*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecHLT__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*0.98*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',      
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'csv_cferr1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                            'csv_cferr1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                            'csv_cferr2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                            'csv_cferr2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                            'csv_hf__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                            'csv_hf__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                            'csv_hfstats1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                            'csv_hfstats1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                            'csv_hfstats2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                            'csv_hfstats2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                            'csv_jes__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                            'csv_jes__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                            'csv_lf__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                            'csv_lf__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                            'csv_lfstats1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)', 
                            'csv_lfstats1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                            'csv_lfstats2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)', 
                            'csv_lfstats2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
                             #add q2 variations. "plus" to not break the next script for rebinning
                            'q2ttbarMuRdnMuFdn__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRupMuFup__plus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRdnMuFct__plus':'(wgtMC__muR_dn__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRupMuFct__plus':'(wgtMC__muR_up__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRctMuFdn__plus':'(wgtMC__muR_ct__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRctMuFup__plus':'(wgtMC__muR_ct__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',

                            #add JEC and JER
                            'jec__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jec__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toppt_reweight__minus':'(wgtMC__topptREWGT_dn)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toppt_reweight__plus':'(wgtMC__topptREWGT_up)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
}
systematic_direction_wjets={'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__plus':'(weight_sfelec_ID)*(weight_pu_up)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__minus':'(weight_sfelec_ID)*(weight_pu_down)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecID__plus':'(weight_sfelec_ID_up)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecID__minus':'(weight_sfelec_ID_down)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecTRK__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_up)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecTRK__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_down)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecHLT__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*1.02*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecHLT__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*0.98*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'csv_cferr1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                            'csv_cferr1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                            'csv_cferr2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                            'csv_cferr2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                            'csv_hf__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                            'csv_hf__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                            'csv_hfstats1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                            'csv_hfstats1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                            'csv_hfstats2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                            'csv_hfstats2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                            'csv_jes__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                            'csv_jes__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                            'csv_lf__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                            'csv_lf__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                            'csv_lfstats1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)', 
                            'csv_lfstats1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                            'csv_lfstats2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)', 
                            'csv_lfstats2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
                             #add q2 variations. "plus" to not break the next script for rebinning
                            'q2wjetsMuRdnMuFdn__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2wjetsMuRupMuFup__plus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2wjetsMuRdnMuFct__plus':'(wgtMC__muR_dn__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2wjetsMuRupMuFct__plus':'(wgtMC__muR_up__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2wjetsMuRctMuFdn__plus':'(wgtMC__muR_ct__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2wjetsMuRctMuFup__plus':'(wgtMC__muR_ct__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            #add JEC and JER
                            'jec__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jec__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
}          
systematic_direction_otherbkgs = {'nominal':ct,
                            'pileup__plus':ct,
                            'pileup__minus':ct,
                            'elecID__plus':ct,
                            'elecID__minus':ct,
                            'elecTRK__plus':ct,
                            'elecTRK__minus':ct,
                            'elecHLT__plus':ct,
                            'elecHLT__minus':ct,
                            'toptag__plus':ct,
                            'toptag__minus':ct,
                            'mistoptag__plus':ct,
                            'mistoptag__minus':ct,
                            'csv_cferr1__plus':ct,
                            'csv_cferr1__minus':ct,
                            'csv_cferr2__plus':ct,
                            'csv_cferr2__minus':ct,
                            'csv_hf__plus':ct,
                            'csv_hf__minus':ct,
                            'csv_hfstats1__plus':ct,
                            'csv_hfstats1__minus':ct,
                            'csv_hfstats2__plus':ct,
                            'csv_hfstats2__minus':ct,
                            'csv_jes__plus':ct,
                            'csv_jes__minus':ct,
                            'csv_lf__plus':ct,
                            'csv_lf__minus':ct,
                            'csv_lfstats1__plus':ct,
                            'csv_lfstats1__minus':ct,
                            'csv_lfstats2__plus':ct,
                            'csv_lfstats2__minus':ct,
                            'q2wjets__plus':ct,
                            'q2wjets__minus':ct,
                            #add JEC and JER
                            'jec__plus':ct,
                            'jec__minus':ct,
                            'jer__plus':ct,
                            'jer__minus':ct,
                            #add PDF
                            'PDF__plus':ct,
                            'PDF__minus':ct,
}                
systematic_direction_signal= {'nominal':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',    
                              'pileup__plus':'(weight_sfelec_ID)*(weight_pu_up)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'pileup__minus':'(weight_sfelec_ID)*(weight_pu_down)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'elecID__plus':'(weight_sfelec_ID_up)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)', 
                              'elecID__minus':'(weight_sfelec_ID_down)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'elecTRK__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_up)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)', 
                              'elecTRK__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_down)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'elecHLT__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*1.02*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'elecHLT__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*0.98*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)', 
                              'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',   
                              'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                              'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                              'csv_cferr1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                              'csv_cferr1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                              'csv_cferr2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                              'csv_cferr2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                              'csv_hf__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                              'csv_hf__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                              'csv_hfstats1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                              'csv_hfstats1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                              'csv_hfstats2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                              'csv_hfstats2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                              'csv_jes__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                              'csv_jes__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                              'csv_lf__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                              'csv_lf__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                              'csv_lfstats1__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)', 
                              'csv_lfstats1__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                              'csv_lfstats2__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)', 
                              'csv_lfstats2__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
                              #add JEC and JER
                              'jec__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'jec__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'jer__plus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                              'jer__minus':'(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
}         

if addPDF:
    for i in range(244):
    #for i in range(300):
        pdfstring  = '*(wgtMC__PDF['+str(i)+'])'
        systematic_direction_ttbar['wgtMCPDF_'+str(i)+'__plus'] = ct+pdfstring
        systematic_direction_wjets['wgtMCPDF_'+str(i)+'__plus'] = ct+pdfstring
        systematic_direction_signal['wgtMCPDF_'+str(i)+'__plus'] = ct+pdfstring

# inputdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_dRPUPPI10_wCSVshapeSF_wMisTopTagSF_wNEW2DEleHLTSF_vetoGapElectrons_HLT1HLT2HLT3_NOTBLINED_WJetsOLDbdt_muRmuF_updTTAGeff_20171020_jer_jec_nominal_topptreweight/T1_v06/elec/"
# #inputdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_dRPUPPI10_wCSVshapeSF_wMisTopTagSF_w2DEleHLTSF_vetoGapElectrons_HLT1HLT2_NOTBLINED_WJetsOLDbdt_muRmuF_updTTAGeff_20171020_jer_jec_nominal/T1_v06/elec/"
# jecupdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_dRPUPPI10_wCSVshapeSF_wMisTopTagSF_w2DEleHLTSF_vetoGapElectrons_HLT1HLT2_NOTBLINED_WJetsOLDbdt_muRmuF_updTTAGeff_20171020_jec_up/T1_v06/elec/"
# jecdowndir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_dRPUPPI10_wCSVshapeSF_wMisTopTagSF_w2DEleHLTSF_vetoGapElectrons_HLT1HLT2_NOTBLINED_WJetsOLDbdt_muRmuF_updTTAGeff_20171020_jec_down/T1_v06/elec/"
# jerupdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_dRPUPPI10_wCSVshapeSF_wMisTopTagSF_w2DEleHLTSF_vetoGapElectrons_HLT1HLT2_NOTBLINED_WJetsOLDbdt_muRmuF_updTTAGeff_20171020_jer_up/T1_v06/elec/"
# jerdowndir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_dRPUPPI10_wCSVshapeSF_wMisTopTagSF_w2DEleHLTSF_vetoGapElectrons_HLT1HLT2_NOTBLINED_WJetsOLDbdt_muRmuF_updTTAGeff_20171020_jer_down/T1_v06/elec/"

inputdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180108_JERhybrid/T1_v06/elec/" 
jecupdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180108_JERhybrid_jec_up/T1_v06/elec/"
jecdowndir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180108_JERhybrid_jec_down/T1_v06/elec/"                                                                                                                                                                   
jerupdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180108_JERhybrid_jer_up/T1_v06/elec/"
jerdowndir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180108_JERhybrid_jer_down/T1_v06/elec/"  
samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA_BLINDED.root',
'diboson':'uhh2.AnalysisModuleRunner.MC.ST_+_DY_+_VV.root',
#'qcd_el':'uhh2.AnalysisModuleRunner.MC.QCD_Pt.root',
'wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets__L.root',
'wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets__B.root',
'wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets__C.root',
'ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root',
'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M0500.root','ZprimeNarrow4000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M4000.root',
'ZprimeNarrow1000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M1000.root','ZprimeNarrow1500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M1500.root',
'ZprimeNarrow0750':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M0750.root','ZprimeNarrow1250':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M1250.root',
'ZprimeNarrow2500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M2500.root', 'ZprimeNarrow2000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M2000.root',
'ZprimeNarrow3000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M3000.root', 'ZprimeNarrow3500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M3500.root',
'ZprimeNarrow4000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M4000.root', 'ZprimeNarrow5000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M5000.root',
'ZprimeNarrow4500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M4500.root',
'ZprimeWide0500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M0500.root', 'ZprimeWide4000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M4000.root',
'ZprimeWide1000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M1000.root', 'ZprimeWide1500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M1500.root',
'ZprimeWide0750':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M0750.root', 'ZprimeWide1250':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M1250.root',
'ZprimeWide2500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M2500.root', 'ZprimeWide2000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M2000.root',
'ZprimeWide3000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M3000.root', 'ZprimeWide3500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M3500.root',
'ZprimeWide4000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M4000.root', 'ZprimeWide5000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M5000.root',
'ZprimeWide4500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_10w_M4500.root',
'ZprimeExtraWide1000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_30w_M1000.root',
'ZprimeExtraWide2000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_30w_M2000.root',
'ZprimeExtraWide3000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_30w_M3000.root',
'ZprimeExtraWide4000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_30w_M4000.root',
'ZprimeExtraWide5000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_30w_M5000.root',
'ZprimeTTJets0500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M0500.root',
'ZprimeTTJets1000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M1000.root','ZprimeTTJets1500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M1500.root',
'ZprimeTTJets0750':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M0750.root','ZprimeTTJets1250':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M1250.root',
'ZprimeTTJets2500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M2500.root','ZprimeTTJets2000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M2000.root',
'ZprimeTTJets3000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M3000.root','ZprimeTTJets3500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M3500.root',
'ZprimeTTJets4000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTTJet_M4000.root',
'RSgluon0500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M0500.root','RSgluon4000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M4000.root',
'RSgluon1000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M1000.root','RSgluon1500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M1500.root',
'RSgluon0750':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M0750.root','RSgluon1250':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M1250.root',
'RSgluon2500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M2500.root', 'RSgluon2000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M2000.root',
'RSgluon3000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M3000.root' ,'RSgluon3500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M3500.root',
'RSgluon4000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M4000.root' ,'RSgluon5000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M5000.root',
'RSgluon4500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M4500.root'      
}

categories=['T0','T1']
#categories=['T1']
subcategoriesT1=['WJetsMVA_chi2']
subcategoriesT0=['antiWJetsMVA2_antichi2','WJetsMVA_chi2','antiWJetsMVA3_antichi2']

fout = TFile('ele_theta_wFlatShapeSyst_Limits.root', 'recreate')
gROOT.SetBatch(kTRUE)
#from FlatScale_ele import *
from FlatScale_ele_JERhybrid import *
#print "scale_ele_1top_WJetsMVA_chi2_mttbar__wjets_c__PDF__plus=", scale_ele_1top_WJetsMVA_chi2_mttbar__wjets_c__PDF__plus
for cat in categories:
    cut_string_GL='(eleN==1 & '
   
    if cat == 'T1':
        h_string_GL='ele_1top_'
        #for subcat in subcategories:
        for subcat in subcategoriesT1:
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__'
            if subcat == 'WJetsMVA4_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.0 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA4_chi2_mttbar__'

            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
                mytree.SetAlias("invmass","Mttbar")
                if key_sample == 'DATA':
                    cut = str(cut_string+' & ttagN==1   & btagN>=0)')
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    tempdata = TH1F("tempdata","tempdata",150,100,10000)
                    mytree.Draw("invmass>>tempdata",cut)
                    tempdata.SetName(h_string+key_sample)
                    tempdata.Print()
                    fout.WriteObject(tempdata,h_string+key_sample)
                    del tempdata
                elif 'Zprime' or 'RSgluon' in key_sample:
                    for syst in systematic_direction_signal:
                        cut = str(cut_string+' & ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",150,100,10000)
                            mytree.Draw("invmass>>temp",cut)
                            temp.SetName(h_string+key_sample)
                            print "Rebinning T1 nom:", str(temp.GetNbinsX())
                            fout.WriteObject(temp,h_string+key_sample)
                            del temp
                        elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                            if syst=='jec__plus':
                                je_file = TFile(jecupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jec__minus':
                                je_file = TFile(jecdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__plus':
                                je_file = TFile(jerupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__minus':
                                je_file = TFile(jerdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            je_tree.SetAlias("invmass","Mttbar")
                            tempsys = TH1F("tempsys","tempsys",150,100,10000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",150,100,10000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                elif 'ttbar' in key_sample:
                    for syst in systematic_direction_ttbar:
                        cut = str(cut_string+' & ttagN==1 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",150,100,10000)
                            mytree.Draw("invmass>>temp",cut)
                            temp.SetName(h_string+key_sample)
                            print "Rebinning T1 nom:", str(temp.GetNbinsX())
                            fout.WriteObject(temp,h_string+key_sample)
                            del temp
                        elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                            if syst=='jec__plus':
                                je_file = TFile(jecupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jec__minus':
                                je_file = TFile(jecdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__plus':
                                je_file = TFile(jerupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__minus':
                                je_file = TFile(jerdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            je_tree.SetAlias("invmass","Mttbar")
                            tempsys = TH1F("tempsys","tempsys",150,100,10000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",150,100,10000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                elif 'wjets_l' in key_sample:
                    if subcat == 'WJetsMVA_chi2':
                        for syst in systematic_direction_otherbkgs:
                            cut = str(cut_string+' &  ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp = TH1F("temp","temp",150,100,10000)
                                mytree.Draw("invmass>>temp",cut)
                                temp.SetName(h_string+key_sample)
                                print "Rebinning T1 nom:", str(temp.GetNbinsX())
                                fout.WriteObject(temp,h_string+key_sample)
                                del temp
                            elif 'nominal' not in syst:
                                scale = scales['scale_'+h_string+key_sample+"__"+syst]
                                tempsys = TH1F("tempsys","tempsys",150,100,10000)
                                mytree.Draw("invmass>>tempsys",cut+'*('+str(scale)+')')
                                tempsys.SetName(h_string+key_sample+"__"+syst)
                                print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                                fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                                del tempsys
                    else:
                        for syst in systematic_direction_wjets:
                            #                    for syst in systematic_direction_otherbkgs:
                            cut = str(cut_string+' &  ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp = TH1F("temp","temp",150,100,10000)
                                mytree.Draw("invmass>>temp",cut)
                                temp.SetName(h_string+key_sample)
                                print "Rebinning T1 nom:", str(temp.GetNbinsX())
                                fout.WriteObject(temp,h_string+key_sample)
                                del temp
                            elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                                if syst=='jec__plus':
                                    je_file = TFile(jecupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jec__minus':
                                    je_file = TFile(jecdowndir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__plus':
                                    je_file = TFile(jerupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__minus':
                                    je_file = TFile(jerdowndir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                je_tree.SetAlias("invmass","Mttbar")
                                tempsys = TH1F("tempsys","tempsys",150,100,10000)
                                je_tree.Draw("invmass>>tempsys",cut)
                                tempsys.SetName(h_string+key_sample+"__"+syst)
                                print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                                fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                tempsys = TH1F("tempsys","tempsys",150,100,10000)
                                mytree.Draw("invmass>>tempsys",cut)
                                tempsys.SetName(h_string+key_sample+"__"+syst)
                                print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                                fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                                del tempsys
                elif 'zjets' or 'diboson'  or 'wjets_b' or 'wjets_c' or 'qcd_el' in key_sample:
                    for syst in systematic_direction_otherbkgs:
                        cut = str(cut_string+' & ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                        print "Applying cut:",cut
                        print "Processing: ",key_sample
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",150,100,10000)
                            mytree.Draw("invmass>>temp",cut)
                            temp.SetName(h_string+key_sample)
                            print "Rebinning T1 nom:", str(temp.GetNbinsX())
                            fout.WriteObject(temp,h_string+key_sample)
                            del temp
                        elif 'nominal' not in syst:
                            scale = scales['scale_'+h_string+key_sample+"__"+syst]
                            tempsys = TH1F("tempsys","tempsys",150,100,10000)
                            mytree.Draw("invmass>>tempsys",cut+'*('+str(scale)+')')
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
    elif cat == 'T0':
        h_string_GL='ele_0top_'
        for subcat in subcategoriesT0:
          
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__'
            if subcat == 'antiWJetsMVA2_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<-0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA2_antichi2_mttbar__'
            if subcat == 'antiWJetsMVA3_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>0.0 & WJets_TMVA_response<0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA3_antichi2_mttbar__'
                
            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
                mytree.SetAlias("invmass","Mttbar")
                if key_sample == 'DATA':
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)')
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    temp2data = TH1F("temp2data","temp2data",150,100,10000)
                    mytree.Draw("invmass>>temp2data",cut)
                    temp2data.SetName(h_string+key_sample)
                    temp2data.Print()
                    fout.WriteObject(temp2data,h_string+key_sample)
                    del temp2data
                elif 'Zprime' or 'RSgluon' in key_sample:
                    for syst in systematic_direction_signal:
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp2 = TH1F("temp2","temp2",150,100,10000)
                            mytree.Draw("invmass>>temp2",cut)
                            temp2.SetName(h_string+key_sample)
                            fout.WriteObject(temp2,h_string+key_sample)
                            del temp2
                        elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                            if syst=='jec__plus':
                                je_file = TFile(jecupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jec__minus':
                                je_file = TFile(jecdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__plus':
                                je_file = TFile(jerupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__minus':
                                je_file = TFile(jerdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            je_tree.SetAlias("invmass","Mttbar")
                            tempsys = TH1F("tempsys","tempsys",150,100,10000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T0 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            temp2sys = TH1F("temp2sys","temp2sys",150,100,10000)
                            mytree.Draw("invmass>>temp2sys",cut)
                            temp2sys.SetName(h_string+key_sample+"__"+syst)
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys
                elif 'ttbar' in key_sample:
                    for syst in systematic_direction_ttbar:
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp2 = TH1F("temp2","temp2",150,100,10000)
                            mytree.Draw("invmass>>temp2",cut)
                            temp2.SetName(h_string+key_sample)
                            fout.WriteObject(temp2,h_string+key_sample)
                            del temp2
                        elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                            if syst=='jec__plus':
                                je_file = TFile(jecupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jec__minus':
                                je_file = TFile(jecdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__plus':
                                je_file = TFile(jerupdir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            if syst=='jer__minus':
                                je_file = TFile(jerdowndir+samplelist[key_sample])
                                je_tree = je_file.Get("AnalysisTree")
                            je_tree.SetAlias("invmass","Mttbar")
                            tempsys = TH1F("tempsys","tempsys",150,100,10000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T0 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            temp2sys = TH1F("temp2sys","temp2sys",150,100,10000)
                            mytree.Draw("invmass>>temp2sys",cut)
                            temp2sys.SetName(h_string+key_sample+"__"+syst)
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys
                elif 'wjets_l' in key_sample:
                    if subcat == 'WJetsMVA_chi2':
                        for syst in systematic_direction_otherbkgs:
                            cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2",150,100,10000)
                                mytree.Draw("invmass>>temp2",cut)
                                temp2.SetName(h_string+key_sample)
                                fout.WriteObject(temp2,h_string+key_sample)
                                del temp2
                            elif 'nominal' not in syst:
                                temp2sys = TH1F("temp2sys","temp2sys",150,100,10000)
                                scale = scales['scale_'+h_string+key_sample+"__"+syst]
                                mytree.Draw("invmass>>temp2sys",cut+'*('+str(scale)+')')
                                temp2sys.SetName(h_string+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                                del temp2sys
                    else:
                        for syst in systematic_direction_wjets:
                            cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2",150,100,10000)
                                mytree.Draw("invmass>>temp2",cut)
                                temp2.SetName(h_string+key_sample)
                                fout.WriteObject(temp2,h_string+key_sample)
                                del temp2
                            elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                                if syst=='jec__plus':
                                    je_file = TFile(jecupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jec__minus':
                                    je_file = TFile(jecdowndir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__plus':
                                    je_file = TFile(jerupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__minus':
                                    je_file = TFile(jerdowndir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                je_tree.SetAlias("invmass","Mttbar")
                                tempsys = TH1F("tempsys","tempsys",150,100,10000)
                                je_tree.Draw("invmass>>tempsys",cut)
                                tempsys.SetName(h_string+key_sample+"__"+syst)
                                print "Rebinning T0 nom+sys:", str(tempsys.GetNbinsX())
                                fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                temp2sys = TH1F("temp2sys","temp2sys",150,100,10000)
                                mytree.Draw("invmass>>temp2sys",cut)
                                temp2sys.SetName(h_string+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                                del temp2sys
                elif 'zjets' or 'diboson' or 'wjets_b' or 'wjets_c' or 'qcd_el' in key_sample:
                    for syst in systematic_direction_otherbkgs:
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp2 = TH1F("temp2","temp2",150,100,10000)
                            mytree.Draw("invmass>>temp2",cut)
                            temp2.SetName(h_string+key_sample)
                            fout.WriteObject(temp2,h_string+key_sample)
                            del temp2
                        elif 'nominal' not in syst:
                            scale = scales['scale_'+h_string+key_sample+"__"+syst]
                            temp2sys = TH1F("temp2sys","temp2sys",150,100,10000)
                            mytree.Draw("invmass>>temp2sys",cut+'*('+str(scale)+')')
                            temp2sys.SetName(h_string+key_sample+"__"+syst)
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys

