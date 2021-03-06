#! /usr/bin/env python
from ROOT import *
import sys
import numpy
#systematic_direction_ttbar={'nominal':'(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_pu)*(wgtMC__ttagSF_ct)'}
#systematic_direction_wjets={'nominal':'(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_pu)*(wgtMC__ttagSF_ct)'}
#systematic_direction_otherbkgs = {'nominal':'(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_pu)*(wgtMC__ttagSF_ct)'}
#systematic_direction_signal= {'nominal':'(weight_sfmu_ID)*(weight_sfmu_HLT)*(weight_pu)*(wgtMC__ttagSF_ct)'}

systematic_direction_ttbar={'nominal':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'btag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'btag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'misbtag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'misbtag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'toptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)',
                          'toptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)',
                          'mistoptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)',
                          'mistoptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)',
                          'pileup__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'pileup__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'q2ttbar__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(wgtMC__muR_up__muF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'q2ttbar__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(wgtMC__muR_dn__muF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'muonID__plus':'(weight_sfmu_ID_up)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'muonID__minus':'(weight_sfmu_ID_down)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'muonTRK__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'muonTRK__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK_down)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                          'muonHLT__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)',
                          'muonHLT__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)'
}

systematic_direction_wjets={'nominal':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'btag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'btag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'misbtag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'misbtag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'toptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)',
                            'toptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)',
                            'mistoptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)',
                            'mistoptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)',
                            'pileup__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'pileup__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'q2wjets__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(wgtMC__muR_up__muF_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'q2wjets__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(wgtMC__muR_dn__muF_dn)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonID__plus':'(weight_sfmu_ID_up)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonID__minus':'(weight_sfmu_ID_down)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonTRK__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonTRK__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK_down)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonHLT__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)',
                            'muonHLT__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)'
}

systematic_direction_otherbkgs = {'nominal':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'btag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'btag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'misbtag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'misbtag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'toptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)',
                            'toptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)',
                            'mistoptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)',
                            'mistoptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)',
                            'pileup__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'pileup__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonID__plus':'(weight_sfmu_ID_up)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonID__minus':'(weight_sfmu_ID_down)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonTRK__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonTRK__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK_down)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                            'muonHLT__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)',
                            'muonHLT__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)'
}

systematic_direction_signal= {'nominal':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'btag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'btag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'misbtag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'misbtag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'toptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)*(weight_sfmu_HLT)',
                             'toptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)*(weight_sfmu_HLT)',
                             'mistoptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)*(weight_sfmu_HLT)',
                             'mistoptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)*(weight_sfmu_HLT)',
                             'pileup__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'pileup__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonID__plus':'(weight_sfmu_ID_up)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonID__minus':'(weight_sfmu_ID_down)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonTRK__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonTRK__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK_down)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonHLT__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)',
                             'muonHLT__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)'
}

# systematic_direction_DY= {'nominal':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'btag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_up)*(wgtMC__ttagSF_ct)',
#                              'btag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_bc_down)*(wgtMC__ttagSF_ct)',
#                              'misbtag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_up)*(wgtMC__ttagSF_ct)',
#                              'misbtag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag_udsg_down)*(wgtMC__ttagSF_ct)',
#                              'toptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upT)',
#                              'toptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnT)',
#                              'mistoptag__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_upL)',
#                              'mistoptag__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_dnL)',
#                              'pileup__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'pileup__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'muonID__plus':'(weight_sfmu_ID_up)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'muonID__minus':'(weight_sfmu_ID_down)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'muonHLT__plus':'(weight_sfmu_ID)*(weight_sfmu_HLT_up)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'muonHLT__minus':'(weight_sfmu_ID)*(weight_sfmu_HLT_down)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'muonTRK__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)',
#                              'muonTRK__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK_down)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)'}

systematic_direction_DY = {'nominal':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'pileup__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_up)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'pileup__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu_down)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonID__plus':'(weight_sfmu_ID_up)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonID__minus':'(weight_sfmu_ID_down)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonTRK__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK_up)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonTRK__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK_down)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT)',
                             'muonHLT__plus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_up)',
                             'muonHLT__minus':'(weight_sfmu_ID)*(weight_sfmu_TRK)*(weight_pu)*(weight_btag)*(wgtMC__ttagSF_ct)*(weight_sfmu_HLT_down)'
}


#samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_NLO.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root', 'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root','ZprimeNarrow0750':'uhh2.AnalysisModuleRunner.MC.Zp01w0750.root','ZprimeNarrow1000':'uhh2.AnalysisModuleRunner.MC.Zp01w1000.root','ZprimeNarrow1250':'uhh2.AnalysisModuleRunner.MC.Zp01w1250.root','ZprimeNarrow1500':'uhh2.AnalysisModuleRunner.MC.Zp01w1500.root','ZprimeNarrow2000':'uhh2.AnalysisModuleRunner.MC.Zp01w2000.root','ZprimeNarrow2500':'uhh2.AnalysisModuleRunner.MC.Zp01w2500.root','ZprimeNarrow3000':'uhh2.AnalysisModuleRunner.MC.Zp01w3000.root','ZprimeNarrow3500':'uhh2.AnalysisModuleRunner.MC.Zp01w3500.root','ZprimeNarrow4000':'uhh2.AnalysisModuleRunner.MC.Zp01w4000.root','ZprimeWide0500':'uhh2.AnalysisModuleRunner.MC.Zp10w0500.root','ZprimeWide0750':'uhh2.AnalysisModuleRunner.MC.Zp10w0750.root','ZprimeWide1000':'uhh2.AnalysisModuleRunner.MC.Zp10w1000.root','ZprimeWide1250':'uhh2.AnalysisModuleRunner.MC.Zp10w1250.root','ZprimeWide1500':'uhh2.AnalysisModuleRunner.MC.Zp10w1500.root','ZprimeWide2000':'uhh2.AnalysisModuleRunner.MC.Zp10w2000.root','ZprimeWide2500':'uhh2.AnalysisModuleRunner.MC.Zp10w2500.root','ZprimeWide3000':'uhh2.AnalysisModuleRunner.MC.Zp10w3000.root','ZprimeWide3500':'uhh2.AnalysisModuleRunner.MC.Zp10w3500.root','ZprimeWide4000':'uhh2.AnalysisModuleRunner.MC.Zp10w4000.root','ZprimeSuperWide1000':'uhh2.AnalysisModuleRunner.MC.Zp30w1000.root','ZprimeSuperWide2000':'uhh2.AnalysisModuleRunner.MC.Zp30w2000.root','ZprimeSuperWide3000':'uhh2.AnalysisModuleRunner.MC.Zp30w3000.root','ZprimeSuperWide4000':'uhh2.AnalysisModuleRunner.MC.Zp30w4000.root','RSgluon500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-500.root','RSgluon750':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-750.root','RSgluon1000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-1000.root','RSgluon1250':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-1250.root','RSgluon1500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-1500.root','RSgluon2000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-2000.root','RSgluon2500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-2500.root','RSgluon3000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-3000.root','RSgluon4000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-4000.root','wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__B.root','wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__C.root','wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__L.root'}

#samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_NLO.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root', 'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root','ZprimeNarrow0750':'uhh2.AnalysisModuleRunner.MC.Zp01w0750.root','ZprimeNarrow1000':'uhh2.AnalysisModuleRunner.MC.Zp01w1000.root','ZprimeNarrow1250':'uhh2.AnalysisModuleRunner.MC.Zp01w1250.root','ZprimeNarrow1500':'uhh2.AnalysisModuleRunner.MC.Zp01w1500.root','ZprimeNarrow2000':'uhh2.AnalysisModuleRunner.MC.Zp01w2000.root','ZprimeNarrow2500':'uhh2.AnalysisModuleRunner.MC.Zp01w2500.root','ZprimeNarrow3000':'uhh2.AnalysisModuleRunner.MC.Zp01w3000.root','ZprimeNarrow3500':'uhh2.AnalysisModuleRunner.MC.Zp01w3500.root','ZprimeNarrow4000':'uhh2.AnalysisModuleRunner.MC.Zp01w4000.root','ZprimeWide0500':'uhh2.AnalysisModuleRunner.MC.Zp10w0500.root','ZprimeWide0750':'uhh2.AnalysisModuleRunner.MC.Zp10w0750.root','ZprimeWide1000':'uhh2.AnalysisModuleRunner.MC.Zp10w1000.root','ZprimeWide1250':'uhh2.AnalysisModuleRunner.MC.Zp10w1250.root','ZprimeWide1500':'uhh2.AnalysisModuleRunner.MC.Zp10w1500.root','ZprimeWide2000':'uhh2.AnalysisModuleRunner.MC.Zp10w2000.root','ZprimeWide2500':'uhh2.AnalysisModuleRunner.MC.Zp10w2500.root','ZprimeWide3000':'uhh2.AnalysisModuleRunner.MC.Zp10w3000.root','ZprimeWide3500':'uhh2.AnalysisModuleRunner.MC.Zp10w3500.root','ZprimeWide4000':'uhh2.AnalysisModuleRunner.MC.Zp10w4000.root','ZprimeSuperWide1000':'uhh2.AnalysisModuleRunner.MC.Zp30w1000.root','ZprimeSuperWide2000':'uhh2.AnalysisModuleRunner.MC.Zp30w2000.root','ZprimeSuperWide3000':'uhh2.AnalysisModuleRunner.MC.Zp30w3000.root','ZprimeSuperWide4000':'uhh2.AnalysisModuleRunner.MC.Zp30w4000.root','RSgluon500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-500.root','RSgluon750':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-750.root','RSgluon1000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-1000.root','RSgluon1250':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-1250.root','RSgluon1500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-1500.root','RSgluon2000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-2000.root','RSgluon2500':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-2500.root','RSgluon3000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-3000.root','RSgluon4000':'uhh2.AnalysisModuleRunner.MC.RSGluonToTT_M-4000.root','wjets':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__All.root'}

#samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_NLO.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root', 'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root', 'wjets':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__All.root', 'qcd':'uhh2.AnalysisModuleRunner.MC.QCD_HT.root'}
#samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_NLO.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root', 'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root', 'wjets':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__All.root'}

#samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_LO.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root','wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__B.root','wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__C.root','wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__L.root', 'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root','qcd':'uhh2.AnalysisModuleRunner.MC.QCD_HT.root'}


samplelist = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root','wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__B.root','wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__C.root','wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__L.root', 'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_LO.root'}

samplelist_mll = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_LO.root'}

#samplelist_mll = {'DATA':'uhh2.AnalysisModuleRunner.DATA.DATA.root','singletop':'uhh2.AnalysisModuleRunner.MC.ST.root','diboson':'uhh2.AnalysisModuleRunner.MC.Diboson.root','ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root','wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__B.root','wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__C.root','wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets_LNu__L.root', 'ZprimeNarrow0500':'uhh2.AnalysisModuleRunner.MC.Zp01w0500.root','zjets':'uhh2.AnalysisModuleRunner.MC.DYJetsToLL_LO.root'}

categories=['T1','T0B1','T0B0']
#fout = TFile('mu_theta_0413_narrow_v1.root', 'recreate')
fout = TFile('mu_theta_20160725.root', 'recreate')
gROOT.SetBatch(kTRUE)
binning = numpy.arange(0,4100,100)
##low chi2
for cat in categories:
    cut_string='(Mttbar<2000. && muoN==1 & rec_chi2<30'
    if cat == 'T1':
        h_string='mu_1top_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","Mttbar")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==1  & btagN>=0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                tempdata = TH1F("tempdata","tempdata",20,0,2000)
                mytree.Draw("invmass>>tempdata",cut)
                tempdata.SetName(h_string+key_sample)
                fout.WriteObject(tempdata,h_string+key_sample)
                del tempdata
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",20,0,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,0,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",20,0,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,0,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",20,0,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,0,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",20,0,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,0,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
    elif cat == 'T0B1':
        h_string='mu_0top1btag_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","Mttbar")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==0 & btagN>0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp2data = TH1F("temp2data","temp2data",200,0,2000)
                mytree.Draw("invmass>>temp2data",cut)
                temp2data.SetName(h_string+key_sample)
                fout.WriteObject(temp2data,h_string+key_sample)
                del temp2data
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",200,0,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",200,0,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",200,0,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",200,0,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",200,0,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",200,0,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",200,0,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",200,0,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
    elif cat == 'T0B0':
#    if cat == 'T0B0':
        h_string='mu_0top0btag_mttbar__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","Mttbar")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==0 & btagN==0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp3data = TH1F("temp3data","temp3data",200,0,2000)
                mytree.Draw("invmass>>temp3data",cut)
                temp3data.SetName(h_string+key_sample)
                fout.WriteObject(temp3data,h_string+key_sample)
                del temp3data
            elif 'Zprime' in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",200,0,2000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",200,0,2000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",200,0,2000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",200,0,2000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",200,0,2000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",200,0,2000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",200,0,2000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",200,0,2000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys 

##high chi2
for cat in categories:
    cut_string='(muoN==1 & rec_chi2>=30'
    if cat == 'T1':
        h_string='mu_1top_mttbar_highChi2__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","Mttbar")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==1  & btagN>=0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                tempdata = TH1F("tempdata","tempdata",80,0,8000)
                mytree.Draw("invmass>>tempdata",cut)
                tempdata.SetName(h_string+key_sample)
                fout.WriteObject(tempdata,h_string+key_sample)
                del tempdata
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",80,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",80,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",80,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",80,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",80,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",80,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",80,0,8000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(h_string+key_sample)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        fout.WriteObject(temp,h_string+key_sample)
                        del temp
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",80,0,8000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(h_string+key_sample+"__"+syst)
                        print "Rebinning T1 nom+sys:", str(tempsys.GetNbinsX())
                        fout.WriteObject(tempsys,h_string+key_sample+"__"+syst)
                        del tempsys
    elif cat == 'T0B1':
        h_string='mu_0top1btag_mttbar_highChi2__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","Mttbar")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==0 & btagN>0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp2data = TH1F("temp2data","temp2data",400,0,8000)
                mytree.Draw("invmass>>temp2data",cut)
                temp2data.SetName(h_string+key_sample)
                fout.WriteObject(temp2data,h_string+key_sample)
                del temp2data
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",400,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",400,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",400,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",400,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",400,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",400,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==0 & btagN>0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",400,0,8000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(h_string+key_sample)
                        fout.WriteObject(temp2,h_string+key_sample)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",400,0,8000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp2sys,h_string+key_sample+"__"+syst)
                        del temp2sys
    elif cat == 'T0B0':
        h_string='mu_0top0btag_mttbar_highChi2__'
        for key_sample in samplelist:
            myfile = TFile(samplelist[key_sample])
            print "opening", myfile
            mytree = myfile.Get("AnalysisTree")
            print "getting", mytree
            mytree.SetAlias("invmass","Mttbar")
            if key_sample == 'DATA':
                cut = str(cut_string+' & ttagN==0 & btagN==0)')
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp3data = TH1F("temp3data","temp3data",400,0,8000)
                mytree.Draw("invmass>>temp3data",cut)
                temp3data.SetName(h_string+key_sample)
                fout.WriteObject(temp3data,h_string+key_sample)
                del temp3data
            elif 'Zprime' in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",400,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",400,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",400,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",400,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'wjets' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",400,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",400,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
            elif 'zjets' or 'diboson' in key_sample:
                for syst in systematic_direction_otherbkgs:
                    cut = str(cut_string+' & ttagN==0  & btagN==0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",400,0,8000)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",400,0,8000)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
                        
# # # # ## m_ll
# # # # h_string='mu_mll__'
# # # # cut_str=str('(muoN==2 && sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))<111 && sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))>71)')
# # # # #cut_str=str('(sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))<111 && sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))>71)')
# # # # for key_sample in samplelist:
# # # #     myfile = TFile(samplelist[key_sample])
# # # #     print "opening", myfile
# # # #     mytree = myfile.Get("AnalysisTree")
# # # #     print "getting", mytree
# # # #     mytree.SetAlias("invmass","sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))")
# # # #     if key_sample == 'DATA':
# # # #         cut = cut_str
# # # #         print "Processing: ",key_sample
# # # #         print "Applying cut:",cut
# # # #         temp3data = TH1F("temp3data","temp3data",10,70,120)
# # # #         mytree.Draw("invmass>>temp3data",cut)
# # # #         temp3data.SetName(h_string+key_sample)
# # # #         fout.WriteObject(temp3data,h_string+key_sample)
# # # #         del temp3data
# # # #     elif 'Zprime' in key_sample:
# # # #         for syst in systematic_direction_signal:
# # # #                     cut = str(cut_str+'*wgtMC__GEN*'+systematic_direction_signal[syst])
# # # #                     print "Processing: ",key_sample
# # # #                     print "Applying cut:",cut
# # # #                     if syst == 'nominal':
# # # #                         temp3 = TH1F("temp3","temp3",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3",cut)
# # # #                         temp3.SetName(h_string+key_sample)
# # # #                         fout.WriteObject(temp3,h_string+key_sample)
# # # #                         del temp3
# # # #                     elif 'nominal' not in syst:
# # # #                         temp3sys = TH1F("temp3sys","temp3sys",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3sys",cut)
# # # #                         temp3sys.SetName(h_string+key_sample+"__"+syst)
# # # #                         fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
# # # #                         del temp3sys
# # # #     elif 'ttbar' in key_sample:
# # # #                 for syst in systematic_direction_ttbar:
# # # #                     cut = str(cut_str+'*wgtMC__GEN*'+systematic_direction_ttbar[syst])
# # # #                     print "Processing: ",key_sample
# # # #                     print "Applying cut:",cut
# # # #                     if syst == 'nominal':
# # # #                         temp3 = TH1F("temp3","temp3",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3",cut)
# # # #                         temp3.SetName(h_string+key_sample)
# # # #                         fout.WriteObject(temp3,h_string+key_sample)
# # # #                         del temp3
# # # #                     elif 'nominal' not in syst:
# # # #                         temp3sys = TH1F("temp3sys","temp3sys",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3sys",cut)
# # # #                         temp3sys.SetName(h_string+key_sample+"__"+syst)
# # # #                         fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
# # # #                         del temp3sys
# # # #     elif 'wjets' in key_sample:
# # # #                 for syst in systematic_direction_wjets:
# # # #                     cut = str(cut_str+'*wgtMC__GEN*'+systematic_direction_wjets[syst])
# # # #                     print "Processing: ",key_sample
# # # #                     print "Applying cut:",cut
# # # #                     if syst == 'nominal':
# # # #                         temp3 = TH1F("temp3","temp3",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3",cut)
# # # #                         temp3.SetName(h_string+key_sample)
# # # #                         fout.WriteObject(temp3,h_string+key_sample)
# # # #                         del temp3
# # # #                     elif 'nominal' not in syst:
# # # #                         temp3sys = TH1F("temp3sys","temp3sys",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3sys",cut)
# # # #                         temp3sys.SetName(h_string+key_sample+"__"+syst)
# # # #                         fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
# # # #                         del temp3sys
# # # #     elif 'diboson' in key_sample:
# # # #                 for syst in systematic_direction_otherbkgs:
# # # #                     cut = str(cut_str+'*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
# # # #                     print "Processing: ",key_sample
# # # #                     print "Applying cut:",cut
# # # #                     if syst == 'nominal':
# # # #                         temp3 = TH1F("temp3","temp3",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3",cut)
# # # #                         temp3.SetName(h_string+key_sample)
# # # #                         fout.WriteObject(temp3,h_string+key_sample)
# # # #                         del temp3
# # # #                     elif 'nominal' not in syst:
# # # #                         temp3sys = TH1F("temp3sys","temp3sys",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3sys",cut)
# # # #                         temp3sys.SetName(h_string+key_sample+"__"+syst)
# # # #                         fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
# # # #                         del temp3sys 

# # # #     elif 'zjets' in key_sample:
# # # #                 for syst in systematic_direction_otherbkgs:
# # # #                     cut = str(cut_str+'*(wgtMC__GEN)*'+systematic_direction_DY[syst])
# # # #                     print "Processing: ",key_sample
# # # #                     print "Applying cut:",cut
# # # #                     if syst == 'nominal':
# # # #                         temp3 = TH1F("temp3","temp3",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3",cut)
# # # #                         temp3.SetName(h_string+key_sample)
# # # #                         fout.WriteObject(temp3,h_string+key_sample)
# # # #                         del temp3
# # # #                     elif 'nominal' not in syst:
# # # #                         temp3sys = TH1F("temp3sys","temp3sys",10,70,120)
# # # #                         mytree.Draw("invmass>>temp3sys",cut)
# # # #                         temp3sys.SetName(h_string+key_sample+"__"+syst)
# # # #                         fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
# # # #                         del temp3sys 


## m_ll
h_string='mu_mll__'
cut_str=str('(muoN==2 && sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))<111 && sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))>71)')
for key_sample in samplelist_mll:
    myfile = TFile(samplelist_mll[key_sample])
    print "opening", myfile
    mytree = myfile.Get("AnalysisTree")
    print "getting", mytree
    mytree.SetAlias("invmass","sqrt(lep1.M()+lep2.M()+2*(lep1.E()*lep2.E()-lep1.Px()*lep2.Px()-lep1.Py()*lep2.Py()-lep1.Pz()*lep2.Pz()))")
    if key_sample == 'DATA':
        cut = cut_str
        print "Processing: ",key_sample
        print "Applying cut:",cut
        temp3data = TH1F("temp3data","temp3data",10,70,120)
        mytree.Draw("invmass>>temp3data",cut)
        temp3data.SetName(h_string+key_sample)
        fout.WriteObject(temp3data,h_string+key_sample)
        del temp3data
    #elif 'Zprime' or 'ttbar' or 'wjets' or 'diboson' or 'zjets' in key_sample:
    elif 'ttbar' or 'zjets' in key_sample:
        for syst in systematic_direction_DY:
                    cut = str(cut_str+'*wgtMC__GEN*'+systematic_direction_DY[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp3 = TH1F("temp3","temp3",10,70,120)
                        mytree.Draw("invmass>>temp3",cut)
                        temp3.SetName(h_string+key_sample)
                        fout.WriteObject(temp3,h_string+key_sample)
                        del temp3
                    elif 'nominal' not in syst:
                        temp3sys = TH1F("temp3sys","temp3sys",10,70,120)
                        mytree.Draw("invmass>>temp3sys",cut)
                        temp3sys.SetName(h_string+key_sample+"__"+syst)
                        fout.WriteObject(temp3sys,h_string+key_sample+"__"+syst)
                        del temp3sys
