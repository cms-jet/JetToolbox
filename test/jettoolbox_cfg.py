import FWCore.ParameterSet.Config as cms

process = cms.Process('jetToolbox')

#process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load('Configuration.StandardSequences.Geometry_cff')
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.GlobalTag.globaltag = 'PHYS14_25_V3'
process.GlobalTag.globaltag = 'MCRUN2_74_V7'

process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.MessageLogger.suppressWarning = cms.untracked.vstring('ecalLaserCorrFilter','manystripclus53X','toomanystripclus53X')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)

from cmsjet.JetToolbox.jetToolbox_cff import *
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, subJETCorrLevels=['L1FastJet'] ) #, Cut='pt > 100 && abs(eta) < 2.4' ) 
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='SK', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrLevels=['L1FastJet', 'L2Relative'] ) 
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True ) 
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrPayload='AK3Fchs', subJETCorrPayload='AK8PFchs', JETCorrLevels=['L1FastJet', 'L2Relative'] )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='Puppi', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='SK', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='CS', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True ) 
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='Puppi', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='SK', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='CS', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', addHEPTopTagger=True, addSoftDrop=True )

#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out' , addPruning=True, addSoftDrop=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True )
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
		#fileNames = cms.untracked.vstring(
		#	'/store/relval/CMSSW_7_4_0_pre9_ROOT6/RelValQCD_Pt_600_800_13/MINIAODSIM/MCRUN2_74_V7-v1/00000/281DDBC1-D3D1-E411-8534-0025905AA9F0.root',
		#	'/store/relval/CMSSW_7_4_0_pre9_ROOT6/RelValQCD_Pt_600_800_13/MINIAODSIM/MCRUN2_74_V7-v1/00000/C01855C8-D3D1-E411-A702-0026189438D7.root'
			#)
						)
from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValTTbarPileUpMINIAODSIM
process.source.fileNames = filesRelValTTbarPileUpMINIAODSIM

#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
#process.source.fileNames = filesRelValProdTTbarAODSIM

