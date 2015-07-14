# JetToolbox
Python framework for configuration of jet tools via the jet toolbox. 

## Instructions

Check the branch for the correspondent release. The master branch is for *CMSSW_7_4_X*, then for example:
```
cmsrel CMSSW_7_4_1
cd CMSSW_7_4_1/src/
git clone https://github.com/cms-jet/JetToolbox JMEAnalysis/JetToolbox
scram b -j 18
```
To test the toolbox:
```
cmsRun JMEAnalysis/JetToolbox/test/jetToolbox_cfg.py
```
In that python file you also can see a basic example on how to use the toolbox.
If you are going to use Puppi, please make sure to download the corresponding packages from here: https://twiki.cern.ch/twiki/bin/view/CMS/PUPPI

## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
