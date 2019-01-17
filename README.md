# JetToolbox
Python framework for configuration of jet tools via the jet toolbox.

## Instructions

Check the branch for the correspondent release. This branch is for *CMSSW_9_4_12* and higher. This version is **needed** for DeepDoubleX and DeepBoostedJet. If you are not planning on using those b-discriminators you can use an ealier release.
Then for example:
```
cmsrel CMSSW_9_4_12/
cd CMSSW_9_4_12/src/
git cms-init
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X_v4
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

## To run DeepDoubleX

While the PR is merged to the main cmssw code, please follow this instructions:
```
git cms-merge-topic 25371
git cms-addpkg RecoBTag/Combined
cd RecoBTag/Combined/
git clone -b V01-01-01 --depth 1 --no-checkout https://github.com/cms-data/RecoBTag-Combined.git data
cd data
git config core.sparseCheckout true
echo 'DeepDoubleX/94X/V01/' > .git/info/sparse-checkout
git checkout --
cd $CMSSW_BASE/src
scram b -j 10
```

## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
