This document describes how to employ the scripts in this directory in order to get the systematics impact on the yields and how to estimate the limits. 


I - CREATING THE TEMPLATES 

a. Create the templates from the uhh2.*.root files from the last selection step.
   To generate the theta files (ch_categ_obs__sample__systematic__direction) use the python script "createtemplates.py"

b. Rebin the histograms such that the error per bin is 30%
   Afte generating the template, rebin it with "rebin.py", do a sanity check by looking at the generated pdf plots to make sure data and MC agree

II - MLF TO THE SYSTEMATIC UNCERTAINTIES  AND PRE-MLF YIELDS 

a. Using the rebinned root file, use the "mle_yields.py" script in the theta/utils directory. To do so, just change the input file name and run it with theta-auto.py 
   This file makes use of "utils.py" (which has to be located in the same directory) at the end it will geneate: 
   i) In the mle_yields directory in the produced index.html a table with the yields, the statistical uncertainty on them  and the impact of the systematic uncertanties will be generated. Also a python file called "factors.py" will be generated and will have the scale factors to reweight your templates.
   ii) To process the information of the yields and the uncertainty due to systematics, the script "yields.py" will find the systematic uncertainties and will add them in quadrature (/sum_{1}^{N_syst}((/delta N)^2)/N_syst. The script "yields.py" makes use of the "process_class.py" script. 

b. To generate the MLF deviations from the prior, run the "mlf_posteriors.py"  script in the theta/utils2 directory. This will:
   i)  Print out a table with the mean and sigma for each post fit systematic
   After generating the table, edit it in a txt file and this will be the input file for the  "nuisance_plot.py" script that will generat the brazilian plot. 

III - GENERATING THE LIMITS 

a. Using the scale values given by the MLF in the "factors.py" edit the "bayesianlimits.py" file and add those values before running theta. 
   Then on the utils2/ directory run the limits 
b. After the evaluations it will generate a index.html file with the expected, expected+/- 1sigma , expected +/- 2 sigma and observed results. Grab those files and save    them on a txt file like "limits_allsyst_mu_wide_0413.txt". Then use "limit_plot.py " which makes use of the "read_input_file.py" and "theory_XsecBR.py" scripts to take the theory x-sections and the right formating.  

IV - PLOTTING TOOLS
To have some sanity check additional plotting tools are available:
a. "plot_systematics.py" script will plot the nominal , up systematic and down systematic templates. 
b. "SFramePlotter.py" will generate the histograms of interest, stacking all backgounds and with the data. It needs a configuration file "SFramePlotter.ini"
