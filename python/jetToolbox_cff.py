###############################################
####
####   Jet Substructure Toolbox (jetToolBox)
####   Python function for easy access of 
####   jet substructure tools implemented in CMS
####
####   Alejandro Gomez Espinosa (gomez@physics.rutgers.edu)
####
###############################################
import FWCore.ParameterSet.Config as cms

from RecoJets.Configuration.RecoPFJets_cff import ak4PFJets, ak8PFJetsCHSSoftDrop, ak8PFJetsCHSSoftDropMass, ak8PFJetsCHSPruned, ak8PFJetsCHSPrunedMass, ak8PFJetsCHSTrimmed, ak8PFJetsCHSTrimmedMass, ak8PFJetsCHSFiltered, ak8PFJetsCHSFilteredMass, ak4PFJetsCHS, ca15PFJetsCHSMassDropFiltered, hepTopTagPFJetsCHS, ak8PFJetsCHSConstituents, puppi
from RecoJets.Configuration.RecoGenJets_cff import ak4GenJets
from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoJets.JetProducers.CATopJetParameters_cfi import *
from PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import selectedPatJets
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection, updateJetCollection


def jetToolbox( proc, jetType, jetSequence, outputFile,
		updateCollection='', updateCollectionSubjets='',
		newPFCollection=False, nameNewPFCollection = '',	
		PUMethod='CHS', 
		miniAOD=True,
		runOnMC=True,
		JETCorrPayload='', JETCorrLevels = [ 'None' ], GetJetMCFlavour=True,
		Cut = '', 
		bTagDiscriminators = None, 
		bTagInfos = None, 
		subJETCorrPayload='', subJETCorrLevels = [ 'None' ], GetSubjetMCFlavour=True,
		CutSubjet = '', 
		addPruning=False, zCut=0.1, rCut=0.5, addPrunedSubjets=False,
		addSoftDrop=False, betaCut=0.0,  zCutSD=0.1, addSoftDropSubjets=False,
		addTrimming=False, rFiltTrim=0.2, ptFrac=0.03,
		addFiltering=False, rfilt=0.3, nfilt=3,
		addCMSTopTagger=False,
		addMassDrop=False,
		addHEPTopTagger=False,
		addNsub=False, maxTau=4,
		addNsubSubjets=False, subjetMaxTau=4,
		addPUJetID=False,
		addQJets=False,
		addQGTagger=False, QGjetsLabel='chs',
		addEnergyCorrFunc=False, ecfBeta = 1.0, maxECF=3,
		):

	runOnData = not runOnMC
	if runOnData:
		GetJetMCFlavour = False
		GetSubjetMCFlavour = False
	
	###############################################################################
	#######  Verifying some inputs and defining variables
	###############################################################################
	print '|---- jetToolbox: Initialyzing collection...'
	if newPFCollection: print '|---- jetToolBox: Using '+ nameNewPFCollection +' as PFCandidates collection'
	supportedJetAlgos = { 'ak': 'AntiKt', 'ca' : 'CambridgeAachen', 'kt' : 'Kt' }
	recommendedJetAlgos = [ 'ak4', 'ak8', 'ca4', 'ca8', 'ca10' ]
	payloadList = [ 'None',
			'AK1PFchs', 'AK2PFchs', 'AK3PFchs', 'AK4PFchs', 'AK5PFchs', 'AK6PFchs', 'AK7PFchs', 'AK8PFchs', 'AK9PFchs', 'AK10PFchs',
			'AK1PFPUPPI', 'AK2PFPUPPI', 'AK3PFPUPPI', 'AK4PFPUPPI', 'AK5PFPUPPI', 'AK6PFPUPPI', 'AK7PFPUPPI', 'AK8PFPUPPI', 'AK9PFPUPPI', 'AK10PFPUPPI',  
			'AK1PFSK', 'AK2PFSK', 'AK3PFSK', 'AK4PFSK', 'AK5PFSK', 'AK6PFSK', 'AK7PFSK', 'AK8PFSK', 'AK9PFSK', 'AK10PFSK',  
			'AK1PF', 'AK2PF', 'AK3PF', 'AK4PF', 'AK5PF', 'AK6PF', 'AK7PF', 'AK8PF', 'AK9PF', 'AK10PF' ]
	JECLevels = [ 'L1Offset', 'L1FastJet', 'L1JPTOffset', 'L2Relative', 'L3Absolute', 'L5Falvour', 'L7Parton' ]
	if runOnData:
		JECLevels += ['L2L3Residual']
	jetAlgo = ''
	algorithm = ''
	size = ''
	for TYPE, tmpAlgo in supportedJetAlgos.iteritems(): 
		if TYPE in jetType.lower():
			jetAlgo = TYPE
			algorithm = tmpAlgo
			size = jetType.replace( TYPE, '' )

	jetSize = 0.
	if int(size) in range(0, 20): jetSize = int(size)/10.
	else: print '|---- jetToolBox: jetSize has not a valid value. Insert a number between 1 and 20 after algorithm, like: AK8'
	### Trick for uppercase/lowercase algo name
	jetALGO = jetAlgo.upper()+size
	jetalgo = jetAlgo.lower()+size
	if jetalgo not in recommendedJetAlgos: print '|---- jetToolBox: CMS recommends the following jet algoritms: '+' '.join(recommendedJetAlgos)+'. You are using', jetalgo,'.'


	#################################################################################
	####### Toolbox start 
	#################################################################################

	elemToKeep = []
	jetSeq = cms.Sequence()
	genParticlesLabel = ''
	pvLabel = ''
	tvLabel = ''
	toolsUsed = []

	### List of Jet Corrections
	if not set(JETCorrLevels).issubset(set(JECLevels)): 
		if ( 'CHS' in PUMethod ) or  ( 'Plain' in PUMethod ): JETCorrLevels = ['L1FastJet','L2Relative', 'L3Absolute']
		else: JETCorrLevels = [ 'L2Relative', 'L3Absolute']
		if runOnData: JETCorrLevels.append('L2L3Residual')
	if not set(subJETCorrLevels).issubset(set(JECLevels)): 
		if ( 'CHS' in PUMethod ) or  ( 'Plain' in PUMethod ): subJETCorrLevels = ['L1FastJet','L2Relative', 'L3Absolute']
		else: subJETCorrLevels = [ 'L2Relative', 'L3Absolute']
		if runOnData: subJETCorrLevels.append('L2L3Residual')


	if not updateCollection: 

		## b-tag discriminators
		if bTagDiscriminators is None:
			bTagDiscriminators = [
					'pfTrackCountingHighEffBJetTags',
					'pfTrackCountingHighPurBJetTags',
					'pfJetProbabilityBJetTags',
					'pfJetBProbabilityBJetTags',
					'pfSimpleSecondaryVertexHighEffBJetTags',
					'pfSimpleSecondaryVertexHighPurBJetTags',
					'pfCombinedSecondaryVertexV2BJetTags',
					'pfCombinedInclusiveSecondaryVertexV2BJetTags',
					'pfCombinedMVAV2BJetTags'
			]

		#### For MiniAOD
		if miniAOD:

			print '|---- jetToolBox: JETTOOLBOX RUNNING ON MiniAOD FOR '+jetALGO+' JETS USING '+PUMethod

			genParticlesLabel = 'prunedGenParticles'
			pvLabel = 'offlineSlimmedPrimaryVertices'
			svLabel = 'slimmedSecondaryVertices'
			tvLabel = 'unpackedTracksAndVertices'
			muLabel = 'slimmedMuons'
			elLabel = 'slimmedElectrons'
			pfCand = nameNewPFCollection if newPFCollection else 'packedPFCandidates'

			if runOnMC:
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

			#for Inclusive Vertex Finder
			proc.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')

		#### For AOD
		else:
			print '|---- jetToolBox: JETTOOLBOX RUNNING ON AOD FOR '+jetALGO+' JETS USING '+PUMethod

			genParticlesLabel = 'genParticles'
			pvLabel = 'offlinePrimaryVertices'
			tvLabel = 'generalTracks'
			muLabel = 'muons'
			elLabel = 'gedGsfElectrons'
			pfCand =  nameNewPFCollection if newPFCollection else 'particleFlow'
			svLabel = 'inclusiveCandidateSecondaryVertices'

			if runOnMC:
				proc.load('RecoJets.Configuration.GenJetParticles_cff')
				setattr( proc, jetalgo+'GenJetsNoNu', ak4GenJets.clone( src = 'genParticlesForJetsNoNu', rParam = jetSize, jetAlgorithm = algorithm ) ) 
				jetSeq += getattr(proc, jetalgo+'GenJetsNoNu' )
			

		####  Creating PATjets
		tmpPfCandName = pfCand.lower()
		if 'Puppi' in PUMethod:
			if ('puppi' in tmpPfCandName): 
				srcForPFJets = pfCand
				print '|---- jetToolBox: Not running puppi algorithm because keyword puppi was specified in nameNewPFCollection, but applying puppi corrections.' 
			else: 
				proc.load('CommonTools.PileupAlgos.Puppi_cff')
				puppi.candName = cms.InputTag( pfCand ) 
				if miniAOD:
				  puppi.vertexName = cms.InputTag('offlineSlimmedPrimaryVertices')
				  puppi.clonePackedCands = cms.bool(True)
				jetSeq += getattr(proc, 'puppi' )
				srcForPFJets = 'puppi'

			from RecoJets.JetProducers.ak4PFJetsPuppi_cfi import ak4PFJetsPuppi
			setattr( proc, jetalgo+'PFJetsPuppi', 
					ak4PFJetsPuppi.clone( src = cms.InputTag( srcForPFJets ),
						doAreaFastjet = True, 
						rParam = jetSize, 
						jetAlgorithm = algorithm ) )  
			jetSeq += getattr(proc, jetalgo+'PFJetsPuppi' )

			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PFPuppi'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PFPuppi'

		elif 'SK' in PUMethod:

			if ('sk' in tmpPfCandName): 
				srcForPFJets = pfCand
				print '|---- jetToolBox: Not running softkiller algorithm because keyword SK was specified in nameNewPFCollection, but applying SK corrections.' 
			else:
				proc.load('CommonTools.PileupAlgos.softKiller_cfi')
				getattr( proc, 'softKiller' ).PFCandidates = cms.InputTag( pfCand ) 
				jetSeq += getattr(proc, 'softKiller' )
				srcForPFJets = 'softKiller'

			from RecoJets.JetProducers.ak4PFJetsSK_cfi import ak4PFJetsSK
			setattr( proc, jetalgo+'PFJetsSK', 
					ak4PFJetsSK.clone(  src = cms.InputTag( srcForPFJets ),
						rParam = jetSize, 
						jetAlgorithm = algorithm ) ) 
			jetSeq += getattr(proc, jetalgo+'PFJetsSK' )

			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PFSK'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PFSK'
		
		elif 'CS' in PUMethod: 

			from RecoJets.JetProducers.ak4PFJetsCHSCS_cfi import ak4PFJetsCHSCS
			setattr( proc, jetalgo+'PFJetsCS', 
					ak4PFJetsCHSCS.clone( doAreaFastjet = True, 
						src = cms.InputTag( pfCand ), #srcForPFJets ),
						csRParam = cms.double(jetSize),
						jetAlgorithm = algorithm ) ) 
			if miniAOD: getattr( proc, jetalgo+'PFJetsCS').src = pfCand
			jetSeq += getattr(proc, jetalgo+'PFJetsCS' )

			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PFCS'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PFCS'

		elif 'CHS' in PUMethod: 
			
			if miniAOD:
				if ('chs' in tmpPfCandName): 
					srcForPFJets = pfCand
					print '|---- jetToolBox: Not running CHS algorithm because keyword CHS was specified in nameNewPFCollection, but applying CHS corrections.' 
				else: 
					setattr( proc, 'chs', cms.EDFilter('CandPtrSelector', src = cms.InputTag( pfCand ), cut = cms.string('fromPV')) )
					jetSeq += getattr(proc, 'chs')
					srcForPFJets = 'chs'
			else:
				if ( pfCand == 'particleFlow' ):
					from RecoParticleFlow.PFProducer.particleFlowTmpPtrs_cfi import particleFlowTmpPtrs
					setattr( proc, 'newParticleFlowTmpPtrs', particleFlowTmpPtrs.clone( src = pfCand ) )
					jetSeq += getattr(proc, 'newParticleFlowTmpPtrs')
					from CommonTools.ParticleFlow.pfNoPileUpJME_cff import pfPileUpJME, pfNoPileUpJME
					proc.load('CommonTools.ParticleFlow.goodOfflinePrimaryVertices_cfi')
					setattr( proc, 'newPfPileUpJME', pfPileUpJME.clone( PFCandidates= 'newParticleFlowTmpPtrs' ) )
					jetSeq += getattr(proc, 'newPfPileUpJME')
					setattr( proc, 'newPfNoPileUpJME', pfNoPileUpJME.clone( topCollection='newPfPileUpJME', bottomCollection= 'newParticleFlowTmpPtrs' ) )
					jetSeq += getattr(proc, 'newPfNoPileUpJME')
					srcForPFJets = 'newPfNoPileUpJME'
				else: 
					proc.load('CommonTools.ParticleFlow.pfNoPileUpJME_cff')
					srcForPFJets = 'pfNoPileUpJME'
				
			setattr( proc, jetalgo+'PFJetsCHS', 
					ak4PFJetsCHS.clone( src = cms.InputTag( srcForPFJets ), 
						doAreaFastjet = True, 
						rParam = jetSize, 
						jetAlgorithm = algorithm ) ) 
			jetSeq += getattr(proc, jetalgo+'PFJetsCHS' )

			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PFchs'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PFchs'

		else: 
			PUMethod = ''
			setattr( proc, jetalgo+'PFJets', 
					ak4PFJets.clone( 
						doAreaFastjet = True, 
						rParam = jetSize, 
						jetAlgorithm = algorithm ) ) 
			if miniAOD: getattr( proc, jetalgo+'PFJets').src = pfCand
			jetSeq += getattr(proc, jetalgo+'PFJets' )
			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PF'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PF'


		if 'None' in JETCorrPayload: JEC = None
		else: JEC = ( JETCorrPayload.replace('CS','chs').replace('SK','chs') , JETCorrLevels, 'None' )   ### temporary
		#else: JEC = ( JETCorrPayload., JETCorrLevels, 'None' ) 
		print '|---- jetToolBox: Applying this corrections: '+str(JEC)

		if addPrunedSubjets or addSoftDropSubjets or addCMSTopTagger:
			if 'None' in subJETCorrPayload: subJEC = None
			else: subJEC = ( subJETCorrPayload.replace('CS','chs').replace('SK','chs') , subJETCorrLevels, 'None' )   ### temporary


		if ( PUMethod in [ 'CHS', 'CS', 'Puppi' ] ) and miniAOD: setattr( proc, jetalgo+'PFJets'+PUMethod+'Constituents', cms.EDFilter("MiniAODJetConstituentSelector", src = cms.InputTag( jetalgo+'PFJets'+PUMethod ), cut = cms.string( Cut ) ))
		else: setattr( proc, jetalgo+'PFJets'+PUMethod+'Constituents', cms.EDFilter("PFJetConstituentSelector", src = cms.InputTag( jetalgo+'PFJets'+PUMethod ), cut = cms.string( Cut ) ))
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Constituents' )

		addJetCollection(
				proc,
				labelName = jetALGO+'PF'+PUMethod,
				jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod),
				algo = jetalgo,
				rParam = jetSize,
				jetCorrections = JEC if JEC is not None else None, 
				pfCandidates = cms.InputTag( pfCand ),  
				svSource = cms.InputTag( svLabel ),  
				genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
				pvSource = cms.InputTag( pvLabel ), 
				muSource = cms.InputTag( muLabel ),
				elSource = cms.InputTag( elLabel ),
				btagDiscriminators = bTagDiscriminators,
				btagInfos = bTagInfos,
				getJetMCFlavour = GetJetMCFlavour,
				genParticles = cms.InputTag(genParticlesLabel),
				outputModules = ['outputFile']
				) 
		getattr(proc,'patJets'+jetALGO+'PF'+PUMethod).addTagInfos = cms.bool(True)

		if 'CS' in PUMethod: getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod ).getJetMCFlavour = False  # CS jets cannot be re-clustered from their constituents
		patJets = 'patJets'
	else:
		print '|---- jetToolBox: JETTOOLBOX IS UPDATING '+updateCollection+' collection'
		genParticlesLabel = 'prunedGenParticles'
		pvLabel = 'offlineSlimmedPrimaryVertices'
		svLabel = 'slimmedSecondaryVertices'
		tvLabel = 'unpackedTracksAndVertices'
		muLabel = 'slimmedMuons'
		elLabel = 'slimmedElectrons'

		if not JETCorrPayload: 
			print '|---- jetToolBox: updateCollection option requires to add JETCorrPayload.'
			print '|---- jetToolBox: EXITING.'
			return None
		if 'Puppi' in updateCollection: PUMethod='Puppi'
		JEC = ( JETCorrPayload, JETCorrLevels, 'None' )   ### temporary
		print '|---- jetToolBox: Applying this corrections: '+str(JEC)
		updateJetCollection(
				proc,
				jetSource = cms.InputTag( updateCollection ),
				labelName = jetALGO+'PF'+PUMethod,
				jetCorrections = JEC, 
				btagDiscriminators = bTagDiscriminators,
				)
		getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod ).payload = JETCorrPayload
		getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod ).levels = JETCorrLevels
		if bTagDiscriminators: print '|---- jetToolBox: Adding this bTagDiscriminators: '+str(bTagDiscriminators)+' in the jet collection.'
		patJets = 'updatedPatJets'

		if updateCollectionSubjets:
			print '|---- jetToolBox: JETTOOLBOX IS UPDATING '+updateCollectionSubjets+' collection for subjets/groomers.'
			if 'SoftDrop' in updateCollectionSubjets: updateSubjetLabel = 'SoftDrop'
			else: updateSubjetLabel = 'Pruned'
			updateJetCollection(
					proc,
					jetSource = cms.InputTag( updateCollectionSubjets ),
					labelName = jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed',
					jetCorrections = JEC, 
					explicitJTA = True,
					fatJets = cms.InputTag( updateCollection ),
					rParam = jetSize, 
					algo = jetALGO,
					btagDiscriminators = bTagDiscriminators,
					)
			getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed' ).payload = subJETCorrPayload
			getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed' ).levels = subJETCorrLevels
			patSubJets = 'updatedPatJets'+jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed'
			if bTagDiscriminators: print '|---- jetToolBox: Adding this bTagDiscriminators: '+str(bTagDiscriminators)+' in the subjet collection.'

		if addPrunedSubjets: 
			addPrunedSubjets = False
			print '|---- jetToolBox: It does not support addPrunedSubjets with updateCollection option for now. Disabling addPrunedSubjets.'
		if addSoftDropSubjets: 
			addSoftDropSubjets = False
			print '|---- jetToolBox: It does not support addSoftDropSubjets with updateCollection option for now. Disabling addSoftDropSubjets.'
		if addCMSTopTagger: 
			addCMSTopTagger = False
			print '|---- jetToolBox: It does not support addCMSTopTagger with updateCollection option for now. Disabling addCMSTopTagger.'
		if addMassDrop: 
			addMassDrop = False
			print '|---- jetToolBox: It does not support addMassDrop with updateCollection option for now. Disabling addMassDrop.'
		if addHEPTopTagger: 
			addHEPTopTagger = False
			print '|---- jetToolBox: It does not support addHEPTopTagger with updateCollection option for now. Disabling addHEPTopTagger.'
	
	#### Groomers
	if addSoftDrop or addSoftDropSubjets: 

		setattr( proc, jetalgo+'PFJets'+PUMethod+'SoftDrop', 
			ak8PFJetsCHSSoftDrop.clone( 
				src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
				rParam = jetSize, 
				jetAlgorithm = algorithm, 
				useExplicitGhosts=True,
				R0= cms.double(jetSize),
				zcut=zCutSD, 
				beta=betaCut,
				doAreaFastjet = cms.bool(True),
				writeCompound = cms.bool(True),
				jetCollInstanceName=cms.string('SubJets') ) )
		setattr( proc, jetalgo+'PFJets'+PUMethod+'SoftDropMass', 
			ak8PFJetsCHSSoftDropMass.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ), 
				matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'SoftDrop'), 
				distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'SoftDropMass_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'SoftDrop' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'SoftDropMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'SoftDropMass']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'SoftDropMass' )

		if addSoftDropSubjets:

			if runOnMC:
				setattr( proc, jetalgo+'GenJetsNoNuSoftDrop',
						ak4GenJets.clone(
							SubJetParameters,
							useSoftDrop = cms.bool(True),
							rParam = jetSize, 
							jetAlgorithm = algorithm, 
							useExplicitGhosts=cms.bool(True),
							#zcut=cms.double(zCutSD), 
							R0= cms.double(jetSize),
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
					jetCorrections = JEC if JEC is not None else None, 
					pvSource = cms.InputTag( pvLabel ),
					btagDiscriminators = ['None'],
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
					getJetMCFlavour = False, # jet flavor should always be disabled for groomed jets
					genParticles = cms.InputTag(genParticlesLabel),
					outputModules = ['outputFile']
					) 

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDrop', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+'SoftDrop', cut = Cut ) )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+'SoftDropSubjets',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+'SoftDrop', 'SubJets'),
					algo = jetalgo,  # needed for subjet b tagging
					rParam = jetSize,  # needed for subjet b tagging
					jetCorrections = subJEC if subJEC is not None else None, 
					pfCandidates = cms.InputTag( pfCand ), 
					pvSource = cms.InputTag( pvLabel), 
					svSource = cms.InputTag( svLabel ),  
					muSource = cms.InputTag( muLabel ),
					elSource = cms.InputTag( elLabel ),
					btagDiscriminators = bTagDiscriminators,
					btagInfos = bTagInfos,
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNuSoftDrop','SubJets'),
					getJetMCFlavour = GetSubjetMCFlavour,
					genParticles = cms.InputTag(genParticlesLabel),
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod+'SoftDrop'), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+'SoftDropSubjets', cut = CutSubjet ))
			getattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropSubjets').addTagInfos = cms.bool(True)

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

                        ## Pack fat jets with subjets
			setattr( proc, 'packedPatJets'+jetALGO+'PF'+PUMethod, 
				 cms.EDProducer("JetSubstructurePacker",
						jetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod),
						distMax = cms.double(0.8),
						fixDaughters = cms.bool(False),
						algoTags = cms.VInputTag(
						cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+'SoftDropPacked')
						), 
						algoLabels =cms.vstring('SoftDrop'
									)
						)
				 )
			jetSeq += getattr(proc, 'packedPatJets'+jetALGO+'PF'+PUMethod)
			elemToKeep += [ 'keep *_packedPatJets'+jetALGO+'PF'+PUMethod+'_*_*' ]
			toolsUsed.append( 'packedPatJets'+jetALGO+'PF'+PUMethod )



	if addPruning or addPrunedSubjets: 

		setattr( proc, jetalgo+'PFJets'+PUMethod+'Pruned', 
			ak8PFJetsCHSPruned.clone( 
				src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
				rParam = jetSize, 
				jetAlgorithm = algorithm, 
				zcut=zCut, 
				rcut_factor=rCut,
				writeCompound = cms.bool(True),
				doAreaFastjet = cms.bool(True),
				jetCollInstanceName=cms.string('SubJets') ) )
		setattr( proc, jetalgo+'PFJets'+PUMethod+'PrunedMass', 
			ak8PFJetsCHSPrunedMass.clone( #src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ), 
				matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Pruned'), 
				distMax = cms.double( jetSize ) ) )

		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Pruned' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'PrunedMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'PrunedMass']
		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'PrunedMass_*_*'] 
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'PrunedMass' )

		if addPrunedSubjets:
			if runOnMC:
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
					jetCorrections = JEC if JEC is not None else None, 
					pvSource = cms.InputTag( pvLabel ),
					btagDiscriminators = ['None'],
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
					getJetMCFlavour = False, # jet flavor should always be disabled for groomed jets
					genParticles = cms.InputTag(genParticlesLabel),
					outputModules = ['outputFile']
					) 

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'Pruned', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+'Pruned', cut = Cut ) )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+'PrunedSubjets',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Pruned', 'SubJets'),
					algo = jetalgo,  # needed for subjet b tagging
					rParam = jetSize,  # needed for subjet b tagging
					jetCorrections = subJEC if subJEC is not None else None, 
					pfCandidates = cms.InputTag( pfCand ),  
					pvSource = cms.InputTag( pvLabel), 
					svSource = cms.InputTag( svLabel ), 
					muSource = cms.InputTag( muLabel ),
					elSource = cms.InputTag( elLabel ),
					getJetMCFlavour = GetSubjetMCFlavour,
					genParticles = cms.InputTag(genParticlesLabel),
					btagDiscriminators = bTagDiscriminators,
					btagInfos = bTagInfos,
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNuPruned','SubJets'),
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod+'Pruned'), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+'PrunedSubjets', cut = CutSubjet ) )
			getattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+'PrunedSubjets').addTagInfos = cms.bool(True)

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
				ak8PFJetsCHSTrimmed.clone( 
					rParam = jetSize, 
					src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
					jetAlgorithm = algorithm,
					rFilt= rFiltTrim,
					trimPtFracMin= ptFrac) ) 
		setattr( proc, jetalgo+'PFJets'+PUMethod+'TrimmedMass', 
				ak8PFJetsCHSTrimmedMass.clone( 
					src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ), 
					matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Trimmed'), 
					distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'TrimmedMass_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Trimmed' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'TrimmedMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'TrimmedMass']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'TrimmedMass' )

	if addFiltering:

		setattr( proc, jetalgo+'PFJets'+PUMethod+'Filtered', 
				ak8PFJetsCHSFiltered.clone( 
					src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
					rParam = jetSize, 
					jetAlgorithm = algorithm,
					rFilt= rfilt,
					nFilt= nfilt ) ) 
		setattr( proc, jetalgo+'PFJets'+PUMethod+'FilteredMass', 
				ak8PFJetsCHSFilteredMass.clone( 
					src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ), 
					matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+'Filtered'), 
					distMax = cms.double( jetSize ) ) )
		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'FilteredMass_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'Filtered' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'FilteredMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'FilteredMass']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'FilteredMass' )

	if addCMSTopTagger :

		if 'CA' in jetALGO : 

			setattr( proc, 'cmsTopTagPFJets'+PUMethod,  
					cms.EDProducer("CATopJetProducer",
						PFJetParameters.clone( 
							src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
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
					jetCorrections = JEC if JEC is not None else None, 
					pfCandidates = cms.InputTag( pfCand ),  
					pvSource = cms.InputTag( pvLabel), 
					svSource = cms.InputTag( svLabel ), 
					muSource = cms.InputTag( muLabel ),
					elSource = cms.InputTag( elLabel ),
					btagDiscriminators = bTagDiscriminators,
					btagInfos = bTagInfos,
					genJetCollection = cms.InputTag(jetalgo+'GenJetsNoNu'),
					getJetMCFlavour = False, # jet flavor should always be disabled for groomed jets
					genParticles = cms.InputTag(genParticlesLabel)
					)
			getattr(proc,'patJetsCMSTopTag'+PUMethod).addTagInfos = True
			getattr(proc,'patJetsCMSTopTag'+PUMethod).tagInfoSources = cms.VInputTag( cms.InputTag('CATopTagInfos'))
			setattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod, selectedPatJets.clone( src = 'patJetsCMSTopTag'+PUMethod, cut = Cut ) )

			addJetCollection(
					proc,
					labelName = 'CMSTopTag'+PUMethod+'Subjets',
					jetSource = cms.InputTag('cmsTopTagPFJets'+PUMethod, 'SubJets'),
					algo = jetalgo,  # needed for subjet b tagging
					rParam = jetSize,  # needed for subjet b tagging
					jetCorrections = subJEC if subJEC is not None else None, 
					pfCandidates = cms.InputTag( pfCand ),  
					pvSource = cms.InputTag( pvLabel), 
					svSource = cms.InputTag( svLabel ), 
					muSource = cms.InputTag( muLabel ),
					elSource = cms.InputTag( elLabel ),
					btagDiscriminators = bTagDiscriminators,
					btagInfos = bTagInfos,
					genJetCollection = cms.InputTag( jetalgo+'GenJetsNoNu'),
					getJetMCFlavour = GetSubjetMCFlavour,
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag('patJetsCMSTopTag'+PUMethod), # needed for subjet flavor clustering
					genParticles = cms.InputTag(genParticlesLabel)
					)

			setattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod+'Subjets', selectedPatJets.clone( src = 'patJetsCMSTopTag'+PUMethod+'Subjets', cut = Cut ) )
			getattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod+'Subjets' ).addTagInfos = cms.bool(True)

			setattr( proc, 'patJetsCMSTopTag'+PUMethod+'Packed', 
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag('patJetsCMSTopTag'+PUMethod ),
						subjetSrc=cms.InputTag('patJetsCMSTopTag'+PUMethod+'Subjets')
						))
			jetSeq += getattr(proc, 'patJetsCMSTopTag'+PUMethod+'Packed' )
			elemToKeep += [ 'keep *_patJetsCMSTopTag'+PUMethod+'Packed_*_*' ]
			toolsUsed.append( 'patJetsCMSTopTag'+PUMethod+'Packed' )

		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for CMS Top Tagger, you are using '+algorithm+'. JetToolbox will not run CMS Top Tagger.'

	if addMassDrop :

		if 'CA' in jetALGO : 
			setattr( proc, jetalgo+'PFJets'+PUMethod+'MassDropFiltered', 
					ca15PFJetsCHSMassDropFiltered.clone( 
						rParam = jetSize,
						src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
						) )
			setattr( proc, jetalgo+'PFJets'+PUMethod+'MassDropFilteredMass', ak8PFJetsCHSPrunedMass.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				matched = cms.InputTag(jetalgo+'PFJets'+PUMethod+'MassDropFiltered'), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'MassDropFilteredMass_*_*' ]
			getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'MassDropFilteredMass' ]
			jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'MassDropFiltered' )
			jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'MassDropFilteredMass' )
		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for Mass Drop, you are using '+algorithm+'. JetToolbox will not run Mass Drop.'
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'MassDropFilteredMass' )

	if addHEPTopTagger: 
		if ( jetSize >= 1. ) and ( 'CA' in jetALGO ): 

			setattr( proc, 'hepTopTagPFJets'+PUMethod, hepTopTagPFJetsCHS.clone( src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ) ) )
			setattr( proc, 'hepTopTagPFJets'+PUMethod+'Mass'+jetALGO, ak8PFJetsCHSPrunedMass.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				matched = cms.InputTag("hepTopTagPFJets"+PUMethod), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_hepTopTagPFJets'+PUMethod+'Mass'+jetALGO+'_*_*' ]
			getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ 'hepTopTagPFJets'+PUMethod+'Mass'+jetALGO ]
			jetSeq += getattr(proc, 'hepTopTagPFJets'+PUMethod )
			jetSeq += getattr(proc, 'hepTopTagPFJets'+PUMethod+'Mass'+jetALGO )
			toolsUsed.append( 'hepTopTagPFJets'+PUMethod+'Mass'+jetALGO )
		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for HEPTopTagger, you are using '+algorithm+', and a jet cone size bigger than 1. JetToolbox will not run HEP TopTagger.'

	####### Nsubjettiness
	if addNsub:
		from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

		rangeTau = range(1,maxTau+1)
		setattr( proc, 'Njettiness'+jetALGO+PUMethod, 
				Njettiness.clone( src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),
					Njets=cms.vuint32(rangeTau),         # compute 1-, 2-, 3-, 4- subjettiness
					# variables for measure definition : 
					measureDefinition = cms.uint32( 0 ), # CMS default is normalized measure
					beta = cms.double(1.0),              # CMS default is 1
					R0 = cms.double( jetSize ),              # CMS default is jet cone size
					Rcutoff = cms.double( 999.0),       # not used by default
					# variables for axes definition :
					axesDefinition = cms.uint32( 6 ),    # CMS default is 1-pass KT axes
					nPass = cms.int32(999),             # not used by default
					akAxesR0 = cms.double(-999.0) ) )        # not used by default

		elemToKeep += [ 'keep *_Njettiness'+jetALGO+PUMethod+'_*_*' ]
		for tau in rangeTau: getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += ['Njettiness'+jetALGO+PUMethod+':tau'+str(tau) ] 
		jetSeq += getattr(proc, 'Njettiness'+jetALGO+PUMethod )
		toolsUsed.append( 'Njettiness'+jetALGO+PUMethod )

	####### Nsubjettiness
	if addNsubSubjets:

		from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

		#if addPrunedSubjets or addSoftDropSubjets:
		groomer = ''
		if addSoftDropSubjets: groomer = 'SoftDrop'
		elif addPrunedSubjets: groomer = 'Pruned'
		elif updateCollectionSubjets: 
			groomer = 'SoftDrop'
                        print '|---- jetToolBox: Using updateCollection option. ASSUMING MINIAOD collection '+ updateCollectionSubjets +' for Nsubjectiness of subjets.'
		else: 
                        print '|---- jetToolBox: Nsubjetiness of subjets needs a Subjet collection. Or create one using addSoftDropSubjets option, or updateCollection.'

			return None
		typeSubjetColl = jetALGO+'PF'+PUMethod+groomer+'Subjets'
		rangeTau = range(1,subjetMaxTau+1)
		setattr( proc, 'Nsubjettiness'+typeSubjetColl, 
				Njettiness.clone( src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+groomer if not updateCollectionSubjets else updateCollectionSubjets ), 'SubJets' ), 
					Njets=cms.vuint32(rangeTau),         # compute 1-, 2-, 3-, 4- subjettiness
					# variables for measure definition : 
					measureDefinition = cms.uint32( 0 ), # CMS default is normalized measure
					beta = cms.double(1.0),              # CMS default is 1
					R0 = cms.double( jetSize ),              # CMS default is jet cone size
					Rcutoff = cms.double( 999.0),       # not used by default
					# variables for axes definition :
					axesDefinition = cms.uint32( 6 ),    # CMS default is 1-pass KT axes
					nPass = cms.int32(999),             # not used by default
					akAxesR0 = cms.double(-999.0) ) )        # not used by default

		elemToKeep += [ 'keep *_Nsubjettiness'+typeSubjetColl+'_*_*' ]
		for tau in rangeTau: getattr( proc, ( 'patJets'+typeSubjetColl if not updateCollectionSubjets else patSubJets ) ).userData.userFloats.src += ['Nsubjettiness'+typeSubjetColl+':tau'+str(tau) ] 
		jetSeq += getattr(proc, 'Nsubjettiness'+typeSubjetColl )
		toolsUsed.append( 'Nsubjettiness'+typeSubjetColl )

	###### QJetsAdder
	'''
	if addQJets:
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
		getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += ['QJetsAdder'+jetALGO+':QjetsVolatility']  
		jetSeq += getattr(proc, 'QJetsAdder'+jetALGO )
		toolsUsed.append( 'QJetsAdder'+jetALGO )
	'''

	###### QGTagger
	if addQGTagger:
		if ( 'ak4' in jetalgo ) and ( PUMethod not in ['Puppi','CS','SK'] ) :
			from RecoJets.JetProducers.QGTagger_cfi import QGTagger
			proc.load('RecoJets.JetProducers.QGTagger_cfi') 	## In 74X you need to run some stuff before.
			setattr( proc, 'QGTagger'+jetALGO+'PF'+PUMethod, 
					QGTagger.clone(
						srcJets = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),    # Could be reco::PFJetCollection or pat::JetCollection (both AOD and miniAOD)
						jetsLabel = cms.string('QGL_AK4PF'+QGjetsLabel)        # Other options (might need to add an ESSource for it): see https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion
						)
					)
			elemToKeep += [ 'keep *_QGTagger'+jetALGO+'PF'+PUMethod+'_*_*' ]
			getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += ['QGTagger'+jetALGO+'PF'+PUMethod+':qgLikelihood']  
			jetSeq += getattr(proc, 'QGTagger'+jetALGO+'PF'+PUMethod )

                        toolsUsed.append( 'QGTagger'+jetALGO+'PF'+PUMethod )
		else:
			print '|---- jetToolBox: QGTagger is optimized for ak4 jets with CHS. NOT running QGTagger'

			
	####### Pileup JetID
        if addPUJetID:
                if ( 'ak4' in jetalgo ) and ( PUMethod not in ['CS','SK'] ):
		        if PUMethod=="Puppi": print '|---- jetToolBox: PUJetID is not yet optimized for ak4 PFjets with PUPPI. USE ONLY FOR TESTING.'
                        from RecoJets.JetProducers.pileupjetidproducer_cfi import pileupJetIdCalculator,pileupJetIdEvaluator

			setattr( proc, jetALGO+'PF'+PUMethod+'pileupJetIdCalculator',
					pileupJetIdCalculator.clone(
						jets = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),
						rho = cms.InputTag("fixedGridRhoFastjetAll"),
						vertexes = cms.InputTag(pvLabel),
						applyJec = cms.bool(True),
						inputIsCorrected = cms.bool(False)
						))

			setattr( proc, jetALGO+'PF'+PUMethod+'pileupJetIdEvaluator',
					pileupJetIdEvaluator.clone(
						jetids = cms.InputTag(jetALGO+'PF'+PUMethod+'pileupJetIdCalculator'),
						jets = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),
						rho = cms.InputTag("fixedGridRhoFastjetAll"),
						vertexes = cms.InputTag(pvLabel)
						)
					)

                        getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [jetALGO+'PF'+PUMethod+'pileupJetIdEvaluator:fullDiscriminant']
                        getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userInts.src += [jetALGO+'PF'+PUMethod+'pileupJetIdEvaluator:cutbasedId',jetALGO+'PF'+PUMethod+'pileupJetIdEvaluator:fullId']
                        elemToKeep += ['keep *_'+jetALGO+'PF'+PUMethod+'pileupJetIdEvaluator_*_*']
                        toolsUsed.append( jetALGO+'PF'+PUMethod+'pileupJetIdEvaluator' )
		else:
                        print '|---- jetToolBox: PUJetID is optimized for ak4 PFjets with CHS. NOT running PUJetID.'

	###### Energy Correlation Functions
	if addEnergyCorrFunc:
		from RecoJets.JetProducers.ECF_cfi import ECF 
		rangeECF = range(1,maxECF+1)
		setattr( proc, jetalgo+'PFJets'+PUMethod+'ECF', ECF.clone(
				src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),
				Njets = cms.vuint32( rangeECF ),
				beta = cms.double( ecfBeta ) 
				))

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+'ECF_*_*'] 
		for ecf in rangeECF: getattr( proc, patJets+jetALGO+'PF'+PUMethod).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+'ECF:ecf'+str(ecf) ]
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+'ECF' )
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+'ECF' )
	
	if hasattr(proc, 'patJetPartons'): proc.patJetPartons.particles = genParticlesLabel


	setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod, selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod, cut = Cut ) )
	elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+'_*_*' ]
	elemToKeep += [ 'drop *_selectedPatJets'+jetALGO+'PF'+PUMethod+'_calo*_*' ]
	elemToKeep += [ 'drop *_selectedPatJets'+jetALGO+'PF'+PUMethod+'_tagInfos_*' ]

	if updateCollectionSubjets: 
		setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed', cut = Cut ) )
		elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed__*' ]


	if len(toolsUsed) > 0 : print '|---- jetToolBox: Running '+', '.join(toolsUsed)+'.'
	print '|---- jetToolBox: Creating selectedPatJets'+jetALGO+'PF'+PUMethod+' collection.'
	if updateCollectionSubjets: print '|---- jetToolBox: Creating selectedPatJets'+jetALGO+'PF'+PUMethod+updateSubjetLabel+'Packed collection.'

	### "return"
	setattr(proc, jetSequence, jetSeq)
	if hasattr(proc, outputFile): getattr(proc, outputFile).outputCommands += elemToKeep
	else: setattr( proc, outputFile, 
			cms.OutputModule('PoolOutputModule', 
				fileName = cms.untracked.string('jettoolbox.root'), 
				outputCommands = cms.untracked.vstring( elemToKeep ) ) )

	if runOnData:
		from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
		removeMCMatching(proc, names=['Jets'], outputModules=[outputFile])
