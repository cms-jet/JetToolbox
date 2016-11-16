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
		postFix='',
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
	recommendedJetAlgos = [ 'ak4', 'ak8', 'ca4', 'ca8', 'ca10', 'ca15' ]
	payloadList = [ 'None',
			'AK1PFchs', 'AK2PFchs', 'AK3PFchs', 'AK4PFchs', 'AK5PFchs', 'AK6PFchs', 'AK7PFchs', 'AK8PFchs', 'AK9PFchs', 'AK10PFchs',
			'AK1PFPuppi', 'AK2PFPuppi', 'AK3PFPuppi', 'AK4PFPuppi', 'AK5PFPuppi', 'AK6PFPuppi', 'AK7PFPuppi', 'AK8PFPuppi', 'AK9PFPuppi', 'AK10PFPuppi',  
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
				postfix = postFix, 
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
		getattr(proc,'patJets'+jetALGO+'PF'+PUMethod+postFix).addTagInfos = cms.bool(True)

		if 'CS' in PUMethod: getattr( proc, 'patJets'+jetALGO+'PF'+PUMethod+postFix ).getJetMCFlavour = False  # CS jets cannot be re-clustered from their constituents
		patJets = 'patJets'
		patSubJets = ''
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
				postfix = postFix,
				jetSource = cms.InputTag( updateCollection ),
				labelName = jetALGO+'PF'+PUMethod,
				jetCorrections = JEC, 
				btagDiscriminators = bTagDiscriminators,
				)
		getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+postFix ).payload = JETCorrPayload
		getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+postFix ).levels = JETCorrLevels
		if bTagDiscriminators: print '|---- jetToolBox: Adding this bTagDiscriminators: '+str(bTagDiscriminators)+' in the jet collection.'
		patJets = 'updatedPatJets'
		patSubJets = ''

		if updateCollectionSubjets:
			print '|---- jetToolBox: JETTOOLBOX IS UPDATING '+updateCollectionSubjets+' collection for subjets/groomers.'
			if 'SoftDrop' in updateCollectionSubjets: updateSubjetLabel = 'SoftDrop'
			else: updateSubjetLabel = 'Pruned'
			updateJetCollection(
					proc,
					jetSource = cms.InputTag( updateCollectionSubjets ),
					labelName = jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed',
					jetCorrections = JEC, 
					explicitJTA = True,
					fatJets = cms.InputTag( updateCollection ),
					rParam = jetSize, 
					algo = jetALGO,
					btagDiscriminators = bTagDiscriminators,
					)
			getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed' ).payload = subJETCorrPayload
			getattr( proc, 'patJetCorrFactors'+jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed' ).levels = subJETCorrLevels
			patSubJets = 'updatedPatJets'+jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed'
			if bTagDiscriminators: print '|---- jetToolBox: Adding this bTagDiscriminators: '+str(bTagDiscriminators)+' in the subjet collection.'

		if addPrunedSubjets or addSoftDropSubjets or addCMSTopTagger or addMassDrop or addHEPTopTagger or addPruning or addSoftDrop: 
			print '|---- jetToolBox: You are trying to add a groomer variable into a clustered jet collection. THIS IS NOT RECOMMENDED, it is recommended to recluster jets instead using a plain jetToolbox configuration. Please use this feature by your own risk.'
	
	#### Groomers
	if addSoftDrop or addSoftDropSubjets: 

		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'SoftDrop', 
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
		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'SoftDropMass', 
			ak8PFJetsCHSSoftDropMass.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ), 
				matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'SoftDrop'), 
				distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+postFix+'SoftDropMass_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'SoftDrop' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'SoftDropMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+postFix+'SoftDropMass']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+postFix+'SoftDropMass' )

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
					labelName = jetALGO+'PF'+PUMethod+postFix+'SoftDrop',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'SoftDrop'),
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

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDrop', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+postFix+'SoftDrop', cut = Cut ) )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+postFix+'SoftDropSubjets',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'SoftDrop', 'SubJets'),
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
					groomedFatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod+postFix+'SoftDrop'), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropSubjets', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+postFix+'SoftDropSubjets', cut = CutSubjet ))
			getattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropSubjets').addTagInfos = cms.bool(True)

			# Establish references between PATified fat jets and subjets using the BoostedJetMerger
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropPacked', 
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDrop'),
						subjetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropSubjets')
						))
			jetSeq += getattr(proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropPacked' )
			elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropPacked_SubJets_*' ]
			toolsUsed.append( 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropPacked:SubJets' )

                        ## Pack fat jets with subjets
			setattr( proc, 'packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDrop', 
				 cms.EDProducer("JetSubstructurePacker",
						jetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix),
						distMax = cms.double( jetSize ),
						fixDaughters = cms.bool(False),
						algoTags = cms.VInputTag(
						cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDropPacked')
						), 
						algoLabels =cms.vstring('SoftDrop')
						)
				 )
			jetSeq += getattr(proc, 'packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDrop')
			elemToKeep += [ 'keep *_packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDrop_*_*' ]
			print '|---- jetToolBox: Creating packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'SoftDrop collection with SoftDrop subjets.'



	if addPruning or addPrunedSubjets: 

		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'Pruned', 
			ak8PFJetsCHSPruned.clone( 
				src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
				rParam = jetSize, 
				jetAlgorithm = algorithm, 
				zcut=zCut, 
				rcut_factor=rCut,
				writeCompound = cms.bool(True),
				doAreaFastjet = cms.bool(True),
				jetCollInstanceName=cms.string('SubJets') ) )
		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'PrunedMass', 
			ak8PFJetsCHSPrunedMass.clone( 
				src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ), 
				matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'Pruned'), 
				distMax = cms.double( jetSize ) ) )

		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'Pruned' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'PrunedMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+postFix+'PrunedMass']
		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+postFix+'PrunedMass_*_*'] 
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+postFix+'PrunedMass' )

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
					labelName = jetALGO+'PF'+PUMethod+postFix+'Pruned',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'Pruned'),
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

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'Pruned', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+postFix+'Pruned', cut = Cut ) )

			addJetCollection(
					proc,
					labelName = jetALGO+'PF'+PUMethod+postFix+'PrunedSubjets',
					jetSource = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'Pruned', 'SubJets'),
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
					groomedFatJets=cms.InputTag(jetalgo+'PFJets'+PUMethod+postFix+'Pruned'), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 

			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedSubjets', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+postFix+'PrunedSubjets', cut = CutSubjet ) )
			getattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedSubjets').addTagInfos = cms.bool(True)

			## Establish references between PATified fat jets and subjets using the BoostedJetMerger
			setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedPacked', 
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'Pruned'),
						subjetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedSubjets')
						))
			jetSeq += getattr(proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedPacked' )
			elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedPacked_SubJets_*' ]
			toolsUsed.append( 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedPacked:SubJets' )

                        ## Pack fat jets with subjets
			setattr( proc, 'packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'Pruned', 
				 cms.EDProducer("JetSubstructurePacker",
						jetSrc=cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix),
						distMax = cms.double( jetSize ),
						fixDaughters = cms.bool(False),
						algoTags = cms.VInputTag(
						cms.InputTag('selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'PrunedPacked')
						), 
						algoLabels =cms.vstring('Pruned')
						)
				 )
			jetSeq += getattr(proc, 'packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'Pruned')
			elemToKeep += [ 'keep *_packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'Pruned_*_*' ]
			print '|---- jetToolBox: Creating packedPatJets'+jetALGO+'PF'+PUMethod+postFix+'Pruned collection with Pruned subjets.'


	if addTrimming:

		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'Trimmed', 
				ak8PFJetsCHSTrimmed.clone( 
					rParam = jetSize, 
					src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
					jetAlgorithm = algorithm,
					rFilt= rFiltTrim,
					trimPtFracMin= ptFrac) ) 
		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'TrimmedMass', 
				ak8PFJetsCHSTrimmedMass.clone( 
					src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ), 
					matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'Trimmed'), 
					distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+postFix+'TrimmedMass_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'Trimmed' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'TrimmedMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+postFix+'TrimmedMass']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+postFix+'TrimmedMass' )

	if addFiltering:

		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'Filtered', 
				ak8PFJetsCHSFiltered.clone( 
					src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
					rParam = jetSize, 
					jetAlgorithm = algorithm,
					rFilt= rfilt,
					nFilt= nfilt ) ) 
		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'FilteredMass', 
				ak8PFJetsCHSFilteredMass.clone( 
					src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ), 
					matched = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix+'Filtered'), 
					distMax = cms.double( jetSize ) ) )
		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+postFix+'FilteredMass_*_*'] 
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'Filtered' )
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'FilteredMass' )
		getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+postFix+'FilteredMass']
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+postFix+'FilteredMass' )

	if addCMSTopTagger :

		if 'CA' in jetALGO : 

			setattr( proc, 'cmsTopTagPFJets'+PUMethod+postFix,  
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
						src = cms.InputTag('cmsTopTagPFJets'+PUMethod+postFix),
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
					labelName = 'CMSTopTag'+PUMethod+postFix,
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
			getattr(proc,'patJetsCMSTopTag'+PUMethod+postFix).addTagInfos = True
			getattr(proc,'patJetsCMSTopTag'+PUMethod+postFix).tagInfoSources = cms.VInputTag( cms.InputTag('CATopTagInfos'))
			setattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod+postFix, selectedPatJets.clone( src = 'patJetsCMSTopTag'+PUMethod+postFix, cut = Cut ) )

			addJetCollection(
					proc,
					labelName = 'CMSTopTag'+PUMethod+postFix+'Subjets',
					jetSource = cms.InputTag('cmsTopTagPFJets'+PUMethod+postFix, 'SubJets'),
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
					groomedFatJets=cms.InputTag('patJetsCMSTopTag'+PUMethod+postFix), # needed for subjet flavor clustering
					genParticles = cms.InputTag(genParticlesLabel)
					)

			setattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod+postFix+'Subjets', selectedPatJets.clone( src = 'patJetsCMSTopTag'+PUMethod+postFix+'Subjets', cut = Cut ) )
			getattr( proc, 'selectedPatJetsCMSTopTag'+PUMethod+postFix+'Subjets' ).addTagInfos = cms.bool(True)

			setattr( proc, 'patJetsCMSTopTag'+PUMethod+postFix+'Packed', 
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag('patJetsCMSTopTag'+PUMethod+postFix ),
						subjetSrc=cms.InputTag('patJetsCMSTopTag'+PUMethod+postFix+'Subjets')
						))
			jetSeq += getattr(proc, 'patJetsCMSTopTag'+PUMethod+postFix+'Packed' )
			elemToKeep += [ 'keep *_patJetsCMSTopTag'+PUMethod+postFix+'Packed_*_*' ]
			toolsUsed.append( 'patJetsCMSTopTag'+PUMethod+postFix+'Packed' )

		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for CMS Top Tagger, you are using '+algorithm+'. JetToolbox will not run CMS Top Tagger.'

	if addMassDrop :

		if 'CA' in jetALGO : 
			setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'MassDropFiltered', 
					ca15PFJetsCHSMassDropFiltered.clone( 
						rParam = jetSize,
						src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ),
						) )
			setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'MassDropFilteredMass', ak8PFJetsCHSPrunedMass.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod+postFix), 
				matched = cms.InputTag(jetalgo+'PFJets'+PUMethod+postFix+'MassDropFiltered'), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+postFix+'MassDropFilteredMass_*_*' ]
			getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+postFix+'MassDropFilteredMass' ]
			jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'MassDropFiltered' )
			jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'MassDropFilteredMass' )
		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for Mass Drop, you are using '+algorithm+'. JetToolbox will not run Mass Drop.'
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+postFix+'MassDropFilteredMass' )

	if addHEPTopTagger: 
		if ( jetSize >= 1. ) and ( 'CA' in jetALGO ): 

			setattr( proc, 'hepTopTagPFJets'+PUMethod+postFix, hepTopTagPFJetsCHS.clone( src = cms.InputTag( (jetalgo+'PFJets'+PUMethod+'Constituents:constituents' if not updateCollection else updateCollection ) ) ) )
			setattr( proc, 'hepTopTagPFJets'+PUMethod+postFix+'Mass'+jetALGO, ak8PFJetsCHSPrunedMass.clone( src = cms.InputTag( jetalgo+'PFJets'+PUMethod), 
				matched = cms.InputTag("hepTopTagPFJets"+PUMethod+postFix), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_hepTopTagPFJets'+PUMethod+postFix+'Mass'+jetALGO+'_*_*' ]
			getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [ 'hepTopTagPFJets'+PUMethod+postFix+'Mass'+jetALGO ]
			jetSeq += getattr(proc, 'hepTopTagPFJets'+PUMethod+postFix )
			jetSeq += getattr(proc, 'hepTopTagPFJets'+PUMethod+postFix+'Mass'+jetALGO )
			toolsUsed.append( 'hepTopTagPFJets'+PUMethod+postFix+'Mass'+jetALGO )
		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for HEPTopTagger, you are using '+algorithm+', and a jet cone size bigger than 1. JetToolbox will not run HEP TopTagger.'

	####### Nsubjettiness
	if addNsub:
		from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

		rangeTau = range(1,maxTau+1)
		setattr( proc, 'Njettiness'+jetALGO+PUMethod+postFix, 
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

		elemToKeep += [ 'keep *_Njettiness'+jetALGO+PUMethod+postFix+'_*_*' ]
		for tau in rangeTau: getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += ['Njettiness'+jetALGO+PUMethod+postFix+':tau'+str(tau) ] 
		jetSeq += getattr(proc, 'Njettiness'+jetALGO+PUMethod+postFix )
		toolsUsed.append( 'Njettiness'+jetALGO+PUMethod+postFix )

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
		typeSubjetColl = jetALGO+'PF'+PUMethod+postFix+groomer+'Subjets'
		rangeTau = range(1,subjetMaxTau+1)
		setattr( proc, 'Nsubjettiness'+typeSubjetColl, 
				Njettiness.clone( src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod+postFix+groomer if not updateCollectionSubjets else updateCollectionSubjets ), 'SubJets' ), 
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
			setattr( proc, 'QGTagger'+jetALGO+'PF'+PUMethod+postFix, 
					QGTagger.clone(
						srcJets = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),    # Could be reco::PFJetCollection or pat::JetCollection (both AOD and miniAOD)
						jetsLabel = cms.string('QGL_AK4PF'+QGjetsLabel)        # Other options (might need to add an ESSource for it): see https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion
						)
					)
			elemToKeep += [ 'keep *_QGTagger'+jetALGO+'PF'+PUMethod+postFix+'_*_*' ]
			getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += ['QGTagger'+jetALGO+'PF'+PUMethod+postFix+':qgLikelihood']  
			jetSeq += getattr(proc, 'QGTagger'+jetALGO+'PF'+PUMethod+postFix )

                        toolsUsed.append( 'QGTagger'+jetALGO+'PF'+PUMethod+postFix )
		else:
			print '|---- jetToolBox: QGTagger is optimized for ak4 jets with CHS. NOT running QGTagger'

			
	####### Pileup JetID
        if addPUJetID:
                if ( 'ak4' in jetalgo ) and ( PUMethod not in ['CS','SK'] ):
		        if PUMethod=="Puppi": print '|---- jetToolBox: PUJetID is not yet optimized for ak4 PFjets with PUPPI. USE ONLY FOR TESTING.'
                        from RecoJets.JetProducers.pileupjetidproducer_cfi import pileupJetIdCalculator,pileupJetIdEvaluator

			setattr( proc, jetALGO+'PF'+PUMethod+postFix+'pileupJetIdCalculator',
					pileupJetIdCalculator.clone(
						jets = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),
						rho = cms.InputTag("fixedGridRhoFastjetAll"),
						vertexes = cms.InputTag(pvLabel),
						applyJec = cms.bool(True),
						inputIsCorrected = cms.bool(False)
						))

			setattr( proc, jetALGO+'PF'+PUMethod+postFix+'pileupJetIdEvaluator',
					pileupJetIdEvaluator.clone(
						jetids = cms.InputTag(jetALGO+'PF'+PUMethod+postFix+'pileupJetIdCalculator'),
						jets = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),
						rho = cms.InputTag("fixedGridRhoFastjetAll"),
						vertexes = cms.InputTag(pvLabel)
						)
					)

                        getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [jetALGO+'PF'+PUMethod+postFix+'pileupJetIdEvaluator:fullDiscriminant']
                        getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userInts.src += [jetALGO+'PF'+PUMethod+postFix+'pileupJetIdEvaluator:cutbasedId',jetALGO+'PF'+PUMethod+postFix+'pileupJetIdEvaluator:fullId']
                        elemToKeep += ['keep *_'+jetALGO+'PF'+PUMethod+postFix+'pileupJetIdEvaluator_*_*']
                        toolsUsed.append( jetALGO+'PF'+PUMethod+postFix+'pileupJetIdEvaluator' )
		else:
                        print '|---- jetToolBox: PUJetID is optimized for ak4 PFjets with CHS. NOT running PUJetID.'

	###### Energy Correlation Functions
	if addEnergyCorrFunc:
		from RecoJets.JetProducers.ECF_cfi import ECF 
		rangeECF = range(1,maxECF+1)
		setattr( proc, jetalgo+'PFJets'+PUMethod+postFix+'ECF', ECF.clone(
				src = cms.InputTag( ( jetalgo+'PFJets'+PUMethod if not updateCollection else updateCollection ) ),
				Njets = cms.vuint32( rangeECF ),
				beta = cms.double( ecfBeta ) 
				))

		elemToKeep += [ 'keep *_'+jetalgo+'PFJets'+PUMethod+postFix+'ECF_*_*'] 
		for ecf in rangeECF: getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [ jetalgo+'PFJets'+PUMethod+postFix+'ECF:ecf'+str(ecf) ]
		jetSeq += getattr(proc, jetalgo+'PFJets'+PUMethod+postFix+'ECF' )
		toolsUsed.append( jetalgo+'PFJets'+PUMethod+postFix+'ECF' )
	
	if hasattr(proc, 'patJetPartons'): proc.patJetPartons.particles = genParticlesLabel


	setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix, selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+postFix, cut = Cut ) )
	elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'_*_*' ]
	elemToKeep += [ 'drop *_selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'_calo*_*' ]
	elemToKeep += [ 'drop *_selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+'_tagInfos_*' ]

	if updateCollectionSubjets: 
		setattr( proc, 'selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed', selectedPatJets.clone( src = patJets+jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed', cut = Cut ) )
		elemToKeep += [ 'keep *_selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed__*' ]


	if len(toolsUsed) > 0 : print '|---- jetToolBox: Running '+', '.join(toolsUsed)+'.'
	print '|---- jetToolBox: Creating selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+' collection.'
	if updateCollectionSubjets: print '|---- jetToolBox: Creating selectedPatJets'+jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed collection.'

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
