#! Text To ASCII from http://patorjk.com/software/taag/#p=display&f=Big&t=MUON%20ISOLATION

import FWCore.ParameterSet.Config as cms

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Jet and reference kinematics
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PileupNtupleMakerParameters = cms.PSet(
    # record flavor information, consider both RefPt and JetPt
    doComposition   = cms.bool(True),
    doFlavor        = cms.bool(True),
    doRefPt         = cms.bool(True),
    doJetPt         = cms.bool(True),
    # MATCHING MODE: deltaR(ref,jet)
    deltaRMax       = cms.double(99.9),
    # deltaR(ref,parton) IF doFlavor is True
    deltaRPartonMax = cms.double(0.25),
    # consider all matched references
    nJetMax         = cms.uint32(0),
)
 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Process
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
process = cms.Process("JRA")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Conditions
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.GlobalTag.globaltag = "PHYS14_25_V2::All"


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Input
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
                                    
dyFiles = cms.untracked.vstring(
#######
# QCD #
#######
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/1020E374-B26B-E411-8F91-E0CB4E29C513.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/1EF51024-986B-E411-A6F6-20CF300E9EAF.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/5AE5B0FC-986B-E411-ACED-20CF3027A57B.root',	
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/7A60863A-9A6B-E411-A19D-002590D0AF6E.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/7EADDD13-9B6B-E411-9AC4-E0CB4E29C4F7.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/984A6622-9D6B-E411-849F-E0CB4E1A1149.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/C0587C5C-996B-E411-8388-20CF305B04D2.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/DA3D4205-9A6B-E411-AA7F-20CF3027A57B.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/EE72ECF8-996B-E411-B541-20CF305B057C.root',
	'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/307D472E-9A6B-E411-BC68-20CF3027A629.root',
###########
# DY Jets #
###########
	# '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0432E62A-7A6C-E411-87BB-002590DB92A8.root',
	# '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/06C61714-7E6C-E411-9205-002590DB92A8.root',
    )
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(20))
process.source = cms.Source("PoolSource", fileNames = dyFiles )

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Run PUPPI, make some new jet collections
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from JMEAnalysis.JetToolbox.jetToolbox_cff import *
jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', PUMethod='Puppi', JETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute'] ) 
jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', JETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']) # CHS jets?
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', JETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute'] ) 
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', JETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']) # CHS jets?

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Services
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('CommonTools.UtilAlgos.TFileService_cfi')
process.TFileService.fileName=cms.string('test.root')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! JME stuff (analyzer)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

jetCollections = [];
correctionLevels = [];
jetSrcName = [];

jetCollections.append('AK4PFchs');
correctionLevels.append(['L1FastJet']);
jetSrcName.append('selectedPatJetsAK4PFCHS');

jetCollections.append('AK8PFchs');
correctionLevels.append(['L1FastJet']);
jetSrcName.append('selectedPatJetsAK8PFCHS');

jetCollections.append('AK4PUPPI');
correctionLevels.append([]);
jetSrcName.append('selectedPatJetsAK4PFPuppi');

jetCollections.append('AK8PUPPI');
correctionLevels.append([]);
jetSrcName.append('selectedPatJetsAK8PFPuppi');

validator_sequence = cms.Sequence()
setattr(process,"validator_sequence",validator_sequence)
for i in range(len(jetCollections)):
	pnm = cms.EDAnalyzer('validatorTreeMaker',
			     PileupNtupleMakerParameters,
			     JetCorLabel       = cms.string(jetCollections[i]),
			     JetCorLevels      = cms.vstring(correctionLevels[i]),
			     srcJet            = cms.InputTag(jetSrcName[i]),
			     srcRho            = cms.InputTag('fixedGridRhoAll'),
			     srcVtx            = cms.InputTag('offlineSlimmedPrimaryVertices'),
			     srcMuons          = cms.InputTag('selectedPatMuons')
			     )

	#process.myseq = cms.Sequence(process.pnm)
	setattr(process,'nt_'+jetCollections[i],pnm)
	validator_sequence = cms.Sequence(validator_sequence*pnm)

# process.p = cms.Path( puppi_onMiniAOD * corrservices_sequence * conversion_sequence * validator_sequence );

process.puppiReader = cms.EDAnalyzer("puppiReader")

process.p = cms.Path( process.puppiReader + validator_sequence )


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Output and Log
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(True)

process.output = cms.OutputModule("PoolOutputModule",                                                                                                                                                     
                                  #outputCommands = cms.untracked.vstring('drop *','keep *_puppi_*_*'),
                                  outputCommands = cms.untracked.vstring('keep *'),
                                  fileName       = cms.untracked.string ("Output.root")                                                                                                                   
)
# schedule definition                                                                                                       
process.outpath  = cms.EndPath(process.out) 

#!
#! THAT'S ALL! CAN YOU BELIEVE IT? :-D
#!
