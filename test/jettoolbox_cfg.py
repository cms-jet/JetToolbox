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

jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='CHS', addPruning=False,  dataTier="AOD", runOnMC=False)   ### For example

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
#jetToolbox( process, 'ca12', 'ca12JetSubs', 'out', addHEPTopTagger=True, addSoftDrop=True, miniAOD=True)

#jetToolbox( process, 'ak4', 'jetSequence', 'out', PUMethod='Puppi', miniAOD=True,
#                #Cut='pt > 200 && abs(eta) < 2.5', # Tight
#                #nameNewPFCollection='hltScoutingPFPacker',
#                #nameNewPFCollection='pippo',
#				#addPruning = True,
#		  		addSoftDrop = True,
#				#addFiltering=True,
#                #addNsub    = True,
#                #addPrunedSubjets=True, addSoftDropSubjets=True,
#                #addNsubSubjets  =True
#				addSoftDropSubjets = True,
#                addEnergyCorrFunc = True, ecfN3 = True,
#                )
#

#jetToolbox( process, 'ak15', 'ak15JetSubs', 'noOutput',
#   PUMethod='Puppi',
#   addPruning=True, addSoftDrop=True ,           # add basic grooming
#   addTrimming=True, addFiltering=True,
#   addSoftDropSubjets=True,
#   addPrunedSubjets=True,
#   addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
#   JETCorrPayload = 'AK8PFPuppi', #JETCorrLevels = ['L2Relative', 'L3Absolute'],
#   runOnMC=False,
#   miniAOD=True,
#   Cut='pt > 100 && abs(eta) < 2.5',
#   GetJetMCFlavour=False,
#   #GetSubJetMCFlavour=True,
#   addHEPTopTagger=True
#   )

#bTagDiscriminators = [
#    #'pfCombinedInclusiveSecondaryVertexV2BJetTags',
#    #'pfBoostedDoubleSecondaryVertexAK8BJetTags',
#    'pfMassIndependentDeepDoubleBvLJetTags:probQCD',
#    'pfMassIndependentDeepDoubleBvLJetTags:probHbb',
#    #'pfDeepCSVJetTags:probb',
#    #'pfDeepCSVJetTags:probbb',
#]
#subjetBTagDiscriminators = [
#    'pfCombinedInclusiveSecondaryVertexV2BJetTags',
#    'pfDeepCSVJetTags:probb',
#    'pfDeepCSVJetTags:probbb',
#]
#JETCorrLevels = ['L2Relative', 'L3Absolute', 'L2L3Residual']
#
#jetToolbox(process, 'ak8', 'dummyseq', 'out',
#           dataTier='miniAOD',
#           PUMethod='Puppi', JETCorrPayload='AK4PFPuppi', JETCorrLevels=JETCorrLevels,
#           #addQGTagger=True,
#           Cut='pt > 170.0 && abs(rapidity()) < 2.4',
#           runOnMC=True,
#           addNsub=True, maxTau=3, addEnergyCorrFunc=True,
#           addSoftDrop=True, addSoftDropSubjets=True, subJETCorrPayload='AK4PFPuppi', subJETCorrLevels=JETCorrLevels,
#           #bTagDiscriminators=bTagDiscriminators,
#           #subjetBTagDiscriminators=subjetBTagDiscriminators
#           )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.source = cms.Source("PoolSource",
#		fileNames = cms.untracked.vstring(#'file:example.root'
                fileNames = cms.untracked.vstring(
                    #'/store/mc/RunIIAutumn18MiniAOD/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/7E65457A-87E5-C146-8321-9A48B4F56ED1.root'
                    '/store/data/Run2017C/DoubleMuon/AOD/17Nov2017-v1/50001/2005DA54-85D3-E711-BF10-02163E011E35.root'
			),
		)

#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValTTbarPileUpMINIAODSIM
#process.source.fileNames = filesRelValTTbarPileUpMINIAODSIM

#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
#process.source.fileNames = filesRelValProdTTbarAODSIM
