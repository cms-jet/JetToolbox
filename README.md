# JetToolbox
Python framework for configuration of jet tools via the jet toolbox.

## Instructions

Check the branch for the correspondent release. This branch is for *CMSSW_9_4_12* and higher. This release is **needed** for DeepDoubleX and DeepBoostedJet. If you are not planning on using those b-discriminators you can use an ealier release.
Then for example:
```
cmsrel CMSSW_9_4_12
cd CMSSW_9_4_12/src/
git cms-init
git clone git@github.com:alefisico/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
scram b -j 8
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

## Instruction to run jetToolbox in nanoAOD (THIS IS A TEST)

This branch is a test to implement the jetToolbox into nanoAOD. *IT IS A WORKING VERSION*.

The only file that needs to be modified is [JMEAnalysis/JetToolbox/python/nanoAOD_jetToolbox_cff.py](https://github.com/alefisico/JetToolbox/blob/jetToolbox_94X/python/nanoAOD_jetToolbox_cff.py#L8-L31), using the same setting as in the miniAOD case. Notice that the parameter `miniAOD=True` has changed to `dataTier=miniAOD` (or in this case `dataTier=nanoAOD`). After modify the `setupCustomizedJetToolbox` function in that file, one can run a cmsDriver command. For instance:

~~~
cmsDriver.py jetToolbox_nanoAOD -n 10 --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 94X_mcRun2_asymptotic_v2 --step NANO --nThreads 4 --era Run2_2016,run2_miniAOD_80XLegacy --customise JMEAnalysis/JetToolbox/nanoAOD_jetToolbox_cff.nanoJTB_customizeMC --filein
/store/mc/RunIISummer16MiniAODv2/ZprimeToTT_M-3000_W-30_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D6D620EF-73BE-E611-8BFB-B499BAA67780.root --fileout file:jetToolbox_nano_mc.root
~~~

Notice that the `--customise` option points to the file `JMEAnalysis/JetToolbox/python/nanoAOD_jetToolbox_cff.py`. 


A working example, after running the cmsDriver command shown above, is located here: [JMEAnalysis/JetToolbox/test/jetToolbox_nanoAOD_NANO.py](https://github.com/alefisico/JetToolbox/blob/jetToolbox_94X/test/jetToolbox_nanoAOD_NANO.py). 

All the variables created by the jetToolbox start with `jetToolbox_selectedJet`.


## More Information

Please visit the twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
