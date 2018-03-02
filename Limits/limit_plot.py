#!/usr/bin/env python
from ROOT import ROOT, TCanvas, TColor, TGraph, TLegend, TPaveText, TString, TLine
from read_input_file import *
from theory_XsecBR_2016 import *
#ROOT.gROOT.SetBatch()

kWhite      = 0     #FFFFFF
kBlack      = 1     #000000
kGray       = 920   #CCCCCC
kRed        = 632   #FF0000
kPink       = 900   #FF0033
kMagenta    = 616   #FF00FF
kViolet     = 880   #CC00FF
kBlue       = 600   #0000FF
kAzure      = 860   #0033FF
kCyan       = 432   #00FFFF
kTeal       = 840   #00FFCC
kGreen      = 416   #00FF00
kSpring     = 820   #33FF00
kYellow     = 400   #FFFF00
kOrange     = 800   #FFCC00

label_TL = '#font[62]{CMS}'
label_TR = '36.0 fb^{-1} (13 TeV)'

signal_dict = {
  'n': ['Z\'', 'Topcolor Z\' 1.0% width'],
  'w': ['Z\'', 'Topcolor Z\' 10% width'],
  'ew': ['Z\'', 'Topcolor Z\' 30% width'],
  'ttjets': ['Z\'', 'Z\' + jets'],
  'r': ['g_{KK}', 'KK gluon']
}

def limit_canvas(limits_, signal_, oname_):

    m = [mp.mass for mp in limits_]
    exp = [mp.exp for mp in limits_]
    exp68up = [mp.exp68up for mp in limits_]
    exp68dn = [mp.exp68dn for mp in limits_]
    exp95up = [mp.exp95up for mp in limits_]
    exp95dn = [mp.exp95dn for mp in limits_]
    obs = [mp.obs for mp in limits_]

    N = len(limits_)
    gExp = TGraph()
    g68 = TGraph(2*N)
    g95 = TGraph(2*N)
    gObs = TGraph()
    gTH = get_theory_XsecBR_graph(signal_)

    for a in range(0,N):
        gExp.SetPoint(a,m[a],exp[a])
        gObs.SetPoint(a,m[a],obs[a])
        g68.SetPoint(a,m[a],exp68dn[a])
        g95.SetPoint(a,m[a],exp95dn[a])
        g68.SetPoint(N+a,m[N-a-1],exp68up[N-a-1])
        g95.SetPoint(N+a,m[N-a-1],exp95up[N-a-1])

    trans = 0
    up = 0
    if signal_ == 'n':
        trans = 0.770776
        up = 3
    if signal_ == 'w':
        trans = 0.836432
        up = 10
    if signal_ == 'r':
        trans = 0.899902
        up = 4

    gExp.SetLineStyle(2)
    gExp.SetLineWidth(4)
    gExp.SetLineColor(TColor.GetColor('#112288'))
    #gExp.Print()

    g68.SetLineStyle(1)
    g68.SetLineWidth(0)
    g68.SetLineColor(kBlack)
    g68.SetFillColor(TColor.GetColor('#4488dd'))

    g95.SetLineStyle(1)
    g95.SetLineWidth(0)
    g95.SetLineColor(kBlack)
    g95.SetFillColor(TColor.GetColor('#99bbff'))

    gObs.SetLineStyle(1)
    gObs.SetLineWidth(4)
    gObs.SetLineColor(kBlack)
    gObs.SetMarkerStyle(21)
    gObs.SetMarkerSize(0.8)

    gTH.SetLineStyle(7)
    gTH.SetLineWidth(4)
    gTH.SetMarkerSize(0)
    gTH.SetMarkerColor(kRed+1)
    gTH.SetLineColor(kRed+1)

    leg = TLegend(0.58,0.633,0.969,0.908)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    leg.AddEntry(gExp,'Expected (95% CL)','l')
    leg.AddEntry(gObs,'Observed (95% CL)','l')
    leg.AddEntry(gTH,signal_dict[signal_][1],'l')
    leg.AddEntry(g68,'#pm1#sigma Expected','f')
    leg.AddEntry(g95,'#pm2#sigma Expected','f')

    text_TL = TPaveText(0.18,0.830,0.44,0.900,'NDC')
    text_TL.AddText(label_TL)
    text_TL.SetFillColor(0)
    text_TL.SetTextAlign(12)
    text_TL.SetTextSize(0.06)
    text_TL.SetTextFont(42)

    text_TR = TPaveText(0.586,0.923,0.999,0.997,'NDC')
    text_TR.AddText(label_TR)
    text_TR.SetFillColor(0)
    text_TR.SetTextAlign(32)
    text_TR.SetTextSize(0.055)
    text_TR.SetTextFont(42)

    c = TCanvas('c','c',950,750)
    c.SetTopMargin(0.08)
    c.SetRightMargin(0.02)
    c.SetBottomMargin(0.135)
    c.SetLeftMargin(0.11)
    #c.SetGrid()
    c.SetLogy()

    #hr = c.DrawFrame(0.401,0.001,3.999,1000)
    #hr = c.DrawFrame(0.401,0.001,4.199,1000)
    hr = c.DrawFrame(0.401,0.001,5.199,1000)
    gExp.Sort()
    gTH.Print()
    g95.Draw('f')
    g95.Print()
    g68.Draw('f')
    gTH.Draw('L')
    gExp.Draw('L')

#Don't draw observed for blind analysis
#    gObs.Sort()
#    gObs.Draw('L')

    hr.GetXaxis().SetTitle('M_{'+signal_dict[signal_][0]+'} [TeV]')
    hr.GetYaxis().SetTitle('Upper limit on #sigma_{'+signal_dict[signal_][0]+'} #times B('+signal_dict[signal_][0]+' #rightarrow t#bar{t}) [pb]')
    #hr.GetYaxis().SetTitle('\\mathrm{Upper~limit~on~}\\sigma_{'+signal_dict[signal_][0]+'}\\times\\mathscr{B}('+signal_dict[signal_][0]+' \\rightarrow t\\bar{t}) [pb]')
    hr.GetXaxis().SetTitleSize(0.055)
    hr.GetYaxis().SetTitleSize(0.055)
    hr.GetXaxis().SetTitleFont(42)
    hr.GetYaxis().SetTitleFont(42)
    hr.GetXaxis().SetTitleOffset(1.00)
    hr.GetYaxis().SetTitleOffset(0.98)
    hr.GetXaxis().SetLabelSize(0.045)
    hr.GetYaxis().SetLabelSize(0.045)

    name = TString(oname_)
    if name.Contains("com"):
        tl = TLine(trans, 1e-3, trans, up)
        tl.SetLineStyle(ROOT.kDashed)
        tl.SetLineColor(kGray+1)
        tl.SetLineWidth(3)
        tl.Draw()

    c.Update()
    text_TL.Draw('same')
    text_TR.Draw('same')
    leg.Draw()

    c.SaveAs(oname_+'.pdf')
    c.Close()

def limit_plot(ifile_, signal_, output_name_):

    limits = get_limits_from_file(ifile_)
    limit_canvas(limits, signal_, output_name_)

###

for s in signal_dict:
#    limit_plot('limits_allsyst_mu_wide_0413.txt', s, s+'_mujets_allsyst_wide_0413')
#    limit_plot('limits.txt', s, s+'_el_theta_0408_narrow_v1')
#    limit_plot('limits_data.txt', s, s+'_el_theta_0408_narrow_v1')
#    limit_plot('limits_muon_narrow.txt', s, s+'_mu_theta_0408_narrow_v1')
#    limit_plot('limits_elec_narrow.txt', s, s+'_el_theta_0408_narrow_v1')
#    limit_plot('limits_muon_narrow.txt', s, s+'_mu_theta_0408_narrow_v1')
 #s = {'n': ['Z\'', 'Topcolor Z\' 1.0% width']}
#s = {'r': ['g_{KK}', 'KK gluon']}
#    limit_plot('limits_muon_'+s+'.txt', s, s+'_mu_theta_v1')
#    limit_plot('limits_elec_'+s+'.txt', s, s+'_el_theta_v1')
#    limit_plot('limits_Zprime_narrow.txt', s, s+'_el_theta_1128_narrow_v1')

#     limit_plot('limits_muon_'+s+'.txt', s, s+'_mu_theta_20170302')
#      limit_plot('limits_elec_'+s+'.txt', s, s+'_el_theta_20170302')
     limit_plot('limits_lep_'+s+'.txt', s, s+'_lep_theta_20170302')


