# JetToolbox
Python framework for configuration of jet tools via the jet toolbox. 

## Instructions

Check the branch for the correspondent release. This branch (jetToolbox_74X) is for *CMSSW_7_4_X*, then for example:
```
cmsrel CMSSW_7_4_0_pre9
cd CMSSW_7_4_0_pre9/src/
git clone https://github.com/cms-jet/JetToolbox -b jetToolbox_74X JMEAnalysis/JetToolbox
scram b -j 18
```
To test the toolbox:
```
cmsRun cmsjet/JetToolbox/test/jetToolbox_cfg.py
```
In that python file you also can see a basic example on how to use the toolbox.

## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
