from ROOT import *
import sys
import numpy

ct = '(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)'
addPDF = True
#addPDF = False

systematic_direction_ttbar={'nominal':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu_up)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu_down)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecID__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID_up)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecID__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID_down)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecTRK__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_up)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',              
                            'elecTRK__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf_down)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecHLT__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*1.02*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'elecHLT__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*0.98*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toptag__plus':'(wgtMC__topptREWGT_ct)*(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'toptag__minus':'(wgtMC__topptREWGT_ct)*(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',      
                            'mistoptag__plus':'(wgtMC__topptREWGT_ct)*(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'mistoptag__minus':'(wgtMC__topptREWGT_ct)*(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'csv_cferr1__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                            'csv_cferr1__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                            'csv_cferr2__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                            'csv_cferr2__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                            'csv_hf__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                            'csv_hf__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                            'csv_hfstats1__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                            'csv_hfstats1__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                            'csv_hfstats2__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                            'csv_hfstats2__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                            'csv_jes__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                            'csv_jes__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                            'csv_lf__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                            'csv_lf__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                            'csv_lfstats1__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)', 
                            'csv_lfstats1__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                            'csv_lfstats2__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)', 
                            'csv_lfstats2__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
                             #add q2 variations. "plus" to not break the next script for rebinning
                            'q2ttbarMuRdnMuFdn__plus':'(wgtMC__topptREWGT_ct)*(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRupMuFup__plus':'(wgtMC__topptREWGT_ct)*(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRdnMuFct__plus':'(wgtMC__topptREWGT_ct)*(wgtMC__muR_dn__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRupMuFct__plus':'(wgtMC__topptREWGT_ct)*(wgtMC__muR_up__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRctMuFdn__plus':'(wgtMC__topptREWGT_ct)*(wgtMC__muR_ct__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',
                            'q2ttbarMuRctMuFup__plus':'(wgtMC__topptREWGT_ct)*(wgtMC__muR_ct__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfelec_Gsf)*(weight_sfelec_ID)*(weight_sfelec_HLT)*(weight_csv_central)',

                            #add JEC and JER
                            'jec__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jec__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__plus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__minus':'(wgtMC__topptREWGT_ct)*(weight_sfelec_ID)*(weight_pu)*(weight_sfelec_Gsf)*(weight_sfelec_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
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
    #for i in range(244):
#    for i in range(9,109):
    for i in range(0,100):
    #for i in range(300):
        pdfstring  = '*(wgtMC__PDF['+str(i)+'])'
        systematic_direction_ttbar['wgtMCPDF_'+str(i)+'__plus'] = ct+pdfstring
        systematic_direction_wjets['wgtMCPDF_'+str(i)+'__plus'] = ct+pdfstring
        systematic_direction_signal['wgtMCPDF_'+str(i)+'__plus'] = ct+pdfstring


inputdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180329_JERhybrid_topptReweight_oldMuonSF_toptagMLE3/T1_v06/elec/"
jecupdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180329_JERhybrid_topptReweight_oldMuonSF_toptagMLE3_jec_up/T1_v06/elec/"
jecdowndir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180329_JERhybrid_topptReweight_oldMuonSF_toptagMLE3_jec_down/T1_v06/elec/"
jerupdir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180329_JERhybrid_topptReweight_oldMuonSF_toptagMLE3_jer_up/T1_v06/elec/"
jerdowndir = "/nfs/dust/cms/user/karavdia/ttbar_semilep_13TeV/RunII_80X_v3/ttbarLJAnalysis/TTbarLJAnalysisLiteModule_NOTBLINDED_20180329_JERhybrid_topptReweight_oldMuonSF_toptagMLE3_jer_down/T1_v06/elec/"


samplelist = {
'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA_SingleElectron_Run2016_BLINDED.root',
'ST':'uhh2.AnalysisModuleRunner.MC.ST.root',
'DY':'uhh2.AnalysisModuleRunner.MC.DY.root',
'wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets__L.root',
'wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets__B.root',
'wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets__C.root',
'ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root',
'Zprime1500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M1500.root','Zprime3000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M3000.root',
}

categories=['T0','T1','T01']
#categories=['T01']
subcategoriesT1=['WJetsMVA_chi2']
subcategoriesT0=['WJetsMVA_chi2','antiWJetsMVA2_chi2','antiWJetsMVA3_chi2']
subcategoriesT01=['chi2']

#Variable stored in the template: name, number of bins, low_bin, high_bin
variables={'Mttbar':[120,200,6000,'M_{t#bar{t}} [GeV]'],'nJets':[40,0,20,'N_{jets};'],
'toppuppijet__Msdp_matched_Nminus1':[100,0,500,'AK8PUPPI M_{softdrop} [GeV]'],
'toppuppijet__tau32_matched_Nminus1':[48, 0, 1.2, 'AK8PUPPI #tau_{32}'],
'toppuppijet__Msdp_matched':[100,0,500,'AK8PUPPI M_{softdrop} [GeV]'],
'toppuppijet__tau32_matched':[48, 0, 1.2, 'AK8PUPPI #tau_{32}'],
'tophad_pt':[120, 0, 1800,'pt_{top-had} [GeV]'],
'toplep_pt':[120, 0, 1800,'pt_{top-lep} [GeV]'],
'Mtophad':[40, 0, 400,'M_{top-had} [GeV]'],
'Mtoplep':[40, 0, 400,'M_{top-lep} [GeV]'],
'dR_lep_cljet':[100,0,2,'#DeltaR_{min}(electron,jets)'],
'met_pt':[90, 0, 900,'MET [GeV]'],
'ljet_pt':[90, 0, 900,'jet p_{T} [GeV]'],
'ljet_eta':[60,-3,3,'jet #eta'],
'jet2_pt':[90, 0, 900,'jet_{2} p_{T} [GeV]'],
'lep_pt':[90, 0, 900,'electron p_{T} [GeV]'],
'lep_eta':[60,-3,3,'electron #eta'],
'WJets_TMVA_response':[100,-1.2,1.8,'W+jets BDT response'],

}

fout = TFile('ele_theta_wFlatShapeSyst_wTopPtrewSymSyst_allVars_addPDF.root', 'recreate')
gROOT.SetBatch(kTRUE)
from FlatScale_ele_JERhybrid_ST_DY_VV_6cat_PDFforDY import *
for cat in categories:
    cut_string_GL='(eleN==1 & Mttbar<2000. & Mttbar>200. & '
   
    if cat == 'T1':
        h_string_GL='ele_1top_'
        #for subcat in subcategories:
        for subcat in subcategoriesT1:
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar_'
            if subcat == 'WJetsMVA4_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.0 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA4_chi2_mttbar_'

            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
                for key_var in variables:
                    mytree.SetAlias("variable",key_var)
                    if key_sample == 'DATA':
                        cut = str(cut_string+' & ttagN==1   & btagN>=0)')
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        tempdata = TH1F("tempdata","tempdata;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                        mytree.Draw("variable>>tempdata",cut)
                        tempdata.SetName(key_var+'_'+h_string+'_'+key_sample)
                        fout.WriteObject(tempdata,key_var+'_'+h_string+'_'+key_sample)
                        del tempdata

                    elif 'Zprime'in key_sample:
                        for syst in systematic_direction_signal:
                            cut = str(cut_string+' & ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp = TH1F("temp","temp;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp",cut)
                                temp.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp,key_var+'_'+h_string+'_'+key_sample)
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
                                je_tree.SetAlias("variable",key_var)
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                je_tree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                    elif 'ttbar' in key_sample:
                        for syst in systematic_direction_ttbar:
                            cut = str(cut_string+' & ttagN==1 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp = TH1F("temp","temp;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp",cut)
                                temp.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp,key_var+'_'+h_string+'_'+key_sample)
                                del temp
                            elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
#                                print "SYSTEMATIC: ",syst
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
                                je_tree.SetAlias("variable",key_var)
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                je_tree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                    elif 'wjets_l' in key_sample:
                        if subcat == 'WJetsMVA_chi2':
                            for syst in systematic_direction_otherbkgs:
                                cut = str(cut_string+' &  ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                                print "Processing: ",key_sample
                                print "Applying cut:",cut
                                if syst == 'nominal':
                                    temp = TH1F("temp","temp;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    mytree.Draw("variable>>temp",cut)
                                    temp.SetName(key_var+'_'+h_string+'_'+key_sample)
                                    fout.WriteObject(temp,key_var+'_'+h_string+'_'+key_sample)
                                    del temp
                                elif 'nominal' not in syst:
                                    scale = scales['scale_'+h_string+'_'+key_sample+"__"+syst]
                                    tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    mytree.Draw("variable>>tempsys",cut+'*('+str(scale)+')')
                                    tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    del tempsys
                        else:
                            for syst in systematic_direction_wjets:
                                cut = str(cut_string+' &  ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                                print "Processing: ",key_sample
                                print "Applying cut:",cut
                                if syst == 'nominal':
                                    temp = TH1F("temp","temp;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    mytree.Draw("variable>>temp",cut)
                                    temp.SetName(key_var+'_'+h_string+'_'+key_sample)
                                    fout.WriteObject(temp,key_var+'_'+h_string+'_'+key_sample)
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
                                    je_tree.SetAlias("variable",key_var)
                                    tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    je_tree.Draw("variable>>tempsys",cut)
                                    tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    del tempsys
                                elif 'nominal' not in syst:
                                    tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    mytree.Draw("variable>>tempsys",cut)
                                    tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    del tempsys
                    elif 'wjets_b' or 'wjets_c' or 'qcd_el' or 'ST' or 'DY' or 'VV' in key_sample:
                        for syst in systematic_direction_otherbkgs:
                            cut = str(cut_string+' & ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                            print "Applying cut:",cut
                            print "Processing: ",key_sample
                            if syst == 'nominal':
                                temp = TH1F("temp","temp;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp",cut)
                                temp.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp,key_var+'_'+h_string+'_'+key_sample)
                                del temp
                            elif 'nominal' not in syst:
                                scale = scales['scale_'+h_string+'_'+key_sample+"__"+syst]
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>tempsys",cut+'*('+str(scale)+')')
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
    elif cat == 'T0':
        h_string_GL='ele_0top_'
        for subcat in subcategoriesT0:
          
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar_'
            if subcat == 'antiWJetsMVA2_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<-0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA2_antichi2_mttbar_'
            if subcat == 'antiWJetsMVA3_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>0.0 & WJets_TMVA_response<0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA3_antichi2_mttbar_'
            if subcat == 'antiWJetsMVA2_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<-0.5 & rec_chi2<30 '
                h_string = h_string_GL + 'antiWJetsMVA2_chi2_mttbar_'
            if subcat == 'antiWJetsMVA3_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>0.0 & WJets_TMVA_response<0.5 & rec_chi2<30 '
                h_string = h_string_GL + 'antiWJetsMVA3_chi2_mttbar_'

            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
                for key_var in variables:
                    mytree.SetAlias("variable",key_var)
                    if key_sample == 'DATA':
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)')
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        temp2data = TH1F("temp2data","temp2data;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                        mytree.Draw("variable>>temp2data",cut)
                        temp2data.SetName(key_var+'_'+h_string+'_'+key_sample)
                        fout.WriteObject(temp2data,key_var+'_'+h_string+'_'+key_sample)
                        del temp2data
                    elif 'Zprime'in key_sample:
                        for syst in systematic_direction_signal:
                            cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2",cut)
                                temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
                                del temp2
                            elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                                if syst=='jec__plus':
                                    je_file = TFile(jecupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__plus':
                                    je_file = TFile(jerupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__minus':
                                    je_file = TFile(jerdowndir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                je_tree.SetAlias("variable",key_var)
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                je_tree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2sys",cut)
                                temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del temp2sys
                    elif 'ttbar' in key_sample:
                        for syst in systematic_direction_ttbar:
                            cut = str(cut_string+' & ttagN==0 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2",cut)
                                temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
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
                                je_tree.SetAlias("variable",key_var)
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                je_tree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2sys",cut)
                                temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del temp2sys
                    elif 'wjets_l' in key_sample:
                        if subcat == 'WJetsMVA_chi2':
                            for syst in systematic_direction_otherbkgs:
                                cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                                print "Processing: ",key_sample
                                print "Applying cut:",cut
                                if syst == 'nominal':
                                    temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    mytree.Draw("variable>>temp2",cut)
                                    temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                    fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
                                    del temp2
                                elif 'nominal' not in syst:
                                    temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    scale = scales['scale_'+h_string+'_'+key_sample+"__"+syst]
                                    mytree.Draw("variable>>temp2sys",cut+'*('+str(scale)+')')
                                    temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    del temp2sys
                        else:
                            for syst in systematic_direction_wjets:
                                cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                                print "Processing: ",key_sample
                                print "Applying cut:",cut
                                if syst == 'nominal':
                                    temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    mytree.Draw("variable>>temp2",cut)
                                    temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                    fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
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
                                    je_tree.SetAlias("variable",key_var)
                                    tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    je_tree.Draw("variable>>tempsys",cut)
                                    tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    del tempsys
                                elif 'nominal' not in syst:
                                    temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                    mytree.Draw("variable>>temp2sys",cut)
                                    temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                    del temp2sys
                    elif 'wjets_b' or 'wjets_c' or 'qcd_el' or 'ST' or 'DY' or 'VV' in key_sample:
                        for syst in systematic_direction_otherbkgs:
                            cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2",cut)
                                temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
                                del temp2
                            elif 'nominal' not in syst:
                                scale = scales['scale_'+h_string+'_'+key_sample+"__"+syst]
                                temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2sys",cut+'*('+str(scale)+')')
                                temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del temp2sys

    elif cat == 'T01':
        h_string_GL='ele_01top_'
        for subcat in subcategoriesT01:
            if subcat == 'chi2':
                cut_string = cut_string_GL+' rec_chi2<30  '
                h_string = h_string_GL + 'chi2_mttbar_'

            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
                for key_var in variables:
                    mytree.SetAlias("variable",key_var)
                    if key_sample == 'DATA':
                        cut = str(cut_string+' & ttagN<2 & btagN>=0)')
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        temp2data = TH1F("temp2data","temp2data;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                        mytree.Draw("variable>>temp2data",cut)
                        temp2data.SetName(key_var+'_'+h_string+'_'+key_sample)
                        fout.WriteObject(temp2data,key_var+'_'+h_string+'_'+key_sample)
                        del temp2data
                    elif 'Zprime'in key_sample:
                        for syst in systematic_direction_signal:
                            cut = str(cut_string+' & ttagN<2 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2",cut)
                                temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
                                del temp2
                            elif syst=='jec__plus' or syst=='jec__minus' or syst=='jer__plus' or syst=='jer__minus':
                                if syst=='jec__plus':
                                    je_file = TFile(jecupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__plus':
                                    je_file = TFile(jerupdir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                if syst=='jer__minus':
                                    je_file = TFile(jerdowndir+samplelist[key_sample])
                                    je_tree = je_file.Get("AnalysisTree")
                                je_tree.SetAlias("variable",key_var)
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                je_tree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2sys",cut)
                                temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del temp2sys
                    elif 'ttbar' in key_sample:
                        for syst in systematic_direction_ttbar:
                            cut = str(cut_string+' & ttagN<2 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2",cut)
                                temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
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
                                je_tree.SetAlias("variable",key_var)
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                je_tree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2sys",cut)
                                temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del temp2sys
                    elif 'wjets_l' or 'wjets_b' or 'wjets_c' or 'qcd_el' or 'ST' or 'DY' or 'VV'in key_sample:
                        for syst in systematic_direction_wjets:
                            cut = str(cut_string+' & ttagN<2 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                            print "Processing: ",key_sample
                            print "Applying cut:",cut
                            if syst == 'nominal':
                                temp2 = TH1F("temp2","temp2;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2",cut)
                                temp2.SetName(key_var+'_'+h_string+'_'+key_sample)
                                fout.WriteObject(temp2,key_var+'_'+h_string+'_'+key_sample)
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
                                je_tree.SetAlias("variable",key_var)
                                tempsys = TH1F("tempsys","tempsys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                je_tree.Draw("variable>>tempsys",cut)
                                tempsys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(tempsys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del tempsys
                            elif 'nominal' not in syst:
                                temp2sys = TH1F("temp2sys","temp2sys;"+variables[key_var][3],variables[key_var][0],variables[key_var][1],variables[key_var][2])
                                mytree.Draw("variable>>temp2sys",cut)
                                temp2sys.SetName(key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                fout.WriteObject(temp2sys,key_var+'_'+h_string+'_'+key_sample+"__"+syst)
                                del temp2sys
