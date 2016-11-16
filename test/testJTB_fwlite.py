#! /usr/bin/env python

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
#ROOT.gROOT.Macro("~/rootlogon.C")
#ROOT.gROOT.SetBatch() 

#HISTOGRAMS
outputFile = ROOT.TFile( 'testJTB.root', "RECREATE")
hJetsPt = ROOT.TH1F("hJetsPt", ";jet pt (GeV)", 100, 0, 1000 )
hJetsTrimmedMass = ROOT.TH1F("hJetsTrimmedMass", ";jet Trimmed mass (GeV)", 30, 0, 300 )
hJetsPrunedMass = ROOT.TH1F("hJetsPrunedMass", ";jet Pruned mass (GeV)", 30, 0, 300 )
hJetsSoftDropMass = ROOT.TH1F("hJetsSoftDropMass", ";jet SoftDrop mass (GeV)", 30, 0, 300 )
hJetsCSV = ROOT.TH1F("hJetsCSV", ";CSV value", 100, 0, 1 )
hJetsCHF = ROOT.TH1F("hJetsCHF", ";Charged Hadron Fraction", 100, 0, 1 )

hJet1Pt = ROOT.TH1F("hJet1Pt", ";jet pt (GeV)", 100, 0, 1000 )
hJet1TrimmedMass = ROOT.TH1F("hJet1TrimmedMass", ";jet Trimmed mass (GeV)", 30, 0, 300 )
hJet1PrunedMass = ROOT.TH1F("hJet1PrunedMass", ";jet Pruned mass (GeV)", 30, 0, 300 )
hJet1SoftDropMass = ROOT.TH1F("hJet1SoftDropMass", ";jet SoftDrop mass (GeV)", 30, 0, 300 )
hJet1CHF = ROOT.TH1F("hJet1CHF", ";Charged Hadron Fraction", 100, 0, 1 )

hNumSubjets = ROOT.TH1F("hNumSubJets", ";Number of Subjets", 10, 0, 10 )
hSubJetsTau1 = ROOT.TH1F("hSubJetsTau1", ";#tau_{1}", 10, 0, 1 )

#EVENT LOOP
events = Events ('jettoolbox.root')
PUMethod = 'CHS'

handle = Handle("std::vector<pat::Jet>")
label = ("selectedPatJetsAK8PF"+PUMethod) 
#label = ('packedPatJetsAK8PFCHSSoftDrop') 
#label = ('packedPatJetsAK8PFCHSPruned') 


# loop over events in this file
nevents = 0
for event in events:

	nevents += 1
	if nevents % 10 == 0 : print '    ---> Event ' + str(nevents)

	event.getByLabel( label, handle )
	jets = handle.product()

	#event.getByLabel( labelSubjets, handleSubjets )
	#subjets = handleSubjets.product()

	for i,j in enumerate(jets):
		print "jetAK8 %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f ungroomed, %5.1f softdrop, %5.1f pruned, %5.1f trimmed, %5.1f filtered. " % ( i, j.pt(), j.pt()*j.jecFactor('Uncorrected'), j.eta(), j.mass(), j.userFloat('ak8PFJetsCHSSoftDropMass'), j.userFloat('ak8PFJetsCHSPrunedMass'), j.userFloat('ak8PFJetsCHSTrimmedMass'), j.userFloat('ak8PFJetsCHSFilteredMass'))
			          
		'''
	i = 0
	for jet in jets:
		#print jet.userFloat("QGTaggerAK4PFCHS:qgLikelihood"), jet.bDiscriminator('pfCombinedInclusiveSecondaryVertexV2BJetTags')
		if ( jet.pt() > 170 ) and ( abs( jet.eta() ) < 2.5 ):
			#print jet.pt(), jet.chargedHadronEnergyFraction(), jet.userFloat("ak8PFJets"+PUMethod+"TrimmedMass"), jet.userFloat("ak8PFJets"+PUMethod+"PrunedMass")
			#print jet.userFloat("ak8PFJets"+PUMethod+"TrimmedMass"), jet.userFloat("ak8PFJets"+PUMethod+"PrunedMass"), jet.userFloat('NjettinessAK8:tau1'), jet.bDiscriminator('pfCombinedInclusiveSecondaryVertexV2BJetTags')

			hJetsPt.Fill( jet.pt() )
			hJetsCHF.Fill( jet.chargedHadronEnergyFraction() )
			hJetsCSV.Fill( jet.bDiscriminator('pfCombinedInclusiveSecondaryVertexV2BJetTags') )
			hJetsTrimmedMass.Fill( jet.userFloat("ak8PFJets"+PUMethod+"TrimmedMass") )
			hJetsPrunedMass.Fill( jet.userFloat("ak8PFJets"+PUMethod+"PrunedMass") )
			hJetsSoftDropMass.Fill( jet.userFloat("ak8PFJets"+PUMethod+"SoftDropMass") )

			i += 1
			if ( i == 1 ):
				hJet1Pt.Fill( jet.pt() )
				hJet1CHF.Fill( jet.chargedHadronEnergyFraction() )
				hJet1TrimmedMass.Fill( jet.userFloat("ak8PFJets"+PUMethod+"TrimmedMass") )
				hJet1PrunedMass.Fill( jet.userFloat("ak8PFJets"+PUMethod+"PrunedMass") )
				hJet1SoftDropMass.Fill( jet.userFloat("ak8PFJets"+PUMethod+"SoftDropMass") )

		'''
			
		wSubjets = j.subjets('SoftDrop')
		#wSubjets = j.subjets('Pruned')
		for iw,wsub in enumerate( wSubjets ) :
			print "   w subjet %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f " % (
			iw, wsub.pt(), wsub.pt()*wsub.jecFactor('Uncorrected'), wsub.eta(), wsub.mass() )


#CLEANUP
outputFile.Write()
outputFile.Close()
