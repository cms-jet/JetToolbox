import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process('jetToolbox', eras.Run2_2017)

process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '92X_upgrade2017_realistic_v1'

process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.MessageLogger.suppressWarning = cms.untracked.vstring('ecalLaserCorrFilter','manystripclus53X','toomanystripclus53X')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)

#process.load("JetMETCorrections.Configuration.JetCorrectionServices_cff")
#process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")

########################################################################
#### THESE EXAMPLES ARE JUST TESTS, MOST OF THEM ARE TOTALLY WRONG.
#### THERE ARE JUST TO TEST SEVERAL FEATURES OF THE JETTOOLBOX.
#######################################################################

from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox

'''
jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='CHS', miniAOD=True,
		#Cut='pt > 200 && abs(eta) < 2.5', # Tight
		runOnMC=False,
		addPruning = True, addSoftDrop = True,
		addNsub    = True,
		#addPrunedSubjets=True, addSoftDropSubjets=True,
		#addNsubSubjets  =True
		)

#jetToolbox( process, 'ak4', 'jetSequence', 'out', PUMethod='Puppi', miniAOD=True, runOnMC=True )
#process.load('CommonTools.PileupAlgos.Puppi_cff')
#process.PuppiOnTheFly = process.puppi.clone( candName = cms.InputTag( 'packedPFCandidates' ), vertexName = cms.InputTag( 'offlineSlimmedPrimaryVertices' ), clonePackedCands = cms.bool(True) )
#process.PuppiOnTheFly.useExistingWeights = True
#jetToolbox(process, 'ak4', 'dummy', 'out', PUMethod = 'Puppi', JETCorrPayload = 'AK4PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute'], miniAOD = True, newPFCollection=True, nameNewPFCollection='puppi')

#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True , JETCorrPayload='AK8PFchs', subJETCorrPayload='AK4PFchs', subJETCorrLevels=['L2Relative', 'L3Absoulte'] ) #, Cut='pt > 100 && abs(eta) < 2.4' )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrLevels=['L1FastJet', 'L2Relative'], newPFCollection=True, nameNewPFCollection='PuppiOnTheFly' )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='SK', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrLevels=['L1FastJet', 'L2Relative'] )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CHS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, addNsubSubjets=True )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CHS', addPruning=True, addSoftDrop=True , addSoftDropSubjets=True,  addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, addNsubSubjets=True )
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out',
		PUMethod='CHS',
		#updateCollection='slimmedJetsAK8',
		JETCorrPayload='AK8PFchs',
		#addEnergyCorrFunc=True,
		#updateCollectionSubjets='slimmedJetsAK8PFCHSSoftDropPacked:SubJets',
		#subJETCorrPayload='AK4PFchs',
		bTagDiscriminators=listBtagDiscriminatorsAK4,
		#addNsubSubjets=True,
		#addPrunedSubjets=True,
		postFix= 'CollectionTests',
		#addTrimming=True,
		#addPruning=True
		)  #, addPrunedSubjets=True, subJETCorrPayload='AK4PFchs' )
listBtagDiscriminatorsAK4 = [
                #'pfJetProbabilityBJetTags',
                #'pfCombinedInclusiveSecondaryVertexV2BJetTags',
                'pfCombinedMVAV2BJetTags',
                #'pfCombinedCvsLJetTags',
                #'pfCombinedCvsBJetTags',
                ]
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out',
		PUMethod='Puppi',
		#updateCollection='slimmedJetsAK8',
		JETCorrPayload='AK8PFPuppi',
		#addEnergyCorrFunc=True,
		#updateCollectionSubjets='slimmedJetsAK8PFCHSSoftDropPacked:SubJets',
		subJETCorrPayload='AK4PFPuppi',
		bTagDiscriminators=listBtagDiscriminatorsAK4,
		addNsub    = True,
		#addNsubSubjets=True,
		#addPrunedSubjets=True,
		#postFix= 'NEWCOLLECTIONOFJETS',
		#addTrimming=True,
		#addFiltering=True,
		#addPruning=True,
		addSoftDrop=True
		)  #, addPrunedSubjets=True, subJETCorrPayload='AK4PFchs' )
'''
#from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
#listBTagInfos = ['pfInclusiveSecondaryVertexFinderTagInfos','pfImpactParameterTagInfos']
#listBtagDiscriminatorsAK8 = [
# 'pfBoostedDoubleSecondaryVertexAK8BJetTags',
#]
#jecLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
##if self.residual: jecLevels.append("L2L3Residual")
#jetToolbox(process,
#	'ak8',
#	'jetSequence',
#	'out',
#	PUMethod = 'Puppi',
#	miniAOD = True,
#	#runOnMC = False,
#	postFix='Clean',
#	Cut = 'pt>170.',
#	addPruning = True,
#	addSoftDropSubjets = True,
#	addNsub = True,
#	maxTau = 3,
#	bTagInfos = listBTagInfos,
#	bTagDiscriminators = listBtagDiscriminatorsAK8,
#	JETCorrLevels = jecLevels,
#	subJETCorrLevels = jecLevels,
#	addEnergyCorrFunc = True,
#)

#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CHS', JETCorrPayload = 'AK8PFchs', addEnergyCorrFunc=True, addNsubSubjets=True, addTrimming=True, addFiltering=True, addPruning=True, addSoftDrop=True, addSoftDropSubjets=True )  #PUMethod='CHS', addPrunedSubjets=True, subJETCorrPayload='AK4PFchs' )


#jetToolbox( process, 'ak4', 'ak4JetSubsUpdate', 'out', updateCollection='slimmedJets', JETCorrPayload = 'AK4PFchs', JETCorrLevels=['L2Relative', 'L3Absolute'], addQGTagger=True, addPUJetID=True, bTagDiscriminators=listBtagDiscriminatorsAK4 )
#jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', addQGTagger=True, addPUJetID=True, postFix='New' )


#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CHS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='CHS', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, JETCorrPayload='AK3Pachs', subJETCorrPayload='AK8PFchs', JETCorrLevels=['L1FastJet', 'L2Relative'], addEnergyCorrFunc=True, maxECF=5 )
#jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', JETCorrPayload='AK4PFchs', JETCorrLevels = ['L1FastJet','L2Relative','L3Absolute'], miniAOD=True, runOnMC=True, addNsub=True, addPUJetID=True, addPruning=False, addTrimming=False, addCMSTopTagger=True, addHEPTopTagger=True, addMassDrop=True, addSoftDrop=False, addQGTagger=True )
#
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='Puppi', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='SK', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, JETCorrPayload='AK8PF' )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, JETCorrPayload='AK8PFchs', JETCorrLevels=['L3Absolute'] )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='Puppi', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='SK', addHEPTopTagger=True, addSoftDrop=True )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', addHEPTopTagger=True, addSoftDrop=True )

#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out' , addPruning=True, addSoftDrop=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True )
#jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', addQGTagger=True) #PUMethod='Puppi', addPUJetID=True, addPruning=True, addSoftDrop=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True )
#jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', addQGTagger=True, QGjetsLabel='', PUMethod='Plain' )
#jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', addQGTagger=True, PUMethod='Puppi' )

#
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='Puppi', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', PUMethod='SK', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', addPruning=True, addSoftDrop=True , addPrunedSubjets=True, addSoftDropSubjets=True, addNsub=True, maxTau=6, addTrimming=True, addFiltering=True, miniAOD=False )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='Puppi', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', PUMethod='SK', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', addCMSTopTagger=True, addMassDrop=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='Puppi', addHEPTopTagger=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', PUMethod='SK', addHEPTopTagger=True, addSoftDrop=True, miniAOD=False )
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', addHEPTopTagger=True, addSoftDrop=True, miniAOD=False )

jetToolbox( process, 'ak4', 'jetSequence', 'out', PUMethod='Puppi', miniAOD=True,
                #Cut='pt > 200 && abs(eta) < 2.5', # Tight
                #nameNewPFCollection='hltScoutingPFPacker',
                #nameNewPFCollection='pippo',
				#addPruning = True,
		  		addSoftDrop = True,
				#addFiltering=True,
                #addNsub    = True,
                #addPrunedSubjets=True, addSoftDropSubjets=True,
                #addNsubSubjets  =True
				addSoftDropSubjets = True,
                addEnergyCorrFunc = True, ecfN3 = True,
				saveJetCollection = True,
                )



process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )
process.source = cms.Source("PoolSource",
#		fileNames = cms.untracked.vstring(#'file:example.root'
		fileNames = cms.untracked.vstring(
			'/store/data/Run2016G/JetHT/MINIAOD/PromptReco-v1/000/280/002/00000/E82E26C7-4375-E611-AE7F-FA163E48F736.root'
			#'/store/mc/RunIIFall17MiniAOD/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/00000/02961665-F9F9-E711-87B5-0026B93F49B0.root'
			#'/store/mc/RunIIFall17MiniAODv2/Res1ToRes2GluTo3Glu_M1-2000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/44F72487-F763-E811-9E6C-6C3BE5B5E4C0.root'
			#'/store/relval/CMSSW_9_4_5_cand1/JetHT/MINIAOD/94X_dataRun2_relval_v11_RelVal_rmaod_jetHT2017B-v1/10000/18B5E95F-992E-E811-9422-0CC47A78A418.root'
			),
		)

from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValTTbarPileUpMINIAODSIM
process.source.fileNames = filesRelValTTbarPileUpMINIAODSIM

#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
#process.source.fileNames = filesRelValProdTTbarAODSIM
