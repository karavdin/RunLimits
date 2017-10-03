#! /usr/bin/env pythonDWE
### Filter definitions ###
print 'Hello World'

#muo_ifile = ['mu_theta_0408_narrow_v1_rebinned.root']
muo_ifile = ['ele_theta_bdt0p5_chi30_rebinned.root']
#ele_ifile = ['mle_theta_0221_allsignals_allsystematics_rebinned.root']
ele_ifile = ['ele_theta_bdt0p5_chi30_rebinned.root']
lep_ifile = ['ele_theta_bdt0p5_chi30_rebinned.root']


def narrow_resonances(hname):
    if not ('RSgluon' in hname or 'Zprime' in hname): return True
    pname = hname.split('__')[1]
    if not 'ZprimeNarrow' in pname: return False
    mass = pname.strip('ZprimeNarrow')
    return float(mass) <= 700

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
        model.add_lognormal_uncertainty('lumi', math.log(1.025), p)
        #if eflag:
            #for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
            #for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar']:
            #for obs in ['el_mttbar']:
                #model.add_lognormal_uncertainty('ele_trig', math.log(1.05), p, obs)

 #   model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.12), 'ttbar')
    #model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.23), 'ttbar')
    #model.add_lognormal_uncertainty('wjetsl_rate',      math.log(1.5), 'wjets_l')
    #model.add_lognormal_uncertainty('wjets_rate',      math.log(1.12), 'wjets')
#    model.add_lognormal_uncertainty('wjets_rate',      math.log(1.25), 'wjets')
    #model.add_lognormal_uncertainty('wjetsh_rate',      math.log(1.5), 'wjets_h')
    #model.add_lognormal_uncertainty('wc_rate',      math.log(1.25), 'wjetsc')
    #model.add_lognormal_uncertainty('wb_rate',      math.log(1.25), 'wjetsb')
    #model.add_lognormal_uncertainty('st_rate',      math.log(1.5), 'singletop')
    #model.add_lognormal_uncertainty('zj_rate',      math.log(1.5), 'zjets')
    #model.add_lognormal_uncertainty('diboson_rate', math.log(1.5), 'diboson')
    model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.12), 'ttbar')
    model.add_lognormal_uncertainty('wjets_l_rate',      math.log(1.25), 'wjets_l')
    model.add_lognormal_uncertainty('wjets_b_rate',      math.log(1.25), 'wjets_b')
    model.add_lognormal_uncertainty('wjets_c_rate',      math.log(1.25), 'wjets_c')
    model.add_lognormal_uncertainty('ST_VV_DY_rate', math.log(1.15), 'diboson')


    for p in model.distribution.get_parameters():
        print p
        d = model.distribution.get_distribution(p)
        if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
            model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])

            
            if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
            #if (p == 'topmistag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
            #         #if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-1.0, 1.0])
            #         #if (p == 'topmistag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-1.0, 1.0])
            if (p == 'ttbar_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
            #         if (p == 'ttbar_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
            #         #if (p == 'st_rate'): model.distribution.set_distribution_parameters(p, mean = 1.0, width = 0.0001)
            if (p == 'wjets_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
            #      #   if (p == 'wjets_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
            #         #if (p == 'wl_rate'): model.distribution.set_distribution_parameters(p, mean = 0.19, width = 0.0001)
            #         #if (p == 'wc_rate'): model.distribution.set_distribution_parameters(p, mean = 1.85, width = 0.0001)
            #        # if (p == 'diboson_rate'): model.distribution.set_distribution_parameters(p, mean = 1.0, width = 0.0001)
            #         #if (p == 'zj_rate'): model.distribution.set_distribution_parameters(p, mean = -0.207, width = 0.0001)
            #        # if (p == 'zj_rate'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
            #         #if (p == 'pileup'): model.distribution.set_distribution_parameters(p, mean = 1.15, width = 0.0001)
            #         #if (p == 'matching_wjets'): model.distribution.set_distribution_parameters(p, mean = -0.44, width = 0.0001)
            #         #if (p == 'jer'): model.distribution.set_distribution_parameters(p, mean = 1.1, width = 0.0001)
            #         #if (p == 'q2'): model.distribution.set_distribution_parameters(p, mean = 0.26, width = 0.0001)
            #         #if (p == 'jec'): model.distribution.set_distribution_parameters(p, mean = 0.33, width = 0.0001)
            #         #if (p == 'eleORjet_trig'): model.distribution.set_distribution_parameters(p, mean = 0.05, width = 0.0001)
            #         #if (p == 'q2_wjets'): model.distribution.set_distribution_parameters(p, mean = 0.17, width = 0.0001)
            #         #if (p == 'lumi'): model.distribution.set_distribution_parameters(p, mean = 0.28, width = 0.0001)
            #         #if (p == 'bmistag'): model.distribution.set_distribution_parameters(p, mean = 0.56, width = 0.0001)
            #         #if (p == 'eleid'): model.distribution.set_distribution_parameters(p, mean = 0.01, width = 0.0001)
            #         #if (p == 'btag'): model.distribution.set_distribution_parameters(p, mean = 1.36, width = 0.0001)
            #         #if (p == 'muoid'): model.distribution.set_distribution_parameters(p, mean = -0.58, width = 0.0001)
            #         #if (p == 'pdf'): model.distribution.set_distribution_parameters(p, mean = -0.66, width = 0.0001)
            #         #model.rebin('el_mttbar',50)
            #         #model.rebin('mu_mttbar',47)


    return model

import exceptions

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

    #for p in ['toptag', 'topmistag', 'bmistag', 'btag']:
        #model.distribution.set_distribution_parameters(p, width = float('inf'), range = [-0.0001,0.0001])
    for p in model.distribution.get_parameters():
        d = model.distribution.get_distribution(p)
        print "channel and model type", p, d
        if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
            model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
            if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
            if (p == 'mistoptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
            #if (p == 'topmistag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-5.0, 5.0])
            #if (p == 'toptag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-1.0, 1.0])
            #if (p == 'topmistag'): model.distribution.set_distribution_parameters(p, width = float('Inf'), range = [-1.0, 1.0])
            #if (p == 'ttbar_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
            #if (p == 'st_rate'): model.distribution.set_distribution_parameters(p, mean = 0.68, width = 0.0001)
            #if (p == 'wjets_rate'): model.distribution.set_distribution_parameters(p,  width = float('Inf'), range = [-5.0, 5.0])
            #if (p == 'wl_rate'): model.distribution.set_distribution_parameters(p, mean = 0.19, width = 0.0001)
            #if (p == 'wc_rate'): model.distribution.set_distribution_parameters(p, mean = 1.85, width = 0.0001)
            #if (p == 'diboson_rate'): model.distribution.set_distribution_parameters(p, mean = 0.08, width = 0.0001)
            #if (p == 'zj_rate'): model.distribution.set_distribution_parameters(p, mean = -0.207, width = 0.0001)
            #if (p == 'pileup'): model.distribution.set_distribution_parameters(p, mean = 1.15, width = 0.0001)
            #if (p == 'matching_wjets'): model.distribution.set_distribution_parameters(p, mean = -0.44, width = 0.0001)
            #if (p == 'jer'): model.distribution.set_distribution_parameters(p, mean = 1.1, width = 0.0001)
            #if (p == 'q2'): model.distribution.set_distribution_parameters(p, mean = 0.26, width = 0.0001)
            #if (p == 'jec'): model.distribution.set_distribution_parameters(p, mean = 0.33, width = 0.0001)
            #if (p == 'eleORjet_trig'): model.distribution.set_distribution_parameters(p, mean = 0.05, width = 0.0001)
            #if (p == 'q2_wjets'): model.distribution.set_distribution_parameters(p, mean = 0.17, width = 0.0001)
            #if (p == 'lumi'): model.distribution.set_distribution_parameters(p, mean = 0.28, width = 0.0001)
            #if (p == 'bmistag'): model.distribution.set_distribution_parameters(p, mean = 0.56, width = 0.0001)
            #if (p == 'eleid'): model.distribution.set_distribution_parameters(p, mean = 0.01, width = 0.0001)
            #if (p == 'btag'): model.distribution.set_distribution_parameters(p, mean = 1.36, width = 0.0001)
            #if (p == 'muoid'): model.distribution.set_distribution_parameters(p, mean = -0.58, width = 0.0001)
            #if (p == 'pdf'): model.distribution.set_distribution_parameters(p, mean = -0.66, width = 0.0001)
    #model.rebin('el_mttbar',50)
    #model.rebin('mu_mttbar',47)

    return model


# Code introduced by theta_driver

# Building the statistical model

#options = Options()
#options.set('minimizer','strategy','robust')

args = {'type': 'narrow_resonances_electron'}
#args = {'type': 'narrow_resonances_muon'}
#args = {'type': 'narrow_resonances_lepton'}
#args = {'type': 'bkg_muon'}
model = build_model(**args)
print model.distribution.get_parameters()
args = {}
model_summary(model)
#model_summary(model)

# print '/Summary'
# #results = mle(model, input = 'data', n = 100, with_error = True, signal_prior = 'fix:0', options = options, **args)
# results = mle(model, input = 'data', n = 1, with_error = True, signal_prior = 'fix:0', **args)
# # print '/MLE'
# # for p in results['']: print p, results[''][p][0][0]
# # for r1 in results:
# #     print r1
# #     for r2 in results[r1]:
# #         print r2,results[r1][r2]
# #     print
# #report.write_html('htmlout')



report.write_html('htmlout')
'''
execfile('/afs/desy.de/user/k/karavdia/xxl/af-cms/RunLimitsZprime_2016/RunLimits/MLF_Yields_Uncertainties/utils.py')
print 'Fitting rate only'

#res = ml_fit(model, input = 'data', n = 1, with_error = True, signal_prior = 'fix:0', options = options, **args)
res = ml_fit(model, input = 'data', n = 1, with_error = True, signal_prior = 'fix:0', **args)
#res = ml_fit(model, input = 'data', signal_prior = 'fix:0', n = 1000)
# #res = mle(model, input='data', n=100, with_error = True)
# #print res
# for p in res['']: print p, res[''][p][0][0]
execfile('/afs/desy.de/user/k/karavdia/RunLimits_Zprime/MLF_Yields_Uncertainties/utils.py')
print 'Fitting rate only'
factors = print_obsproc_factors_rateonly(model)
file = open('factors.py', 'w')
file.write(repr(factors))
file.close()
apply_factors(model, factors)
tables = model_summary(model)
generate_yield_table(tables['rate_table'])
#print_obsproc_factors_shapes(tables)
print 'Fitting all the parameters'

# #res = ml_fit(model, input = 'data', n = 1, with_error = True, signal_prior = 'fix:0', options = options, **args)
res = ml_fit(model, signal_processes = [''], nuisance_constraint = 'shape:free', signal_prior = 'fix:0')
# #for p in res['']: print p, res[''][p][0][0]
#for p in res['']: print res[''][p][0][0], res[''][p][0][1], p
# factors = print_obsproc_factors_rateonly(model)                                                                                                                       
# file = open('factors.py', 'w')                                                                                                                                        
# file.write(repr(factors))                                                                                                                                             
# file.close()                                                                                                                                                          
# apply_factors(model, factors)                                                                                                                                         
# tables = model_summary(model)                                                                                                                                         
# generate_yield_table(tables['rate_table'])    

# # # #res = ml_fit(model, input = 'data', n = 1, with_error = True, signal_prior = 'fix:0', options = options, **args)
#res = ml_fit(model, signal_processes = [''], nuisance_constraint = '',signal_prior = 'fix:0', n = 100, **args)
#for p in res['']: print p, res[''][p][0][0], res[''][p][0][1]
#report.write_html('htmlout')



# #results = bayesian_limits(model, run_theta = True, **args)
# #exp, obs = results
# #execfile("utils.py")
# #limit_table(exp, obs)
