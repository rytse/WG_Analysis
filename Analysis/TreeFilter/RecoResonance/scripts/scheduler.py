import os
from argparse import ArgumentParser

import scheduler_base
from scheduler_base import JobConf

p = ArgumentParser()
p.add_argument( '--check', dest='check', default=False, action='store_true', help='Run check of completion' )
p.add_argument( '--clean', dest='clean', default=False, action='store_true', help='Run cleanup of extra files' )
p.add_argument( '--resubmit', dest='resubmit', default=False, action='store_true', help='Only submit missing output' )
p.add_argument( '--local', dest='local', default=False, action='store_true', help='Run locally' )
p.add_argument( '--test', dest='test', default=False, action='store_true', help='Run a test job' )
options = p.parse_args()

if not options.check :
    options.run = True
else :
    options.run = False

options.batch = ( not options.local )

### ATTENTION! Here you specify the directory containing the raw ntuples that you want to process further.
### Also specify the version number of the raw ntuples with the version_* variables below.
#base = '/store/user/jkunkle'
#base = '/store/user/yofeng/WGamma'
base = '/store/user/kawong/WGamma'
options.nFilesPerJob = 50

options.nproc = 1
options.treename='UMDNTuple/EventTree'
options.exename='RunAnalysis'
options.copyInputFiles=False
options.enableKeepFilter=True
options.enableRemoveFilter=False
options.filekey = 'ntuple'
#options.PUPath='/data/users/jkunkle/Resonances/PileupHistograms'
#options.PUPath='/data/users/friccita/WGammaNtuple/Pileup'
#options.PUPath='/data/users/kakw/Resonances2017/pileuptest/' ## testonly
options.PUPath='/data/users/kakw/Resonances2017/pileup3'

if options.test : 
    options.nproc = 1
    options.nFilesPerJob = 1
    options.nJobs = 1
    options.batch = False
    options.local = True

### ATTENTION! Specify the output directory where the processed ntuple output will be saved.
output_base = '/data2/users/kakw/Resonances2017/'
jobtag = '_2019_05_02_test'

#version = 'UMDNTuple_0620'
version_sig = ''
version = 'UMDNTuple_20190329testb'
version_py = 'UMDNTuple_20190329testc'
version_data = 'UMDNTuple_20190404data17test'
version_madgraph = 'UMDNTuple_20190329test'
version_g = 'UMDNTuple_20190329testg'

jobs = [
        #--------------------------
        #JobConf(base, 'SingleMuon', isData=True, version=version_data),
        #JobConf(base, 'SingleElectron', isData=True, version=version_data),

        #JobConf(base, 'WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8', version=version, tags=['NLO']                        ),
        #JobConf(base, 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', version=version                         ),
        #JobConf(base, 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', version=version                         ),
        #JobConf(base, 'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),
        #JobConf(base, 'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),  
        #JobConf(base, 'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),  
        #JobConf(base, 'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),  
        #JobConf(base, 'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', version=version), 
        #JobConf(base, 'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),
        #JobConf(base, 'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', version=version), 
        #JobConf(base, 'TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8', version=version     ),
        #JobConf(base, 'TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8', version=version     ),
        #JobConf(base, 'TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8' , version=version    ),
        #JobConf(base, 'TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', version=version, tags=['NLO'] ),
        #JobConf( base, 'GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),
        #JobConf( base, 'GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),
        #JobConf( base, 'GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),
        #JobConf( base, 'GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8', version=version ),
        #JobConf( base, 'GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', version=version),
        #JobConf( base, 'DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8', version=version, tags=['NLO']),
        #JobConf( base, 'WTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8', version=version),
        #JobConf(base, 'WWG_TuneCP5_13TeV-amcatnlo-pythia8', version=version, tags=['NLO']     ),
        #JobConf(base, 'WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', version=version, tags=['NLO']     ),
        #JobConf(base, 'WZG_TuneCP5_13TeV-amcatnlo-pythia8', version=version, tags=['NLO']     ),

        #JobConf( base, 'ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8', version=version_madgraph ,tags=['NLO']),
        JobConf( base, 'WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8',        version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M900_width5',     version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M900_width0p01',  version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M800_width5',     version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M800_width0p01',  version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M700_width0p01',  version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M500_width5',     version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M450_width5',     version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M400_width5',     version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M4000_width5',    version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M350_width0p01',  version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M3500_width5',    version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M300_width5',     version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M2800_width0p01', version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M2600_width0p01', version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M250_width5',     version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M2200_width5',    version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M2200_width0p01', version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M200_width0p01',  version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M2000_width5',    version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M2000_width0p01', version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M1800_width5',    version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M1400_width5',    version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M1400_width0p01', version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M1200_width0p01', version=version_madgraph ),
        #JobConf( base, 'MadGraphChargedResonance_WGToLNuG_M1000_width0p01', version=version_madgraph ),
        #JobConf( base, 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',version=version_g , tags=['NLO']),

        ###### signal stuff ######
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1000_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1200_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1400_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1600_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1800_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2000_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M200_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2200_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2400_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M250_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2800_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M300_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M3500_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M350_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M4000_width5' , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M400_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M450_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M500_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M600_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M700_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M800_width5'  , version=version_sig   ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M900_width5'  , version=version_sig   ),

        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1000_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1200_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1400_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1600_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M1800_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2000_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M200_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2200_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2400_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M250_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2600_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M2800_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M3000_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M300_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M3500_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M350_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M4000_width0p01', version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M400_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M450_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M500_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M600_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M700_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M800_width0p01' , version=version_sig ),
        #JobConf(base,'MadGraphChargedResonance_WGToLNu_M900_width0p01' , version=version_sig ),

        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M1000_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M1200_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M1400_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M1800_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M1800_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M2000_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M200_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M2200_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M2400_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M250_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M2600_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M300_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M300_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M3500_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M3500_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M350_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M4000_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M450_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M450_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M500_width0p01'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M500_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M600_width5'  , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNuG_M800_width0p01'  , version=version_py ),

        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1000_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1200_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1400_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1600_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1800_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2000_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M200_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2200_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2400_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M250_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2800_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M300_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M3500_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M350_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M4000_width5' , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M400_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M450_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M500_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M600_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M700_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M800_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M900_width5'  , version=version_py   ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1000_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1200_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1400_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1600_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M1800_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2000_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M200_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2200_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2400_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M250_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2600_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M2800_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M3000_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M300_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M3500_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M350_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M4000_width0p01', version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M400_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M450_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M500_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M600_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M700_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M800_width0p01' , version=version_py ),
        #JobConf(base,'PythiaChargedResonance_WGToLNu_M900_width0p01' , version=version_py ),

]


args_nlo = { 'ApplyNLOWeight' : 'true', 'doFHPFS' : 'true' }
### ATTENTION! Choose (uncomment and modify as necessary) the type of ntuple you want to make. Single lepton, dilepton, single lepton plus gamma, etc.
configs = [

    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_el', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 10 ', 'phot_id' : 'None' },
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '',
    #    'output' : output_base+'SingleLepNoPhId_el_2019_03_17',
    #    'dataset': 'SingleElectron',
    #    'keepSelection': 'tight',
    #    'tag'    : 'el',
    #},
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_mu', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 10 ', 'phot_id' : 'None'  },
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '',
    #    'output' : output_base+'SingleLepNoPhId_mu_2019_03_17',
    #    'dataset': 'SingleMuon',
    #    'keepSelection': 'tight',
    #    'tag'    : 'mu',
    #},
#    {
#        'module' : 'Conf.py',
#        'args'   : { 'function' : 'make_final_mumu', 'mu_pt' : ' > 30 ' },
#        'args_tag_NLO' : args_nlo,
#        'input'  : '',
#        'output' : output_base+'LepLep_mumu' + jobtag,
#        'tag'    : 'mumu',
#        'keepSelection': 'tight',
#        'dataset': 'SingleMuon',
#    },
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_mumu', 'mu_pt' : ' > 30 ' },
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '',
    #    'output' : output_base+'LepLep_mumu_2019_03_17',
    #    'tag'    : 'mumu',
    #    'keepSelection': 'tight',
    #    'dataset': 'SingleMuon',
    #},
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_mu', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 10 ', 'phot_vars' : 'False' },
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '',
    #    'output' : output_base+'SingleLep_mu_2019_03_17',
    #    'tag'    : 'mu',
    #    'dataset': 'SingleMuon',
    #},
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_el', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 10 ', 'eleVeto' : 'None', 'phot_vars' : 'False'},
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '' ,
    #    'output' : output_base+'SingleLep_el_2019_03_17',
    #    'tag'    : 'el',
    #    'dataset': 'SingleElectron',
    #},
    {
        'module' : 'Conf.py',
        'args'   : { 'function' : 'make_final_mumu', 'mu_pt' : ' > 30 ' },
        'args_tag_NLO' : args_nlo,
        'input'  : '',
        'output' : output_base+'LepLep_mumu'+jobtag,
        'tag'    : 'mumu',
        'keepSelection': 'tight',
        'dataset': 'SingleMuon',
    },
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_muel', 'el_pt' : ' > 30 ' },
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '',
    #    'output' : output_base+'LepLep_muel_2018_03_28',
    #    'tag'    : 'muel',
    #    'keepSelection': 'tight',
    #    'dataset': 'SingleMuon',
    #},
#    {
#        'module' : 'Conf.py',
#        'args'   : { 'function' : 'make_final_elel', 'el_pt' : ' > 30 ' },
#        'args_tag_NLO' : args_nlo,
#        'input'  : '',
#        'output' : output_base+'LepLep_elel'+jobtag,
#        'tag'    : 'elel',
#        'keepSelection': 'tight',
#        'dataset': 'SingleElectron',
#    },
#    {
#        'module' : 'Conf.py',
#        'args'   : { 'function' : 'make_final_mug', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 15 ', 'phot_vars' : 'True' },
#        'args_tag_NLO' : args_nlo,
#        'input'  : '',
#        'output' : output_base+'LepGamma_mug'+jobtag,
#        'tag'    : 'mug',
#        'dataset': 'SingleMuon',
#    },
#    {
#        'module' : 'Conf.py',
#        'args'   : { 'function' : 'make_final_elg', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 15 ', 'eleVeto' : 'None', 'phot_vars' : 'True'},
#        'args_tag_NLO' : args_nlo,
#        'input'  : '' ,
#        'output' : output_base+'LepGamma_elg'+jobtag,
#        'tag'    : 'elg',
#        'dataset': 'SingleElectron',
#    },
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_elg', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 15 ', 'eleVeto' : 'None', 'phot_vars' : 'True', 'eleOlap' : 'False'},
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '' ,
    #    'output' : output_base+'LepGammaNoEleOlapMod_elg_2018_06_11',
    #    'tag'    : 'elgnov',
    #    'dataset': 'SingleElectron',
    #},
    {
        'module' : 'Conf.py',
        'args'   : { 'function' : 'make_final_mug', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 10 ', 'phot_vars' : 'true', 'phot_id' : 'None', 'unblind' : 'true' },
        'args_tag_NLO' : args_nlo,
        'input'  : '',
        'output' : output_base+'LepGammaNoPhId_mug_2019_03_17',
        'dataset': 'SingleMuon',
        'tag'    : 'muglph',
    },
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_elg', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 10 ', 'phot_vars' : 'True', 'phot_id' : 'None', 'unblind' : 'True' },
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : '',
    #    'output' : output_base+'LepGammaNoPhId_elg_2019_03_17',
    #    'dataset': 'SingleElectron',
    #    'tag'    : 'elglph',
    #},
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_mug', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 30 ', 'muphtrig' : 'True' },
    #    'args_tag_NLO' : args_nlo,
    #    'input'  : input_base,
    #    'output' : base+'LepGamma_mug_ditrig_2017_03_06',
    #    'tag'    : 'mugditrig',
    #},
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_mug', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 15 ', 'phot_vars' : 'True', 'phot_id' : 'loose', 'sec_lep_veto' : 'False' },
    #    'input'  : input_base,
    #    'output' : base+'LepGamma_mug_noseclepveto_2017_03_14',
    #    'tag'    : 'mugnslv',
    #},
    #{
    #    'module' : 'Conf.py',
    #    'args'   : { 'function' : 'make_final_elg', 'mu_pt' : ' > 10 ', 'el_pt' : ' > 10 ' , 'ph_pt' : ' > 15 ', 'phot_vars' : 'True', 'phot_id' : 'loose', 'sec_lep_veto' : 'False' },
    #    'input'  : input_base,
    #    'output' : base+'LepGamma_elg_noseclepveto_2017_03_14',
    #    'tag'    : 'elgnslv',
    #},
    #{
    #    'module' : 'conf.py',
    #    'args'   : { 'function' : 'make_nofilt' , 'pass_lepton' : 'true'},
    #    'input'  : '',
    #    'output' : output_base+'SigNoFilt_2018_07_03',
    #    'tag'    : 'nofilt',
    #},
    ##{
    ##    'module' : 'Conf.py',
    ##    'args'   : { 'function' : 'make_final_elgjj', 'el_pt' : ' > 30 ' },
    ##    'input'  : input_base_new,
    ##    'output' : base+'LepGammaDiJet_elgjj_2017_01_03',
    ##    'tag'    : 'elgjj',
    ##},
    ##{
    ##    'module' : 'Conf.py',
    ##    'args'   : { 'function' : 'make_final_mugjj', 'mu_pt' : ' > 30 ' },
    ##    'input'  : input_base_new,
    ##    'output' : base+'LepGammaDiJet_mugjj_2017_01_03',
    ##    'tag'    : 'mugjj',
    ##},

]


scheduler_base.RunJobs( jobs, configs, options)

