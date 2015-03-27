import FWCore.ParameterSet.Config as cms

process = cms.Process('jetToolbox')

process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.GlobalTag.globaltag = 'PHYS14_25_V3'
process.GlobalTag.globaltag = 'MCRUN2_73_V4'

process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.MessageLogger.suppressWarning = cms.untracked.vstring('ecalLaserCorrFilter','manystripclus53X','toomanystripclus53X')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)

from JMEAnalysis.JetToolbox.jetToolbox_cff import *
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', JETCorrLevels=['L2Relative', 'L3Absolute'] ) #, addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrLevels=['L2Relative', 'L3Absolute'] ) #, Cut='pt > 100 && abs(eta) < 2.4' ) 
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrLevels=['L2Relative', 'L3Absolute'] ) #, Cut='pt > 100 && abs(eta) < 2.4' ) 
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='SK' ) #, addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrLevels=['L1FastJet', 'L2Relative'] ) 
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True ) 
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out' ) #, addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrPayload='AK3Fchs', subJETCorrPayload='AK8PFchs', JETCorrLevels=['L1FastJet', 'L2Relative'] )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='Puppi', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='SK', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='CS', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='Puppi', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='SK', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='CS', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', addHEPTopTagger=True, addSoftDrop=True )

#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Plain' ) #, addPruning=True, addSoftDrop=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True)
#
#
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False ) 
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='SK', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False ) 
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False ) 
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='Puppi', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, miniAOD=False ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='SK', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, miniAOD=False ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='CS', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, miniAOD=False ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, miniAOD=False ) 
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='Puppi', addHEPTopTagger=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='SK', addHEPTopTagger=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='CS', addHEPTopTagger=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', addHEPTopTagger=True, addSoftDrop=True, miniAOD=False )

process.endpath = cms.EndPath(process.out)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
process.source = cms.Source("PoolSource",
				fileNames = cms.untracked.vstring('file:example.root')
						)
from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarPileUpMINIAODSIM
process.source.fileNames = filesRelValProdTTbarPileUpMINIAODSIM

#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
#process.source.fileNames = filesRelValProdTTbarAODSIM

