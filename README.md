# JetToolbox
Python framework for configuration of jet tools via the jet toolbox.

## Instructions

Check the branch for the correspondent release. This branch is for *CMSSW_10_2_X* and higher. 
Then for example:
```
cmsrel CMSSW_10_2_9/
cd CMSSW_10_2_9/src/
git cms-init
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_102X_v1
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
