#! /usr/bin/env python

### Filter definitions ###

#muo_ifile = ['mu_theta_0413_narrow_v1_rebinned.root']
#ele_ifile = ['el_theta_0411_narrow_v1_rebinned.root']
#muo_ifile = ['mu_theta_20160703_rebinned.root']
#ele_ifile = ['el_theta_weight_rebinned.root']
ele_ifile = ['el_theta_20161127_rebinned.root']
lep_ifile = ['']

def narrow_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'ZprimeNarrow' in pname: return False
    mass = pname.strip('ZprimeNarrow')
    return float(mass) <= 4000

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

def build_boosted_semileptonic_model(files, filter, signal, eflag=False):
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = True)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)

    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.07), p)
        for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
      #  for obs in ['mu_0top0btag_mttbar','mu_0top1btag_mttbar','mu_1top_mttbar']:
            if 'ttbar' in p and '0top0btag' in obs:
                model.scale_predictions(1.00,p)
            elif 'ttbar' in p and '0top1btag' in obs:
                model.scale_predictions(1.0,p,obs)
            elif 'ttbar' in p and '1top' in obs:
                model.scale_predictions(1.0,p,obs)
            elif 'wjets' in p and '0top1btag' in obs :
                model.scale_predictions(1.0,p,obs)
            elif 'wjets' in p and '1top' in obs:
                model.scale_predictions(1.0,p,obs)
            elif 'wjets' in p and '1top'in obs:
                 model.scale_predictions(1.0,p,obs)
            elif 'zjets' in p:
                 model.scale_predictions(1.0,p)
        #if eflag:
            #for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
                #model.add_lognormal_uncertainty('eleORjet_trig', math.log(1.01), p, obs)

    model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.09), 'ttbar')
#    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets')
    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_c')
    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_b')
    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.09), 'wjets_l')
#    model.add_lognormal_uncertainty('wjetsh_rate',      math.log(1.09), 'wjets_h')
    #model.add_lognormal_uncertainty('wb_rate',      math.log(1.23), 'wb')
    model.add_lognormal_uncertainty('st_rate',      math.log(1.20), 'singletop')
    model.add_lognormal_uncertainty('zj_rate',      math.log(1.20), 'zjets')
    model.add_lognormal_uncertainty('diboson_rate', math.log(1.20), 'diboson')

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

#args = {'type': 'narrow_resonances_electron_no_nuisance'}
args = {'type': 'narrow_resonances_electron'}
#args = {'type': 'wide_resonances_electron'}
#args = {'type': 'rsg_resonances_electron'}

model = build_model(**args)

args = {}

#results = bayesian_limits(model, run_theta = True, **args)
#results = bayesian_limits(model, run_theta = True, n_toy = 1000, n_data = 2, **args)
results = bayesian_limits(model, run_theta = True, n_toy = 100, n_data = 2, **args)
# results = bayesian_limits(model, input='toys:0', n=10, run_theta = True, **args)
exp, obs = results
print exp
#print obs
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
