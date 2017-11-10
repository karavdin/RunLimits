from ROOT import *
import sys
import numpy
#ct = '(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)*(weight_sfmu_ID)'
ct = '(weight_pu)*(wgtMC__ttagSF_ct)'
systematic_direction_ttbar={'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
 #                           'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
 #                           'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2ttbar__plus':'(wgtMC__muRmuF_max)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2ttbar__minus':'(wgtMC__muRmuF_min)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
  #                          'q2ttbar__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
  #                          'q2ttbar__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2ttbarMuR__plus':'(wgtMC__muR_dn__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2ttbarMuR__minus':'(wgtMC__muR_up__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2ttbarMuF__plus':'(wgtMC__muR_ct__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2ttbarMuF__minus':'(wgtMC__muR_ct__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'jec__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jec__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'csv_cferr1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                            'csv_cferr1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                            'csv_cferr2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                            'csv_cferr2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                            'csv_hf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                            'csv_hf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                            'csv_hfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                            'csv_hfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                            'csv_hfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                            'csv_hfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                            'csv_jes__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                            'csv_jes__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                            'csv_lf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                            'csv_lf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                            'csv_lfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)',
                            'csv_lfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                            'csv_lfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)',
                            'csv_lfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
}
systematic_direction_wjets={'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
#                            'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
#                            'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2wjets__plus':'(wgtMC__muRmuF_max)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2wjets__minus':'(wgtMC__muRmuF_min)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
#                            'q2wjets__plus':'(wgtMC__muR_dn__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
#                            'q2wjets__minus':'(wgtMC__muR_up__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2wjetsMuR__plus':'(wgtMC__muR_dn__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2wjetsMuR__minus':'(wgtMC__muR_up__muF_ct)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2wjetsMuF__plus':'(wgtMC__muR_ct__muF_dn)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            # 'q2wjetsMuF__minus':'(wgtMC__muR_ct__muF_up)*(weight_pu)*(wgtMC__ttagSF_ct)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'jec__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jec__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'csv_cferr1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                            'csv_cferr1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                            'csv_cferr2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                            'csv_cferr2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                            'csv_hf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                            'csv_hf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                            'csv_hfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                            'csv_hfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                            'csv_hfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                            'csv_hfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                            'csv_jes__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                            'csv_jes__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                            'csv_lf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                            'csv_lf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                            'csv_lfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)',
                            'csv_lfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                            'csv_lfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)',
                            'csv_lfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
}
systematic_direction_otherbkgs={'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
 #                           'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
 #                           'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'jec__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jec__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'csv_cferr1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                            'csv_cferr1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                            'csv_cferr2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                            'csv_cferr2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                            'csv_hf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                            'csv_hf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                            'csv_hfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                            'csv_hfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                            'csv_hfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                            'csv_hfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                            'csv_jes__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                            'csv_jes__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                            'csv_lf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                            'csv_lf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                            'csv_lfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)',
                            'csv_lfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                            'csv_lfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)',
                            'csv_lfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
}
systematic_direction_signal= {'nominal':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                             'pileup__plus':'(weight_sfmu_ID)*(weight_pu_up)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                             'pileup__minus':'(weight_sfmu_ID)*(weight_pu_down)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                             'muID__plus':'(weight_sfmu_ID_up)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                             'muID__minus':'(weight_sfmu_ID_down)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                             'muTRK__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_up)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                             'muTRK__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK_down)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
 #                            'muHLT__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_up)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
 #                            'muHLT__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT_down)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                             'toptag__plus':'(weight_pu)*(wgtMC__ttagSF_upT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                             'toptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnT)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                             'mistoptag__plus':'(weight_pu)*(wgtMC__ttagSF_upL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                             'mistoptag__minus':'(weight_pu)*(wgtMC__ttagSF_dnL)*(weight_sfmu_TRK)*(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_csv_central)',
                            'jec__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jec__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'jer__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)',
                            'csv_cferr1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1up)',
                            'csv_cferr1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr1down)',
                            'csv_cferr2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2up)',
                            'csv_cferr2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_cferr2down)',
                            'csv_hf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfup)',
                            'csv_hf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfdown)',
                            'csv_hfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1up)',
                            'csv_hfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats1down)',
                            'csv_hfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2up)',
                            'csv_hfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_hfstats2down)',
                            'csv_jes__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesup)',
                            'csv_jes__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_jesdown)',
                            'csv_lf__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfup)',
                            'csv_lf__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfdown)',
                            'csv_lfstats1__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1up)',
                            'csv_lfstats1__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats1down)',
                            'csv_lfstats2__plus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2up)',
                            'csv_lfstats2__minus':'(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_lfstats2down)',
}

inputdir = "/uscms_data/d2/drberry/ZPrimeSemiLeptonic_2016/CMSSW_8_0_24_patch1/src/UHH2/ZprimeSemiLeptonic/config/TTbarLJAnalysisLiteResults/"
jecupdir = "/uscms_data/d2/drberry/ZPrimeSemiLeptonic_2016/CMSSW_8_0_24_patch1/src/UHH2/ZprimeSemiLeptonic/config/TTbarLJAnalysisLiteResults_JECup/"
jecdowndir = "/uscms_data/d2/drberry/ZPrimeSemiLeptonic_2016/CMSSW_8_0_24_patch1/src/UHH2/ZprimeSemiLeptonic/config/TTbarLJAnalysisLiteResults_JECdown/"
jerupdir = "/uscms_data/d2/drberry/ZPrimeSemiLeptonic_2016/CMSSW_8_0_24_patch1/src/UHH2/ZprimeSemiLeptonic/config/TTbarLJAnalysisLiteResults_JERup/"
jerdowndir = "/uscms_data/d2/drberry/ZPrimeSemiLeptonic_2016/CMSSW_8_0_24_patch1/src/UHH2/ZprimeSemiLeptonic/config/TTbarLJAnalysisLiteResults_JERdown/"
samplelist = {'DATA':'TTbarLJAnalysis.DATA_SingleMuon.root',
#'singletop':'TTbarLJAnalysis.SingleTop.root','diboson':'TTbarLJAnalysis.Diboson.root',
#'zjets':'TTbarLJAnalysis.DYJets.root',
#'zjets':'TTbarLJAnalysis.DY.root',
'diboson':'TTbarLJAnalysis.DiBoson.root',
'ST':'TTbarLJAnalysis.SingleTop.root',
'DY':'TTbarLJAnalysis.DrellYan.root',
#'diboson':'TTbarLJAnalysis.ST_+_DY_+_VV.root',
'qcd':'TTbarLJAnalysis.QCD_MuEnrichedPt5.root',
#'wjets':'TTbarLJAnalysis.WJets.root',
'wjets_l':'TTbarLJAnalysis.WJets__L.root',
'wjets_b':'TTbarLJAnalysis.WJets__B.root',
'wjets_c':'TTbarLJAnalysis.WJets__C.root',
'ttbar':'TTbarLJAnalysis.TTbar.root',
'ZprimeNarrow0500':'TTbarLJAnalysis.ZprimeToTT_01w_M0500.root','ZprimeNarrow4000':'TTbarLJAnalysis.ZprimeToTT_01w_M4000.root',
'ZprimeNarrow1000':'TTbarLJAnalysis.ZprimeToTT_01w_M1000.root','ZprimeNarrow1500':'TTbarLJAnalysis.ZprimeToTT_01w_M1500.root',
'ZprimeNarrow0750':'TTbarLJAnalysis.ZprimeToTT_01w_M0750.root','ZprimeNarrow1250':'TTbarLJAnalysis.ZprimeToTT_01w_M1250.root',
'ZprimeNarrow2500':'TTbarLJAnalysis.ZprimeToTT_01w_M2500.root', 'ZprimeNarrow2000':'TTbarLJAnalysis.ZprimeToTT_01w_M2000.root',
'ZprimeNarrow3000':'TTbarLJAnalysis.ZprimeToTT_01w_M3000.root' ,'ZprimeNarrow3500':'TTbarLJAnalysis.ZprimeToTT_01w_M3500.root',
'ZprimeNarrow4000':'TTbarLJAnalysis.ZprimeToTT_01w_M4000.root' ,'ZprimeNarrow5000':'TTbarLJAnalysis.ZprimeToTT_01w_M5000.root' ,
'ZprimeNarrow4500':'TTbarLJAnalysis.ZprimeToTT_01w_M4500.root' ,
'ZprimeWide0500':'TTbarLJAnalysis.ZprimeToTT_10w_M0500.root','ZprimeWide4000':'TTbarLJAnalysis.ZprimeToTT_10w_M4000.root',
'ZprimeWide1000':'TTbarLJAnalysis.ZprimeToTT_10w_M1000.root','ZprimeWide1500':'TTbarLJAnalysis.ZprimeToTT_10w_M1500.root',
'ZprimeWide0750':'TTbarLJAnalysis.ZprimeToTT_10w_M0750.root','ZprimeWide1250':'TTbarLJAnalysis.ZprimeToTT_10w_M1250.root',
'ZprimeWide2500':'TTbarLJAnalysis.ZprimeToTT_10w_M2500.root', 'ZprimeWide2000':'TTbarLJAnalysis.ZprimeToTT_10w_M2000.root',
'ZprimeWide3000':'TTbarLJAnalysis.ZprimeToTT_10w_M3000.root' ,'ZprimeWide3500':'TTbarLJAnalysis.ZprimeToTT_10w_M3500.root',
'ZprimeWide4000':'TTbarLJAnalysis.ZprimeToTT_10w_M4000.root' ,'ZprimeWide5000':'TTbarLJAnalysis.ZprimeToTT_10w_M5000.root' ,
'ZprimeWide4500':'TTbarLJAnalysis.ZprimeToTT_10w_M4500.root' ,
'RSgluon0500':'TTbarLJAnalysis.RSGluonToTT_M0500.root','RSgluon4000':'TTbarLJAnalysis.RSGluonToTT_M4000.root',
'RSgluon1000':'TTbarLJAnalysis.RSGluonToTT_M1000.root','RSgluon1500':'TTbarLJAnalysis.RSGluonToTT_M1500.root',
'RSgluon0750':'TTbarLJAnalysis.RSGluonToTT_M0750.root','RSgluon1250':'TTbarLJAnalysis.RSGluonToTT_M1250.root',
'RSgluon2500':'TTbarLJAnalysis.RSGluonToTT_M2500.root', 'RSgluon2000':'TTbarLJAnalysis.RSGluonToTT_M2000.root',
'RSgluon3000':'TTbarLJAnalysis.RSGluonToTT_M3000.root' ,'RSgluon3500':'TTbarLJAnalysis.RSGluonToTT_M3500.root',
'RSgluon4000':'TTbarLJAnalysis.RSGluonToTT_M4000.root', 'RSgluon5000':'TTbarLJAnalysis.RSGluonToTT_M5000.root' ,
'RSgluon4500':'TTbarLJAnalysis.RSGluonToTT_M4500.root'}
#categories=['T1','T0','T01']
categories=['T0','T1']
#categories=['T1','T0']
#subcategoriesT1=['chi2']
#subcategoriesT0=['WJetsMVA_chi2']
#subcategoriesT0=['WJetsMVA_chi2','antiWJetsMVA2_chi2']
#subcategoriesT01=['antiWJetsMVA2_antichi2']
#subcategoriesT01=['antiWJetsMVA_antichi2']
subcategoriesT1=['WJetsMVA_chi2']
#subcategoriesT1=['WJetsMVA4_chi2']
#subcategoriesT1=['WJetsMVA_chi2','antiWJetsMVA2_chi2']
#subcategoriesT0=['antiWJetsMVA2_antichi2','WJetsMVA_chi2','antiWJetsMVA3_antichi2','antiWJetsMVA3_chi2']
subcategoriesT0=['antiWJetsMVA2_antichi2','WJetsMVA_chi2','antiWJetsMVA3_antichi2']

subcategories=['WJetsMVA_chi2','antiWJetsMVA_chi2']
subcategories2=['WJetsMVA_antichi2','antiWJetsMVA_antichi2']
#categories=['T1_WJetsMVA','T0_WJetsMVA','T1_antiWJetsMVA','T0_antiWJetsMVA']
fout = TFile('mu_theta_bdt0p5_chi30_Limits.root', 'recreate')
gROOT.SetBatch(kTRUE)
for cat in categories:
#    cut_string='(muoN==1 & rec_chi2<30 & WJets_TMVA_response>=0.5'
#    cut_string_GL='(muoN==1 & weight_sfmu_HLT_up>0 & weight_sfmu_HLT_down>0 & wgtMC__muR_dn__muF_dn>0 & wgtMC__muR_dn__muF_dn<1.5 & wgtMC__muR_up__muF_up>0 & wgtMC__muR_up__muF_up<1.1 & '
#    cut_string_GL='(muoN==1 & rec_chi2<500 & '
    cut_string_GL='(muoN==1 & '
    if cat == 'T01':
        h_string_GL='mu_01top_'
    #    for subcat in subcategories2:
        for subcat in subcategoriesT01:
            # if subcat == 'WJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
            #     h_string = h_string_GL + 'WJetsMVA_mttbar__'
            # if subcat == 'antiWJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response<0.5'
            #     h_string = h_string_GL + 'antiWJetsMVA_mttbar__'
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__'
            if subcat == 'antiWJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & rec_chi2<30 '
                h_string = h_string_GL + 'antiWJetsMVA_chi2_mttbar__'
            if subcat == 'WJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'WJetsMVA_antichi2_mttbar__'
            if subcat == 'antiWJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA_antichi2_mttbar__'
            if subcat == 'antiWJetsMVA2_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<-0.75 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA2_antichi2_mttbar__'

            for key_sample in samplelist:
                myfile = TFile(inputdir+samplelist[key_sample])
                print "opening", myfile
                mytree = myfile.Get("AnalysisTree")
                print "getting", mytree
        #        mytree.SetAlias("invmass","sqrt(pow(rec_tlep.Energy()+rec_thad.Energy(),2)-(pow(rec_thad.Px(),2)+pow(rec_thad.Py(),2)+pow(rec_thad.Pz(),2)+pow(rec_tlep.Px(),2)+pow(rec_tlep.Py(),2)+pow(rec_tlep.Pz(),2)+2*(rec_thad.Px()*rec_tlep.Px()+rec_thad.Py()*rec_tlep.Py()+rec_thad.Pz()*rec_tlep.Pz())))")
                mytree.SetAlias("invmass","Mttbar")
                if key_sample == 'DATA':
                    #cut = str(cut_string+' & ttagN>=0   & btagN>=0)')
                    cut = str(cut_string+' & ttagN<1   & btagN>=0)')
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    tempdata = TH1F("tempdata","tempdata",100,100,7000)
                    mytree.Draw("invmass>>tempdata",cut)
                    tempdata.SetName(h_string+key_sample)
                    fout.WriteObject(tempdata,h_string+key_sample)
                    del tempdata
                elif 'Zprime'in key_sample:
                    for syst in systematic_direction_signal:
#                        cut = str(cut_string+' & ttagN>=0 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                        cut = str(cut_string+' & ttagN<1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                elif 'ttbar' in key_sample:
                    for syst in systematic_direction_ttbar:
#                        cut = str(cut_string+' & ttagN==1 & btagN>=0)*0.75*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        #cut = str(cut_string+' & ttagN>=0 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        cut = str(cut_string+' & ttagN<1 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                elif 'wjets_l' in key_sample:
                     for syst in systematic_direction_wjets:
#                    for syst in systematic_direction_otherbkgs:
#                        cut = str(cut_string+' &  ttagN>=0 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                        cut = str(cut_string+' &  ttagN<1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                elif 'zjets' or 'diboson' or 'others' or 'wjets_b' or 'wjets_c' in key_sample:
                    for syst in systematic_direction_otherbkgs:
#                        cut = str(cut_string+' & ttagN>=0 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                        cut = str(cut_string+' & ttagN<1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys

    if cat == 'T1':
        h_string_GL='mu_1top_'
        #for subcat in subcategories:
        for subcat in subcategoriesT1:
            # if subcat == 'WJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
            #     h_string = h_string_GL + 'WJetsMVA_mttbar__'
            # if subcat == 'antiWJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response<0.5'
            #     h_string = h_string_GL + 'antiWJetsMVA_mttbar__'
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__'
            if subcat == 'WJetsMVA4_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.0 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA4_chi2_mttbar__'
            if subcat == 'antiWJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & rec_chi2<30 '
                h_string = h_string_GL + 'antiWJetsMVA_chi2_mttbar__'
            if subcat == 'WJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'WJetsMVA_antichi2_mttbar__'
            if subcat == 'antiWJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA_antichi2_mttbar__'
            if subcat == 'chi2':
                cut_string = cut_string_GL+' & rec_chi2<30  '
                h_string = h_string_GL + 'chi2_mttbar__'

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
                    tempdata = TH1F("tempdata","tempdata",100,100,7000)
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
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
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
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                elif 'wjets_l' in key_sample:
                     for syst in systematic_direction_wjets:
#                    for syst in systematic_direction_otherbkgs:
                        cut = str(cut_string+' &  ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                #elif 'zjets' or 'diboson' or 'others' or 'wjets_b' or 'wjets_c' in key_sample:
                elif 'zjets' or 'diboson' or 'others' or 'ST' in key_sample:
                    for syst in systematic_direction_otherbkgs:
                        cut = str(cut_string+' & ttagN==1 &  btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp = TH1F("temp","temp",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            mytree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
    elif cat == 'T0':
        h_string_GL='mu_0top_'
        #for subcat in subcategories:
        for subcat in subcategoriesT0:
            # if subcat == 'WJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response>=0.5'
            #     h_string = h_string_GL + 'WJetsMVA_mttbar__'
            # if subcat == 'antiWJetsMVA':
            #     cut_string = cut_string_GL+' WJets_TMVA_response<0.5'
            #     h_string = h_string_GL + 'antiWJetsMVA_mttbar__'
            if subcat == 'WJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
                h_string = h_string_GL + 'WJetsMVA_chi2_mttbar__'
            if subcat == 'antiWJetsMVA_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & rec_chi2<30 '
                h_string = h_string_GL + 'antiWJetsMVA_chi2_mttbar__'
            if subcat == 'WJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'WJetsMVA_antichi2_mttbar__'
            if subcat == 'antiWJetsMVA_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA_antichi2_mttbar__'
            if subcat == 'antiWJetsMVA2_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<-0.75 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA2_antichi2_mttbar__'
            if subcat == 'antiWJetsMVA3_antichi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & WJets_TMVA_response>0.0 & rec_chi2>=30 '
                h_string = h_string_GL + 'antiWJetsMVA3_antichi2_mttbar__'

            if subcat == 'antiWJetsMVA2_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<-0.75 & rec_chi2<30 '
                h_string = h_string_GL + 'antiWJetsMVA2_chi2_mttbar__'
            if subcat == 'antiWJetsMVA3_chi2':
                cut_string = cut_string_GL+' WJets_TMVA_response<0.5 & WJets_TMVA_response>0.0 & rec_chi2<30 '
                h_string = h_string_GL + 'antiWJetsMVA3_chi2_mttbar__'


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
                    temp2data = TH1F("temp2data","temp2data",100,100,7000)
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
                            temp2 = TH1F("temp2","temp2",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            temp2sys = TH1F("temp2sys","temp2sys",100,100,7000)
                            mytree.Draw("invmass>>temp2sys",cut)
                            temp2sys.SetName(h_string+key_sample+"__"+syst)
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys
                elif 'ttbar' in key_sample:
                    for syst in systematic_direction_ttbar:
#                   for syst in systematic_direction_otherbkgs:
#                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*0.75*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp2 = TH1F("temp2","temp2",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            temp2sys = TH1F("temp2sys","temp2sys",100,100,7000)
                            mytree.Draw("invmass>>temp2sys",cut)
                            temp2sys.SetName(h_string+key_sample+"__"+syst)
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys
#                elif 'wjets_l' in key_sample:
                elif 'wjets_l' or 'ST' in key_sample:
                    for syst in systematic_direction_wjets:
#                    for syst in systematic_direction_otherbkgs:
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp2 = TH1F("temp2","temp2",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            temp2sys = TH1F("temp2sys","temp2sys",100,100,7000)
                            mytree.Draw("invmass>>temp2sys",cut)
                            temp2sys.SetName(h_string+key_sample+"__"+syst)
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys
#                elif 'zjets' or 'diboson' or 'others' or 'wjets_b' or 'wjets_c' or 'ST' or 'qcd' in key_sample:
                elif 'zjets' or 'diboson' or 'others' or 'wjets_b' or 'wjets_c' or 'qcd' in key_sample:
                    for syst in systematic_direction_otherbkgs:
                        cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                        print "Processing: ",key_sample
                        print "Applying cut:",cut
                        if syst == 'nominal':
                            temp2 = TH1F("temp2","temp2",100,100,7000)
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
                            tempsys = TH1F("tempsys","tempsys",100,100,7000)
                            je_tree.Draw("invmass>>tempsys",cut)
                            tempsys.SetName(h_string+key_sample+"__"+syst)
                            print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                            fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                            del tempsys
                        elif 'nominal' not in syst:
                            temp2sys = TH1F("temp2sys","temp2sys",100,100,7000)
                            mytree.Draw("invmass>>temp2sys",cut)
                            temp2sys.SetName(h_string+key_sample+"__"+syst)
                            temp2sys.Print()
                            fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                            del temp2sys

