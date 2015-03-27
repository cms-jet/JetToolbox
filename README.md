# JetToolbox
Python framework for configuration of jet tools via the jet toolbox. 

## Instructions

The master version works for CMSSW_7_3_X, then for example:
```
cmsrel CMSSW_7_3_0
cd CMSSW_7_3_0/src/
git clone https://github.com/cms-jet/JetToolbox JMEAnalysis/JetToolbox
scram b -j 18
```
To test the toolbox:
```
cmsRun JMEAnalysis/JetToolbox/test/jetToolbox_cfg.py
```
In that python file you also can see a basic example on how to use the toolbox.

## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
