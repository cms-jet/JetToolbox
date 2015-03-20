###############################################
####
####   Jet Substructure Toolbox (jetToolBox)
####   Python function for easy access of jet substructure tools implemented in CMS
####
####   Alejandro Gomez Espinosa (gomez@physics.rutgers.edu)
####   First version: 2015 - 01 - 28
####
###############################################
import FWCore.ParameterSet.Config as cms

from RecoJets.Configuration.RecoPFJets_cff import ak4PFJets, ak8PFJetsCHSSoftDrop, ak8PFJetsCHSSoftDropLinks, ak8PFJetsCHSPruned, ak8PFJetsCHSPrunedLinks, ak8PFJetsCHSTrimmed, ak8PFJetsCHSTrimmedLinks, ak8PFJetsCHSFiltered, ak8PFJetsCHSFilteredLinks, ak8PFJetsCSConstituents, ak4PFJetsCHS, ca15PFJetsCHSMassDropFiltered, hepTopTagPFJetsCHS, ak8PFJetsCHSConstituents, puppi
from RecoJets.Configuration.RecoGenJets_cff import ak4GenJets
from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoJets.JetProducers.CATopJetParameters_cfi import *
from PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import selectedPatJets
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection


def jetToolbox( proc, jetType, jetSequence, outputFile, 
		PUMethod='CHS',                    #### Options: Puppi, CS, SK
		JETCorrPayload='None', JETCorrLevels = [ 'None' ],
		subJETCorrPayload='None', subJETCorrLevels = [ 'None' ],
		miniAOD=True,
		Cut = '', 
		addPruning=False, zCut=0.1, rCut=0.5, addPrunedSubjets=False,
		addSoftDrop=False, betaCut=0.0,  zCutSD=0.1, addSoftDropSubjets=False,
		addTrimming=False, rFiltTrim=0.2, ptFrac=0.03,
		addFiltering=False, rfilt=0.3, nfilt=3,
		addCMSTopTagger=False,
		addMassDrop=False,
		addHEPTopTagger=False,
		addNsub=False, maxTau=4, 
		addQJets=False 
		):
	
	###############################################################################
	#######  Verifying some inputs and defining variables
	###############################################################################
	print '|---- jetToolbox: Initialyzing...'
	supportedJetAlgos = { 'ak': 'AntiKt', 'ca' : 'CambridgeAachen', 'kt' : 'Kt' }
	recommendedJetAlgos = [ 'ak4', 'ak8', 'ca4', 'ca8', 'ca10' ]
	payloadList = [ 'AK1PFchs', 'AK2PFchs', 'AK3PFchs', 'AK4PFchs', 'AK5PFchs', 'AK6PFchs', 'AK7PFchs', 'AK8PFchs', 'AK9PFchs', 'AK10PFchs' ]
	JECLevels = [ 'L1Offset', 'L1FastJet', 'L1JPTOffset', 'L2Relative', 'L3Absolute', 'L5Falvour', 'L7Parton' ]
	jetAlgo = ''
	algorithm = ''
	size = ''
	for type, tmpAlgo in supportedJetAlgos.iteritems(): 
		if type in jetType.lower():
			jetAlgo = type
			algorithm = tmpAlgo
			size = jetType.replace( type, '' )

	jetSize = 0.
	if int(size) in range(0, 20): jetSize = int(size)/10.
	else: print '|---- jetToolBox: jetSize has not a valid value. Insert a number between 1 and 20 after algorithm, like: AK8'
	### Trick for uppercase/lowercase algo name
	jetALGO = jetAlgo.upper()+size
	jetalgo = jetAlgo.lower()+size
	if jetalgo not in recommendedJetAlgos: print '|---- jetToolBox: CMS recommends the following jet algoritms: '+' '.join(recommendedJetAlgos)+'. You are using', jetalgo,'.'

	if JETCorrPayload not in payloadList:
		if( int(size) > 10 ): 
			size = '10' 
			print '|---- jetToolbox: For jets bigger than 1.0, the jet corrections are AK10PFchs.'
		if not 'None' in JETCorrPayload: print '|---- jetToolBox: Payload given for Jet corrections ('+JETCorrPayload+') is not correct. Using a default AK'+size+'PFchs instead.'
		JETCorrPayload = 'AK'+size+'PFchs'
	else: print '|---- jetToolBox: Using '+JETCorrPayload+' payload for jet corrections.'

	if not set(JETCorrLevels).issubset(set(JECLevels)) :
		if not 'None' in JETCorrLevels: print '|---- jetToolbox: JEC levels given ( '+' '.join(JETCorrLevels)+' ) are incorrect. Using the default levels: L1FastJet, L2Relative, L3Absolute.'
		JETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
	
	print '|---- jetToolBox: Applying these jet corrections: ( '+JETCorrPayload+', '+' '.join(JETCorrLevels)+' )'
	JEC = ( JETCorrPayload, JETCorrLevels , 'None')

	if addPrunedSubjets or addSoftDropSubjets or addCMSTopTagger:
		if subJETCorrPayload not in payloadList: 
			if not 'None' in subJETCorrPayload: print '|---- jetToolBox: Payload given for subjet corrections ('+JETCorrPayload+') is not correct. Using default AK4PFchs instead.'
			subJETCorrPayload = 'AK4PFchs'
		if not set(subJETCorrLevels).issubset(set(JECLevels)) or not subJETCorrLevels:
			if not 'None' in subJETCorrLevels: print '|---- jetToolbox: Subjet JEC levels given ( '+' '.join(subJETCorrLevels)+' ) are incorrect. Using the default levels: L1FastJet, L2Relative, L3Absolute.'
			subJETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
		print '|---- jetToolBox: Applying these subjet corrections: ( '+subJETCorrPayload+', '+' '.join(subJETCorrLevels)+' )'
		subJEC = ( subJETCorrPayload, subJETCorrLevels , 'None')


	#################################################################################
	####### Toolbox start 
	#################################################################################

	elemToKeep = []
	jetSeq = cms.Sequence()
	genParticlesLabel = ''
	pvLabel = ''
	tvLabel = ''
	toolsUsed = []

	#### For MiniAOD
	if miniAOD:

		print '|---- jetToolBox: JETTOOLBOX RUNNING ON MiniAOD FOR '+jetALGO+' JETS USING '+PUMethod

		genParticlesLabel = 'prunedGenParticles'
		pvLabel = 'offlineSlimmedPrimaryVertices'
		svLabel = 'slimmedSecondaryVertices'
		tvLabel = 'unpackedTracksAndVertices'
		pfCand = 'packedPFCandidates'

		setattr( proc, 'chs', cms.EDFilter('CandPtrSelector', src = cms.InputTag('packedPFCandidates'), cut = cms.string('fromPV')) )
		jetSeq += getattr(proc, 'chs')


		## Filter out neutrinos from packed GenParticles
		setattr( proc, 'packedGenParticlesForJetsNoNu', 
				cms.EDFilter("CandPtrSelector", 
					src = cms.InputTag("packedGenParticles"), 
					cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16")
					))
		jetSeq += getattr(proc, 'packedGenParticlesForJetsNoNu' )
		    
		setattr( proc, jetalgo+'GenJetsNoNu', 
				ak4GenJets.clone( src = 'packedGenParticlesForJetsNoNu', 
					rParam = jetSize, 
					jetAlgorithm = algorithm ) ) 
		jetSeq += getattr(proc, jetalgo+'GenJetsNoNu' )
		#fixedGridRhoFastjetAll.pfCandidatesTag = 'packedPFCandidates'

		#for Inclusive Vertex Finder
		proc.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')

	#### For AOD
	else:
		print '|---- jetToolBox: JETTOOLBOX RUNNING ON AOD FOR '+jetALGO+' JETS USING '+PUMethod

		genParticlesLabel = 'genParticles'
		pvLabel = 'offlinePrimaryVertices'
		tvLabel = 'generalTracks'
		pfCand = 'particleFlow'
		svLabel = 'inclusiveSecondaryVertices'

		proc.load('RecoJets.Configuration.GenJetParticles_cff')
		proc.load('CommonTools.ParticleFlow.pfNoPileUpJME_cff')
		setattr( proc, jetalgo+'GenJetsNoNu', ak4GenJets.clone( src = 'genParticlesForJetsNoNu', rParam = jetSize, jetAlgorithm = algorithm ) ) 
		jetSeq += getattr(proc, jetalgo+'GenJetsNoNu' )
		setattr( proc, jetalgo+'PFJetsCHS', ak4PFJets.clone( rParam = jetSize, jetAlgorithm = algorithm ) ) 
		jetSeq += getattr(proc, jetalgo+'PFJetsCHS' )
		
		

	## b-tag discriminators
	bTagDiscriminators = [
			'pfTrackCountingHighEffBJetTags',
			'pfTrackCountingHighPurBJetTags',
			'pfJetProbabilityBJetTags',
			'pfJetBProbabilityBJetTags',
			'pfSimpleSecondaryVertexHighEffBJetTags',
			'pfSimpleSecondaryVertexHighPurBJetTags',
			'pfCombinedSecondaryVertexBJetTags',
			'pfCombinedInclusiveSecondaryVertexV2BJetTags'
	    ]

	####  Creating PATjets
	if 'Puppi' in PUMethod:

		proc.load('CommonTools.PileupAlgos.Puppi_cff')
		from RecoJets.JetProducers.ak4PFJetsPuppi_cfi import ak4PFJetsPuppi
		setattr( proc, jetalgo+'PFJetsPuppi', 
				ak4PFJetsPuppi.clone( doAreaFastjet = True, 
					rParam = jetSize, 
					jetAlgorithm = algorithm ) )  
		if miniAOD:
			puppi.candName = cms.InputTag('packedPFCandidates')
			puppi.vertexName = cms.InputTag('offlineSlimmedPrimaryVertices')
		jetSeq += getattr(proc, 'puppi' )
		jetSeq += getattr(proc, jetalgo+'PFJetsPuppi' )

	elif 'CS' in PUMethod:

		from RecoJets.JetProducers.ak4PFJetsCS_cfi import ak4PFJetsCS
		setattr( proc, jetalgo+'PFJetsCS', 
				ak4PFJetsCS.clone( doAreaFastjet = True, 
					csRParam = cms.double(jetSize),
					jetAlgorithm = algorithm ) ) 
		if miniAOD: getattr( proc, jetalgo+'PFJetsCS').src = 'chs'
		jetSeq += getattr(proc, jetalgo+'PFJetsCS' )

		setattr( proc, jetalgo+'PFJetsCSConstituents', ak8PFJetsCSConstituents.clone( src = cms.InputTag(jetalgo+'PFJetsCS') ) )
		jetSeq += getattr(proc, jetalgo+'PFJetsCS' )

	elif 'SK' in PUMethod:

		proc.load('CommonTools.PileupAlgos.softKiller_cfi')
		from RecoJets.JetProducers.ak4PFJetsSK_cfi import ak4PFJetsSK
		setattr( proc, jetalgo+'PFJetsSK', 
				ak4PFJetsSK.clone( rParam = jetSize, 
					jetAlgorithm = algorithm ) ) 
		if miniAOD: getattr( proc, 'softKiller' ).PFCandidates = cms.InputTag('packedPFCandidates')
		jetSeq += getattr(proc, 'softKiller' )
		jetSeq += getattr(proc, jetalgo+'PFJetsSK' )
	
	else: 
		setattr( proc, jetalgo+'PFJetsCHS', 
				ak4PFJetsCHS.clone( 
					doAreaFastjet = True, 
					rParam = jetSize, 
					jetAlgorithm = algorithm ) ) 
		if miniAOD: getattr( proc, jetalgo+'PFJetsCHS').src = 'chs'
		jetSeq += getattr(proc, jetalgo+'PFJetsCHS' )
		#elemToKeep += [ 'keep *_'+jetalgo+'PFJetsCHS_*_*' ]

	#if miniAOD: setattr( proc, jetalgo+'PFJets'+PUMethod+'Constituents', cms.EDFilter("MiniAODJetConstituentSelector", src = cms.InputTag( jetalgo+'PFJets'+PUMethod ), cut = cms.string( 'pt > 100.0 ' ) ))
	#else: setattr( proc, jetalgo+'PFJets'+PUMethod+'Constituents', cms.EDFilter("PFJetConstituentSelector", src = cms.InputTag( jetalgo+'PFJets'+PUMethod ), cut = cms.string( Cut ) ))
	#jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Constituents' )

	addJetCollection(
			proc,
			labelName = jetALGO+'PF'+PUMethod,
			jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod),
			algo = jetalgo,
			rParam = jetSize,
			jetCorrections = JEC, #( 'AK'+size+'PFchs', cms.vstring( ['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
			pfCandidates = cms.InputTag( pfCand ),  #'packedPFCandidates'),
			svSource = cms.InputTag( svLabel ),   #'slimmedSecondaryVertices'),
			genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
			pvSource = cms.InputTag( pvLabel ), #'offlineSlimmedPrimaryVertices'),
			btagDiscriminators = bTagDiscriminators,
			outputModules = ['outputFile']
			) 

	getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod ).primaryVertices = pvLabel  #'offlineSlimmedPrimaryVertices' 
	getattr( proc, 'jetTracksAssociatorAtVertex'+jetALGO+'PF'+PUMethod ).tracks = tvLabel  # 'unpackedTracksAndVertices'

	getattr(proc,'patJetPartons').particles = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
	getattr(proc,'patJetPartonMatch'+jetALGO+'PF'+PUMethod).matched = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
	if hasattr(proc,'pfInclusiveSecondaryVertexFinderTagInfos'+jetALGO+'PF'+PUMethod):
		    getattr(proc,'pfInclusiveSecondaryVertexFinderTagInfos'+jetALGO+'PF'+PUMethod).extSVCollection = cms.InputTag( svLabel ) #'slimmedSecondaryVertices')
	if miniAOD:
		getattr(proc,'patJets'+jetALGO+'PF'+PUMethod).addAssociatedTracks = cms.bool(False) # needs to be disabled since there is no track collection present in MiniAOD
		getattr(proc,'patJets'+jetALGO+'PF'+PUMethod).addJetCharge = cms.bool(False)        # needs to be disabled since there is no track collection present in MiniAOD
	

	if addSoftDrop or addSoftDropSubjets: 

		setattr( proc, jetalgo+'PFJets'+PUMethod+'SoftDrop', 
			ak8PFJetsCHSSoftDrop.clone( 
				#src = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Constituents', 'constituents' ),
				rParam = jetSize, 
				jetAlgorithm = algorithm, 
				useExplicitGhosts=True,
				zcut=zCutSD, 
				beta=betaCut,
				writeCompound = cms.bool(True),
				jetCollInstanceName=cms.string('SubJets') ) )
		if miniAOD: getattr( proc, jetalgo+'PFJets'+PUMethod+'SoftDrop').src = 'chs'
		setattr( proc, jetalgo+'PFJets'+PUMethod+'SoftDropLinks', 
			ak8PFJetsCHSSoftDropLinks.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'SoftDrop'), 
				distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'SoftDropLinks_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'SoftDrop' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'SoftDropLinks' )
		getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'SoftDropLinks']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'SoftDropLinks' )

		if addSoftDropSubjets:

			setattr( proc, jetalgo+'GenJetsNoNuSoftDrop',
					ak4GenJets.clone(
						SubJetParameters,
						useSoftDrop = cms.bool(True),
						rParam = jetSize, 
						jetAlgorithm = algorithm, 
						useExplicitGhosts=cms.bool(True),
						#zcut=cms.double(zCutSD), 
						beta=cms.double(betaCut),
						writeCompound = cms.bool(True),
						jetCollInstanceName=cms.string('SubJets')
						))
			if miniAOD: getattr( proc, jetalgo+'GenJetsNoNuSoftDrop' ).src = 'packedGenParticlesForJetsNoNu'
			jetSeq += getattr(proc, jetalgo+'GenJetsNoNuSoftDrop' )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+'SoftDrop',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+'SoftDrop'),
					algo = jetalgo,
					rParam = jetSize,
					jetCorrections = JEC,
					btagDiscriminators = ['None'],
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
					getJetMCFlavour = False,
					outputModules = ['outputFile']
					) 
			getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+'SoftDrop' ).primaryVertices = pvLabel  #'offlineSlimmedPrimaryVertices' 
			getattr(proc,'patJetPartonMatch'+jetALGO+'PF'+PUMethod+'SoftDrop').matched = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDrop', selectedPatJets.clone( src = 'patJets'+jetALGO+'PF'+PUMethod+'SoftDrop', cut = Cut ) )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+'SoftDropSubjets',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+'SoftDrop', 'SubJets'),
					algo = jetalgo,  # needed for subjet b tagging
					rParam = jetSize,  # needed for subjet b tagging
					jetCorrections = subJEC, #( 'AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
					pfCandidates = cms.InputTag( pfCand ),  #'packedPFCandidates'),
					pvSource = cms.InputTag( pvLabel), #'offlineSlimmedPrimaryVertices'),
					svSource = cms.InputTag( svLabel ),   #'slimmedSecondaryVertices'),
					btagDiscriminators = bTagDiscriminators,
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNuSoftDrop','SubJets'),
					#getJetMCFlavour = False,
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod+'SoftDrop'), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 
			getattr( proc,'patJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets').addAssociatedTracks = cms.bool(False) # needs to be disabled since there is no track collection present in MiniAOD
			getattr( proc,'patJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets').addJetCharge = cms.bool(False)        # needs to be disabled since there is no track collection present in MiniAOD
			if hasattr(proc,'pfInclusiveSecondaryVertexFinderTagInfos'+jetALGO+'PF'+PUMethod+'SoftDropSubjets'):
				    getattr(proc,'pfInclusiveSecondaryVertexFinderTagInfos'+jetALGO+'PF'+PUMethod+'SoftDropSubjets').extSVCollection = cms.InputTag( svLabel ) #'slimmedSecondaryVertices')
			getattr(proc,'patJetCorrFactors'+jetALGO+'PF'+PUMethod+'SoftDropSubjets' ).primaryVertices = pvLabel  #'offlineSlimmedPrimaryVertices' 
			getattr(proc,'patJetPartonMatch'+jetALGO+'PF'+PUMethod+'SoftDropSubjets').matched = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets', selectedPatJets.clone( src = 'patJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets', cut = Cut ) )

			## Establish references between PATified fat jets and subjets using the BoostedJetMerger
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropPacked', 
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDrop'),
						subjetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets')
						))
			jetSeq += getattr(proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropPacked' )
			elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropPacked_*_*' ]
			toolsUsed.append( 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropPacked' )
			toolsUsed.append( 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets' )

	if addPruning or addPrunedSubjets: 

		setattr( proc, jetalgo+'PFJets'+PUMethod+'Pruned', 
			ak8PFJetsCHSPruned.clone( 
				rParam = jetSize, 
				jetAlgorithm = algorithm, 
				zcut=zCut, 
				rcut_factor=rCut,
				writeCompound = cms.bool(True),
				doAreaFastjet = cms.bool(True),
				jetCollInstanceName=cms.string('SubJets') ) )
		if miniAOD: getattr( proc, jetalgo+'PFJets'+PUMethod+'Pruned').src = 'chs'
		setattr( proc, jetalgo+'PFJets'+PUMethod+'PrunedLinks', 
			ak8PFJetsCHSPrunedLinks.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Pruned'), 
				distMax = cms.double( jetSize ) ) )

		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Pruned' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'PrunedLinks' )
		getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'PrunedLinks']
		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'PrunedLinks_*_*'] 
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'PrunedLinks' )

		if addPrunedSubjets:
			setattr( proc, jetalgo+'GenJetsNoNuPruned',
					ak4GenJets.clone(
						SubJetParameters,
						rParam = jetSize,
						usePruning = cms.bool(True),
						writeCompound = cms.bool(True),
						jetCollInstanceName=cms.string('SubJets')
						))
			if miniAOD: getattr( proc, jetalgo+'GenJetsNoNuPruned' ).src = 'packedGenParticlesForJetsNoNu'
			jetSeq += getattr(proc, jetalgo+'GenJetsNoNuPruned' )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+'Pruned',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Pruned'),
					algo = jetalgo,
					rParam = jetSize,
					jetCorrections = JEC,
					btagDiscriminators = ['None'],
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
					getJetMCFlavour = False,
					outputModules = ['outputFile']
					) 
			getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+'Pruned' ).primaryVertices = pvLabel  #'offlineSlimmedPrimaryVertices' 
			getattr(proc,'patJetPartonMatch'+jetALGO+'PF'+PUMethod+'Pruned').matched = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'Pruned', selectedPatJets.clone( src = 'patJets'+jetALGO+'PF'+PUMethod+'Pruned', cut = Cut ) )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+'PrunedSubjets',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Pruned', 'SubJets'),
					algo = jetalgo,  # needed for subjet b tagging
					rParam = jetSize,  # needed for subjet b tagging
					jetCorrections = subJEC,
					pfCandidates = cms.InputTag( pfCand ),  #'packedPFCandidates'),
					pvSource = cms.InputTag( pvLabel), #'offlineSlimmedPrimaryVertices'),
					svSource = cms.InputTag( svLabel ),   #'slimmedSecondaryVertices'),
					btagDiscriminators = bTagDiscriminators,
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNuPruned','SubJets'),
					#getJetMCFlavour = False,
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod+'Pruned'), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 

			getattr(proc,'patJetPartonMatch'+jetALGO+'PF'+PUMethod+'PrunedSubjets').matched = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
			getattr(proc,'patJetCorrFactors'+jetALGO+'PF'+PUMethod+'PrunedSubjets' ).primaryVertices = pvLabel  #'offlineSlimmedPrimaryVertices' 
			if hasattr(proc,'pfInclusiveSecondaryVertexFinderTagInfos'+jetALGO+'PF'+PUMethod+'PrunedSubjets'):
				getattr(proc,'pfInclusiveSecondaryVertexFinderTagInfos'+jetALGO+'PF'+PUMethod+'PrunedSubjets').extSVCollection = cms.InputTag( svLabel ) #'slimmedSecondaryVertices')
			if miniAOD:
				getattr( proc,'patJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets').addAssociatedTracks = cms.bool(False) # needs to be disabled since there is no track collection present in MiniAOD
				getattr( proc,'patJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets').addJetCharge = cms.bool(False)        # needs to be disabled since there is no track collection present in MiniAOD
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets', selectedPatJets.clone( src = 'patJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets', cut = Cut ) )

			## Establish references between PATified fat jets and subjets using the BoostedJetMerger
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedPacked', 
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+'Pruned'),
						subjetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets')
						))
			jetSeq += getattr(proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedPacked' )
			elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedPacked_*_*' ]
			toolsUsed.append( 'selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedPacked' )
			toolsUsed.append( 'selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets' )


	if addTrimming:

		setattr( proc, jetalgo+'PFJets'+PUMethod+'Trimmed', 
				ak8PFJetsCHSTrimmed.clone( #src = 'chs',
					rParam = jetSize, 
					jetAlgorithm = algorithm,
					rFilt= rFiltTrim,
					trimPtFracMin= ptFrac) ) 
		if miniAOD: getattr( proc, jetalgo+'PFJets'+PUMethod+'Trimmed').src = 'chs'
		setattr( proc, jetalgo+'PFJets'+PUMethod+'TrimmedLinks', 
				ak8PFJetsCHSTrimmedLinks.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
					matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Trimmed'), 
					distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'TrimmedLinks_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Trimmed' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'TrimmedLinks' )
		getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'TrimmedLinks']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'TrimmedLinks' )

	if addFiltering:

		setattr( proc, jetalgo+'PFJets'+PUMethod+'Filtered', 
				ak8PFJetsCHSFiltered.clone( #src = 'chs', 
					rParam = jetSize, 
					jetAlgorithm = algorithm,
					rFilt= rfilt,
					nFilt= nfilt ) ) 
		if miniAOD: getattr( proc, jetalgo+'PFJets'+PUMethod+'Filtered').src = 'chs'
		setattr( proc, jetalgo+'PFJets'+PUMethod+'FilteredLinks', 
				ak8PFJetsCHSFilteredLinks.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
					matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Filtered'), 
					distMax = cms.double( jetSize ) ) )
		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'FilteredLinks_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Filtered' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'FilteredLinks' )
		getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'FilteredLinks']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'FilteredLinks' )

	if addCMSTopTagger :

		if 'CA' in jetALGO : 

			setattr( proc, 'cmsTopTagPFJets'+PUMethod,  
					cms.EDProducer("CATopJetProducer",
						PFJetParameters.clone( #src = cms.InputTag("chs"), #ak8PFJetsCHSConstituents", "constituents"),
							doAreaFastjet = cms.bool(True),
							doRhoFastjet = cms.bool(False),
							jetPtMin = cms.double(100.0)
							),
						AnomalousCellParameters,
						CATopJetParameters.clone( jetCollInstanceName = cms.string("SubJets"),
							verbose = cms.bool(False),
							algorithm = cms.int32(1), # 0 = KT, 1 = CA, 2 = anti-KT
							tagAlgo = cms.int32(0), #0=legacy top
							useAdjacency = cms.int32(2), # modified adjacency
							centralEtaCut = cms.double(2.5), # eta for defining "central" jets
							sumEtBins = cms.vdouble(0,1600,2600), # sumEt bins over which cuts vary. vector={bin 0 lower bound, bin 1 lower bound, ...}
							rBins = cms.vdouble(0.8,0.8,0.8), # Jet distance paramter R. R values depend on sumEt bins.
							ptFracBins = cms.vdouble(0.05,0.05,0.05), # minimum fraction of central jet pt for subjets (deltap)
							deltarBins = cms.vdouble(0.19,0.19,0.19), # Applicable only if useAdjacency=1. deltar adjacency values for each sumEtBin
							nCellBins = cms.vdouble(1.9,1.9,1.9),
							),
						jetAlgorithm = cms.string("CambridgeAachen"),
						rParam = cms.double(jetSize),
						writeCompound = cms.bool(True)
						)
					)
			if miniAOD: getattr( proc, 'cmsTopTagPFJets'+PUMethod ).src = 'chs'
			
			setattr( proc, "CATopTagInfos", 
					cms.EDProducer("CATopJetTagger",
						src = cms.InputTag('cmsTopTagPFJets'+PUMethod),
						TopMass = cms.double(171),
						TopMassMin = cms.double(0.),
						TopMassMax = cms.double(250.),
						WMass = cms.double(80.4),
						WMassMin = cms.double(0.0),
						WMassMax = cms.double(200.0),
						MinMassMin = cms.double(0.0),
						MinMassMax = cms.double(200.0),
						verbose = cms.bool(False)
						)
					)
			addJetCollection(
					proc,
					labelName = 'CMSTopTag'+PUMethod,
					jetSource = cms.InputTag('cmsTopTagPFJets'+PUMethod),
					jetCorrections = JEC,
					pfCandidates = cms.InputTag( pfCand ),  #'packedPFCandidates'),
					pvSource = cms.InputTag( pvLabel), #'offlineSlimmedPrimaryVertices'),
					svSource = cms.InputTag( svLabel ),   #'slimmedSecondaryVertices'),
					btagDiscriminators = bTagDiscriminators,
					genJetCollection = cms.InputTag(jetalgo+'GenJetsNoNu'),
					getJetMCFlavour = False
					)
			getattr(proc,'patJetPartonMatchCMSTopTag'+PUMethod).matched = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
			if hasattr(proc,'pfInclusiveSecondaryVertexFinderTagInfosCMSTopTag'+PUMethod):
				getattr(proc,'pfInclusiveSecondaryVertexFinderTagInfosCMSTopTag'+PUMethod).extSVCollection = cms.InputTag( svLabel ) #'slimmedSecondaryVertices')
			getattr(proc,'patJetsCMSTopTag'+PUMethod).addTagInfos = True
			getattr(proc,'patJetsCMSTopTag'+PUMethod).tagInfoSources = cms.VInputTag( cms.InputTag('CATopTagInfos'))
			getattr(proc,'patJetCorrFactorsCMSTopTag'+PUMethod ).primaryVertices = pvLabel  #'offlineSlimmedPrimaryVertices' 
			getattr(proc,'patJetsCMSTopTag'+PUMethod).addAssociatedTracks = cms.bool(False) # needs to be disabled since there is no track collection present in MiniAOD
			getattr(proc,'patJetsCMSTopTag'+PUMethod).addJetCharge = cms.bool(False)        # needs to be disabled since there is no track collection present in MiniAOD
			setattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod, selectedPatJets.clone( src = 'patJetsCMSTopTag'+PUMethod, cut = Cut ) )

			addJetCollection(
					proc,
					labelName = 'CMSTopTag'+PUMethod+'Subjets',
					jetSource = cms.InputTag('cmsTopTagPFJets'+PUMethod, 'SubJets'),
					algo = jetalgo,  # needed for subjet b tagging
					rParam = jetSize,  # needed for subjet b tagging
					jetCorrections = subJEC,
					pfCandidates = cms.InputTag( pfCand ),  #'packedPFCandidates'),
					pvSource = cms.InputTag( pvLabel), #'offlineSlimmedPrimaryVertices'),
					svSource = cms.InputTag( svLabel ),   #'slimmedSecondaryVertices'),
					btagDiscriminators = bTagDiscriminators,
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
					#getJetMCFlavour = False,
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag('CMSTopTag'+PUMethod), # needed for subjet flavor clustering
					)

			getattr(proc,'patJetPartonMatchCMSTopTag'+PUMethod+'Subjets').matched = cms.InputTag( genParticlesLabel ) #'prunedGenParticles')
			if hasattr(proc,'pfInclusiveSecondaryVertexFinderTagInfosCMSTopTag'+PUMethod+'Subjets'):
				getattr(proc,'pfInclusiveSecondaryVertexFinderTagInfosCMSTopTag'+PUMethod+'Subjets').extSVCollection = cms.InputTag(svLabel) #'slimmedSecondaryVertices')
			getattr(proc,'patJetCorrFactorsCMSTopTag'+PUMethod+'Subjets' ).primaryVertices = pvLabel  #'offlineSlimmedPrimaryVertices' 
			getattr(proc,'patJetsCMSTopTag'+PUMethod+'Subjets').addAssociatedTracks = cms.bool(False) # needs to be disabled since there is no track collection present in MiniAOD
			getattr(proc,'patJetsCMSTopTag'+PUMethod+'Subjets').addJetCharge = cms.bool(False)        # needs to be disabled since there is no track collection present in MiniAOD
			setattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod+'Subjets', selectedPatJets.clone( src = 'patJetsCMSTopTag'+PUMethod+'Subjets', cut = Cut ) )

			setattr( proc, 'patJetsCMSTopTag'+PUMethod+'Packed', 
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag('patJetsCMSTopTag'+PUMethod ),
						subjetSrc=cms.InputTag('patJetsCMSTopTag'+PUMethod+'Subjets')
						))
			jetSeq += getattr(proc, 'patJetsCMSTopTag'+PUMethod+'Packed' )
			elemToKeep += [ 'keep *_patJetsCMSTopTag'+PUMethod+'Packed_*_*' ]
			toolsUsed.append( 'patJetsCMSTopTag'+PUMethod+'Packed' )

		else: print '|----- CMS recommends CambridgeAachen for CMS Top Tagger, you are using '+algorithm+'. JetToolbox will not run CMS Top Tagger.'

	if addMassDrop :

		if 'CA' in jetALGO : 
			setattr( proc, jetalgo+'PFJets'+PUMethod+'MassDropFiltered', ca15PFJetsCHSMassDropFiltered.clone( rParam = jetSize ) )
			if miniAOD: getattr( proc, jetalgo+'PFJets'+PUMethod+'MassDropFiltered').src = 'chs'
			setattr( proc, jetalgo+'PFJets'+PUMethod+'MassDropFilteredLinks', ak8PFJetsCHSPrunedLinks.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				matched = cms.InputTag(jetalgo+'PFJets'+PUMethod+'MassDropFiltered'), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'MassDropFilteredLinks_*_*' ]
			getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'MassDropFilteredLinks' ]
			jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'MassDropFiltered' )
			jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'MassDropFilteredLinks' )
		else: print '|----- CMS recommends CambridgeAachen for Mass Drop, you are using '+algorithm+'. JetToolbox will not run Mass Drop.'
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'MassDropFilteredLinks' )

	if addHEPTopTagger: 
		if ( jetSize >= 1. ) and ( 'CA' in jetALGO ): 

			if miniAOD: setattr( proc, 'hepTopTagPFJets'+PUMethod, hepTopTagPFJetsCHS.clone( src = 'chs' ) )
			else: 
				setattr( proc, jetalgo+'PFJets'+PUMethod+'Constituents', ak8PFJetsCHSConstituents.clone( src = jetalgo+'PFJets'+PUMethod ) )
				setattr( proc, 'hepTopTagPFJets'+PUMethod, hepTopTagPFJetsCHS.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Constituents', 'constituents' ) ) )
			setattr( proc, 'hepTopTagPFJets'+PUMethod+'Links'+jetALGO, ak8PFJetsCHSPrunedLinks.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				matched = cms.InputTag("hepTopTagPFJets"+PUMethod), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_hepTopTagPFJets'+PUMethod+'Links'+jetALGO+'_*_*' ]
			getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ 'hepTopTagPFJets'+PUMethod+'Links'+jetALGO ]
			jetSeq += getattr(proc, 'hepTopTagPFJets'+PUMethod )
			jetSeq += getattr(proc, 'hepTopTagPFJets'+PUMethod+'Links'+jetALGO )
			toolsUsed.append( 'hepTopTagPFJets'+PUMethod+'Links'+jetALGO )
		else: print '|----- CMS recommends CambridgeAachen for HEPTopTagger, you are using '+algorithm+', and a jet cone size bigger than 1. JetToolbox will not run HEP TopTagger.'

	####### Nsubjettiness
	if addNsub:
		from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

		rangeTau = range(1,maxTau+1)
		setattr( proc, 'Njettiness'+jetALGO+PUMethod, 
				Njettiness.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
					Njets=cms.vuint32(rangeTau),         # compute 1-, 2-, 3-, 4- subjettiness
					# variables for measure definition : 
					measureDefinition = cms.uint32( 0 ), # CMS default is normalized measure
					beta = cms.double(1.0),              # CMS default is 1
					R0 = cms.double( jetSize ),              # CMS default is jet cone size
					Rcutoff = cms.double( -999.0),       # not used by default
					# variables for axes definition :
					axesDefinition = cms.uint32( 6 ),    # CMS default is 1-pass KT axes
					nPass = cms.int32(-999),             # not used by default
					akAxesR0 = cms.double(-999.0) ) )        # not used by default

		elemToKeep += [ 'keep *_Njettiness'+jetALGO+PUMethod+'_*_*' ]
		for tau in rangeTau: getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += ['Njettiness'+jetALGO+PUMethod+':tau'+str(tau) ] 
		jetSeq += getattr(proc, 'Njettiness'+jetALGO+PUMethod )
		toolsUsed.append( 'Njettiness'+jetALGO+PUMethod )

	###### QJetsAdder
	if addQJets:
		#This is the old way before 731
		### there must be a better way to do this random number introduction
		setattr( proc, 'RandomNumberGeneratorService', cms.Service("RandomNumberGeneratorService", 
							QJetsAdderCA8 = cms.PSet(initialSeed = cms.untracked.uint32(7)),
							QJetsAdderAK8 = cms.PSet(initialSeed = cms.untracked.uint32(31)),
							QJetsAdderCA15 = cms.PSet(initialSeed = cms.untracked.uint32(76)), ) )

		from RecoJets.JetProducers.qjetsadder_cfi import QJetsAdder
		setattr( proc, 'QJetsAdder'+jetALGO, 
				QJetsAdder.clone( src = cms.InputTag(jetalgo+'PFJets'+PUMethod), 
					jetRad = cms.double( jetSize ), 
					jetAlgo = cms.string( jetALGO[0:2] )))
		elemToKeep += [ 'keep *_QJetsAdder'+jetALGO+'_*_*' ]
		getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += ['QJetsAdder'+jetALGO+':QjetsVolatility']  
		jetSeq += getattr(proc, 'QJetsAdder'+jetALGO )
		toolsUsed.append( 'QJetsAdder'+jetALGO )
		'''
		### This is for 731 or higher
		if 'ak4' in jetalgo:
			proc.load('RecoJets.JetProducers.QGTagger_cfi')
			proc.QGTagger.srcJets = cms.InputTag(jetalgo+'PFJets'+PUMethod)    # Could be reco::PFJetCollection or pat::JetCollection (both AOD and miniAOD)
			proc.QGTagger.jetsLabel = cms.string('QGL_AK4PFchs')        # Other options (might need to add an ESSource for it): see https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion
			elemToKeep += [ 'keep *_QGTagger_*_*' ]
			getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod).userData.userFloats.src += ['QJetsAdder'+jetALGO+':qgLikelihood']  
			jetSeq += getattr(proc, 'QGTagger' )
		else:
			'QGTagger is optimized for ak4 jets.'
		'''

	setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod, selectedPatJets.clone( src = 'patJets'+jetALGO+'PF'+PUMethod, cut = Cut ) )
	elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+'_*_*' ]
	elemToKeep += [ 'drop *_selectedPatJets'+jetALGO+'PF'+PUMethod+'_calo*_*' ]
	elemToKeep += [ 'drop *_selectedPatJets'+jetALGO+'PF'+PUMethod+'_tagInfos_*' ]

	print '|---- jetToolBox: Running '+', '.join(toolsUsed)+'.'

	### "return"
	setattr(proc, jetSequence, jetSeq)
	if hasattr(proc, outputFile): getattr(proc, outputFile).outputCommands += elemToKeep
	else: setattr( proc, outputFile, 
			cms.OutputModule('PoolOutputModule', 
				fileName = cms.untracked.string('jettoolbox.root'), 
				outputCommands = cms.untracked.vstring( elemToKeep ) ) )


