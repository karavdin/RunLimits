#! /usr/bin/env pythonDWE
### Filter definitions ###
print 'Hello MLE'

ele_ifile = ['ele_theta_wFlatShapeSyst_addedPDF_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_addedPDF_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_addedPDF_addedQ2_rebinned_woPDF_wST_wDY_wVV.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_addedPDF_addedQ2_rebinned_wPDF_wST_wDY_wVV_wDiboson.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_widerBins_addedPDF_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min250_addedPDF_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_widerBins_min250_addedPDF_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_narrowBins_addedPDF_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_chi2below600_addedPDF_addedQ2_rebinned.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_chi2below600_addedPDF_addedQ2_rebinned15.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_chi2below600_addedPDF_addedQ2_rebinned30.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_chi2below600_addedPDF_addedQ2_rebinned15.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_allPDF_addedPDF_addedQ2_rebinned30.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_allPDF_rebinned30_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_PDFttbarAndWjetsL_rebinned_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_allPDF_rebinned10_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_20bins_allPDF_rebinnedSmallBkg_rebinned_addedPDF_addedQ2.root']

#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCDt0only_rebinned_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCD_SR_CR4_only_rebinned_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_20bins_allPDF_QCD_SR_CR4_only_rebinnedSmallBkg_rebinned_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_20bins_allPDF_MET120_rebinned_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_allPDF_rebinned05_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_allPDF_rebinned01_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_QCDHT_allPDF_rebinned_addedPDF_addedQ2.root']

#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_allPDF_addedPDF_addedQ2_rebinned05.root']
#muo_ifile = ['mu_theta_wFlatShapeSyst_min200_allPDF_addedPDF_addedQ2_rebinned01.root']

#muo_ifile = ['mu_theta_wFlatShapeSyst_METcut_addedPDF_addedQ2_rebinned.root']

muo_ifile = ['mu_theta_wFlatShapeSyst_min200_20bins_wTopPtrewSymSyst_rebinned_addedPDF_addedQ2.root']
lep_ifile = ['lep_theta_wFlatShapeSyst_rebinned_addedQ2_addedPDF.root']

def narrow_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
#    if not 'ZprimeNarrow' in pname: return False
    if not 'Zprime' in pname: return False
#    mass = pname.strip('ZprimeNarrow')
    mass = pname.strip('Zprime')
    return float(mass) <= 2000

def wide_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'ZprimeWide' in pname: return False
    mass = pname.strip('ZprimeWide')
    return float(mass) <= 4000

def rsg_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'RSgluon' in pname: return False
    mass = pname.strip('RSgluon')
    return float(mass) <= 4000

def build_boosted_semileptonic_model(files, filter, signal, mcstat = True):
#def build_boosted_semileptonic_model(files, filter, signal, mcstat = False):
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    #model.fill_histogram_zerobins(epsilon=0.01)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    obs =  model.get_observables()
    print "set1 ", obs
#    model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_chi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar','mu_0top_antiWJetsMVA2_chi2_mttbar',]))

    #model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_antichi2_mttbar', 'mu_0top_antiWJetsMVA2_antichi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar']))
    model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_chi2_mttbar', 'mu_0top_antiWJetsMVA2_chi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar']))
#    model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_chi2_mttbar', 'mu_0top_antiWJetsMVA2_chi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar','mu_0top_antiWJetsMVA3_antichi2_mttbar']))

#    model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_chi2_mttbar','mu_0top_antiWJetsMVA2_chi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar', 'mu_0top_antiWJetsMVA3_antichi2_mttbar']))
   #model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_chi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar']))
   #model.restrict_to_observables(set(['mu_0top_antiWJetsMVA2_chi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar']))
   #model.restrict_to_observables(set(['mu_0top_antiWJetsMVA2_antichi2_mttbar', 'mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar']))
   # model.restrict_to_observables(set(['mu_1top_WJetsMVA_chi2_mttbar', 'mu_0top_WJetsMVA_chi2_mttbar']))
#    model.restrict_to_observables(set(['mu_1top_WJetsMVA_chi2_mttbar']))
#    model.restrict_to_observables(set(['mu_0top_WJetsMVA_chi2_mttbar']))
    #model.restrict_to_observables(set(['mu_0top_WJetsMVA_chi2_mttbar']))
    #model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_antichi2_mttbar','mu_0top_antiWJetsMVA2_antichi2_mttbar']))
    #model.restrict_to_observables(set(['mu_0top_antiWJetsMVA2_antichi2_mttbar']))
    #model.restrict_to_observables(set(['mu_0top_antiWJetsMVA3_antichi2_mttbar']))
    obs =  model.get_observables()
    print "set2 ", obs
    #print model

    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.025), p)
        if 'VV' in p:
            print "!!! scale predictions by 0.0 for ",p
            model.scale_predictions(0.0,p)
        if 'diboson' in p:
            print "!!! scale predictions by 0.0 for ",p
            model.scale_predictions(0.0,p)
        # if 'ttbar' in p:
        #     print "!!! scale predictions by 0.91 for ",p
        #     model.scale_predictions(0.91,p)
        # if 'qcd_mu' in p:
        #     print "!!! scale predictions by 0.7 for ",p
        #     model.scale_predictions(0.7,p)
        # if 'qcd_mu' in p:
        #     print "!!! scale predictions by 0.08 for ",p
        #     model.scale_predictions(0.08,p)

        # if 'ST' in p:
        #     print "!!! scale predictions by 0.8 for ",p
        #     model.scale_predictions(0.8,p)

        # if 'wjets_l' in p:
        #     print "!!! scale predictions by 0.0 for ",p
        #     model.scale_predictions(0.0,p)
        # if 'wjets_b' in p:
        #     print "!!! scale predictions by 0.0 for ",p
        #     model.scale_predictions(0.0,p)
        # if 'wjets_c' in p:
        #     print "!!! scale predictions by 0.0 for ",p
        #     model.scale_predictions(0.0,p)
        # if 'qcd_mu' in p:
        #     print "!!! scale predictions by 0.0 for ",p
        #     model.scale_predictions(0.0,p)
        # if 'ST' in p:
        #     print "!!! scale predictions by 0.0 for ",p
        #     model.scale_predictions(0.0,p)
        # if 'DY' in p:
        #     print "!!! scale predictions by 0.0 for ",p
        #     model.scale_predictions(0.0,p)
        # if 'ttbar' in p:
        #     print "!!! scale predictions by 0.0 for ",p
        #     model.scale_predictions(0.0,p)

    # for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
    #     if 'ttbar' in p:
    #         models.scale_predictions(0.921,obs)
            
#     # for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
#     #     model.add_lognormal_uncertainty('eleORjet_trig', math.log(1.05), p, obs)

    model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.10), 'ttbar')
 #   model.add_asymmetric_lognormal_uncertainty('ttbar_rate',   math.log(1.20),math.log(1.20), 'ttbar')
    # model.add_lognormal_uncertainty('others_rate',  math.log(1.50), 'wjets_b')
    # model.add_lognormal_uncertainty('others_rate',  math.log(1.50), 'wjets_c')
#    model.add_lognormal_uncertainty('wh_rate',  math.log(1.50), 'wjets_b')
#    model.add_lognormal_uncertainty('wh_rate',  math.log(1.50), 'wjets_c')
    # model.add_lognormal_uncertainty('wb_rate',  math.log(1.50), 'wjets_b')
    # model.add_lognormal_uncertainty('wc_rate',  math.log(1.50), 'wjets_c')

    model.add_lognormal_uncertainty('other_rate',  math.log(1.50), 'wjets_b')
    model.add_lognormal_uncertainty('other_rate',  math.log(1.50), 'wjets_c')

    #model.add_lognormal_uncertainty('wb_rate',  math.log(1.50), 'wjets_b')
# #    model.add_lognormal_uncertainty('others_rate',  math.log(1.50), 'wjets_b')
    #model.add_lognormal_uncertainty('wc_rate',  math.log(1.50), 'wjets_c')
#    model.add_lognormal_uncertainty('others_rate',  math.log(1.50), 'wjets_c')
    model.add_lognormal_uncertainty('wl_rate',  math.log(1.10), 'wjets_l')
    model.add_lognormal_uncertainty('ST_rate', math.log(1.50), 'ST')
#    model.add_lognormal_uncertainty('other_rate', math.log(1.50), 'ST')
    model.add_lognormal_uncertainty('other_rate', math.log(1.50), 'DY')
#    model.add_lognormal_uncertainty('other2_rate', math.log(1.50), 'ST')
#    model.add_lognormal_uncertainty('DY_rate', math.log(1.50), 'DY')
#    model.add_lognormal_uncertainty('qcd_rate', math.log(1.50), 'qcd_mu')

#    model.add_lognormal_uncertainty('other_rate', math.log(1.50), 'ST')
#    model.add_lognormal_uncertainty('other_rate', math.log(1.50), 'DY')
    model.add_lognormal_uncertainty('other_rate', math.log(1.50), 'qcd_mu')
    
    for obs in model.get_observables():
        model.rebin(obs,1)

    return model


import exceptions
import pickle

def build_model(type):

    model = None

    if type == 'narrow_resonances_muon':
        model = build_boosted_semileptonic_model(
           muo_ifile,
           narrow_resonances,
           'Zprime*',
           #eflag = False
        )

    elif type == 'wide_resonances_muon':

        model = build_boosted_semileptonic_model(
           muo_ifile,
           wide_resonances,
           'ZprimeWide*',
           #eflag = False
        )

    elif type == 'rsg_resonances_muon':

        model = build_boosted_semileptonic_model(
           muo_ifile,
           rsg_resonances,
           'RSgluon*',
           #eflag = False
        )

    elif type == 'narrow_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           narrow_resonances,
           'Zprime*',
           #eflag = True
        )

    elif type == 'wide_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           wide_resonances,
           'ZprimeWide*',
          # eflag = True
        )

    elif type == 'rsg_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           rsg_resonances,
           'RSgluon*',
          # eflag = True
        )

    elif type == 'narrow_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           narrow_resonances,
           'Zprime*',
           #eflag = False
        )

    elif type == 'wide_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           wide_resonances,
           'ZprimeWide*',
           #eflag = True
        )

    elif type == 'rsg_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           rsg_resonances,
           'RSgluon*',
           #eflag = True
        )

    else: raise exceptions.ValueError('Type %s is undefined' % type)

    # for p in model.distribution.get_parameters():
    #     d = model.distribution.get_distribution(p)
    #     if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
    #         model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
    #     if p == 'toptag' or p == 'subjbtag':
    #         model.distribution.set_distribution_parameters(p, width = float("inf"))
    #     if (p == 'topmistag'): model.distribution.set_distribution_parameters(p, width = float(1.25))
    #     #        if (p == 'subjbtag'): model.distribution.set_distribution_parameters(p, width = float(0.00001))
    #     if (p == 'q2'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
    #     if (p == 'q2_wjets'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
    #     if (p == 'matching_wjets'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
    #     if (p == 'pdf'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
    #     if (p == 'misErr'): model.distribution.set_distribution_parameters(p, width = float(0.0001))

    for p in model.distribution.get_parameters():
        #print p
        d = model.distribution.get_distribution(p)
#        print d
        if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
          #   model.distribution.set_distribution_parameters(p, range = [-1.0, 1.0])
#            model.distribution.set_distribution_parameters(p, range = [-3.0, 3.0])
            model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
  #       #if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'))
        if (p == 'wl_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
      #  if (p == 'other_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
        #if (p == 'wc_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
        #if (p == 'ST_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
#  #       if (p == 'diboson_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
#        if (p == 'qcd_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
        if (p == 'ttbar_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
#        if (p == 'qcd_rate'): model.distribution.set_distribution_parameters(p, width = 0.1) 

        #if (p == 'diboson_rate'): model.distribution.set_distribution_parameters(p,  mean = -1.00, width = 0.001) 

#        if (p == 'toppt_reweight'): model.distribution.set_distribution_parameters(p, width = 0.001)
        #if (p == 'q2wjets'): model.distribution.set_distribution_parameters(p, width = 0.001)

        #if (p == 'PDF'): model.distribution.set_distribution_parameters(p, width = 0.0001)
        # #if (p == 'lumi'): model.distribution.set_distribution_parameters(p, width = 0.0001)
        # if (p == 'muHLT'): model.distribution.set_distribution_parameters(p, width = 0.0001)
        # if (p == 'muID'): model.distribution.set_distribution_parameters(p, width = 0.0001)
        # if (p == 'muTRK'): model.distribution.set_distribution_parameters(p, width = 0.0001)
        # # if (p == 'q2ttbar'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # # if (p == 'pileup'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # # if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # # if (p == 'mistoptag'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # if (p == 'jec'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # # if (p == 'jer'): model.distribution.set_distribution_parameters(p, width = 0.001)

        # # #switch off all not so important cvs systematics for test
        # if (p == 'csv_hf'): model.distribution.set_distribution_parameters(p, width = 0.0001)
        # if (p == 'csv_lf'): model.distribution.set_distribution_parameters(p, width = 0.0001)
        # if (p == 'csv_hfstats1'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # if (p == 'csv_hfstats2'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # if (p == 'csv_cferr1'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # if (p == 'csv_cferr2'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # if (p == 'csv_jes'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # if (p == 'csv_lfstats1'): model.distribution.set_distribution_parameters(p, width = 0.001)
        # if (p == 'csv_lfstats2'): model.distribution.set_distribution_parameters(p, width = 0.001)
        

        # if (p == 'qcd_rate'): model.distribution.set_distribution_parameters(p,  width = 0.001) 
        # if (p == 'ST_rate'): model.distribution.set_distribution_parameters(p,  width = 0.001) 
        # if (p == 'DY_rate'): model.distribution.set_distribution_parameters(p,  width = 0.001) 
        # if (p == 'VV_rate'): model.distribution.set_distribution_parameters(p,  width = 0.001) 
        # if (p == 'diboson_rate'): model.distribution.set_distribution_parameters(p,  width = 0.001) 
        # if (p == 'wh_rate'): model.distribution.set_distribution_parameters(p,  width = 0.001) 
        # if (p == 'wl_rate'): model.distribution.set_distribution_parameters(p,  width = 0.001) 

        print p, model.distribution.get_distribution(p)
        
 #    # #     #     # if p == 'mistoptag':
 #    # #     #     #     model.distribution.set_distribution_parameters(p, width = float('Inf'))
 #    # #     #     #     print p, model.distribution.get_distribution(p)
        
 #    #     # if (p == 'wb_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'))  
 #    #     # if (p == 'wc_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'))  
 #    #     #if (p == 'wl_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'))  
 #    #     # if (p == 'wh_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf')) 
        
  
 #    # # #for p in ['toptag', 'topmistag', 'bmistag', 'btag']:
 #    # # #model.distribution.set_distribution_parameters(p, width = float('inf'), range = [-0.0001,0.0001])
 #    # # for p in model.distribution.get_parameters():
 #    # #     print p
 #    # #     # d = model.distribution.get_distribution(p)
 #    # #     # if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
 #    # #     #     model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
 #    # #     if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
 #    # #     #if (p == 'topmistag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
 #    # #     #if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-1.0, 1.0])
 #    # #     #if (p == 'topmistag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-1.0, 1.0])
 #    # #     if (p == 'ttbar_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
        
 #    # #     if (p == 'wjets_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
 #    # #     #if (p == 'wl_rate'): model.distribution.set_distribution_parameters(p, mean = 0.19, width = 0.0001)
 #    # #     #if (p == 'wc_rate'): model.distribution.set_distribution_parameters(p, mean = 1.85, width = 0.0001)
 #    # #     if (p == 'diboson_rate'): model.distribution.set_distribution_parameters(p, mean = 1.0, width = 0.0001)
 #    # #     #if (p == 'zj_rate'): model.distribution.set_distribution_parameters(p, mean = -0.207, width = 0.0001)
 #    # #     if (p == 'zj_rate'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
 #    # #     #if (p == 'pileup'): model.distribution.set_distribution_parameters(p, mean = 1.3, width = 0.0001)
 #    # #     #if (p == 'matching_wjets'): model.distribution.set_distribution_parameters(p, mean = -0.44, width = 0.0001)
 #    # #     #if (p == 'jer'): model.distribution.set_distribution_parameters(p, mean = 1.1, width = 0.0001)
 #    # #     #if (p == 'q2'): model.distribution.set_distribution_parameters(p, mean = 0.26, width = 0.0001)
 #    # #     #if (p == 'jec'): model.distribution.set_distribution_parameters(p, mean = 0.33, width = 0.0001)
 #    # #     #if (p == 'eleORjet_trig'): model.distribution.set_distribution_parameters(p, mean = 0.05, width = 0.0001)
 #    # #     #if (p == 'q2_wjets'): model.distribution.set_distribution_parameters(p, mean = 0.17, width = 0.0001)
 #    # #     #if (p == 'lumi'): model.distribution.set_distribution_parameters(p, mean = 0.28, width = 0.0001)
 #    # #     #if (p == 'bmistag'): model.distribution.set_distribution_parameters(p, mean = 0.56, width = 0.0001)
 #    # #     #if (p == 'eleid'): model.distribution.set_distribution_parameters(p, mean = 0.01, width = 0.0001)
 #    # #     #if (p == 'btag'): model.distribution.set_distribution_parameters(p, mean = 1.36, width = 0.0001)
 #    # #     #if (p == 'muoid'): model.distribution.set_distribution_parameters(p, mean = -0.58, width = 0.0001)
 #    # #     #if (p == 'pdf'): model.distribution.set_distribution_parameters(p, mean = -0.66, width = 0.0001)
 #    # #     #model.rebin('el_mttbar',50)
 #    # #     #model.rebin('mu_mttbar',47)

    return model


# Code introduced by theta_driver

# Building the statistical model

#options = Options()
#options.set('minimizer','strategy','robust')

#args = {'type': 'narrow_resonances_electron'}
args = {'type': 'narrow_resonances_muon'}
#args = {'type': 'narrow_resonances_lepton'}
#args = {'type': 'bkg_muon'}
model = build_model(**args)
#print model.distribution.get_parameters()
#model_summary(model)
#execfile('/afs/desy.de/user/k/karavdia/RunLimits_Zprime/MLF_Yields_Uncertainties/utils.py')
execfile('/afs/desy.de/user/k/karavdia/xxl/af-cms/RunLimitsZprime_2016/RunLimits/MLF_Yields_Uncertainties/utils.py')
#model_summary(model,create_plots=True, all_nominal_templates=True, shape_templates=True)
tablesIn = model_summary(model)
#generate_yield_table_AN(tablesIn['rate_table'],'BEFORE','elec')
generate_yield_table_AN(tablesIn['rate_table'],'BEFORE','muon')
#generate_yield_table_AN(tablesIn['rate_table'],'BEFORE','lep')
# # # file3 = open('before_MLE_rates.txt', 'w')
# # # file3.write(tablesIn['rate_table'].tex())
# # # file3.close()



### theta 2 ###
options = Options()
#options.set('minimizer', 'strategy', 'newton_vanilla')
#options.set('minimizer', 'strategy', 'tminuit')

#TEST
#options.set('minimizer', 'strategy', 'fast') #TEST
options.set('minimizer', 'strategy', 'robust') #TEST
#options.set('minimizer', 'minuit_tolerance_factor', '10')
#options.set('minimizer', 'minuit_tolerance_factor', '10000')
options.set('minimizer', 'minuit_tolerance_factor', '100000')
options.set('minimizer', 'mcmc_iterations', '1000')
#options.set('minimizer', 'always_mcmc', 'True')
#options.set('cls_limits', 'write_debuglog', 'True')
#options.set('mcmc', 'strategy', 'asimov_widths')
#options.set('mcmc', 'strategy', 'asimov_der_cov')

#options.set('global', 'debug', 'True')

#options.set('minimizer', 'strategy', 'robust')
sig = ''
sig_a = []
if sig != '': sig_a.append(sig)
res = mle(model, input='data', n=1, signal_process_groups = {sig : sig_a}, signal_prior = 'fix:0', chi2 = True, ks=True, with_error = True, with_covariance=True, options = options)
#res = mle(model, input='data', n=1, signal_process_groups = {sig : sig_a}, signal_prior = 'fix:0', chi2 = True, ks=True, with_error = True, options = options)
#
#toys:X. This uses toy data as input where the signal strength parameter beta_signal is set to X. Nuisance parameters are sampled according to their priors, using model.distribution
#res = mle(model, input='toys:0.0', n=1000, signal_process_groups = {sig : sig_a}, chi2 = True,  with_error = True, options = options)

#res = mle(model, input='toys:0.0', n=100, signal_process_groups = {sig : sig_a}, chi2 = True, ks = True, with_error = True, with_covariance=True, options = options)

#res = mle(model, input='/afs/desy.de/user/k/karavdia/xxl/af-cms/RunLimitsZprime_2016/RunLimits/MLF_Yields_Uncertainties/produce_toys_for_mle_yields_2016_theta2_muon/cache/pdw-toys:0.0--7c00521156.db', n=1000, signal_process_groups = {sig : sig_a}, chi2 = True, ks = True, with_error = True, with_covariance=True, options = options)

#res_nll_scan = nll_scan(model, input='/afs/desy.de/user/k/karavdia/xxl/af-cms/RunLimitsZprime_2016/RunLimits/MLF_Yields_Uncertainties/produce_toys_for_mle_yields_2016_theta2_muon/cache/pdw-toys:0.0--7c00521156.db', n=1000, npoints=10, range=[0.0, 3.0], parameter='jec', signal_process_groups = {sig : sig_a}, options = options)
# #print res_nll_scan
#print len(res_nll_scan[sig])

#res = mle(model, input='toys:0.0', n=1, signal_process_groups = {sig : sig_a}, chi2 = True,  with_error = True, with_covariance=True, options = options)
# hist_data = model.get_data_histogram('mu_0top_WJetsMVA_chi2_mttbar')
# write_histograms_to_rootfile(hist_data,'data_'+'mu_0top_WJetsMVA_chi2_mttbar'+'.root')
for obs in model.get_observables():
    print "binning for ", obs 
    print "  is ", model.get_range_nbins(obs)
#evaluate_prediction(model,res)

#toys-asimov:X. This uses asimov toy data (i.e., toy data without Poisson smearing) where beta_signal is set to X. Nuisance parameters are fixed to the mean value from model.distribution (usually 0, but can be modified)
# res = mle(model, input='toys-asimov:0.0', n=1000, signal_process_groups = {sig : sig_a}, chi2 = True,  with_error = True, options = options)
print '\\n-- MLE: fit results (# = '+str(len(res[sig][model.get_parameters(sig_a)[0]]))+')'
fitres = {}
print 'chi2 =',res[sig]['__chi2']
print 'ks =',res[sig]['__ks']
file1 = open('mle_fit.txt', 'w')
for p in model.get_parameters(sig_a):
    mean = sdev = 0.0
    for pair in res[sig][p]:
        mean += pair[0]
        sdev += pair[1]
    mean /= len(res[sig][p])
    sdev /= len(res[sig][p])
    fitres[p] = {}
    fitres[p][0] = mean
    fitres[p][1] = sdev
    line = ''
    if mean>=0: line += ' '
    line += ' %.3f' % mean + '  %.3f' % sdev + '  ' + p
    print line
    file1.write(line+'\n')
file1.close()

par_values = {}
par_err_values = {}
#print model.get_parameters([])
for p in model.get_parameters([]):
    par_values[p] = fitres[p][0]
    par_err_values[p] = fitres[p][1]
    print par_err_values[p], p
# rate-scale factors for each process in each observable
mle_coeff = {}
for obs in model.get_observables():
    mle_coeff[obs] = {}
    for p in model.get_processes(obs):
        coeff = model.get_coeff(obs, p).get_value(par_values)
        mle_coeff[obs][p] = coeff
#print mle_coeff
# add stuff.. eg make histograms at the ML point
# print '\\n'
# for p in par_values:
#     # if p == 'ttbar_rate':     print '%.3f' % 1.3**par_values[p] + ' ' + p
#     # elif p == 'wjets_rate':   print '%.3f' % 1.3**par_values[p] + ' ' + p
#     # elif p == 'wl_rate':      print '%.3f' % 1.09**par_values[p] + ' ' + p
#     # elif p == 'wc_rate':      print '%.3f' % 1.23**par_values[p] + ' ' + p
#     # elif p == 'wb_rate':      print '%.3f' % 1.23**par_values[p] + ' ' + p
#     # elif p == 'st_rate':      print '%.3f' % 1.23**par_values[p] + ' ' + p
#     # elif p == 'zj_rate':      print '%.3f' % 1.50**par_values[p] + ' ' + p
#     # elif p == 'diboson_rate': print '%.3f' % 1.20**par_values[p] + ' ' + p
#     # elif p == 'toptag':       print '%.3f' % 1.20**par_values[p] + ' ' + p
#     # elif p == 'subjbtag':     print '%.3f' % 1.20**par_values[p] + ' ' + p
#     if p == 'lumi':     print '%.3f' % 1.027**par_values[p] + ' ' + p
#     if p == 'ttbar_rate':     print '%.3f' % 1.20**par_values[p] + ' ' + p
#     elif p == 'w_rate':      print '%.3f' % 1.25**par_values[p] + ' ' + p
#     elif p == 'wl_rate':      print '%.3f' % 1.25**par_values[p] + ' ' + p
#     elif p == 'wc_rate':      print '%.3f' % 1.25**par_values[p] + ' ' + p
#     elif p == 'wb_rate':      print '%.3f' % 1.50**par_values[p] + ' ' + p
#     elif p == 'st_rate':      print '%.3f' % 1.20**par_values[p] + ' ' + p
#     elif p == 'zj_rate':      print '%.3f' % 1.20**par_values[p] + ' ' + p
#     elif p == 'diboson_rate': print '%.3f' % 1.50**par_values[p] + ' ' + p
#     elif p == 'others_rate': print '%.3f' % 1.50**par_values[p] + ' ' + p
#     elif p == 'toptag':       print '%.3f' % 1.25**par_values[p] + ' ' + p
#     elif p == 'subjbtag':     print '%.3f' % 1.50**par_values[p] + ' ' + p
#     elif p == 'qcd_rate':     print '%.3f' % 1.5**par_values[p] + ' ' + p


print '\\n'
for p in par_values:
    if p == 'lumi':     print '%.3f' % 1.025**par_values[p] + ' ' + p
    if p == 'ttbar_rate':     print '%.3f' % 1.10**par_values[p] + ' ' + p
    elif p == 'w_rate':      print '%.3f' % 1.20**par_values[p] + ' ' + p
    elif p == 'wl_rate':      print '%.3f' % 1.10**par_values[p] + ' ' + p
    elif p == 'wc_rate':      print '%.3f' % 1.50**par_values[p] + ' ' + p
    elif p == 'wb_rate':      print '%.3f' % 1.50**par_values[p] + ' ' + p
    elif p == 'wh_rate':      print '%.3f' % 1.20**par_values[p] + ' ' + p
    elif p == 'ST_rate':      print '%.3f' % 1.50**par_values[p] + ' ' + p
    elif p == 'zjets_rate':      print '%.3f' % 1.50**par_values[p] + ' ' + p
    elif p == 'diboson_rate': print '%.3f' % 1.15**par_values[p] + ' ' + p
    elif p == 'others_rate': print '%.3f' % 1.50**par_values[p] + ' ' + p
    elif p == 'toptag':       print '%.3f' % 1.15**par_values[p] + ' ' + p
    elif p == 'mistoptag':    print '%.3f' % 1.15**par_values[p] + ' ' + p
    elif p == 'subjbtag':     print '%.3f' % 1.50**par_values[p] + ' ' + p
    elif p == 'qcd_rate':     print '%.3f' % 1.5**par_values[p] + ' ' + p
print '\\n'
for p in par_values:
    if p == 'lumi':     print '%.3f' % 1.025**par_values[p], '%.3f' % 1.025**par_err_values[p] + ' ' + p
    if p == 'ttbar_rate':     print '%.3f' % 1.10**par_values[p], '%.3f' % 1.20**par_err_values[p] + ' ' + p
    elif p == 'w_rate':      print '%.3f' % 1.20**par_values[p], '%.3f' % 1.20**par_err_values[p] + ' ' + p
    elif p == 'wl_rate':      print '%.3f' % 1.10**par_values[p], '%.3f' % 1.20**par_err_values[p] + ' ' + p
    elif p == 'wc_rate':      print '%.3f' % 1.50**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p
    elif p == 'wb_rate':      print '%.3f' % 1.50**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p
    elif p == 'wh_rate':      print '%.3f' % 1.20**par_values[p], '%.3f' % 1.20**par_err_values[p] + ' ' + p
    elif p == 'ST_rate':      print '%.3f' % 1.50**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p
    elif p == 'other_rate':      print '%.3f' % 1.50**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p
    elif p == 'zjets_rate':      print '%.3f' % 1.50**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p
    elif p == 'diboson_rate': print '%.3f' % 1.15**par_values[p], '%.3f' % 1.15**par_err_values[p] + ' ' + p
    elif p == 'others_rate': print '%.3f' % 1.50**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p
    elif p == 'toptag':       print '%.3f' % 1.15**par_values[p], '%.3f' % 1.15**par_err_values[p] + ' ' + p
    elif p == 'mistoptag':    print '%.3f' % 1.15**par_values[p], '%.3f' % 1.15**par_err_values[p] + ' ' + p
    elif p == 'subjbtag':     print '%.3f' % 1.50**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p
    elif p == 'qcd_rate':     print '%.3f' % 1.5**par_values[p], '%.3f' % 1.50**par_err_values[p] + ' ' + p



#factors = print_obsproc_factors_rateonly2(model)
file = open('mle_coeff.py', 'w')
file.write(repr(mle_coeff))
file.close()
pickle.dump(mle_coeff, open( "mle_coeff.p", "wb" ) )
apply_factors(model, mle_coeff)
tables = model_summary(model)
#generate_yield_table(tables['rate_table'])
generate_yield_table_AN(tables['rate_table'],'AFTER','muon')
#generate_yield_table_AN(tables['rate_table'],'AFTER','elec')
#generate_yield_table_AN(tables['rate_table'],'AFTER','lep')

#histos = evaluate_prediction(model, par_values, include_signal=False, observables=None)
#write_histograms_to_rootfile(histos, 'histos-mle.root')
#tables = model_summary(model)
# file2 = open('after_MLE_rates.txt', 'w')
# file2.write(tables['rate_table'].tex())
# file2.close()
#print histos
#plot(histos['ele_01top_antiWJetsMVA_antichi2_mttbar'],'Mttbar','N')

#model_summary(model)

### fit covariance matrix
#run_cov_matrix=False
run_cov_matrix=True
if run_cov_matrix:

    corr = []
    pars = model.get_parameters(sig_a)

    file_cov = open('mle_cov.txt', 'w')
    for i in range(0, len(res[sig]['__cov'][0])):
        corr.append(list())
        file_cov.write(pars[i]+'\\n')
        for j in range(0, len(res[sig]['__cov'][0][i])):
            sigma_ij = res[sig]['__cov'][0][i][j]
            corr[i].append(sigma_ij / (fitres[pars[i]][1] * fitres[pars[j]][1]))
#            if abs(corr[i][j])>2e2 or abs(corr[i][j])<0.001: corr[i][j] = 0 #set 0 for switched off systematics
            if corr[i][j] >= 0: line = ' '
            else: line = ''
            line += '%.3f   '% corr[i][j] + pars[j]
        file_cov.write(line+'\\n')
        file_cov.write('\\n')
    file_cov.close()

    cv = ROOT.TCanvas()
    max_cn = 0
    for line in corr: max_cn = max(max_cn, len(line))
    h2 = ROOT.TH2F('mle_cov', '', max_cn, 0, max_cn, len(corr), 0, len(corr))
    for l in range(0, len(corr)):
        h2.GetYaxis().SetBinLabel(len(corr)-l, pars[l]);
        for c in range(0, len(corr[l])):
            if not l: h2.GetXaxis().SetBinLabel(c+1, pars[c]);
            h2.SetBinContent(c+1, len(corr)-l, corr[l][c])
            h2.SetStats(0)
            h2.SetMarkerSize(0.5)
            ROOT.gStyle.SetPaintTextFormat('1.3g')
            h2.Draw('colz,text')
            h2.GetXaxis().SetNdivisions(-414);
            h2.GetYaxis().SetNdivisions(-414);
            h2.Draw('axis,same')
    cv.SaveAs('mle_cov.pdf')
    cv.SaveAs('mle_cov.root')
    cv.Close() 

report.write_html('htmlout')
