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

handleSubjets = Handle("std::vector<pat::Jet>")
labelSubjets = ("selectedPatJetsAK8PF"+PUMethod+'PrunedPacked') 


# loop over events in this file
nevents = 0
for event in events:

	nevents += 1
	if nevents % 10 == 0 : print '    ---> Event ' + str(nevents)

	event.getByLabel( label, handle )
	jets = handle.product()

	event.getByLabel( labelSubjets, handleSubjets )
	subjets = handleSubjets.product()

	i = 0
	for jet in jets:
		if ( jet.pt() > 50 ) and ( abs( jet.eta() ) < 2.5 ):
			#print jet.pt(), jet.chargedHadronEnergyFraction()
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

	j=0
	for subjet in subjets:
		j+=1
		hSubJetsTau1.Fill( subjet.userFloat("NjettinessAK8"+PUMethod+"Pruned:tau1") )
	hNumSubjets.Fill( j )


#CLEANUP
outputFile.Write()
outputFile.Close()
