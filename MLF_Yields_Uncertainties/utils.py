
def limit_table(exp, obs):
    file = open('limits.yaml', 'w')
    for i in range(len(exp.x)):
        file.write(
            '%.2f: [%.6f, %.6f, %.6f, %.6f, %.6f, %.6f]\n' % (
                exp.x[i], exp.y[i],
                exp.bands[1][1][i] - exp.y[i], exp.bands[1][0][i] - exp.y[i],
                exp.bands[0][1][i] - exp.y[i], exp.bands[0][0][i] - exp.y[i],
                obs.y[i]
            )
        )


def apply_factors(model, factors):
    #print factors
    for obs in factors:
        for proc in factors[obs]:
            f = factors[obs][proc]
            if type(f) == str: continue # can happen for "n/a"
            #print f, proc, obs
            model.scale_predictions(f, proc, obs)


def generate_yield_table(rate_table):
    rows = rate_table.get_raw_rows()
    cols = rate_table.get_columns()
    f = open('yield-table.tex', 'w')
    f.write('\\begin{tabular}{|l|')
    for c in cols: f.write('r|')
    f.write('}\n \\hline\n Process')
    for c in cols:
        if c=='process': continue
        latex_colname = {#'el_0btag_mttbar': 'electron channel, $N_{\\text{b-tag}}=0$',
                         #'el_1btag_mttbar': 'electron channel, $N_{\\text{b-tag}} \\ge 1$',
                         #'el_0top0btag_mttbar': 'electron channel, $N_{\\text{top-tag}} \\ge 0, $N_{\\text{b-tag}} \\ge 0$',
                         #'el_0top1btag_mttbar': 'electron channel, $N_{\\text{top-tag}} \\ge 0, $N_{\\text{b-tag}} \\ge 1$',
                         #'el_0top2btag_mttbar': 'electron channel, $N_{\\text{top-tag}} \\ge 0, $N_{\\text{b-tag}} \\ge 2$',
                         #'el_1top0btag_mttbar': 'electron channel, $N_{\\text{top-tag}} \\ge 1, $N_{\\text{b-tag}} \\ge 0$',
                         #'el_1top1btag_mttbar': 'electron channel, $N_{\\text{top-tag}} \\ge 1, $N_{\\text{b-tag}} \\ge 1$',
                         #'el_1top2btag_mttbar': 'electron channel, $N_{\\text{top-tag}} \\ge 1, $N_{\\text{b-tag}} \\ge 2$'
                         'ele_1top_WJetsMVA_mttbar': 'elec channel, $N_{\\text{top-tag}}=1$, WJets MVA\ge0.5',
                         'ele_0top_WJetsMVA_mttbar': 'elec channel, $N_{\\text{top-tag}}=0$, WJets MVA\ge0.5',
                         'ele_1top_antiWJetsMVA_mttbar': 'elec channel, $N_{\\text{top-tag}}=1$, WJets MVA<0.5',
                         'ele_0top_antiWJetsMVA_mttbar': 'elec channel, $N_{\\text{top-tag}}=0$, WJets MVA<0.5',

                         'ele_1top_mttbar': 'elec channel, $N_{\\text{top-tag}}=1$',
                         'ele_0top_mttbar': 'elec channel, $N_{\\text{top-tag}}=0$',
                         'ele_0top1btag_mttbar': 'elec channel, $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 1$',
                         'ele_0top0btag_mttbar': 'elec channel, $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 0$'}[c]
                         #'mu_1top_mttbar': 'muon channel, $N_{\\text{top-tag}}=1$',
                         #'mu_0top1btag_mttbar': 'muon channel, $N_{\\text{top-tag}} = 0 $N_{\\text{b-tag}} = 1$',
                         #'mu_0top0btag_mttbar': 'muon channel, $N_{\\text{top-tag}} = 0 $N_{\\text{b-tag}} = 0$'}[c]

        f.write('& %s' % latex_colname)
    f.write('\\\\\n')
    for r in rows:
        print 'r',r
        print 'r0',r[0]
        print 'r1',r[1]
        print 'r2',r[2]
        f.write('%10s' % r[0])
        for val in r[1:]:
            if type(val)==tuple: val = val[0]
            if type(val)==float: f.write(' & %6.1f' % val)
            else: f.write(' & %10s' % val)
        f.write('\\\\ \n')
    f.write('\\\\ \n \\hline')
    f.write('\\end{tabular}\n')


def generate_yield_table_AN(rate_table,prefix,channel):
    rows = rate_table.get_raw_rows()
    cols = rate_table.get_columns()
    f = open('yield-table_'+channel+'_'+prefix+'.tex', 'w')
    f.write('\\begin{tabular}{|l|')
    for c in cols: f.write('r|')
    f.write('}\n \\hline\n ')
    if channel=='muon':
        f.write('$\mu$+jets')
    if channel=='elec':
        f.write('$e$+jets')
    for c in cols:
        print c
        if c=='process': continue
        if channel=='muon':
            latex_colname = {'mu_1top_mttbar': ' 1-t',
                'mu_0top1btag_mttbar': ' 0-t, 1-b',
                'mu_0top0btag_mttbar': ' 0-t, 0-b',
                'mu_1top_mttbar_highChi2': ' 1-t, $\chi^{2}$>30',
                'mu_0top1btag_mttbar_highChi2': ' 0-t, 1-b, $\chi^{2}$>30',
                'mu_0top0btag_mttbar_highChi2': ' 0-t, 0-b, $\chi^{2}$>30',
                'mu_0top_WJetsMVA_mttbar': '$T0$, BDT$_{W+jets}$>0.5',
                'mu_1top_WJetsMVA_mttbar': '$T1$, BDT$_{W+jets}$>0.5',
                'mu_0top_antiWJetsMVA_mttbar': '$T0$, BDT$_{W+jets}$<0.5',
                'mu_1top_antiWJetsMVA_mttbar': '$T1$, BDT$_{W+jets}$<0.5',
                'mu_0top_WJetsMVA_chi2_mttbar': '$T0$, SR',
                'mu_1top_WJetsMVA_chi2_mttbar': '$T1$, SR',
                'mu_0top_antiWJetsMVA_chi2_mttbar': '$T0$, a-bdt, $\chi^{2}$',
 #               'mu_0top_antiWJetsMVA2_chi2_mttbar': 'CR1',
                'mu_1top_antiWJetsMVA_chi2_mttbar': '$T1$, a-bdt, $\chi^{2}$',
                'mu_0top_WJetsMVA_antichi2_mttbar': '$T0$, bdt, a-$\chi^{2}$',
                'mu_1top_WJetsMVA_antichi2_mttbar': '$T1$, bdt, a-$\chi^{2}$',
                'mu_0top_antiWJetsMVA_antichi2_mttbar': '$T0$, a-bdt, a-$\chi^{2}$',
                'mu_0top_antiWJetsMVA2_antichi2_mttbar': 'CR1',
                'mu_0top_antiWJetsMVA3_antichi2_mttbar': 'CR2',
                'mu_0top_antiWJetsMVA3_chi2_mttbar': 'CR3',
#                'mu_0top_antiWJetsMVA3_chi2_mttbar': 'CR2',
                'mu_1top_WJetsMVA4_chi2_mttbar': '$T1$, bdt4, $\chi^{2}$',
                'mu_1top_antiWJetsMVA_antichi2_mttbar': '$T1$, a-bdt, a-$\chi^{2}$',
                'mu_01top_WJetsMVA_antichi2_mttbar': 'bdt, a-$\chi^{2}$ ',
                'mu_01top_antiWJetsMVA_antichi2_mttbar': 'a-bdt, a-$\chi^{2}$' ,
                'mu_01top_antiWJetsMVA2_antichi2_mttbar': 'a-bdt2, a-$\chi^{2}$' ,
                'mu_1top_chi2_mttbar': '$T1$, $\chi^{2}$',
                'mu_mll': ' $M_{ll}$'}[c]

        if channel=='elec':
            latex_colname = {'el_1top_mttbar': ' $N_{\\text{top-tag}}=1$, $\chi^{2}$<30',
                'ele_0top_antiWJetsMVA2_antichi2_mttbar': 'CR1',
                'ele_0top_antiWJetsMVA3_antichi2_mttbar': 'CR2',
                'ele_0top_antiWJetsMVA_chi2_mttbar': 'CR3',
                'ele_0top_WJetsMVA_chi2_mttbar': '$T0$, SR',
                'ele_1top_WJetsMVA_chi2_mttbar': '$T1$, SR',
#                'el_0top1btag_mttbar': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 1$, $\chi^{2}$<30',
#                'el_0top0btag_mttbar': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 0$, $\chi^{2}$<30',
#                'el_1top_mttbar_highChi2': ' $N_{\\text{top-tag}}=1$, $\chi^{2}$>30',
#                'el_0top1btag_mttbar_highChi2': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 1$, $\chi^{2}$>30',
#                'el_0top0btag_mttbar_highChi2': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 0$, $\chi^{2}$>30',
#                'ele_0top_WJetsMVA_mttbar': '$T0$, BDT$_{W+jets}$>0.5',
#                'ele_1top_WJetsMVA_mttbar': '$T1$, BDT$_{W+jets}$>0.5',
#                'ele_0top_antiWJetsMVA_mttbar': '$T0$, BDT$_{W+jets}$<0.5',
#                'ele_1top_antiWJetsMVA_mttbar': '$T1$, BDT$_{W+jets}$<0.5',
#                'ele_0top_antiWJetsMVA_chi2_mttbar': '$T0$, a-bdt, $\chi^{2}$',
#                'ele_0top_antiWJetsMVA2_chi2_mttbar': '$T0$, a-bdt2, $\chi^{2}$',
#                'ele_1top_antiWJetsMVA_chi2_mttbar': '$T1$, a-bdt, $\chi^{2}$',
#                'ele_1top_chi2_mttbar': '$T1$, SR',
#                'ele_0top_chi2_mttbar': '$T0$, SR',
#                'ele_0top_WJetsMVA_antichi2_mttbar': '$T0$, bdt, a-$\chi^{2}$',
#                'ele_01top_WJetsMVA_antichi2_mttbar': 'bdt, a-$\chi^{2}$',
#                'ele_01top_antiWJetsMVA_antichi2_mttbar': 'a-bdt, a-$\chi^{2}$',
#                'ele_0top_antiWJetsMVA3_chi2_mttbar': 't0, a-bdt3, $\chi^{2}$',
#                'ele_1top_antiWJetsMVA2_antichi2_mttbar': 't1, a-bdt2, a-$\chi^{2}$',
#                'ele_1top_antiWJetsMVA3_chi2_mttbar': 't1, a-bdt3, $\chi^{2}$',
#                'ele_1top_WJetsMVA4_chi2_mttbar': 't1, bdt4, $\chi^{2}$',
#                'ele_01top_antiWJetsMVA2_antichi2_mttbar': 'a-bdt-2, a-$\chi^{2}$',
#                'ele_01top_antiWJetsMVA_antichi2_mttbar': '$T1$, a-bdt, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step1_antichi2_mttbar': 't0, bdt st1, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step2_antichi2_mttbar': 't0, bdt st2, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step3_antichi2_mttbar': 't0, bdt st3, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step4_antichi2_mttbar': 't0, bdt st4, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step5_antichi2_mttbar': 't0, bdt st5, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step6_antichi2_mttbar': 't0, bdt st6, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step7_antichi2_mttbar': 't0, bdt st7, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step8_antichi2_mttbar': 't0, bdt st8, a-$\chi^{2}$',
#                 'ele_0top_WJetsMVA_step1_chi2_mttbar': 't0, bdt st1, $\chi^{2}$',
#                 'ele_0top_WJetsMVA_step2_chi2_mttbar': 't0, bdt st2, $\chi^{2}$',
#                 'ele_0top_WJetsMVA_step3_chi2_mttbar': 't0, bdt st3, $\chi^{2}$',
#                 'ele_0top_WJetsMVA_step4_chi2_mttbar': 't0, bdt st4, $\chi^{2}$',
#                 'ele_0top_WJetsMVA_step5_chi2_mttbar': 't0, bdt st5, $\chi^{2}$',
                 # 'ele_0top_WJetsMVA_step6_chi2_mttbar': 't0, bdt st6, $\chi^{2}$',
                 # 'ele_0top_WJetsMVA_step7_chi2_mttbar': 't0, bdt st7, $\chi^{2}$',
                 # 'ele_0top_WJetsMVA_step8_chi2_mttbar': 't0, bdt st8, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step1_antichi2_mttbar': 't1, bdt st1, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step2_antichi2_mttbar': 't1, bdt st2, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step3_antichi2_mttbar': 't1, bdt st3, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step4_antichi2_mttbar': 't1, bdt st4, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step5_antichi2_mttbar': 't1, bdt st5, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step6_antichi2_mttbar': 't1, bdt st6, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step7_antichi2_mttbar': 't1, bdt st7, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step8_antichi2_mttbar': 't1, bdt st8, a-$\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step1_chi2_mttbar': 't1, bdt st1, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step2_chi2_mttbar': 't1, bdt st2, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step3_chi2_mttbar': 't1, bdt st3, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step4_chi2_mttbar': 't1, bdt st4, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step5_chi2_mttbar': 't1, bdt st5, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step6_chi2_mttbar': 't1, bdt st6, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step7_chi2_mttbar': 't1, bdt st7, $\chi^{2}$',
                 # 'ele_1top_WJetsMVA_step8_chi2_mttbar': 't1, bdt st8, $\chi^{2}$',
                'el_mll': ' $M_{ll}$'}[c]

        if channel=='lep':
            latex_colname = {'mu_1top_mttbar': ' 1-t',
                'mu_0top1btag_mttbar': ' 0-t, 1-b',
                'mu_0top0btag_mttbar': ' 0-t, 0-b',
                'mu_1top_mttbar_highChi2': ' 1-t, $\chi^{2}$>30',
                'mu_0top1btag_mttbar_highChi2': ' 0-t, 1-b, $\chi^{2}$>30',
                'mu_0top0btag_mttbar_highChi2': ' 0-t, 0-b, $\chi^{2}$>30',
                'mu_mll': ' $M_{\mu\mu}$',
                'el_1top_mttbar': ' $N_{\\text{top-tag}}=1$, $\chi^{2}$<30',
                'el_0top1btag_mttbar': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 1$, $\chi^{2}$<30',
                'el_0top0btag_mttbar': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 0$, $\chi^{2}$<30',
                'el_1top_mttbar_highChi2': ' $N_{\\text{top-tag}}=1$, $\chi^{2}$>30',
                'el_0top1btag_mttbar_highChi2': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 1$, $\chi^{2}$>30',
                'el_0top0btag_mttbar_highChi2': ' $N_{\\text{top-tag}} = 0$, $N_{\\text{b-tag}} = 0$, $\chi^{2}$>30',
                'mu_0top_WJetsMVA_chi2_mttbar': '$\mu$, $T0$, SR',
                'mu_1top_WJetsMVA_chi2_mttbar': '$\mu$, $T1$, SR',
                'mu_0top_antiWJetsMVA_chi2_mttbar': '$\mu$, $T0$, a-bdt, $\chi^{2}$ ',
                'mu_1top_antiWJetsMVA_chi2_mttbar': '$\mu$, $T1$, a-bdt, $\chi^{2}$ ',
                'mu_0top_WJetsMVA_antichi2_mttbar': '$\mu$, $T0$, bdt, a-$\chi^{2}$ ',
                'mu_1top_WJetsMVA_antichi2_mttbar': '$\mu$, $T1$, bdt, a-$\chi^{2}$ ',
                'mu_0top_antiWJetsMVA_antichi2_mttbar': '$\mu$, $T0$, a-bdt, a-$\chi^{2}$ ',
                'mu_1top_antiWJetsMVA_antichi2_mttbar': '$\mu$, $T1$, a-bdt, a-$\chi^{2}$ ',
                'mu_01top_WJetsMVA_antichi2_mttbar': '$\mu$, bdt, a-$\chi^{2}$ ',
                'mu_01top_antiWJetsMVA_antichi2_mttbar': '$\mu$, a-bdt, a-$\chi^{2}$' ,
                'ele_0top_WJetsMVA_chi2_mttbar': '$e$, $T0$, SR',
                'ele_1top_WJetsMVA_chi2_mttbar': '$e$, $T1$, SR',
                'ele_0top_antiWJetsMVA_chi2_mttbar': '$e$, $T0$, a-bdt, $\chi^{2}$',
                'ele_1top_antiWJetsMVA_chi2_mttbar': '$e$, $T1$, a-bdt, $\chi^{2}$',
                'ele_0top_WJetsMVA_antichi2_mttbar': '$e$, $T0$, bdt, a-$\chi^{2}$',
                'ele_1top_WJetsMVA_antichi2_mttbar': '$e$, $T1$, bdt, a-$\chi^{2}$',
                'ele_0top_antiWJetsMVA_antichi2_mttbar': '$e$, $T0$, a-bdt, a-$\chi^{2}$',
                'ele_1top_antiWJetsMVA_antichi2_mttbar': '$e$, $T1$, a-bdt, a-$\chi^{2}$',
                'ele_01top_WJetsMVA_antichi2_mttbar': '$e$, bdt, a-$\chi^{2}$',
                'ele_01top_antiWJetsMVA_antichi2_mttbar': '$e$, a-bdt, a-$\chi^{2}$',
                'mu_01top_WJetsMVA_antichi2_mttbar': '$\mu$, bdt, a-$\chi^{2}$ ',
                'mu_01top_antiWJetsMVA_antichi2_mttbar': '$\mu$, a-bdt, a-$\chi^{2}$' ,
                'mu_0top_antiWJetsMVA2_antichi2_mttbar': '$\mu$, CR1',
                'mu_0top_antiWJetsMVA2_chi2_mttbar': '$\mu$, $T0$, a-bdt2, $\chi^{2}$',
                'mu_0top_antiWJetsMVA3_antichi2_mttbar': '$\mu$, CR2',
                'mu_0top_antiWJetsMVA3_chi2_mttbar': '$\mu$, aCR2',
                'ele_0top_antiWJetsMVA3_antichi2_mttbar': '$e$, CR2',
                'ele_0top_antiWJetsMVA2_antichi2_mttbar': '$e$, CR1',
                'ele_1top_antiWJetsMVA2_antichi2_mttbar': '$e$, t1, a-bdt2, a-$\chi^{2}$',
                'ele_1top_WJetsMVA4_chi2_mttbar': '$e$, t1, bdt4, $\chi^{2}$',
                'mu_1top_WJetsMVA4_chi2_mttbar': '$\mu$, t1, bdt4, $\chi^{2}$',
                'el_mll': ' $M_{ll}$'}[c]

        f.write('& %s' % latex_colname)
    f.write('\\\\\n')
    for r in rows:
        # print 'r',r
        # print 'r0',r[0]
        # print 'r1',r[1]
        # print 'r2',r[2]
        # print 'r3',r[3]
        # print 'r4',r[4]
        # print 'r5',r[5]
        # print 'r6',r[6]
        # print 'r7',r[7]
        f.write('%10s' % r[0])
        for val in r[1:]:
            if type(val)==tuple: 
                val_mean = val[0]
                val_err = val[1]
            if type(val)==float:
                val_mean = val
                val_err = 0

            f.write(' & %6.0f' % val_mean)
            f.write(' $\pm$ %6.0f' % val_err)
        f.write('\\\\ \\hline \n ')
    f.write('\\end{tabular}\n')
        


def print_obsproc_factors_shapes(model):
    result = {}
    res = ml_fit2(model, signal_processes = [''], nuisance_constraint = '')
    par_values = {}
    par_values0 = {}
    for par in model.get_parameters(''):
        par_values[par] = res[''][par][0][0]
        par_values0[par] = 0.0 # assuming 0.0 means "nominal"
    for p in par_values: print p, par_values[p]
    templates0 = get_shifted_templates(model, par_values0, False)
    templates = get_shifted_templates(model, par_values, False)
    for obs in templates:
        print("\n" + obs)
        result[obs] = {}
        for proc in templates[obs]:
            nominal_rate = sum(templates0[obs][proc][2])
            if nominal_rate == 0.0: factor = "n/a (%f / %f)" % (sum(templates[obs][proc][2]), nominal_rate)
            else: factor = sum(templates[obs][proc][2]) / nominal_rate
            print "  ", proc, factor
            result[obs][proc] = factor
    return result


def print_obsproc_factors_rateonly(model):
    result = {}
    res = ml_fit_coefficients(model, signal_processes = [''])
    #print "results from print_obsproc_factors_rateonly", res
    for obs in res['']:
        print("\n" + obs)
        result[obs] = {}
        for proc in res[''][obs]:
            print "  ", proc, res[''][obs][proc]
            result[obs][proc] = res[''][obs][proc]
    return result
