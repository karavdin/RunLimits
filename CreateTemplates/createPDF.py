import ROOT as R 
import sys
import numpy as np

nbins = 30
fin = R.TFile("ttbar_pdf.root")




#create dictionaries
values_per_bin = {}
sigmas = []
for i in range(30):
    values_per_bin[str(i)]  = []

#get values per bin 
dir = R.gDirectory.GetListOfKeys()
print dir 
print values_per_bin

for key in dir:
    hist  = key.ReadObj()
    print hist
    for bin in range(30):
        values_per_bin[str(bin)].append(hist.GetBinContent(bin))    

nominal = fin.Get("mu_1top_mttbar__ttbar")
pdf_plus = R.TH1F("mu_1top_mttbar__ttbar__PDF__plus", "mu_1top_mttbar__ttbar__PDF__plus",30,100,2000)
pdf_minus = R.TH1F("mu_1top_mttbar__ttbar__PDF__plus","mu_1top_mttbar__ttbar___PDF__minus",30,100,2000)

print values_per_bin['0'], np.std(np.array(values_per_bin['0']))

fout = R.TFile("templatespdf.root", 'recreate')
for bin in range(30):
        values = []
        values = np.array(values_per_bin[str(bin)])
        sigmas.insert(bin, np.std(values))
        print np.std(values)
        print bin, nominal.GetBinContent(bin), nominal.GetBinContent(bin)+np.std(values), nominal.GetBinContent(bin)-np.std(values)
        pdf_plus.SetBinContent(bin,( nominal.GetBinContent(bin)+ np.std(values)))
        pdf_minus.SetBinContent(bin,( nominal.GetBinContent(bin) - np.std(values)))

fout.WriteObject(pdf_plus,"mu_1top_mttbar__ttbar__PDF__plus" )
fout.WriteObject(pdf_minus, "mu_1top_mttbar__ttbar__PDF__minus")
fout.WriteObject(nominal, "mu_1top_mttbar__ttbar")
       


#estimate sigma per bin and fill/save histogram

              
