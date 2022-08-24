import FWCore.ParameterSet.Config as cms
###
### cmsRun ClusterWithToolboxAndPlot.py
###  make jet plots from miniAOD with some additional jet collections clustered
### Jet Algorithm HATS 2015 - Dolen, Rappoccio, Stupak
### Updated for Jet Algorithm HATS 2016 - Dolen, Pilot, Kries, Perloff, Tran
###


process = cms.Process("Ana")

### SETUP
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '92X_upgrade2017_realistic_v1'
process.GlobalTag.globaltag = '94X_mc2017_realistic_v12'
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(True)
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

### INPUT
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cmsxrootd.fnal.gov//store/test/xrootd/T2_US_MIT/store/mc/RunIISummer20UL18MiniAODv2/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2430000/0984A792-8B13-1543-AA86-063CC14B1678.root'),
)

#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValTTbarPileUpMINIAODSIM
#process.source.fileNames = filesRelValTTbarPileUpMINIAODSIM

btagDiscAK4 = [
            'pfCombinedInclusiveSecondaryVertexV2BJetTags',
            'pfCombinedCvsLJetTags',
            'pfCombinedCvsBJetTags',
            'pfDeepCSVJetTags:probb',
            'pfDeepCSVJetTags:probbb',
            'pfDeepCSVJetTags:probc',
            'pfDeepCSVJetTags:probudsg',
            'pfDeepFlavourJetTags:probb',
            'pfDeepFlavourJetTags:probbb',
            'pfDeepFlavourJetTags:problepb',
            'pfDeepFlavourJetTags:probc',
            'pfDeepFlavourJetTags:probuds',
            'pfDeepFlavourJetTags:probg',
        ]

btagDiscAK8 = [
            'pfBoostedDoubleSecondaryVertexAK8BJetTags',
            #'pfMassIndependentDeepDoubleBvLJetTags:probQCD',
            #'pfMassIndependentDeepDoubleBvLJetTags:probHbb',
            #'pfMassIndependentDeepDoubleCvLJetTags:probQCD',
            #'pfMassIndependentDeepDoubleCvLJetTags:probHcc',
            #'pfMassIndependentDeepDoubleCvBJetTags:probHbb',
            #'pfMassIndependentDeepDoubleCvBJetTags:probHcc',
	    "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:bbvsLight",
	    "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ccvsLight",
	    "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD",
	    "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHccvsQCD",
 	    "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:WvsQCD",
 	    "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHbbvsQCD"
            ]

### ADD SOME NEW JET COLLECTIONS
from JMEAnalysis.JetToolbox.jetToolbox_cff import *

# updating slimmedJets (ak4 CHS jets) from miniAOD
jetToolbox( process, 'ak4', 'ak4UpdJetSubs', 'noOutput',
        dataTier="miniAOD",
        updateCollection='slimmedJets',
        JETCorrPayload='AK4PFchs',
        postFix='Updated',
        bTagDiscriminators=btagDiscAK4
        )

# AK R=0.4 jets from CHS inputs
jetToolbox( process, 'ak4', 'ak4JetSubs', 'noOutput',
  dataTier="miniAOD",
  PUMethod='CHS',
#  JETCorrPayload = 'AK4PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
  addPUJetID=True,
  addQGTagger=True,
  Cut='pt>30 && abs(eta)<2.5'
)

# AK R=0.4 jets from Puppi inputs
jetToolbox( process, 'ak4', 'ak4JetSubs', 'noOutput',
  dataTier="miniAOD",
  PUMethod='Puppi',
#  JETCorrPayload = 'AK4PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
  Cut='pt>30 && abs(eta)<2.5'
)

# AK R=0.4 jets from PF inputs
jetToolbox( process, 'ak4', 'ak4JetSubs', 'noOutput',
  dataTier="miniAOD",
  PUMethod='Plain',
#  JETCorrPayload = 'AK4PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
  Cut='pt>30 && abs(eta)<2.5'
)



# updating slimmedAK8Jets (ak8 puppi jets) from miniAOD
jetToolbox( process, 'ak8', 'ak8UpdJetSubs', 'noOutput',
        dataTier="miniAOD",
        PUMethod='Puppi',
        updateCollection='slimmedJetsAK8',
        JETCorrPayload='AK8PFPuppi',
        postFix='Updated',
        bTagDiscriminators=btagDiscAK8
        )

# AK R=0.8 jets from CHS
jetToolbox( process, 'ak8', 'ak8JetSubs', 'noOutput',
  dataTier="miniAOD",
  Cut="pt>170 && abs(eta)<2.5",
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute'],
)

# AK R=0.8 from PUPPI
jetToolbox( process, 'ak8', 'ak8JetSubs', 'noOutput',
  dataTier="miniAOD",
  PUMethod='Puppi',
  Cut="pt>170 && abs(eta)<2.5",
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  addEnergyCorrFunc=True,
  #JETCorrPayload = 'AK8PFPuppi', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# CA R=0.8 jets from CHS
jetToolbox( process, 'ca8', 'ca8JetSubs', 'noOutput',
  Cut="pt>170 && abs(eta)<2.5",
  dataTier="miniAOD",
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# KT R=0.8 jets from CHS
jetToolbox( process, 'kt8', 'kt8JetSubs', 'noOutput',
  dataTier="miniAOD",
  Cut="pt>170 && abs(eta)<2.5",
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=0.8 jets from Puppi, modified Softdrop
jetToolbox( process, 'ak8', 'ak8JetSubs', 'noOutput',
  dataTier="miniAOD",
  Cut="pt>170 && abs(eta)<2.5",
  PUMethod='Puppi',
  postFix='modSD',
  addSoftDrop=True , betaCut=1,           # add basic grooming
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=0.8 jets from SK
jetToolbox( process, 'ak8', 'ak8JetSubs', 'noOutput',
  dataTier="miniAOD",
  Cut="pt>170 && abs(eta)<2.5",
  PUMethod='SK',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

## AK R=0.8 jets from CS
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'noOutput',
#  PUMethod='CS',
#  addPruning=True, addSoftDrop=True ,           # add basic grooming
#  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
#)

# CA R=1.2 jets from CHS inputs with basic grooming, W tagging, and top tagging
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'noOutput',
#  PUMethod='CHS',
#  addHEPTopTagger=True,
#)


## AK R=1.2 jets from CHS inputs with basic grooming, W tagging, and top tagging
#jetToolbox( process, 'ak12', 'ak12JetSubs', 'noOutput',
#  PUMethod='CHS',
#  addPruning=True, addSoftDrop=True ,           # add basic grooming
#  addTrimming=True, addFiltering=True,
#  addSoftDropSubjets=True,
#  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
#  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
#)
#
## AK R=1.5 jets from CHS inputs with basic grooming, W tagging, and top tagging
#jetToolbox( process, 'ak15', 'ak15JetSubs', 'noOutput',
#  PUMethod='CHS',
#  addPruning=True, addSoftDrop=True ,           # add basic grooming
#  addTrimming=True, addFiltering=True,
#  addSoftDropSubjets=True,
#  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
#  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
#)

### MAKE SOME HISTOGRAMS
process.ana = cms.EDAnalyzer('JetTester'
)

### OUT
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("jetToolbox_longTest.root"),
      closeFileFast = cms.untracked.bool(True)
  )

process.p = cms.Path(process.ana)
