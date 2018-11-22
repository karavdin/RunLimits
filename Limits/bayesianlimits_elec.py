#! /usr/bin/env python
import pickle

### Filter definitions ###

#ele_ifile = ['ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF_addedQ2_ALL_rebinned.root']
ele_ifile = ['ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF_addedQ2_rebinned.root']

muo_ifile = ['mu_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF_addedQ2.root']
#muo_ifile = ['mu_theta_bdt0p5_chi30_limits_rebinned.root']
#ele_ifile = ['ele_theta_bdt0p5_chi30_limits_rebinned.root']
#ele_ifile = ['ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF_addedQ2.root']
#ele_ifile = ['ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_25bins_rebinned_addedPDF_addedQ2.root']
#ele_ifile = ['ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_woPDF_rebinned_addedPDF_addedQ2.root']
#ele_ifile = ['ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_addedPDF_addedQ2_rebinned.root']
#ele_ifile = ['ele_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinnedSmallBkg_rebinned_addedPDF_addedQ2.root']
#lep_ifile = ['lep_theta_wFlatShapeSyst_allSyst_LIMITS.root']
lep_ifile = ['lep_theta_wFlatShapeSyst_allSyst_wTopPtrewSymSyst_LIMITS_rebinned_addedPDF_addedQ2.root']
#mle_coeff_file = '../MLF_Yields_Uncertainties/mle_coeff.p'
#mle_coeff_file = 'mle_coeff_lep.p'
mle_coeff_file = 'mle_coeff_elec.p'

def apply_factors(model, factors):
    #print factors
    for obs in factors:
        for proc in factors[obs]:
            f = factors[obs][proc]
            if type(f) == str: continue # can happen for "n/a"
            if "Zprime" in proc or "RSgluon" in proc: continue
            print f, proc, obs
            model.scale_predictions(f, proc, obs)

def narrow_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'ZprimeNarrow' in pname: return False
    mass = pname.strip('ZprimeNarrow')
    return float(mass) <= 8000

def wide_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'ZprimeWide' in pname: return False
    mass = pname.strip('ZprimeWide')
    return float(mass) <= 8000

def extrawide_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'ZprimeExtraWide' in pname: return False
    mass = pname.strip('ZprimeExtraWide')
    return float(mass) <= 8000

def ttjets_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'ZprimeTTJets' in pname: return False
    mass = pname.strip('ZprimeTTJets')
    return float(mass) <= 8000

def rsg_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'RSgluon' in pname: return False
    mass = pname.strip('RSgluon')
    return float(mass) <= 8000

def build_boosted_semileptonic_model(files, filter, signal, eflag=False):
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = True)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)

    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.025), p)
      #   for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
      # #  for obs in ['mu_0top0btag_mttbar','mu_0top1btag_mttbar','mu_1top_mttbar']:
      #       if 'ttbar' in p and '0top0btag' in obs:
      #           model.scale_predictions(1.00,p)
      #       elif 'ttbar' in p and '0top1btag' in obs:
      #           model.scale_predictions(1.0,p,obs)
      #       elif 'ttbar' in p and '1top' in obs:
      #           model.scale_predictions(1.0,p,obs)
      #       elif 'wjets' in p and '0top1btag' in obs :
      #           model.scale_predictions(1.0,p,obs)
      #       elif 'wjets' in p and '1top' in obs:
      #           model.scale_predictions(1.0,p,obs)
      #       elif 'wjets' in p and '1top'in obs:
      #            model.scale_predictions(1.0,p,obs)
      #       elif 'zjets' in p:
      #            model.scale_predictions(1.0,p)
      #   #if eflag:
      #       #for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
      #           #model.add_lognormal_uncertainty('eleORjet_trig', math.log(1.01), p, obs)

    mle_coeff = pickle.load(open(mle_coeff_file,"rb"))
    apply_factors(model, mle_coeff)

#    model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.09), 'ttbar')
#    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets')
#    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_c')
#    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_b')
#    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_l')
#    model.add_lognormal_uncertainty('wjetsh_rate',      math.log(1.09), 'wjets_h')
#    model.add_lognormal_uncertainty('wb_rate',      math.log(1.23), 'wb')
#    model.add_lognormal_uncertainty('st_rate',      math.log(1.20), 'singletop')
#    model.add_lognormal_uncertainty('zj_rate',      math.log(1.20), 'zjets')
#    model.add_lognormal_uncertainty('ST_DY_VV_rate', math.log(1.20), 'diboson')
#    model.add_lognormal_uncertainty('ST_rate', math.log(1.20), 'ST')

    return model


def build_boosted_semileptonic_model_no_nuisance(files, filter, signal, eflag=False):
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = True)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)

    # for p in model.processes:
#         model.add_lognormal_uncertainty('lumi', math.log(1.07), p)
#         for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
#       #  for obs in ['mu_0top0btag_mttbar','mu_0top1btag_mttbar','mu_1top_mttbar']:
#             if 'ttbar' in p and '0top0btag' in obs:
#                 model.scale_predictions(1.00,p)
#             elif 'ttbar' in p and '0top1btag' in obs:
#                 model.scale_predictions(1.0,p,obs)
#             elif 'ttbar' in p and '1top' in obs:
#                 model.scale_predictions(1.0,p,obs)
#             elif 'wjets' in p and '0top1btag' in obs :
#                 model.scale_predictions(1.0,p,obs)
#             elif 'wjets' in p and '1top' in obs:
#                 model.scale_predictions(1.0,p,obs)
#             elif 'wjets' in p and '1top'in obs:
#                  model.scale_predictions(1.0,p,obs)
#             elif 'zjets' in p:
#                  model.scale_predictions(1.0,p)
#         #if eflag:
#             #for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
#                 #model.add_lognormal_uncertainty('eleORjet_trig', math.log(1.01), p, obs)

#     model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.09), 'ttbar')
# #    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets')
#     model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_c')
#     model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_b')
#     model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_l')
# #    model.add_lognormal_uncertainty('wjetsh_rate',      math.log(1.09), 'wjets_h')
#     #model.add_lognormal_uncertainty('wb_rate',      math.log(1.23), 'wb')
#     model.add_lognormal_uncertainty('st_rate',      math.log(1.20), 'singletop')
#     model.add_lognormal_uncertainty('zj_rate',      math.log(1.20), 'zjets')
#     model.add_lognormal_uncertainty('diboson_rate', math.log(1.20), 'diboson')

    return model

import exceptions

def build_model(type):

    model = None

    if type == 'narrow_resonances_muon':
        model = build_boosted_semileptonic_model(
           muo_ifile,
           narrow_resonances,
           'ZprimeNarrow*',
           eflag = False
        )

    elif type == 'wide_resonances_muon':

        model = build_boosted_semileptonic_model(
           muo_ifile,
           wide_resonances,
           'ZprimeWide*',
           eflag = False
        )
    elif type == 'ttjets_resonances_muon':

        model = build_boosted_semileptonic_model(
           muo_ifile,
           ttjets_resonances,
           'ZprimeTTJets*',
           eflag = False
        )

    elif type == 'extrawide_resonances_muon':

        model = build_boosted_semileptonic_model(
           muo_ifile,
           extrawide_resonances,
           'ZprimeExtraWide*',
           eflag = False
        )

    elif type == 'rsg_resonances_muon':

        model = build_boosted_semileptonic_model(
           muo_ifile,
           rsg_resonances,
           'RSgluon*',
           eflag = False
        )

    elif type == 'narrow_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           narrow_resonances,
           'ZprimeNarrow*',
           eflag = True
        )

    elif type == 'narrow_resonances_electron_no_nuisance':

        model = build_boosted_semileptonic_model_no_nuisance(
           ele_ifile,
           narrow_resonances,
           'ZprimeNarrow*',
           eflag = True
        )

    elif type == 'wide_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           wide_resonances,
           'ZprimeWide*',
           eflag = True
        )

    elif type == 'ttjets_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           ttjets_resonances,
           'ZprimeTTJets*',
           eflag = True
        )

    elif type == 'extrawide_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           extrawide_resonances,
           'ZprimeExtraWide*',
           eflag = True
        )

    elif type == 'rsg_resonances_electron':

        model = build_boosted_semileptonic_model(
           ele_ifile,
           rsg_resonances,
           'RSgluon*',
           eflag = True
        )

    elif type == 'narrow_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           narrow_resonances,
           'ZprimeNarrow*',
           eflag = True
        )

    elif type == 'wide_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           wide_resonances,
           'ZprimeWide*',
           eflag = True
        )

    elif type == 'ttjets_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           ttjets_resonances,
           'ZprimeTTJets*',
           eflag = True
        )

    elif type == 'extrawide_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           extrawide_resonances,
           'ZprimeExtraWide*',
           eflag = True
        )

    elif type == 'rsg_resonances_lepton':

        model = build_boosted_semileptonic_model(
           lep_ifile,
           rsg_resonances,
           'RSgluon*',
           eflag = True
        )

    else: raise exceptions.ValueError('Type %s is undefined' % type)

    # free_params = [
    #     #      'xsec_ttbar',
    #     #      'xsec_wjets',
    #     #      'xsec_zjets',
    #     # 'toptag',
    #     ]

    # fixd_params = [
    #     #      'muRF_ttbar',
    #     #      'muRF_wjets',
    #     ]

    # for p in model.distribution.get_parameters():
    #     if p in free_params: model.distribution.set_distribution_parameters(p, width = float('inf'))
    #     if p in fixd_params: model.distribution.set_distribution_parameters(p, width = float(.0001))


    for p in model.distribution.get_parameters():
        d = model.distribution.get_distribution(p)
        if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
            model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
            if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float("inf"))

    return model


# Code introduced by theta_driver

# Building the statistical model
#args = {'type': 'narrow_resonances_electron'}

#args = {'type': 'narrow_resonances_muon'}
#args = {'type': 'wide_resonances_muon'}
#args = {'type': 'rsg_resonances_muon'}
#args = {'type': 'extrawide_resonances_muon'}
#args = {'type': 'ttjets_resonances_muon'}

#args = {'type': 'narrow_resonances_electron'}
#args = {'type': 'wide_resonances_electron'}
#args = {'type': 'extrawide_resonances_electron'}
#args = {'type': 'rsg_resonances_electron'}
args = {'type': 'ttjets_resonances_electron'}

#args = {'type': 'narrow_resonances_lepton'}
#args = {'type': 'wide_resonances_lepton'}
#args = {'type': 'rsg_resonances_lepton'}
#args = {'type': 'extrawide_resonances_lepton'}
#args = {'type': 'ttjets_resonances_lepton'}

model = build_model(**args)

args = {}

#results = bayesian_limits(model, run_theta = True, **args)
#results = bayesian_limits(model, run_theta = True, n_toy = 1000, n_data = 2, **args)
results = bayesian_limits(model, run_theta = True, n_toy = 100, n_data = 2, **args)
# results = bayesian_limits(model, input='toys:0', n=10, run_theta = True, **args)
exp, obs = results
print exp
print obs
# #parameters = model.get_parameters('narrow_resonances_muon')
# #parameters = model.get_parameters('narrow_resonances_electron')
# #print parameters
# #print obs
# #execfile("utils.py")
# #limit_table(exp, obs)


# exp_l = bayesian_quantiles(model, input='toys:0', n=1000, run_theta=False, hint_method='zero')
# print exp_l
#obs_l = bayesian_quantiles(model, input='data'  , n=  10, run_theta=False, hint_method='zero')
#for spid in exp_l: exp_l[spid].get_configfile(opts)
#for spid in obs_l: obs_l[spid].get_configfile(opts)
