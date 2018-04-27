# JetToolbox
Python framework for configuration of jet tools via the jet toolbox. 

## Instructions

Check the branch for the correspondent release. This branch is for *CMSSW_9_4_X* and higher, then for example:
```
cmsrel CMSSW_9_4_4/
cd CMSSW_9_4_4/src/
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X_v1
scram b -j 18
```
To test the toolbox:
```
cmsRun JMEAnalysis/JetToolbox/test/jetToolbox_cfg.py
```
In that python file you also can see a basic example on how to use the toolbox.

## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
