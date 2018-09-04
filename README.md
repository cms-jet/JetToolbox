# JetToolbox
Python framework for configuration of jet tools via the jet toolbox.

## Instructions

Check the branch for the correspondent release. This branch is for *CMSSW_9_4_X* and higher, then for example:
```
cmsrel CMSSW_9_4_7/
cd CMSSW_9_4_7/src/
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X_v3
scram b -j 18
```
To test the toolbox:
```
cmsRun JMEAnalysis/JetToolbox/test/jetToolbox_cfg.py
```
This config file run only a test of the capabilities of the jetToolbox, it is physics meaningless. If you want a more meaningful test, please run (takes quite a long time):
~~~
cmsRun JMEAnalysis/JetToolbox/test/ClusterWithToolboxAndMakeHistos.py
~~~
In this python file you also can see a basic example on how to use the toolbox.

## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
