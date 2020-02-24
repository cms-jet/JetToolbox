# JetToolbox
Python framework for configuration of jet tools via the jet toolbox.

## Instructions

### Notice that the parameter `miniAOD=True` has changed to `dataTier=miniAOD`

Check the branch for the correspondent release. This branch is for *CMSSW_10_2_X* and higher. 
Then for example:
```
cmsrel CMSSW_10_6_1/
cd CMSSW_10_6_1/src/
git cms-init
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_102X_v3
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

## Instruction to produce modified nanoAOD with the jetToolbox (beta version)

This is a beta version on how to modify nanoAOD production to incorporate different jet collections in nanoAOD format. This will create the standard nanoAOD variables plus new variables run by the jetToolbox.

The only file that needs to be modified is [JMEAnalysis/JetToolbox/python/nanoAOD_jetToolbox_cff.py](python/nanoAOD_jetToolbox_cff.py), using the same setting as in the miniAOD case.
*The main change is the dataTier parameter, in case of nanoAOD:* `dataTier="nanoAOD"`.
After modify the `setupCustomizedJetToolbox` function in that file, one can run a cmsDriver command. For instance (for nanoAOD v5 2018):

~~~
cmsDriver.py nanoAOD_jetToolbox_cff -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_upgrade2018_realistic_v19 --era Run2_2018,run2_nanoAOD_102Xv1 --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))" --customise JMEAnalysis/JetToolbox/nanoAOD_jetToolbox_cff.nanoJTB_customizeMC --filein /store/mc/RunIIAutumn18MiniAOD/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/7E65457A-87E5-C146-8321-9A48B4F56ED1.root --fileout file:jetToolbox_nano_mc.root
~~~

Notice that the `--customise` option points to the file [JMEAnalysis/JetToolbox/python/nanoAOD_jetToolbox_cff.py](python/nanoAOD_jetToolbox_cff.py). 


A working example, after running the cmsDriver command shown above, is located here: [JMEAnalysis/JetToolbox/test/jetToolbox_nanoAODv05_cfg.py](test/jetToolbox_nanoAODv05_cfg.py). 

All the variables created by the jetToolbox start with `selectedPatJets**`.


## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
