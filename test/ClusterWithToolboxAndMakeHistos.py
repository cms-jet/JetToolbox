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
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)
process.MessageLogger.cerr.FwkReport.reportEvery = 100

### INPUT
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/mc/RunIISummer17MiniAOD/ZprimeToTT_M-3000_W-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/150000/E45A17E6-AAAC-E711-A423-00266CFFC80C.root'
    )
)


from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValTTbarPileUpMINIAODSIM
process.source.fileNames = filesRelValTTbarPileUpMINIAODSIM

### ADD SOME NEW JET COLLECTIONS
from JMEAnalysis.JetToolbox.jetToolbox_cff import *

# AK R=0.4 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak4', 'ak4JetSubs', 'out',
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK4PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=0.8 jets from PF inputs with basic grooming, W tagging, and top tagging
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out',
#  PUMethod='Plain',
#  addPruning=True, addSoftDrop=True ,           # add basic grooming
#  addTrimming=True, addFiltering=True,
#  addSoftDropSubjets=True,
#  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
#  JETCorrPayload = 'AK8PF', JETCorrLevels = ['L2Relative', 'L3Absolute']
#)

# AK R=0.8 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out',
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=0.8 from PUPPI inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out',
  PUMethod='Puppi',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFPuppi', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# CA R=0.8 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ca8', 'ca8JetSubs', 'out',
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# KT R=0.8 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'kt8', 'kt8JetSubs', 'out',
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=1.2 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak12', 'ak12JetSubs', 'out',
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=1.5 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak15', 'ak15JetSubs', 'out',
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True,
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

### MAKE SOME HISTOGRAMS
process.ana = cms.EDAnalyzer('JetTester'
)

### OUT
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("JetClusterHistos_ZP3.root"),
      closeFileFast = cms.untracked.bool(True)
  )

# Uncomment the following line if you would like to output the jet collections in a root file
# process.endpath = cms.EndPath(process.out)

process.p = cms.Path(process.ana)
