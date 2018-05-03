###############################################
####
####   Jet Substructure Toolbox (jetToolBox)
####   Python function for easy access of 
####   jet substructure tools implemented in CMS
####
####   Alejandro Gomez Espinosa (alejandro.gomez@cern.ch)
####   with several contributions from others
####
###############################################
import FWCore.ParameterSet.Config as cms

from RecoJets.Configuration.RecoPFJets_cff import ak4PFJets, ak8PFJetsCHSSoftDrop, ak8PFJetsCHSSoftDropMass, ak8PFJetsCHSPruned, ak8PFJetsCHSPrunedMass, ak8PFJetsCHSTrimmed, ak8PFJetsCHSTrimmedMass, ak8PFJetsCHSFiltered, ak8PFJetsCHSFilteredMass, ak4PFJetsCHS, ca15PFJetsCHSMassDropFiltered, ak8PFJetsCHSConstituents, puppi
from RecoJets.JetProducers.caTopTaggers_cff import hepTopTagPFJetsCHS
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
		addEnergyCorrFunc=False, 
		addEnergyCorrFuncSubjets=False,
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
	mod = {}

	### List of Jet Corrections
	if not set(JETCorrLevels).issubset(set(JECLevels)): 
		if ( 'CHS' in PUMethod ) or  ( 'Plain' in PUMethod ): JETCorrLevels = ['L1FastJet','L2Relative', 'L3Absolute']
		else: JETCorrLevels = [ 'L2Relative', 'L3Absolute']
		if runOnData: JETCorrLevels.append('L2L3Residual')
	if not set(subJETCorrLevels).issubset(set(JECLevels)): 
		if ( 'CHS' in PUMethod ) or  ( 'Plain' in PUMethod ): subJETCorrLevels = ['L1FastJet','L2Relative', 'L3Absolute']
		else: subJETCorrLevels = [ 'L2Relative', 'L3Absolute']
		if runOnData: subJETCorrLevels.append('L2L3Residual')


	mod["PATJetsLabel"] = jetALGO+'PF'+PUMethod
	mod["PATJetsLabelPost"] = mod["PATJetsLabel"]+postFix
	# some substructure quantities don't include the 'PF' in the name
	mod["SubstructureLabel"] = jetALGO+PUMethod+postFix
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

		mod["GenJetsNoNu"] = jetalgo+'GenJetsNoNu'
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
				mod["GenParticlesNoNu"] = 'packedGenParticlesForJetsNoNu'
				setattr( proc, mod["GenParticlesNoNu"],
						cms.EDFilter("CandPtrSelector", 
							src = cms.InputTag("packedGenParticles"), 
							cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16")
							))
				jetSeq += getattr(proc, mod["GenParticlesNoNu"])

				setattr( proc, mod["GenJetsNoNu"], 
						ak4GenJets.clone( src = mod["GenParticlesNoNu"],
							rParam = jetSize, 
							jetAlgorithm = algorithm ) ) 
				jetSeq += getattr(proc, mod["GenJetsNoNu"])

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
				setattr( proc, mod["GenJetsNoNu"], ak4GenJets.clone( src = 'genParticlesForJetsNoNu', rParam = jetSize, jetAlgorithm = algorithm ) ) 
				jetSeq += getattr(proc, mod["GenJetsNoNu"])
			

		####  Creating PATjets
		tmpPfCandName = pfCand.lower()
		mod["PFJets"] = ""
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

			from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJetsPuppi
			mod["PFJets"] = jetalgo+'PFJetsPuppi'+postFix
			setattr( proc, mod["PFJets"], 
					ak4PFJetsPuppi.clone( src = cms.InputTag( srcForPFJets ),
						doAreaFastjet = True, 
						rParam = jetSize, 
						jetAlgorithm = algorithm ) )  
			jetSeq += getattr(proc, mod["PFJets"])

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
			mod["PFJets"] = jetalgo+'PFJetsSK'+postFix
			setattr( proc, mod["PFJets"], 
					ak4PFJetsSK.clone(  src = cms.InputTag( srcForPFJets ),
						rParam = jetSize, 
						jetAlgorithm = algorithm ) ) 
			jetSeq += getattr(proc, mod["PFJets"])

			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PFSK'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PFSK'
		
		elif 'CS' in PUMethod: 

			from RecoJets.JetProducers.ak4PFJetsCHSCS_cfi import ak4PFJetsCHSCS
			mod["PFJets"] = jetalgo+'PFJetsCS'+postFix
			setattr( proc, mod["PFJets"], 
					ak4PFJetsCHSCS.clone( doAreaFastjet = True, 
						src = cms.InputTag( pfCand ), #srcForPFJets ),
						csRParam = cms.double(jetSize),
						jetAlgorithm = algorithm ) ) 
			if miniAOD: getattr( proc, mod["PFJets"]).src = pfCand
			jetSeq += getattr(proc, mod["PFJets"])

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
				
			mod["PFJets"] = jetalgo+'PFJetsCHS'+postFix
			setattr( proc, mod["PFJets"], 
					ak4PFJetsCHS.clone( src = cms.InputTag( srcForPFJets ), 
						doAreaFastjet = True, 
						rParam = jetSize, 
						jetAlgorithm = algorithm ) ) 
			jetSeq += getattr(proc, mod["PFJets"])

			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PFchs'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PFchs'

		else: 
			PUMethod = ''
			mod["PFJets"] = jetalgo+'PFJets'+postFix
			setattr( proc, mod["PFJets"], 
					ak4PFJets.clone( 
						doAreaFastjet = True, 
						rParam = jetSize, 
						jetAlgorithm = algorithm ) ) 
			if miniAOD: getattr( proc, mod["PFJets"]).src = pfCand
			jetSeq += getattr(proc, mod["PFJets"])
			if JETCorrPayload not in payloadList: JETCorrPayload = 'AK'+size+'PF'
			if subJETCorrPayload not in payloadList: subJETCorrPayload = 'AK4PF'


		if 'None' in JETCorrPayload: JEC = None
		else: JEC = ( JETCorrPayload.replace('CS','chs').replace('SK','chs') , JETCorrLevels, 'None' )   ### temporary
		#else: JEC = ( JETCorrPayload., JETCorrLevels, 'None' ) 
		print '|---- jetToolBox: Applying this corrections: '+str(JEC)

		if addPrunedSubjets or addSoftDropSubjets or addCMSTopTagger:
			if 'None' in subJETCorrPayload: subJEC = None
			else: subJEC = ( subJETCorrPayload.replace('CS','chs').replace('SK','chs') , subJETCorrLevels, 'None' )   ### temporary


		mod["PFJetsConstituents"] = mod["PFJets"]+'Constituents'
		mod["PFJetsConstituentsColon"] = mod["PFJets"]+'Constituents:constituents'
		mod["PFJetsConstituentsColonOrUpdate"] = mod["PFJetsConstituentsColon"] if not updateCollection else updateCollection
		if ( PUMethod in [ 'CHS', 'CS', 'Puppi' ] ) and miniAOD: setattr( proc, mod["PFJetsConstituents"], cms.EDProducer("MiniAODJetConstituentSelector", src = cms.InputTag( mod["PFJets"] ), cut = cms.string( Cut ) ))
		else: setattr( proc, mod["PFJetsConstituents"], cms.EDProducer("PFJetConstituentSelector", src = cms.InputTag( mod["PFJets"] ), cut = cms.string( Cut ) ))
		jetSeq += getattr(proc, mod["PFJetsConstituents"])

		addJetCollection(
				proc,
				labelName = mod["PATJetsLabel"],
				jetSource = cms.InputTag(mod["PFJets"]),
				postfix = postFix, 
				algo = jetalgo,
				rParam = jetSize,
				jetCorrections = JEC if JEC is not None else None, 
				pfCandidates = cms.InputTag( pfCand ),  
				svSource = cms.InputTag( svLabel ),  
				genJetCollection = cms.InputTag(mod["GenJetsNoNu"]),
				pvSource = cms.InputTag( pvLabel ), 
				muSource = cms.InputTag( muLabel ),
				elSource = cms.InputTag( elLabel ),
				btagDiscriminators = bTagDiscriminators,
				btagInfos = bTagInfos,
				getJetMCFlavour = GetJetMCFlavour,
				genParticles = cms.InputTag(genParticlesLabel),
				outputModules = ['outputFile']
				)
		patJets = 'patJets'
		patSubJets = ''
		selectedPatJets = 'selectedPatJets'
		mod["PATJets"] = patJets+mod["PATJetsLabelPost"]
		mod["selPATJets"] = selectedPatJets+mod["PATJetsLabelPost"]
		getattr(proc, mod["PATJets"]).addTagInfos = cms.bool(True)

		if 'CS' in PUMethod: getattr( proc, mod["PATJets"] ).getJetMCFlavour = False  # CS jets cannot be re-clustered from their constituents
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
				labelName = mod["PATJetsLabel"],
				jetCorrections = JEC, 
				btagDiscriminators = bTagDiscriminators,
				)
		mod["PATJetsCorrFactors"] = 'patJetCorrFactors'+mod["PATJetsLabelPost"]
		getattr( proc, mod["PATJetsCorrFactors"] ).payload = JETCorrPayload
		getattr( proc, mod["PATJetsCorrFactors"] ).levels = JETCorrLevels
		if bTagDiscriminators: print '|---- jetToolBox: Adding this bTagDiscriminators: '+str(bTagDiscriminators)+' in the jet collection.'
		patJets = 'updatedPatJets'
		patSubJets = ''
		mod["PATJets"] = patJets+mod["PATJetsLabelPost"]
		mod["selPATJets"] = selectedPatJets+mod["PATJetsLabelPost"]

		if updateCollectionSubjets:
			print '|---- jetToolBox: JETTOOLBOX IS UPDATING '+updateCollectionSubjets+' collection for subjets/groomers.'
			if 'SoftDrop' in updateCollectionSubjets: updateSubjetLabel = 'SoftDrop'
			else: updateSubjetLabel = 'Pruned'
			mod["PATSubjetsLabel"] = jetALGO+'PF'+PUMethod+postFix+updateSubjetLabel+'Packed'
			updateJetCollection(
					proc,
					jetSource = cms.InputTag( updateCollectionSubjets ),
					labelName = mod["PATSubjetsLabel"],
					jetCorrections = JEC, 
					explicitJTA = True,
					fatJets = cms.InputTag( updateCollection ),
					rParam = jetSize, 
					algo = jetALGO,
					btagDiscriminators = bTagDiscriminators,
					)
			mod["PATSubjetsCorrFactors"] = 'patJetCorrFactors'+mod["PATSubjetsLabel"]
			getattr( proc, mod["PATSubjetsCorrFactors"] ).payload = subJETCorrPayload
			getattr( proc, mod["PATSubjetsCorrFactors"] ).levels = subJETCorrLevels
			patSubJets = 'updatedPatJets'+mod["PATSubjetsLabel"]
			if bTagDiscriminators: print '|---- jetToolBox: Adding this bTagDiscriminators: '+str(bTagDiscriminators)+' in the subjet collection.'

		if addPrunedSubjets or addSoftDropSubjets or addCMSTopTagger or addMassDrop or addHEPTopTagger or addPruning or addSoftDrop: 
			print '|---- jetToolBox: You are trying to add a groomer variable into a clustered jet collection. THIS IS NOT RECOMMENDED, it is recommended to recluster jets instead using a plain jetToolbox configuration. Please use this feature by your own risk.'

	mod["PFJetsOrUpdate"] = mod["PFJets"] if not updateCollection else updateCollection

	#### Groomers
	if addSoftDrop or addSoftDropSubjets: 

		mod["PFJetsSoftDrop"] = mod["PFJets"]+'SoftDrop'
		mod["SoftDropMass"] = mod["PFJets"]+'SoftDropMass'
		setattr( proc, mod["PFJetsSoftDrop"],
			ak8PFJetsCHSSoftDrop.clone( 
				src = cms.InputTag( mod["PFJetsConstituentsColonOrUpdate"] ),
				rParam = jetSize, 
				jetAlgorithm = algorithm, 
				useExplicitGhosts=True,
				R0= cms.double(jetSize),
				zcut=zCutSD, 
				beta=betaCut,
				doAreaFastjet = cms.bool(True),
				writeCompound = cms.bool(True),
				jetCollInstanceName=cms.string('SubJets') ) )
		setattr( proc, mod["SoftDropMass"],
			ak8PFJetsCHSSoftDropMass.clone( src = cms.InputTag( mod["PFJetsOrUpdate"] ), 
				matched = cms.InputTag( mod["PFJetsSoftDrop"] ),
				distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+mod["SoftDropMass"]+'_*_*'] 
		jetSeq += getattr(proc, mod["PFJetsSoftDrop"] )
		jetSeq += getattr(proc, mod["SoftDropMass"] )
		getattr( proc, mod["PATJets"]).userData.userFloats.src += [ mod["SoftDropMass"] ]
		toolsUsed.append( mod["SoftDropMass"] )

		if addSoftDropSubjets:

			if runOnMC:
				mod["GenJetsNoNuSoftDrop"] = mod["GenJetsNoNu"]+'SoftDrop'
				setattr( proc, mod["GenJetsNoNuSoftDrop"],
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
				if miniAOD: getattr( proc, mod["GenJetsNoNuSoftDrop"] ).src = mod["GenParticlesNoNu"]
				jetSeq += getattr(proc, mod["GenJetsNoNuSoftDrop"] )

			mod["PATJetsSoftDropLabel"] = mod["PATJetsLabelPost"]+'SoftDrop'
			addJetCollection(
					proc,
					labelName = mod["PATJetsSoftDropLabel"],
					jetSource = cms.InputTag( mod["PFJetsSoftDrop"]),
					algo = jetalgo,
					rParam = jetSize,
					jetCorrections = JEC if JEC is not None else None, 
					pvSource = cms.InputTag( pvLabel ),
					btagDiscriminators = ['None'],
					genJetCollection = cms.InputTag( mod["GenJetsNoNu"]),
					getJetMCFlavour = False, # jet flavor should always be disabled for groomed jets
					genParticles = cms.InputTag(genParticlesLabel),
					outputModules = ['outputFile']
					)
			mod["PATJetsSoftDrop"] = patJets+mod["PATJetsSoftDropLabel"]
			mod["selPATJetsSoftDrop"] = selectedPatJets+mod["PATJetsSoftDropLabel"]

			setattr( proc, mod["selPATJetsSoftDrop"], selectedPatJets.clone( src = mod["PATJetsSoftDrop"], cut = Cut ) )

			mod["PATSubjetsSoftDropLabel"] = mod["PATJetsSoftDropLabel"]+'Subjets'
			addJetCollection(
					proc,
					labelName = mod["PATSubjetsSoftDropLabel"],
					jetSource = cms.InputTag( mod["PFJetsSoftDrop"], 'SubJets'),
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
					genJetCollection = cms.InputTag( mod["GenJetsNoNuSoftDrop"],'SubJets'),
					getJetMCFlavour = GetSubjetMCFlavour,
					genParticles = cms.InputTag(genParticlesLabel),
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(mod["PFJets"]),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag(mod["PFJetsSoftDrop"]), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 
			mod["PATSubjetsSoftDrop"] = patJets+mod["PATSubjetsSoftDropLabel"]
			mod["selPATSubjetsSoftDrop"] = selectedPatJets+mod["PATSubjetsSoftDropLabel"]

			setattr( proc, mod["selPATSubjetsSoftDrop"], selectedPatJets.clone( src = mod["PATSubjetsSoftDrop"], cut = CutSubjet ))

			# Establish references between PATified fat jets and subjets using the BoostedJetMerger
			mod["selPATJetsSoftDropPacked"] = mod["selPATJetsSoftDrop"]+'Packed'
			setattr( proc, mod["selPATJetsSoftDropPacked"],
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag(mod["selPATJetsSoftDrop"]),
						subjetSrc=cms.InputTag(mod["selPATSubjetsSoftDrop"])
						))
			jetSeq += getattr(proc, mod["selPATJetsSoftDropPacked"] )
			elemToKeep += [ 'keep *_'+mod["selPATJetsSoftDropPacked"]+'_SubJets_*' ]
			toolsUsed.append( mod["selPATJetsSoftDropPacked"]+':SubJets' )

			## Pack fat jets with subjets
			mod["packedPATJetsSoftDrop"] = 'packedPatJets'+mod["PATSubjetsSoftDropLabel"]
			setattr( proc, mod["packedPATJetsSoftDrop"],
				 cms.EDProducer("JetSubstructurePacker",
						jetSrc=cms.InputTag(mod["selPATJets"]),
						distMax = cms.double( jetSize ),
						fixDaughters = cms.bool(False),
						algoTags = cms.VInputTag(
						cms.InputTag(mod["selPATJetsSoftDropPacked"])
						), 
						algoLabels =cms.vstring('SoftDrop')
						)
				 )
			jetSeq += getattr(proc, mod["packedPATJetsSoftDrop"])
			elemToKeep += [ 'keep *_'+mod["packedPATJetsSoftDrop"]+'_*_*' ]
			print '|---- jetToolBox: Creating '+mod["packedPATJetsSoftDrop"]+' collection with SoftDrop subjets.'



	if addPruning or addPrunedSubjets: 

		mod["PFJetsPruned"] = mod["PFJets"]+'Pruned'
		mod["PrunedMass"] =  mod["PFJets"]+'PrunedMass'
		setattr( proc, mod["PFJetsPruned"],
			ak8PFJetsCHSPruned.clone( 
				src = cms.InputTag( mod["PFJetsConstituentsColonOrUpdate"] ),
				rParam = jetSize, 
				jetAlgorithm = algorithm, 
				zcut=zCut, 
				rcut_factor=rCut,
				writeCompound = cms.bool(True),
				doAreaFastjet = cms.bool(True),
				jetCollInstanceName=cms.string('SubJets') ) )
		setattr( proc, mod["PrunedMass"],
			ak8PFJetsCHSPrunedMass.clone( 
				src = cms.InputTag( mod["PFJetsOrUpdate"] ), 
				matched = cms.InputTag( mod["PFJetsPruned"]), 
				distMax = cms.double( jetSize ) ) )

		jetSeq += getattr(proc, mod["PFJetsPruned"])
		jetSeq += getattr(proc, mod["PrunedMass"])
		getattr( proc, mod["PATJets"]).userData.userFloats.src += [ mod["PrunedMass"] ]
		elemToKeep += [ 'keep *_'+mod["PrunedMass"]+'_*_*'] 
		toolsUsed.append( mod["PrunedMass"] )

		if addPrunedSubjets:
			if runOnMC:
				mod["GenJetsNoNuPruned"] = mod["GenJetsNoNu"]+'Pruned'
				setattr( proc, mod["GenJetsNoNuPruned"],
						ak4GenJets.clone(
							SubJetParameters,
							rParam = jetSize,
							usePruning = cms.bool(True),
							writeCompound = cms.bool(True),
							jetCollInstanceName=cms.string('SubJets')
							))
				if miniAOD: getattr( proc, mod["GenJetsNoNuPruned"] ).src = mod["GenParticlesNoNu"]
				jetSeq += getattr(proc, mod["GenJetsNoNuPruned"])

			mod["PATJetsPrunedLabel"] = mod["PATJetsLabelPost"]+'Pruned'
			addJetCollection(
					proc,
					labelName = mod["PATJetsPrunedLabel"],
					jetSource = cms.InputTag( mod["PFJetsPruned"]),
					algo = jetalgo,
					rParam = jetSize,
					jetCorrections = JEC if JEC is not None else None, 
					pvSource = cms.InputTag( pvLabel ),
					btagDiscriminators = ['None'],
					genJetCollection = cms.InputTag( mod["GenJetsNoNu"]),
					getJetMCFlavour = False, # jet flavor should always be disabled for groomed jets
					genParticles = cms.InputTag(genParticlesLabel),
					outputModules = ['outputFile']
					)
			mod["PATJetsPruned"] = patJets+mod["PATJetsPrunedLabel"]
			mod["selPATJetsPruned"] = selectedPatJets+mod["PATJetsPrunedLabel"]

			setattr( proc, mod["selPATJetsPruned"], selectedPatJets.clone( src = mod["PATJetsPruned"], cut = Cut ) )

			mod["PATSubjetsPrunedLabel"] = mod["PATJetsPrunedLabel"]+'Subjets'
			addJetCollection(
					proc,
					labelName = mod["PATSubjetsPrunedLabel"],
					jetSource = cms.InputTag( mod["PFJetsPruned"], 'SubJets'),
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
					genJetCollection = cms.InputTag( mod["GenJetsNoNuPruned"],'SubJets'),
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(mod["PFJets"]),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag(mod["PFJetsPruned"]), # needed for subjet flavor clustering
					outputModules = ['outputFile']
					) 
			mod["PATSubjetsPruned"] = patJets+mod["PATSubjetsPrunedLabel"]
			mod["selPATSubjetsPruned"] = selectedPatJets+mod["PATSubjetsPrunedLabel"]

			setattr( proc, mod["selPATSubjetsPruned"], selectedPatJets.clone( src = mod["PATSubjetsPruned"], cut = CutSubjet ) )

			## Establish references between PATified fat jets and subjets using the BoostedJetMerger
			mod["selPATJetsPrunedPacked"] = mod["selPATJetsPruned"]+'Packed'
			setattr( proc, mod["selPATJetsPrunedPacked"],
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag(mod["selPATJetsPruned"]),
						subjetSrc=cms.InputTag(mod["selPATSubjetsPruned"]),
						))
			jetSeq += getattr(proc, mod["selPATJetsPrunedPacked"])
			elemToKeep += [ 'keep *_'+mod["selPATJetsPrunedPacked"]+'_SubJets_*' ]
			toolsUsed.append( mod["selPATJetsPrunedPacked"]+':SubJets' )

			## Pack fat jets with subjets
			mod["packedPATJetsPruned"] = 'packedPatJets'+mod["PATSubjetsPrunedLabel"]
			setattr( proc, mod["packedPATJetsPruned"],
				 cms.EDProducer("JetSubstructurePacker",
						jetSrc=cms.InputTag(mod["selPATJets"]),
						distMax = cms.double( jetSize ),
						fixDaughters = cms.bool(False),
						algoTags = cms.VInputTag(
						cms.InputTag(mod["selPATJetsPrunedPacked"])
						), 
						algoLabels =cms.vstring('Pruned')
						)
				 )
			jetSeq += getattr(proc, mod["packedPATJetsPruned"])
			elemToKeep += [ 'keep *_'+mod["packedPATJetsPruned"]+'_*_*' ]
			print '|---- jetToolBox: Creating '+mod["packedPATJetsPruned"]+' collection with Pruned subjets.'


	if addTrimming:

		mod["PFJetsTrimmed"] = mod["PFJets"]+'Trimmed'
		mod["TrimmedMass"] = mod["PFJets"]+'TrimmedMass'
		setattr( proc, mod["PFJetsTrimmed"],
				ak8PFJetsCHSTrimmed.clone( 
					rParam = jetSize, 
					src = cms.InputTag( mod["PFJetsConstituentsColonOrUpdate"] ),
					jetAlgorithm = algorithm,
					rFilt= rFiltTrim,
					trimPtFracMin= ptFrac) ) 
		setattr( proc, mod["TrimmedMass"], 
				ak8PFJetsCHSTrimmedMass.clone( 
					src = cms.InputTag( mod["PFJetsOrUpdate"] ), 
					matched = cms.InputTag( mod["PFJetsTrimmed"]), 
					distMax = cms.double( jetSize ) ) )

		elemToKeep += [ 'keep *_'+mod["TrimmedMass"]+'_*_*'] 
		jetSeq += getattr(proc, mod["PFJetsTrimmed"])
		jetSeq += getattr(proc, mod["TrimmedMass"])
		getattr( proc, mod["PFJetsTrimmed"]).userData.userFloats.src += [mod["TrimmedMass"]]
		toolsUsed.append( mod["TrimmedMass"] )

	if addFiltering:

		mod["PFJetsFiltered"] = mod["PFJets"]+'Filtered'
		mod["FilteredMass"] = mod["PFJets"]+'FilteredMass'
		setattr( proc, mod["PFJetsFiltered"],
				ak8PFJetsCHSFiltered.clone( 
					src = cms.InputTag( mod["PFJetsConstituentsColonOrUpdate"] ),
					rParam = jetSize, 
					jetAlgorithm = algorithm,
					rFilt= rfilt,
					nFilt= nfilt ) ) 
		setattr( proc, mod["FilteredMass"],
				ak8PFJetsCHSFilteredMass.clone( 
					src = cms.InputTag( mod["PFJetsOrUpdate"] ), 
					matched = cms.InputTag( mod["PFJetsFiltered"]), 
					distMax = cms.double( jetSize ) ) )
		elemToKeep += [ 'keep *_'+mod["FilteredMass"]+'_*_*'] 
		jetSeq += getattr(proc, mod["PFJetsFiltered"])
		jetSeq += getattr(proc, mod["FilteredMass"])
		getattr( proc, patJets+jetALGO+'PF'+PUMethod+postFix).userData.userFloats.src += [mod["FilteredMass"]]
		toolsUsed.append( mod["FilteredMass"] )

	if addCMSTopTagger :

		if 'CA' in jetALGO : 

			mod["PFJetsCMSTopTag"] = mod["PFJets.replace"](jetalgo,"cmsTopTag")
			setattr( proc, mod["PFJetsCMSTopTag"],
					cms.EDProducer("CATopJetProducer",
						PFJetParameters.clone( 
							src = cms.InputTag( mod["PFJetsConstituentsColonOrUpdate"] ),
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
						src = cms.InputTag(mod["PFJetsCMSTopTag"]),
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
			mod["PATJetsCMSTopTagLabel"] = 'CMSTopTag'+PUMethod+postFix
			addJetCollection(
					proc,
					labelName = mod["PATJetsCMSTopTagLabel"],
					jetSource = cms.InputTag(mod["PFJetsCMSTopTag"]),
					jetCorrections = JEC if JEC is not None else None, 
					pfCandidates = cms.InputTag( pfCand ),  
					pvSource = cms.InputTag( pvLabel), 
					svSource = cms.InputTag( svLabel ), 
					muSource = cms.InputTag( muLabel ),
					elSource = cms.InputTag( elLabel ),
					btagDiscriminators = bTagDiscriminators,
					btagInfos = bTagInfos,
					genJetCollection = cms.InputTag(mod["GenJetsNoNu"]),
					getJetMCFlavour = False, # jet flavor should always be disabled for groomed jets
					genParticles = cms.InputTag(genParticlesLabel)
					)
			mod["PATJetsCMSTopTag"] = patJets+mod["PATJetsCMSTopTagLabel"]
			mod["selPATJetsCMSTopTag"] = selectedPatJets+mod["PATJetsCMSTopTagLabel"]
			getattr(proc,mod["PATJetsCMSTopTag"]).addTagInfos = True
			getattr(proc,mod["PATJetsCMSTopTag"]).tagInfoSources = cms.VInputTag( cms.InputTag('CATopTagInfos'))
			setattr( proc, mod["selPATJetsCMSTopTag"], selectedPatJets.clone( src = mod["PATJetsCMSTopTag"], cut = Cut ) )

			mod["PATSubjetsCMSTopTagLabel"] = mod["PATJetsCMSTopTagLabel"]+'Subjets'
			addJetCollection(
					proc,
					labelName = mod["PATSubjetsCMSTopTagLabel"],
					jetSource = cms.InputTag(mod["PFJetsCMSTopTag"], 'SubJets'),
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
					genJetCollection = cms.InputTag( mod["GenJetsNoNu"]),
					getJetMCFlavour = GetSubjetMCFlavour,
					explicitJTA = True,  # needed for subjet b tagging
					svClustering = True, # needed for subjet b tagging
					fatJets=cms.InputTag(mod["PFJets"]),             # needed for subjet flavor clustering
					groomedFatJets=cms.InputTag(mod["PATJetsCMSTopTag"]), # needed for subjet flavor clustering
					genParticles = cms.InputTag(genParticlesLabel)
					)
			mod["PATSubjetsCMSTopTag"] = patJets+mod["PATSubjetsCMSTopTagLabel"]
			mod["selPATSubjetsCMSTopTag"] = selectedPatJets+mod["PATSubjetsCMSTopTagLabel"]

			setattr( proc, mod["selPATSubjetsCMSTopTag"], selectedPatJets.clone( src = mod["PATSubjetsCMSTopTag"], cut = Cut ) )

			mod["PATJetsCMSTopTagPacked"] = mod["PATJetsCMSTopTag"]+'Packed'
			setattr( proc, mod["packedPATJetsCMSTopTag"],
					cms.EDProducer("BoostedJetMerger",
						jetSrc=cms.InputTag(mod["PATJetsCMSTopTag"]),
						subjetSrc=cms.InputTag(mod["PATSubjetsCMSTopTag"])
						))
			jetSeq += getattr(proc, mod["PATJetsCMSTopTagPacked"])
			elemToKeep += [ 'keep *_'+mod["PATJetsCMSTopTagPacked"]+'_*_*' ]
			toolsUsed.append( mod["PATJetsCMSTopTagPacked"] )

		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for CMS Top Tagger, you are using '+algorithm+'. JetToolbox will not run CMS Top Tagger.'

	if addMassDrop :

		if 'CA' in jetALGO :
			mod["PFJetsMassDrop"] = mod["PFJets"]+'MassDropFiltered'
			mod["MassDropFilteredMass"] = mod["PFJetsMassDrop"]+'Mass'
			setattr( proc, mod["PFJetsMassDrop"],
					ca15PFJetsCHSMassDropFiltered.clone( 
						rParam = jetSize,
						src = cms.InputTag( mod["PFJetsConstituentsColonOrUpdate"] ),
						) )
			setattr( proc, mod["MassDropFilteredMass"], ak8PFJetsCHSPrunedMass.clone( src = cms.InputTag( mod["PFJets"]),
				matched = cms.InputTag(mod["PFJetsMassDrop"]), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_'+mod["MassDropFilteredMass"]+'_*_*' ]
			getattr( proc, mod["PATJets"]).userData.userFloats.src += [ mod["MassDropFilteredMass"] ]
			jetSeq += getattr(proc, mod["PFJetsMassDrop"])
			jetSeq += getattr(proc, mod["MassDropFilteredMass"])
			toolsUsed.append( mod["MassDropFilteredMass"] )
		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for Mass Drop, you are using '+algorithm+'. JetToolbox will not run Mass Drop.'

	if addHEPTopTagger: 
		if ( jetSize >= 1. ) and ( 'CA' in jetALGO ): 

			mod["PFJetsHEPTopTag"] = mod["PFJets.replace"](jetalgo,"hepTopTag")
			mod["PFJetsHEPTopTagMass"] = mod["PFJetsHEPTopTag"]+'Mass'+jetALGO
			setattr( proc, mod["PFJetsHEPTopTag"], hepTopTagPFJetsCHS.clone( src = cms.InputTag( mod["PFJetsConstituentsColonOrUpdate"] ) ) )
			setattr( proc, mod["PFJetsHEPTopTagMass"], ak8PFJetsCHSPrunedMass.clone( src = cms.InputTag(mod["PFJets"]), 
				matched = cms.InputTag(mod["PFJetsHEPTopTag"]), distMax = cms.double( jetSize ) ) )
			elemToKeep += [ 'keep *_'+mod["PFJetsHEPTopTagMass"]+'_*_*' ]
			getattr( proc, mod["PATJets"]).userData.userFloats.src += [ mod["PFJetsHEPTopTagMass"] ]
			jetSeq += getattr(proc, mod["PFJetsHEPTopTag"])
			jetSeq += getattr(proc, mod["PFJetsHEPTopTagMass"])
			toolsUsed.append( mod["PFJetsHEPTopTagMass"] )
		else: print '|---- jetToolBox: CMS recommends CambridgeAachen for HEPTopTagger, you are using '+algorithm+', and a jet cone size bigger than 1. JetToolbox will not run HEP TopTagger.'

	####### Nsubjettiness
	if addNsub:
		from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

		rangeTau = range(1,maxTau+1)
		mod["Njettiness"] = 'Njettiness'+mod["SubstructureLabel"]
		setattr( proc, mod["Njettiness"],
				Njettiness.clone( src = cms.InputTag( mod["PFJetsOrUpdate"] ),
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

		elemToKeep += [ 'keep *_'+mod["Njettiness"]+'_*_*' ]
		for tau in rangeTau: getattr( proc, mod["PATJets"]).userData.userFloats.src += [mod["Njettiness"]+':tau'+str(tau) ] 
		jetSeq += getattr(proc, mod["Njettiness"])
		toolsUsed.append( mod["Njettiness"] )

	####### Nsubjettiness
	if addNsubSubjets:

		from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

		mod["NsubGroomer"] = ''
		mod["NsubSubjets"] = ''
		mod["NsubPATJets"] = ''
		if addSoftDropSubjets or updateCollectionSubjets:
			mod["NsubGroomer"] = mod["PFJetsSoftDrop"]
			mod["NsubSubjets"] = mod["PATSubjetsSoftDropLabel"]
			mod["NsubPATSubjets"] = mod["PATSubjetsSoftDrop"]
			if updateCollectionSubjets:
				print '|---- jetToolBox: Using updateCollection option. ASSUMING MINIAOD collection '+ updateCollectionSubjets +' for Nsubjettiness of subjets.'
		elif addPrunedSubjets:
			mod["NsubGroomer"] = mod["PFJetsPruned"]
			mod["NsubSubjets"] = mod["PATSubjetsPrunedLabel"]
			mod["NsubPATSubjets"] = mod["PATSubjetsPruned"]
		else: 
			print '|---- jetToolBox: Nsubjettiness of subjets needs a Subjet collection. Or create one using addSoftDropSubjets option, or updateCollection.'
			return None

		mod["Nsubjettiness"] = 'Nsubjettiness'+mod["NsubSubjets"]
		rangeTau = range(1,subjetMaxTau+1)
		setattr( proc, mod["Nsubjettiness"],
				Njettiness.clone( src = cms.InputTag( ( mod["NsubGroomer"] if not updateCollectionSubjets else updateCollectionSubjets ), 'SubJets' ), 
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

		elemToKeep += [ 'keep *_'+mod["Nsubjettiness"]+'_*_*' ]
		for tau in rangeTau: getattr( proc, ( mod["NsubPATSubjets"] if not updateCollectionSubjets else patSubJets ) ).userData.userFloats.src += [mod["Nsubjettiness"]+':tau'+str(tau) ] 
		jetSeq += getattr(proc, mod["Nsubjettiness"])
		toolsUsed.append( mod["Nsubjettiness"] )

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
				QJetsAdder.clone( src = cms.InputTag(jetalgo+'PFJets'+PUMethod+postFix), 
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
			mod["QGTagger"] = 'QGTagger'+mod["PATJetsLabelPost"]
			setattr( proc, mod["QGTagger"],
					QGTagger.clone(
						srcJets = cms.InputTag( mod["PFJetsOrUpdate"] ),    # Could be reco::PFJetCollection or pat::JetCollection (both AOD and miniAOD)
						jetsLabel = cms.string('QGL_AK4PF'+QGjetsLabel)        # Other options (might need to add an ESSource for it): see https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion
						)
					)
			elemToKeep += [ 'keep *_'+mod["QGTagger"]+'_*_*' ]
			getattr( proc, mod["PATJets"]).userData.userFloats.src += [mod["QGTagger"]+':qgLikelihood']
			jetSeq += getattr(proc, mod["QGTagger"])

			toolsUsed.append( mod["QGTagger"] )
		else:
			print '|---- jetToolBox: QGTagger is optimized for ak4 jets with CHS. NOT running QGTagger'

			
	####### Pileup JetID
	if addPUJetID:
		if ( 'ak4' in jetalgo ) and ( PUMethod not in ['CS','SK'] ):
			if PUMethod=="Puppi": print '|---- jetToolBox: PUJetID is not yet optimized for ak4 PFjets with PUPPI. USE ONLY FOR TESTING.'
			from RecoJets.JetProducers.pileupjetidproducer_cfi import pileupJetIdCalculator,pileupJetIdEvaluator

			mod["PUJetIDCalc"] = mod["PATJetsLabelPost"]+'pileupJetIdCalculator'
			setattr( proc, mod["PUJetIDCalc"],
					pileupJetIdCalculator.clone(
						jets = cms.InputTag( mod["PFJetsOrUpdate"] ),
						rho = cms.InputTag("fixedGridRhoFastjetAll"),
						vertexes = cms.InputTag(pvLabel),
						applyJec = cms.bool(True),
						inputIsCorrected = cms.bool(False)
						))

			mod["PUJetIDEval"] = mod["PATJetsLabelPost"]+'pileupJetIdEvaluator'
			setattr( proc, mod["PUJetIDEval"],
					pileupJetIdEvaluator.clone(
						jetids = cms.InputTag(mod["PUJetIDCalc"]),
						jets = cms.InputTag( mod["PFJetsOrUpdate"] ),
						rho = cms.InputTag("fixedGridRhoFastjetAll"),
						vertexes = cms.InputTag(pvLabel)
						)
					)

                        getattr( proc, mod["PATJets"]).userData.userFloats.src += [mod["PUJetIDEval"]+':fullDiscriminant']
                        getattr( proc, mod["PATJets"]).userData.userInts.src += [mod["PUJetIDEval"]+':cutbasedId',mod["PUJetIDEval"]+':fullId']
                        elemToKeep += ['keep *_'+mod["PUJetIDEval"]+'_*_*']
                        toolsUsed.append( mod["PUJetIDEval"] )
		else:
                        print '|---- jetToolBox: PUJetID is optimized for ak4 PFjets with CHS. NOT running PUJetID.'

	###### Energy Correlation Functions
	if addEnergyCorrFunc:
		if PUMethod!="Puppi" or (addSoftDrop==False and addSoftDropSubjets==False):
			raise ValueError("addEnergyCorrFunc only supported for Puppi w/ addSoftDrop or addSoftDropSubjets")
		from RecoJets.JetProducers.ECF_cff import ecfNbeta1, ecfNbeta2
		mod["ECFnb1"] = 'nb1'+mod["SubstructureLabel"]+'SoftDrop'
		mod["ECFnb2"] = 'nb2'+mod["SubstructureLabel"]+'SoftDrop'
		setattr(proc, mod["ECFnb1"], ecfNbeta1.clone(src = cms.InputTag(mod["PFJetsSoftDrop"]), cuts = cms.vstring('', '', 'pt > 250')))
		setattr(proc, mod["ECFnb2"], ecfNbeta2.clone(src = cms.InputTag(mod["PFJetsSoftDrop"]), cuts = cms.vstring('', '', 'pt > 250')))
		elemToKeep += [ 'keep *_'+mod["ECFnb1"]+'_*_*', 'keep *_'+mod["ECFnb2"]+'_*_*']
		jetSeq += getattr(proc, mod["ECFnb1"])
		jetSeq += getattr(proc, mod["ECFnb2"])
		toolsUsed.extend([mod["ECFnb1"], mod["ECFnb2"]])

		# set up user floats
		getattr(proc, mod["PATJetsSoftDrop"]).userData.userFloats.src += [
			mod["ECFnb1"]+':ecfN2',
			mod["ECFnb1"]+':ecfN3',
			mod["ECFnb2"]+':ecfN2',
			mod["ECFnb2"]+':ecfN3',
		]
		# rekey the groomed ECF value maps to the ungroomed reco jets, which will then be picked
		# up by PAT in the user floats. 
		mod["PFJetsSoftDropValueMap"] = mod["PFJetsSoftDrop"]+'ValueMap'
		setattr(proc, mod["PFJetsSoftDropValueMap"],
			cms.EDProducer("RecoJetToPatJetDeltaRValueMapProducer",
				src = cms.InputTag(mod["PFJets"]),
				matched = cms.InputTag(mod["PATJetsSoftDrop"]),
				distMax = cms.double(jetSize),
				values = cms.vstring([
					'userFloat("'+mod["ECFnb1"]+':ecfN2'+'")',
					'userFloat("'+mod["ECFnb1"]+':ecfN3'+'")',
					'userFloat("'+mod["ECFnb2"]+'SoftDrop'+':ecfN2'+'")',
					'userFloat("'+mod["ECFnb2"]+':ecfN3'+'")',
				]),
				valueLabels = cms.vstring( [
					mod["ECFnb1"]+'N2',
					mod["ECFnb1"]+'N3',
					mod["ECFnb2"]+'N2',
					mod["ECFnb2"]+'N3',
				]),
			)
		)
		getattr(proc, mod["PATJets"]).userData.userFloats.src += [
			mod["PFJetsSoftDropValueMap"]+':'+mod["ECFnb1"]+'N2',
			mod["PFJetsSoftDropValueMap"]+':'+mod["ECFnb1"]+'N3',
			mod["PFJetsSoftDropValueMap"]+':'+mod["ECFnb2"]+'N2',
			mod["PFJetsSoftDropValueMap"]+':'+mod["ECFnb2"]+'N3',
		]

	if addEnergyCorrFuncSubjets:
		if PUMethod!="Puppi" or addSoftDropSubjets==False:
			raise ValueError("addEnergyCorrFuncSubjets only supported for Puppi w/ addSoftDropSubjets")
		from RecoJets.JetProducers.ECF_cff import ecfNbeta1, ecfNbeta2
		mod["ECFnb1Subjets"] = 'nb1'+mod["SubstructureLabel"]+'SoftDropSubjets'
		mod["ECFnb2Subjets"] = 'nb2'+mod["SubstructureLabel"]+'SoftDropSubjets'
		setattr(proc, mod["ECFnb1Subjets"], ecfNbeta1.clone(src = cms.InputTag(mod["PFJetsSoftDrop"],'SubJets')))
		setattr(proc, mod["ECFnb2Subjets"], ecfNbeta2.clone(src = cms.InputTag(mod["PFJetsSoftDrop"],'SubJets')))
		elemToKeep += [ 'keep *_'+mod["ECFnb1Subjets"]+'_*_*', 'keep *_'+mod["ECFnb2Subjets"]+'_*_*']
		jetSeq += getattr(proc, mod["ECFnb1Subjets"])
		jetSeq += getattr(proc, mod["ECFnb2Subjets"])
		toolsUsed.extend([mod["ECFnb1Subjets"],mod["ECFnb2Subjets"]])

		# set up user floats
		getattr(proc, mod["PATSubjetsSoftDrop"]).userData.userFloats.src += [
			mod["ECFnb1Subjets"]+':ecfN2',
			mod["ECFnb1Subjets"]+':ecfN3',
			mod["ECFnb2Subjets"]+':ecfN2',
			mod["ECFnb2Subjets"]+':ecfN3',
		]

	if hasattr(proc, 'patJetPartons'): proc.patJetPartons.particles = genParticlesLabel

	mod["selPATJets"] = selectedPatJets+mod["PATJetsLabelPost"]
	setattr( proc, mod["selPATJets"], selectedPatJets.clone( src = mod["PATJets"], cut = Cut ) )
	elemToKeep += [ 'keep *_'+mod["selPATJets"]+'_*_*' ]
	elemToKeep += [ 'drop *_'+mod["selPATJets"]+'_calo*_*' ]
	elemToKeep += [ 'drop *_'+mod["selPATJets"]+'_tagInfos_*' ]

	if updateCollectionSubjets:
		mod["PATSubjets"] = patJets+mod["PATSubjetsLabel"]
		mod["selPATSubjets"] = selectedPatJets+mod["PATSubjetsLabel"]
		setattr( proc, mod["selPATSubjets"], selectedPatJets.clone( src = mod["PATSubjets"], cut = Cut ) )
		elemToKeep += [ 'keep *_'+mod["selPATSubjets"]+'__*' ]


	if len(toolsUsed) > 0 : print '|---- jetToolBox: Running '+', '.join(toolsUsed)+'.'
	print '|---- jetToolBox: Creating '+mod["selPATJets"]+' collection.'
	if updateCollectionSubjets: print '|---- jetToolBox: Creating '+mod["selPATSubjets"]+' collection.'

	### "return"
	setattr(proc, jetSequence, jetSeq)
	if hasattr(proc, outputFile): getattr(proc, outputFile).outputCommands += elemToKeep
	else: setattr( proc, outputFile, 
			cms.OutputModule('PoolOutputModule', 
				fileName = cms.untracked.string('jettoolbox.root'), 
				outputCommands = cms.untracked.vstring( elemToKeep ) ) )

	##### (Temporary?) fix to replace unschedule mode
	if hasattr(proc, 'myTask'): 
		getattr( proc, 'myTask', cms.Task() ).add(*[getattr(proc,prod) for prod in proc.producers_()])
		getattr( proc, 'myTask', cms.Task() ).add(*[getattr(proc,filt) for filt in proc.filters_()])
	else:
		setattr( proc, 'myTask', cms.Task() )
		getattr( proc, 'myTask', cms.Task() ).add(*[getattr(proc,prod) for prod in proc.producers_()])
		getattr( proc, 'myTask', cms.Task() ).add(*[getattr(proc,filt) for filt in proc.filters_()])

	if hasattr(proc, 'endpath'): 
		getattr( proc, 'endpath').associate( getattr( proc, 'myTask', cms.Task() ) )
	else: 
		setattr( proc, 'endpath',
				cms.EndPath(getattr(proc, outputFile), getattr( proc, 'myTask', cms.Task() )) )

	#### removing mc matching for data
	if runOnData:
		from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
		removeMCMatching(proc, names=['Jets'], outputModules=[outputFile])
