# JetToolbox
Python framework for configuration of jet tools via the jet toolbox. 

## Instructions

Check the branch for the correspondent release. This branch is for *CMSSW_8_0_X*, then for example:
```
cmsrel CMSSW_8_0_20
cd CMSSW_8_0_20/src/
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_8_0_X_V1
scram b -j 18
```
To test the toolbox:
```
cmsRun JMEAnalysis/JetToolbox/test/jetToolbox_cfg.py
```
In that python file you also can see a basic example on how to use the toolbox.
#If you are going to use Puppi, please make sure to follow this instructions: https://twiki.cern.ch/twiki/bin/viewauth/CMS/PUPPI#Using_PUPPI

## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
