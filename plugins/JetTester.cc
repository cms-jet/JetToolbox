// -*- C++ -*-
//
// Package:    Analysis/JetTester
// Class:      JetTester
// 
/**\class JetTester JetTester.cc Analysis/JetTester/plugins/JetTester.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  James Dolen
//         Created:  Thu, 11 Jun 2015 22:52:52 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// DataFormats
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

// TFile
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// root
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TLorentzVector.h"

//
// class declaration
//

class JetTester : public edm::EDAnalyzer {
   public:
      explicit JetTester(const edm::ParameterSet&);
      ~JetTester();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
      edm::EDGetTokenT<pat::JetCollection> ak4PFCHSminiAODjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak4PFPuppiminiAODjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak4PFCHSUpdatedjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak4PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak4PFPuppijetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak4PFjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFPuppiminiAODjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFPuppiUpdatedjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFPuppijetToken_;

      edm::EDGetTokenT<pat::JetCollection> ak8PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ca8PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> kt8PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFPUPPIjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFPuppimodSDjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFSKjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFCSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ca12PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak15PFCHSjetToken_;
      //edm::EDGetTokenT<reco::GenJetCollection> ak4genjetToken_;
      //edm::EDGetTokenT<reco::GenJetCollection> ak8genjetToken_;
      edm::EDGetTokenT<edm::View<reco::GenParticle> > prunedGenToken_;
      edm::EDGetTokenT<double> rhoToken_;
      edm::EDGetTokenT<std::vector<reco::Vertex> > vtxToken_;


	  TH1D * h_ak4chsminiAOD_pt           ;
	  TH1D * h_ak4chsminiAOD_uncpt        ;
	  TH1D * h_ak4chsminiAOD_eta          ;
	  TH1D * h_ak4chsminiAOD_btagCSVv2    ;
      TH1D * h_ak4chsminiAOD_area          ;  
	  TH1D * h_ak4chsminiAOD_nhf          ;
	  TH1D * h_ak4chsminiAOD_nemf         ;
	  TH1D * h_ak4chsminiAOD_chf          ;
	  TH1D * h_ak4chsminiAOD_muf          ;
	  TH1D * h_ak4chsminiAOD_cemf         ;
	  TH1D * h_ak4chsminiAOD_numConst     ;
	  TH1D * h_ak4chsminiAOD_numNeuPar    ;
	  TH1D * h_ak4chsminiAOD_chm          ;
	  TH1D * h_ak4puppiminiAOD_pt           ;
	  TH1D * h_ak4puppiminiAOD_uncpt        ;
	  TH1D * h_ak4puppiminiAOD_eta          ;
	  TH1D * h_ak4puppiminiAOD_btagCSVv2    ;
      TH1D * h_ak4puppiminiAOD_area          ;  
	  TH1D * h_ak4puppiminiAOD_nhf          ;
	  TH1D * h_ak4puppiminiAOD_nemf         ;
	  TH1D * h_ak4puppiminiAOD_chf          ;
	  TH1D * h_ak4puppiminiAOD_muf          ;
	  TH1D * h_ak4puppiminiAOD_cemf         ;
	  TH1D * h_ak4puppiminiAOD_numConst     ;
	  TH1D * h_ak4puppiminiAOD_numNeuPar    ;
	  TH1D * h_ak4puppiminiAOD_chm          ;
	  TH1D * h_ak4chsupdated_pt           ;
	  TH1D * h_ak4chsupdated_uncpt        ;
	  TH1D * h_ak4chsupdated_eta          ;
	  TH1D * h_ak4chsupdated_btagCSVv2    ;
	  TH1D * h_ak4chsupdated_btagCvsL     ;
	  TH1D * h_ak4chsupdated_btagCvsB     ;
	  TH1D * h_ak4chsupdated_btagDeepCSVb ;
	  TH1D * h_ak4chsupdated_btagDeepCSVbb;
	  TH1D * h_ak4chsupdated_btagDeepCSVc ;
	  TH1D * h_ak4chsupdated_btagDeepCSVl ;
	  TH1D * h_ak4chsupdated_btagDeepFlavourb ;
	  TH1D * h_ak4chsupdated_btagDeepFlavourbb;
	  TH1D * h_ak4chsupdated_btagDeepFlavourc ;
	  TH1D * h_ak4chsupdated_btagDeepFlavourl ;
	  TH1D * h_ak4chsupdated_btagDeepFlavourg ;
	  TH1D * h_ak4chsupdated_btagDeepFlavourlepb;
	  TH1D * h_ak4chsupdated_area         ;
	  TH1D * h_ak4chsupdated_pileupJetId  ;
	  TH1D * h_ak4chsupdated_nhf          ;
	  TH1D * h_ak4chsupdated_nemf         ;
	  TH1D * h_ak4chsupdated_chf          ;
	  TH1D * h_ak4chsupdated_muf          ;
	  TH1D * h_ak4chsupdated_cemf         ;
	  TH1D * h_ak4chsupdated_numConst     ;
	  TH1D * h_ak4chsupdated_numNeuPar    ;
	  TH1D * h_ak4chsupdated_chm          ;
	  TH1D * h_ak4chs_pt           ;
	  TH1D * h_ak4chs_uncpt        ;
	  TH1D * h_ak4chs_eta          ;
	  TH1D * h_ak4chs_btagCSVv2    ;
	  TH1D * h_ak4chs_pileupJetId  ;
	  TH1D * h_ak4chs_qglikelihood  ;
      TH1D * h_ak4chs_area          ;  
	  TH1D * h_ak4chs_nhf          ;
	  TH1D * h_ak4chs_nemf         ;
	  TH1D * h_ak4chs_chf          ;
	  TH1D * h_ak4chs_muf          ;
	  TH1D * h_ak4chs_cemf         ;
	  TH1D * h_ak4chs_numConst     ;
	  TH1D * h_ak4chs_numNeuPar    ;
	  TH1D * h_ak4chs_chm          ;
	  TH1D * h_ak4puppi_pt           ;
	  TH1D * h_ak4puppi_uncpt        ;
	  TH1D * h_ak4puppi_eta          ;
	  TH1D * h_ak4puppi_btagCSVv2    ;
      TH1D * h_ak4puppi_area          ;  
	  TH1D * h_ak4puppi_nhf          ;
	  TH1D * h_ak4puppi_nemf         ;
	  TH1D * h_ak4puppi_chf          ;
	  TH1D * h_ak4puppi_muf          ;
	  TH1D * h_ak4puppi_cemf         ;
	  TH1D * h_ak4puppi_numConst     ;
	  TH1D * h_ak4puppi_numNeuPar    ;
	  TH1D * h_ak4puppi_chm          ;
	  TH1D * h_ak4pf_pt           ;
	  TH1D * h_ak4pf_uncpt        ;
	  TH1D * h_ak4pf_eta          ;
	  TH1D * h_ak4pf_btagCSVv2    ;
      TH1D * h_ak4pf_area          ;  
	  TH1D * h_ak4pf_nhf          ;
	  TH1D * h_ak4pf_nemf         ;
	  TH1D * h_ak4pf_chf          ;
	  TH1D * h_ak4pf_muf          ;
	  TH1D * h_ak4pf_cemf         ;
	  TH1D * h_ak4pf_numConst     ;
	  TH1D * h_ak4pf_numNeuPar    ;
	  TH1D * h_ak4pf_chm          ;
  

      TH1D * h_ak8miniAOD_pt            ;
      TH1D * h_ak8miniAOD_mass          ;
      TH1D * h_ak8miniAOD_eta      ;
      TH1D * h_ak8miniAOD_phi      ;
      TH1D * h_ak8miniAOD_CHSPrunedMass    ;
      TH1D * h_ak8miniAOD_CHSSoftDropMass    ;
      TH1D * h_ak8miniAOD_PuppiSoftDropMass    ;
      TH1D * h_ak8miniAOD_PuppiTau1          ;
      TH1D * h_ak8miniAOD_PuppiTau2          ;
      TH1D * h_ak8miniAOD_PuppiTau3          ;
      TH1D * h_ak8miniAOD_PuppiTau4          ;
      TH1D * h_ak8miniAOD_PuppiTau32         ;
      TH1D * h_ak8miniAOD_PuppiTau21         ;
      TH1D * h_ak8miniAOD_CHSTau1          ;
      TH1D * h_ak8miniAOD_CHSTau2          ;
      TH1D * h_ak8miniAOD_CHSTau3          ;
      TH1D * h_ak8miniAOD_CHSTau4          ;
      TH1D * h_ak8miniAOD_CHSTau32         ;
      TH1D * h_ak8miniAOD_CHSTau21         ;
      TH1D * h_ak8miniAOD_PuppiECFnb1N2         ;
      TH1D * h_ak8miniAOD_PuppiECFnb1N3         ;
      TH1D * h_ak8miniAOD_PuppiECFnb2N2         ;
      TH1D * h_ak8miniAOD_PuppiECFnb2N3         ;
      TH1D * h_ak8miniAOD_ndau          ;
      TH1D * h_ak8miniAOD_area          ;
      TH1D * h_ak8miniAOD_subjetMass    ;  
      TH1D * h_ak8miniAOD_subjetPt    ;  
      TH1D * h_ak8miniAOD_subjetEta    ;  
      TH1D * h_ak8miniAOD_subjetPhi    ;  
      TH1D * h_ak8miniAOD_subjetBdisc    ;  

      TH1D * h_ak8puppiupdated_pt            ;
      TH1D * h_ak8puppiupdated_mass          ;
      TH1D * h_ak8puppiupdated_eta      ;
      TH1D * h_ak8puppiupdated_phi      ;
      TH1D * h_ak8puppiupdated_CHSPrunedMass    ;
      TH1D * h_ak8puppiupdated_CHSSoftDropMass    ;
      TH1D * h_ak8puppiupdated_PuppiSoftDropMass    ;
      TH1D * h_ak8puppiupdated_PuppiTau1          ;
      TH1D * h_ak8puppiupdated_PuppiTau2          ;
      TH1D * h_ak8puppiupdated_PuppiTau3          ;
      TH1D * h_ak8puppiupdated_PuppiTau4          ;
      TH1D * h_ak8puppiupdated_PuppiTau32         ;
      TH1D * h_ak8puppiupdated_PuppiTau21         ;
      TH1D * h_ak8puppiupdated_CHSTau1          ;
      TH1D * h_ak8puppiupdated_CHSTau2          ;
      TH1D * h_ak8puppiupdated_CHSTau3          ;
      TH1D * h_ak8puppiupdated_CHSTau4          ;
      TH1D * h_ak8puppiupdated_CHSTau32         ;
      TH1D * h_ak8puppiupdated_CHSTau21         ;
      TH1D * h_ak8puppiupdated_PuppiECFnb1N2         ;
      TH1D * h_ak8puppiupdated_PuppiECFnb1N3         ;
      TH1D * h_ak8puppiupdated_PuppiECFnb2N2         ;
      TH1D * h_ak8puppiupdated_PuppiECFnb2N3         ;
      TH1D * h_ak8puppiupdated_ndau          ;
      TH1D * h_ak8puppiupdated_area          ;
      TH1D * h_ak8puppiupdated_doubleB ;  
      TH1D * h_ak8puppiupdated_deepDoubleBvLQCD ;  
      TH1D * h_ak8puppiupdated_deepDoubleBvLHbb ;  
      TH1D * h_ak8puppiupdated_deepDoubleCvLQCD ;  
      TH1D * h_ak8puppiupdated_deepDoubleCvLHcc ;  
      TH1D * h_ak8puppiupdated_deepDoubleCvBHbb ;  
      TH1D * h_ak8puppiupdated_deepDoubleCvBHcc ;  
      TH1D * h_ak8puppiupdated_deepBoostedJetbbvsl;  
      TH1D * h_ak8puppiupdated_deepBoostedJetccvsl;  
      TH1D * h_ak8puppiupdated_deepBoostedJetTvsQCD;  
      TH1D * h_ak8puppiupdated_deepBoostedJetZHccvsQCD;  
      TH1D * h_ak8puppiupdated_deepBoostedJetWvsQCD;  
      TH1D * h_ak8puppiupdated_deepBoostedJetZHbbvsQCD;  
      TH1D * h_ak8puppiupdated_subjetMass    ;  
      TH1D * h_ak8puppiupdated_subjetPt    ;  
      TH1D * h_ak8puppiupdated_subjetEta    ;  
      TH1D * h_ak8puppiupdated_subjetPhi    ;  
      TH1D * h_ak8puppiupdated_subjetBdisc    ;  

      TH1D * h_ak8puppi_pt            ;
      TH1D * h_ak8puppi_mass          ;
      TH1D * h_ak8puppi_eta      ;
      TH1D * h_ak8puppi_phi      ;
      TH1D * h_ak8puppi_PrunedMass    ;
      TH1D * h_ak8puppi_SoftDropMass    ;
      TH1D * h_ak8puppi_TrimmedMass    ;
      TH1D * h_ak8puppi_FilteredMass    ;
      TH1D * h_ak8puppi_Tau1          ;
      TH1D * h_ak8puppi_Tau2          ;
      TH1D * h_ak8puppi_Tau3          ;
      TH1D * h_ak8puppi_Tau4          ;
      TH1D * h_ak8puppi_Tau32         ;
      TH1D * h_ak8puppi_Tau21         ;
      TH1D * h_ak8puppi_ECFnb1N2         ;
      TH1D * h_ak8puppi_ECFnb1N3         ;
      TH1D * h_ak8puppi_ndau          ;
      TH1D * h_ak8puppi_area          ;
      TH1D * h_ak8puppi_doubleB ;  
      TH1D * h_ak8puppi_subjetMass    ;  
      TH1D * h_ak8puppi_subjetPt    ;  
      TH1D * h_ak8puppi_subjetEta    ;  
      TH1D * h_ak8puppi_subjetPhi    ;  
      TH1D * h_ak8puppi_subjetBdisc    ;  


      TH1D * h_ak8chs_pt            ;
      TH1D * h_ak8chs_mass          ;
      TH1D * h_ak8chs_eta      ;
      TH1D * h_ak8chs_phi      ;
      TH1D * h_ak8chs_PrunedMass    ;
      TH1D * h_ak8chs_SoftDropMass    ;
      TH1D * h_ak8chs_TrimmedMass    ;
      TH1D * h_ak8chs_FilteredMass    ;
      TH1D * h_ak8chs_Tau1          ;
      TH1D * h_ak8chs_Tau2          ;
      TH1D * h_ak8chs_Tau3          ;
      TH1D * h_ak8chs_Tau4          ;
      TH1D * h_ak8chs_Tau32         ;
      TH1D * h_ak8chs_Tau21         ;
      TH1D * h_ak8chs_ndau          ;
      TH1D * h_ak8chs_area          ;
      TH1D * h_ak8chs_doubleB ;  
      TH1D * h_ak8chs_subjetMass    ;  
      TH1D * h_ak8chs_subjetPt    ;  
      TH1D * h_ak8chs_subjetEta    ;  
      TH1D * h_ak8chs_subjetPhi    ;  
      TH1D * h_ak8chs_subjetBdisc    ;  

      TH1D * h_ca8chs_pt            ;
      TH1D * h_ca8chs_mass          ;
      TH1D * h_ca8chs_eta      ;
      TH1D * h_ca8chs_phi      ;
      TH1D * h_ca8chs_PrunedMass    ;
      TH1D * h_ca8chs_SoftDropMass    ;
      TH1D * h_ca8chs_Tau1          ;
      TH1D * h_ca8chs_Tau2          ;
      TH1D * h_ca8chs_Tau3          ;
      TH1D * h_ca8chs_Tau4          ;
      TH1D * h_ca8chs_Tau32         ;
      TH1D * h_ca8chs_Tau21         ;
      TH1D * h_ca8chs_ndau          ;
      TH1D * h_ca8chs_area          ;
      TH1D * h_ca8chs_doubleB ;  
      TH1D * h_ca8chs_subjetMass    ;  
      TH1D * h_ca8chs_subjetPt    ;  
      TH1D * h_ca8chs_subjetEta    ;  
      TH1D * h_ca8chs_subjetPhi    ;  
      TH1D * h_ca8chs_subjetBdisc    ;  

      TH1D * h_kt8chs_pt            ;
      TH1D * h_kt8chs_mass          ;
      TH1D * h_kt8chs_eta      ;
      TH1D * h_kt8chs_phi      ;
      TH1D * h_kt8chs_PrunedMass    ;
      TH1D * h_kt8chs_SoftDropMass    ;
      TH1D * h_kt8chs_Tau1          ;
      TH1D * h_kt8chs_Tau2          ;
      TH1D * h_kt8chs_Tau3          ;
      TH1D * h_kt8chs_Tau4          ;
      TH1D * h_kt8chs_Tau32         ;
      TH1D * h_kt8chs_Tau21         ;
      TH1D * h_kt8chs_ndau          ;
      TH1D * h_kt8chs_area          ;
      TH1D * h_kt8chs_doubleB ;  
      TH1D * h_kt8chs_subjetMass    ;  
      TH1D * h_kt8chs_subjetPt    ;  
      TH1D * h_kt8chs_subjetEta    ;  
      TH1D * h_kt8chs_subjetPhi    ;  
      TH1D * h_kt8chs_subjetBdisc    ;  

      TH1D * h_ak8puppimodsd_pt            ;
      TH1D * h_ak8puppimodsd_mass          ;
      TH1D * h_ak8puppimodsd_eta      ;
      TH1D * h_ak8puppimodsd_phi      ;
      TH1D * h_ak8puppimodsd_SoftDropMass    ;

      TH1D * h_ak8sk_pt            ;
      TH1D * h_ak8sk_mass          ;
      TH1D * h_ak8sk_eta      ;
      TH1D * h_ak8sk_phi      ;
      TH1D * h_ak8sk_SoftDropMass    ;

      TH1D * h_ak8cs_pt            ;
      TH1D * h_ak8cs_mass          ;
      TH1D * h_ak8cs_eta      ;
      TH1D * h_ak8cs_phi      ;
      TH1D * h_ak8cs_SoftDropMass    ;





      TH1D * h_ak12chs_pt            ;
      TH1D * h_ak12chs_mass          ;
      TH1D * h_ak12chs_eta      ;
      TH1D * h_ak12chs_prunedMass    ;
      TH1D * h_ak12chs_trimmedMass   ;
      TH1D * h_ak12chs_filteredMass  ;
      TH1D * h_ak12chs_softDropMass  ;
      TH1D * h_ak12chs_tau1          ;
      TH1D * h_ak12chs_tau2          ;
      TH1D * h_ak12chs_tau3          ;
      TH1D * h_ak12chs_tau4          ;
      TH1D * h_ak12chs_tau32         ;
      TH1D * h_ak12chs_tau21         ;
      TH1D * h_ak12chs_ndau          ;
      TH1D * h_ak12chs_subjetMass    ;  
      TH1D * h_ak12chs_area          ;  
      TH1D * h_ak12chs_pt200_mass          ; 
      TH1D * h_ak12chs_pt200_prunedMass    ; 
      TH1D * h_ak12chs_pt200_trimmedMass   ; 
      TH1D * h_ak12chs_pt200_filteredMass  ; 
      TH1D * h_ak12chs_pt200_softDropMass  ; 
      TH1D * h_ak12chs_pt200_tau32         ; 
      TH1D * h_ak12chs_pt200_tau21         ; 
      TH1D * h_ak12chs_pt200_subjetMass    ; 
      TH1D * h_ak12chs_pt500_mass          ; 
      TH1D * h_ak12chs_pt500_prunedMass    ; 
      TH1D * h_ak12chs_pt500_trimmedMass   ; 
      TH1D * h_ak12chs_pt500_filteredMass  ; 
      TH1D * h_ak12chs_pt500_softDropMass  ; 
      TH1D * h_ak12chs_pt500_tau32         ; 
      TH1D * h_ak12chs_pt500_tau21         ; 
      TH1D * h_ak12chs_pt500_subjetMass    ; 

      TH1D * h_ak15chs_pt            ;
      TH1D * h_ak15chs_mass          ;
      TH1D * h_ak15chs_eta      ;
      TH1D * h_ak15chs_prunedMass    ;
      TH1D * h_ak15chs_trimmedMass   ;
      TH1D * h_ak15chs_filteredMass  ;
      TH1D * h_ak15chs_softDropMass  ;
      TH1D * h_ak15chs_tau1          ;
      TH1D * h_ak15chs_tau2          ;
      TH1D * h_ak15chs_tau3          ;
      TH1D * h_ak15chs_tau4          ;
      TH1D * h_ak15chs_tau32         ;
      TH1D * h_ak15chs_tau21         ;
      TH1D * h_ak15chs_ndau          ;
      TH1D * h_ak15chs_subjetMass    ;  
      TH1D * h_ak15chs_area          ;  
      TH1D * h_ak15chs_pt200_mass          ; 
      TH1D * h_ak15chs_pt200_prunedMass    ; 
      TH1D * h_ak15chs_pt200_trimmedMass   ; 
      TH1D * h_ak15chs_pt200_filteredMass  ; 
      TH1D * h_ak15chs_pt200_softDropMass  ; 
      TH1D * h_ak15chs_pt200_tau32         ; 
      TH1D * h_ak15chs_pt200_tau21         ; 
      TH1D * h_ak15chs_pt200_subjetMass    ; 
      TH1D * h_ak15chs_pt500_mass          ; 
      TH1D * h_ak15chs_pt500_prunedMass    ; 
      TH1D * h_ak15chs_pt500_trimmedMass   ; 
      TH1D * h_ak15chs_pt500_filteredMass  ; 
      TH1D * h_ak15chs_pt500_softDropMass  ; 
      TH1D * h_ak15chs_pt500_tau32         ; 
      TH1D * h_ak15chs_pt500_tau21         ; 
      TH1D * h_ak15chs_pt500_subjetMass    ; 
};

//
// constructors and destructor
//
JetTester::JetTester(const edm::ParameterSet& iConfig):
    ak4PFCHSminiAODjetToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJets"))),
    ak4PFPuppiminiAODjetToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJetsPuppi"))),
    ak4PFCHSUpdatedjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK4PFCHSUpdated"))),
    ak4PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK4PFCHS"))),
    ak4PFPuppijetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK4PFPuppi"))),
    ak4PFjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK4PFPlain"))),
    ak8PFPuppiminiAODjetToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJetsAK8"))),
    ak8PFPuppiUpdatedjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFPuppiUpdated"))),
    ak8PFPuppijetToken_(consumes<pat::JetCollection>(edm::InputTag("packedPatJetsAK8PFPuppiSoftDrop"))),
    ak8PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("packedPatJetsAK8PFCHSSoftDrop"))),
    ca8PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsCA8PFCHS"))),
    kt8PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsKT8PFCHS"))),
    ak8PFPuppimodSDjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFPuppimodSD"))),
    ak8PFSKjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFSK"))),
    ak8PFCSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFCS"))),

    ca12PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsHEPTopTagCHS"))),
    //ca12PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("hepTopTagPFJetsCHS"))),
    ak15PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK15PFCHS"))),

    //ak4genjetToken_(consumes<reco::GenJetCollection>(edm::InputTag("slimmedGenJets"))),
    //ak8genjetToken_(consumes<reco::GenJetCollection>(edm::InputTag("slimmedGenJetsAK8"))),
    prunedGenToken_(consumes<edm::View<reco::GenParticle> >(edm::InputTag("prunedGenParticles"))),
    rhoToken_(consumes<double>(edm::InputTag("fixedGridRhoFastjetAll"))),
    vtxToken_(consumes<std::vector<reco::Vertex> >(edm::InputTag("offlineSlimmedPrimaryVertices")))
{

  edm::Service<TFileService> fs;
  h_ak4chsminiAOD_pt                  =  fs->make<TH1D>("h_ak4chsminiAOD_pt"                     ,"",100,0,3000); 
  h_ak4chsminiAOD_uncpt          =  fs->make<TH1D>("h_ak4chsminiAOD_uncpt"                     ,"",100,0,3000); 
  h_ak4chsminiAOD_eta            =  fs->make<TH1D>("h_ak4chsminiAOD_eta"               ,"",100,-5, 5); 
  h_ak4chsminiAOD_btagCSVv2            =  fs->make<TH1D>("h_ak4chsminiAOD_btagCSVv2"               ,"",20, 0, 1); 
  h_ak4chsminiAOD_area                =  fs->make<TH1D>("h_ak4chsminiAOD_area"                   ,"",100,0,  8); 
  h_ak4chsminiAOD_nhf                =  fs->make<TH1D>("h_ak4chsminiAOD_nhf"                   ,"",20, 0, 1); 
  h_ak4chsminiAOD_nemf                =  fs->make<TH1D>("h_ak4chsminiAOD_nemf"                   ,"",20, 0, 1); 
  h_ak4chsminiAOD_chf                =  fs->make<TH1D>("h_ak4chsminiAOD_chf"                   ,"",20, 0, 1); 
  h_ak4chsminiAOD_muf                =  fs->make<TH1D>("h_ak4chsminiAOD_muf"                   ,"",20, 0, 1); 
  h_ak4chsminiAOD_cemf                =  fs->make<TH1D>("h_ak4chsminiAOD_cemf"                   ,"",20, 0, 1); 
  h_ak4chsminiAOD_numConst                =  fs->make<TH1D>("h_ak4chsminiAOD_numConst"                   ,"",100, 0, 100); 
  h_ak4chsminiAOD_numNeuPar                =  fs->make<TH1D>("h_ak4chsminiAOD_numNeuPar"                   ,"",100, 0, 100); 
  h_ak4chsminiAOD_chm                =  fs->make<TH1D>("h_ak4chsminiAOD_chm"                   ,"",100, 0, 100); 
  h_ak4puppiminiAOD_pt                  =  fs->make<TH1D>("h_ak4puppiminiAOD_pt"                     ,"",100,0,3000); 
  h_ak4puppiminiAOD_uncpt          =  fs->make<TH1D>("h_ak4puppiminiAOD_uncpt"                     ,"",100,0,3000); 
  h_ak4puppiminiAOD_eta            =  fs->make<TH1D>("h_ak4puppiminiAOD_eta"               ,"",100,-5, 5); 
  h_ak4puppiminiAOD_btagCSVv2            =  fs->make<TH1D>("h_ak4puppiminiAOD_btagCSVv2"               ,"",20, 0, 1); 
  h_ak4puppiminiAOD_area                =  fs->make<TH1D>("h_ak4puppiminiAOD_area"                   ,"",100,0,  8); 
  h_ak4puppiminiAOD_nhf                =  fs->make<TH1D>("h_ak4puppiminiAOD_nhf"                   ,"",20, 0, 1); 
  h_ak4puppiminiAOD_nemf                =  fs->make<TH1D>("h_ak4puppiminiAOD_nemf"                   ,"",20, 0, 1); 
  h_ak4puppiminiAOD_chf                =  fs->make<TH1D>("h_ak4puppiminiAOD_chf"                   ,"",20, 0, 1); 
  h_ak4puppiminiAOD_muf                =  fs->make<TH1D>("h_ak4puppiminiAOD_muf"                   ,"",20, 0, 1); 
  h_ak4puppiminiAOD_cemf                =  fs->make<TH1D>("h_ak4puppiminiAOD_cemf"                   ,"",20, 0, 1); 
  h_ak4puppiminiAOD_numConst                =  fs->make<TH1D>("h_ak4puppiminiAOD_numConst"                   ,"",100, 0, 100); 
  h_ak4puppiminiAOD_numNeuPar                =  fs->make<TH1D>("h_ak4puppiminiAOD_numNeuPar"                   ,"",100, 0, 100); 
  h_ak4puppiminiAOD_chm                =  fs->make<TH1D>("h_ak4puppiminiAOD_chm"                   ,"",100, 0, 100); 

  h_ak4chsupdated_pt             =  fs->make<TH1D>("h_ak4chsupdated_pt"                     ,"",100,0,3000); 
  h_ak4chsupdated_uncpt          =  fs->make<TH1D>("h_ak4chsupdated_uncpt"                     ,"",100,0,3000); 
  h_ak4chsupdated_eta            =  fs->make<TH1D>("h_ak4chsupdated_eta"               ,"",100,-5, 5); 
  h_ak4chsupdated_btagCSVv2            =  fs->make<TH1D>("h_ak4chsupdated_btagCSVv2"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagCvsL            =  fs->make<TH1D>("h_ak4chsupdated_btagCvsL"               ,"",40,-1, 1); 
  h_ak4chsupdated_btagCvsB            =  fs->make<TH1D>("h_ak4chsupdated_btagCvsB"               ,"",40,-1, 1); 
  h_ak4chsupdated_btagDeepCSVb            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepCSVb"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepCSVbb            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepCSVbb"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepCSVc            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepCSVc"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepCSVl            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepCSVl"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepFlavourb            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepFlavourb"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepFlavourbb            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepFlavourbb"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepFlavourc            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepFlavourc"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepFlavourl            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepFlavourl"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepFlavourg            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepFlavourg"               ,"",20, 0, 1); 
  h_ak4chsupdated_btagDeepFlavourlepb            =  fs->make<TH1D>("h_ak4chsupdated_btagDeepFlavourlepb"               ,"",20, 0, 1); 
  h_ak4chsupdated_area                =  fs->make<TH1D>("h_ak4chsupdated_area"                   ,"",100,0,  8); 
  h_ak4chsupdated_nhf                =  fs->make<TH1D>("h_ak4chsupdated_nhf"                   ,"",20, 0, 1); 
  h_ak4chsupdated_nemf                =  fs->make<TH1D>("h_ak4chsupdated_nemf"                   ,"",20, 0, 1); 
  h_ak4chsupdated_chf                =  fs->make<TH1D>("h_ak4chsupdated_chf"                   ,"",20, 0, 1); 
  h_ak4chsupdated_muf                =  fs->make<TH1D>("h_ak4chsupdated_muf"                   ,"",20, 0, 1); 
  h_ak4chsupdated_cemf                =  fs->make<TH1D>("h_ak4chsupdated_cemf"                   ,"",20, 0, 1); 
  h_ak4chsupdated_numConst                =  fs->make<TH1D>("h_ak4chsupdated_numConst"                   ,"",100, 0, 100); 
  h_ak4chsupdated_numNeuPar                =  fs->make<TH1D>("h_ak4chsupdated_numNeuPar"                   ,"",100, 0, 100); 
  h_ak4chsupdated_chm                =  fs->make<TH1D>("h_ak4chsupdated_chm"                   ,"",100, 0, 100); 

  h_ak4chs_pt                  =  fs->make<TH1D>("h_ak4chs_pt"                     ,"",100,0,3000); 
  h_ak4chs_uncpt          =  fs->make<TH1D>("h_ak4chs_uncpt"                     ,"",100,0,3000); 
  h_ak4chs_eta            =  fs->make<TH1D>("h_ak4chs_eta"               ,"",100,-5, 5); 
  h_ak4chs_btagCSVv2            =  fs->make<TH1D>("h_ak4chs_btagCSVv2"               ,"",20, 0, 1); 
  h_ak4chs_pileupJetId                =  fs->make<TH1D>("h_ak4chs_pileupJetId"                   ,"",20, 0, 1); 
  h_ak4chs_qglikelihood                =  fs->make<TH1D>("h_ak4chs_qglikelihood"                   ,"",20, 0, 1); 
  h_ak4chs_area                =  fs->make<TH1D>("h_ak4chs_area"                   ,"",100,0,  8); 
  h_ak4chs_nhf                =  fs->make<TH1D>("h_ak4chs_nhf"                   ,"",20, 0, 1); 
  h_ak4chs_nemf                =  fs->make<TH1D>("h_ak4chs_nemf"                   ,"",20, 0, 1); 
  h_ak4chs_chf                =  fs->make<TH1D>("h_ak4chs_chf"                   ,"",20, 0, 1); 
  h_ak4chs_muf                =  fs->make<TH1D>("h_ak4chs_muf"                   ,"",20, 0, 1); 
  h_ak4chs_cemf                =  fs->make<TH1D>("h_ak4chs_cemf"                   ,"",20, 0, 1); 
  h_ak4chs_numConst                =  fs->make<TH1D>("h_ak4chs_numConst"                   ,"",100, 0, 100); 
  h_ak4chs_numNeuPar                =  fs->make<TH1D>("h_ak4chs_numNeuPar"                   ,"",100, 0, 100); 
  h_ak4chs_chm                =  fs->make<TH1D>("h_ak4chs_chm"                   ,"",100, 0, 100); 

  h_ak4puppi_pt                  =  fs->make<TH1D>("h_ak4puppi_pt"                     ,"",100,0,3000); 
  h_ak4puppi_uncpt          =  fs->make<TH1D>("h_ak4puppi_uncpt"                     ,"",100,0,3000); 
  h_ak4puppi_eta            =  fs->make<TH1D>("h_ak4puppi_eta"               ,"",100,-5, 5); 
  h_ak4puppi_btagCSVv2            =  fs->make<TH1D>("h_ak4puppi_btagCSVv2"               ,"",20, 0, 1); 
  h_ak4puppi_area                =  fs->make<TH1D>("h_ak4puppi_area"                   ,"",100,0,  8); 
  h_ak4puppi_nhf                =  fs->make<TH1D>("h_ak4puppi_nhf"                   ,"",20, 0, 1); 
  h_ak4puppi_nemf                =  fs->make<TH1D>("h_ak4puppi_nemf"                   ,"",20, 0, 1); 
  h_ak4puppi_chf                =  fs->make<TH1D>("h_ak4puppi_chf"                   ,"",20, 0, 1); 
  h_ak4puppi_muf                =  fs->make<TH1D>("h_ak4puppi_muf"                   ,"",20, 0, 1); 
  h_ak4puppi_cemf                =  fs->make<TH1D>("h_ak4puppi_cemf"                   ,"",20, 0, 1); 
  h_ak4puppi_numConst                =  fs->make<TH1D>("h_ak4puppi_numConst"                   ,"",100, 0, 100); 
  h_ak4puppi_numNeuPar                =  fs->make<TH1D>("h_ak4puppi_numNeuPar"                   ,"",100, 0, 100); 
  h_ak4puppi_chm                =  fs->make<TH1D>("h_ak4puppi_chm"                   ,"",100, 0, 100); 


  h_ak4pf_pt                  =  fs->make<TH1D>("h_ak4pf_pt"                     ,"",100,0,3000); 
  h_ak4pf_uncpt          =  fs->make<TH1D>("h_ak4pf_uncpt"                     ,"",100,0,3000); 
  h_ak4pf_eta            =  fs->make<TH1D>("h_ak4pf_eta"               ,"",100,-5, 5); 
  h_ak4pf_btagCSVv2            =  fs->make<TH1D>("h_ak4pf_btagCSVv2"               ,"",20, 0, 1); 
  h_ak4pf_area                =  fs->make<TH1D>("h_ak4pf_area"                   ,"",100,0,  8); 
  h_ak4pf_nhf                =  fs->make<TH1D>("h_ak4pf_nhf"                   ,"",20, 0, 1); 
  h_ak4pf_nemf                =  fs->make<TH1D>("h_ak4pf_nemf"                   ,"",20, 0, 1); 
  h_ak4pf_chf                =  fs->make<TH1D>("h_ak4pf_chf"                   ,"",20, 0, 1); 
  h_ak4pf_muf                =  fs->make<TH1D>("h_ak4pf_muf"                   ,"",20, 0, 1); 
  h_ak4pf_cemf                =  fs->make<TH1D>("h_ak4pf_cemf"                   ,"",20, 0, 1); 
  h_ak4pf_numConst                =  fs->make<TH1D>("h_ak4pf_numConst"                   ,"",100, 0, 100); 
  h_ak4pf_numNeuPar                =  fs->make<TH1D>("h_ak4pf_numNeuPar"                   ,"",100, 0, 100); 
  h_ak4pf_chm                =  fs->make<TH1D>("h_ak4pf_chm"                   ,"",100, 0, 100); 

  h_ak8miniAOD_pt                  =  fs->make<TH1D>("h_ak8miniAOD_pt"                     ,"",100,0,3000); 
  h_ak8miniAOD_mass                =  fs->make<TH1D>("h_ak8miniAOD_mass"                   ,"",100,0,500); 
  h_ak8miniAOD_eta            =  fs->make<TH1D>("h_ak8miniAOD_eta"               ,"",100,-5, 5); 
  h_ak8miniAOD_phi            =  fs->make<TH1D>("h_ak8miniAOD_phi"               ,"",100,-5, 5); 
  h_ak8miniAOD_CHSPrunedMass          =  fs->make<TH1D>("h_ak8miniAOD_CHSPrunedMass"             ,"",100,0,500); 
  h_ak8miniAOD_CHSSoftDropMass          =  fs->make<TH1D>("h_ak8miniAOD_CHSSoftDropMass"             ,"",100,0,500); 
  h_ak8miniAOD_PuppiSoftDropMass          =  fs->make<TH1D>("h_ak8miniAOD_PuppiSoftDropMass"             ,"",100,0,500); 
  h_ak8miniAOD_PuppiTau1                =  fs->make<TH1D>("h_ak8miniAOD_PuppiTau1"                   ,"",100,0,  1); 
  h_ak8miniAOD_PuppiTau2                =  fs->make<TH1D>("h_ak8miniAOD_PuppiTau2"                   ,"",100,0,  1); 
  h_ak8miniAOD_PuppiTau3                =  fs->make<TH1D>("h_ak8miniAOD_PuppiTau3"                   ,"",100,0,  1); 
  h_ak8miniAOD_PuppiTau4                =  fs->make<TH1D>("h_ak8miniAOD_PuppiTau4"                   ,"",100,0,  1); 
  h_ak8miniAOD_PuppiTau32               =  fs->make<TH1D>("h_ak8miniAOD_PuppiTau32"                  ,"",100,0,  1); 
  h_ak8miniAOD_PuppiTau21               =  fs->make<TH1D>("h_ak8miniAOD_PuppiTau21"                  ,"",100,0,  1); 
  h_ak8miniAOD_CHSTau1                =  fs->make<TH1D>("h_ak8miniAOD_CHSTau1"                   ,"",100,0,  1); 
  h_ak8miniAOD_CHSTau2                =  fs->make<TH1D>("h_ak8miniAOD_CHSTau2"                   ,"",100,0,  1); 
  h_ak8miniAOD_CHSTau3                =  fs->make<TH1D>("h_ak8miniAOD_CHSTau3"                   ,"",100,0,  1); 
  h_ak8miniAOD_CHSTau4                =  fs->make<TH1D>("h_ak8miniAOD_CHSTau4"                   ,"",100,0,  1); 
  h_ak8miniAOD_CHSTau32               =  fs->make<TH1D>("h_ak8miniAOD_CHSTau32"                  ,"",100,0,  1); 
  h_ak8miniAOD_CHSTau21               =  fs->make<TH1D>("h_ak8miniAOD_CHSTau21"                  ,"",100,0,  1); 
  h_ak8miniAOD_PuppiECFnb1N2          =  fs->make<TH1D>("h_ak8miniAOD_PuppiECFnb1N2"                  ,"",100,-1,  1); 
  h_ak8miniAOD_PuppiECFnb1N3          =  fs->make<TH1D>("h_ak8miniAOD_PuppiECFnb1N3"                  ,"",100,-1,  1); 
  h_ak8miniAOD_PuppiECFnb2N2          =  fs->make<TH1D>("h_ak8miniAOD_PuppiECFnb2N2"                  ,"",100,-1,  1); 
  h_ak8miniAOD_PuppiECFnb2N3          =  fs->make<TH1D>("h_ak8miniAOD_PuppiECFnb2N3"                  ,"",100,-1,  1); 
  h_ak8miniAOD_area                =  fs->make<TH1D>("h_ak8miniAOD_area"                   ,"",100,0,  8); 
  h_ak8miniAOD_ndau                =  fs->make<TH1D>("h_ak8miniAOD_ndau"                   ,"",300,0,300); 
  h_ak8miniAOD_subjetMass          =  fs->make<TH1D>("h_ak8miniAOD_subjetMass"             ,"",100,0,400); 
  h_ak8miniAOD_subjetPt                  =  fs->make<TH1D>("h_ak8miniAOD_subjetPt"                     ,"",100,0,3000); 
  h_ak8miniAOD_subjetEta            =  fs->make<TH1D>("h_ak8miniAOD_subjetEta"               ,"",100,-5, 5); 
  h_ak8miniAOD_subjetPhi            =  fs->make<TH1D>("h_ak8miniAOD_subjetPhi"               ,"",100,-5, 5); 
  h_ak8miniAOD_subjetBdisc                =  fs->make<TH1D>("h_ak8miniAOD_subjetBdisc"                   ,"",100,0,  1); 



  h_ak8puppiupdated_pt                  =  fs->make<TH1D>("h_ak8puppiupdated_pt"                     ,"",100,0,3000); 
  h_ak8puppiupdated_mass                =  fs->make<TH1D>("h_ak8puppiupdated_mass"                   ,"",100,0,500); 
  h_ak8puppiupdated_eta            =  fs->make<TH1D>("h_ak8puppiupdated_eta"               ,"",100,-5, 5); 
  h_ak8puppiupdated_phi            =  fs->make<TH1D>("h_ak8puppiupdated_phi"               ,"",100,-5, 5); 
  h_ak8puppiupdated_CHSPrunedMass          =  fs->make<TH1D>("h_ak8puppiupdated_CHSPrunedMass"             ,"",100,0,500); 
  h_ak8puppiupdated_CHSSoftDropMass          =  fs->make<TH1D>("h_ak8puppiupdated_CHSSoftDropMass"             ,"",100,0,500); 
  h_ak8puppiupdated_PuppiSoftDropMass          =  fs->make<TH1D>("h_ak8puppiupdated_PuppiSoftDropMass"             ,"",100,0,500); 
  h_ak8puppiupdated_PuppiTau1                =  fs->make<TH1D>("h_ak8puppiupdated_PuppiTau1"                   ,"",100,0,  1); 
  h_ak8puppiupdated_PuppiTau2                =  fs->make<TH1D>("h_ak8puppiupdated_PuppiTau2"                   ,"",100,0,  1); 
  h_ak8puppiupdated_PuppiTau3                =  fs->make<TH1D>("h_ak8puppiupdated_PuppiTau3"                   ,"",100,0,  1); 
  h_ak8puppiupdated_PuppiTau4                =  fs->make<TH1D>("h_ak8puppiupdated_PuppiTau4"                   ,"",100,0,  1); 
  h_ak8puppiupdated_PuppiTau32               =  fs->make<TH1D>("h_ak8puppiupdated_PuppiTau32"                  ,"",100,0,  1); 
  h_ak8puppiupdated_PuppiTau21               =  fs->make<TH1D>("h_ak8puppiupdated_PuppiTau21"                  ,"",100,0,  1); 
  h_ak8puppiupdated_CHSTau1                =  fs->make<TH1D>("h_ak8puppiupdated_CHSTau1"                   ,"",100,0,  1); 
  h_ak8puppiupdated_CHSTau2                =  fs->make<TH1D>("h_ak8puppiupdated_CHSTau2"                   ,"",100,0,  1); 
  h_ak8puppiupdated_CHSTau3                =  fs->make<TH1D>("h_ak8puppiupdated_CHSTau3"                   ,"",100,0,  1); 
  h_ak8puppiupdated_CHSTau4                =  fs->make<TH1D>("h_ak8puppiupdated_CHSTau4"                   ,"",100,0,  1); 
  h_ak8puppiupdated_CHSTau32               =  fs->make<TH1D>("h_ak8puppiupdated_CHSTau32"                  ,"",100,0,  1); 
  h_ak8puppiupdated_CHSTau21               =  fs->make<TH1D>("h_ak8puppiupdated_CHSTau21"                  ,"",100,0,  1); 
  h_ak8puppiupdated_PuppiECFnb1N2          =  fs->make<TH1D>("h_ak8puppiupdated_PuppiECFnb1N2"                  ,"",100,-1,  1); 
  h_ak8puppiupdated_PuppiECFnb1N3          =  fs->make<TH1D>("h_ak8puppiupdated_PuppiECFnb1N3"                  ,"",100,-1,  1); 
  h_ak8puppiupdated_PuppiECFnb2N2          =  fs->make<TH1D>("h_ak8puppiupdated_PuppiECFnb2N2"                  ,"",100,-1,  1); 
  h_ak8puppiupdated_PuppiECFnb2N3          =  fs->make<TH1D>("h_ak8puppiupdated_PuppiECFnb2N3"                  ,"",100,-1,  1); 
  h_ak8puppiupdated_area                =  fs->make<TH1D>("h_ak8puppiupdated_area"                   ,"",100,0,  8); 
  h_ak8puppiupdated_doubleB                =  fs->make<TH1D>("h_ak8puppiupdated_doubleB"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepDoubleBvLQCD                =  fs->make<TH1D>("h_ak8puppiupdated_deepDoubleBvLQCD"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepDoubleBvLHbb                =  fs->make<TH1D>("h_ak8puppiupdated_deepDoubleBvLHbb"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepDoubleCvLQCD                =  fs->make<TH1D>("h_ak8puppiupdated_deepDoubleCvLQCD"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepDoubleCvLHcc                =  fs->make<TH1D>("h_ak8puppiupdated_deepDoubleCvLHcc"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepDoubleCvBHbb                =  fs->make<TH1D>("h_ak8puppiupdated_deepDoubleCvBHbb"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepDoubleCvBHcc                =  fs->make<TH1D>("h_ak8puppiupdated_deepDoubleCvBHcc"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepBoostedJetbbvsl                =  fs->make<TH1D>("h_ak8puppiupdated_deepBoostedJetbbvsl"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepBoostedJetccvsl                =  fs->make<TH1D>("h_ak8puppiupdated_deepBoostedJetccvsl"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepBoostedJetTvsQCD                =  fs->make<TH1D>("h_ak8puppiupdated_deepBoostedJetTvsQCD"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepBoostedJetZHccvsQCD                =  fs->make<TH1D>("h_ak8puppiupdated_deepBoostedJetZHccvsQCD"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepBoostedJetWvsQCD                =  fs->make<TH1D>("h_ak8puppiupdated_deepBoostedJetWvsQCD"                   ,"",100,0,  1); 
  h_ak8puppiupdated_deepBoostedJetZHbbvsQCD                =  fs->make<TH1D>("h_ak8puppiupdated_deepBoostedJetZHbbvsQCD"                   ,"",100,0,  1); 
  h_ak8puppiupdated_ndau                =  fs->make<TH1D>("h_ak8puppiupdated_ndau"                   ,"",300,0,300); 
  h_ak8puppiupdated_subjetMass          =  fs->make<TH1D>("h_ak8puppiupdated_subjetMass"             ,"",100,0,400); 
  h_ak8puppiupdated_subjetPt                  =  fs->make<TH1D>("h_ak8puppiupdated_subjetPt"                     ,"",100,0,3000); 
  h_ak8puppiupdated_subjetEta            =  fs->make<TH1D>("h_ak8puppiupdated_subjetEta"               ,"",100,-5, 5); 
  h_ak8puppiupdated_subjetPhi            =  fs->make<TH1D>("h_ak8puppiupdated_subjetPhi"               ,"",100,-5, 5); 
  h_ak8puppiupdated_subjetBdisc                =  fs->make<TH1D>("h_ak8puppiupdated_subjetBdisc"                   ,"",100,0,  1); 


  h_ak8puppi_pt                  =  fs->make<TH1D>("h_ak8puppi_pt"                     ,"",100,0,3000); 
  h_ak8puppi_mass                =  fs->make<TH1D>("h_ak8puppi_mass"                   ,"",100,0,500); 
  h_ak8puppi_eta            =  fs->make<TH1D>("h_ak8puppi_eta"               ,"",100,-5, 5); 
  h_ak8puppi_phi            =  fs->make<TH1D>("h_ak8puppi_phi"               ,"",100,-5, 5); 
  h_ak8puppi_PrunedMass          =  fs->make<TH1D>("h_ak8puppi_PrunedMass"             ,"",100,0,500); 
  h_ak8puppi_SoftDropMass          =  fs->make<TH1D>("h_ak8puppi_SoftDropMass"             ,"",100,0,500); 
  h_ak8puppi_FilteredMass          =  fs->make<TH1D>("h_ak8puppi_FilteredMass"             ,"",100,0,500); 
  h_ak8puppi_TrimmedMass          =  fs->make<TH1D>("h_ak8puppi_TrimmedMass"             ,"",100,0,500); 
  h_ak8puppi_Tau1                =  fs->make<TH1D>("h_ak8puppi_Tau1"                   ,"",100,0,  1); 
  h_ak8puppi_Tau2                =  fs->make<TH1D>("h_ak8puppi_Tau2"                   ,"",100,0,  1); 
  h_ak8puppi_Tau3                =  fs->make<TH1D>("h_ak8puppi_Tau3"                   ,"",100,0,  1); 
  h_ak8puppi_Tau4                =  fs->make<TH1D>("h_ak8puppi_Tau4"                   ,"",100,0,  1); 
  h_ak8puppi_Tau32               =  fs->make<TH1D>("h_ak8puppi_Tau32"                  ,"",100,0,  1); 
  h_ak8puppi_Tau21               =  fs->make<TH1D>("h_ak8puppi_Tau21"                  ,"",100,0,  1); 
  h_ak8puppi_ECFnb1N2          =  fs->make<TH1D>("h_ak8puppi_ECFnb1N2"                  ,"",100,-1,  1); 
  h_ak8puppi_ECFnb1N3          =  fs->make<TH1D>("h_ak8puppi_ECFnb1N3"                  ,"",100,-1,  1); 
  h_ak8puppi_area                =  fs->make<TH1D>("h_ak8puppi_area"                   ,"",100,0,  8); 
  h_ak8puppi_doubleB                =  fs->make<TH1D>("h_ak8puppi_doubleB"                   ,"",100,0,  1); 
  h_ak8puppi_ndau                =  fs->make<TH1D>("h_ak8puppi_ndau"                   ,"",300,0,300); 
  h_ak8puppi_subjetMass          =  fs->make<TH1D>("h_ak8puppi_subjetMass"             ,"",100,0,400); 
  h_ak8puppi_subjetPt                  =  fs->make<TH1D>("h_ak8puppi_subjetPt"                     ,"",100,0,3000); 
  h_ak8puppi_subjetEta            =  fs->make<TH1D>("h_ak8puppi_subjetEta"               ,"",100,-5, 5); 
  h_ak8puppi_subjetPhi            =  fs->make<TH1D>("h_ak8puppi_subjetPhi"               ,"",100,-5, 5); 
  h_ak8puppi_subjetBdisc                =  fs->make<TH1D>("h_ak8puppi_subjetBdisc"                   ,"",100,0,  1); 

  h_ak8chs_pt                  =  fs->make<TH1D>("h_ak8chs_pt"                     ,"",100,0,3000); 
  h_ak8chs_mass                =  fs->make<TH1D>("h_ak8chs_mass"                   ,"",100,0,500); 
  h_ak8chs_eta            =  fs->make<TH1D>("h_ak8chs_eta"               ,"",100,-5, 5); 
  h_ak8chs_phi            =  fs->make<TH1D>("h_ak8chs_phi"               ,"",100,-5, 5); 
  h_ak8chs_PrunedMass          =  fs->make<TH1D>("h_ak8chs_PrunedMass"             ,"",100,0,500); 
  h_ak8chs_SoftDropMass          =  fs->make<TH1D>("h_ak8chs_SoftDropMass"             ,"",100,0,500); 
  h_ak8chs_FilteredMass          =  fs->make<TH1D>("h_ak8chs_FilteredMass"             ,"",100,0,500); 
  h_ak8chs_TrimmedMass          =  fs->make<TH1D>("h_ak8chs_TrimmedMass"             ,"",100,0,500); 
  h_ak8chs_Tau1                =  fs->make<TH1D>("h_ak8chs_Tau1"                   ,"",100,0,  1); 
  h_ak8chs_Tau2                =  fs->make<TH1D>("h_ak8chs_Tau2"                   ,"",100,0,  1); 
  h_ak8chs_Tau3                =  fs->make<TH1D>("h_ak8chs_Tau3"                   ,"",100,0,  1); 
  h_ak8chs_Tau4                =  fs->make<TH1D>("h_ak8chs_Tau4"                   ,"",100,0,  1); 
  h_ak8chs_Tau32               =  fs->make<TH1D>("h_ak8chs_Tau32"                  ,"",100,0,  1); 
  h_ak8chs_Tau21               =  fs->make<TH1D>("h_ak8chs_Tau21"                  ,"",100,0,  1); 
  h_ak8chs_area                =  fs->make<TH1D>("h_ak8chs_area"                   ,"",100,0,  8); 
  h_ak8chs_doubleB                =  fs->make<TH1D>("h_ak8chs_doubleB"                   ,"",100,0,  1); 
  h_ak8chs_ndau                =  fs->make<TH1D>("h_ak8chs_ndau"                   ,"",300,0,300); 
  h_ak8chs_subjetMass          =  fs->make<TH1D>("h_ak8chs_subjetMass"             ,"",100,0,400); 
  h_ak8chs_subjetPt                  =  fs->make<TH1D>("h_ak8chs_subjetPt"                     ,"",100,0,3000); 
  h_ak8chs_subjetEta            =  fs->make<TH1D>("h_ak8chs_subjetEta"               ,"",100,-5, 5); 
  h_ak8chs_subjetPhi            =  fs->make<TH1D>("h_ak8chs_subjetPhi"               ,"",100,-5, 5); 
  h_ak8chs_subjetBdisc                =  fs->make<TH1D>("h_ak8chs_subjetBdisc"                   ,"",100,0,  1); 

  h_ca8chs_pt                  =  fs->make<TH1D>("h_ca8chs_pt"                     ,"",100,0,3000); 
  h_ca8chs_mass                =  fs->make<TH1D>("h_ca8chs_mass"                   ,"",100,0,500); 
  h_ca8chs_eta            =  fs->make<TH1D>("h_ca8chs_eta"               ,"",100,-5, 5); 
  h_ca8chs_phi            =  fs->make<TH1D>("h_ca8chs_phi"               ,"",100,-5, 5); 
  h_ca8chs_PrunedMass          =  fs->make<TH1D>("h_ca8chs_PrunedMass"             ,"",100,0,500); 
  h_ca8chs_SoftDropMass          =  fs->make<TH1D>("h_ca8chs_SoftDropMass"             ,"",100,0,500); 
  h_ca8chs_Tau1                =  fs->make<TH1D>("h_ca8chs_Tau1"                   ,"",100,0,  1); 
  h_ca8chs_Tau2                =  fs->make<TH1D>("h_ca8chs_Tau2"                   ,"",100,0,  1); 
  h_ca8chs_Tau3                =  fs->make<TH1D>("h_ca8chs_Tau3"                   ,"",100,0,  1); 
  h_ca8chs_Tau4                =  fs->make<TH1D>("h_ca8chs_Tau4"                   ,"",100,0,  1); 
  h_ca8chs_Tau32               =  fs->make<TH1D>("h_ca8chs_Tau32"                  ,"",100,0,  1); 
  h_ca8chs_Tau21               =  fs->make<TH1D>("h_ca8chs_Tau21"                  ,"",100,0,  1); 
  h_ca8chs_area                =  fs->make<TH1D>("h_ca8chs_area"                   ,"",100,0,  8); 
  h_ca8chs_doubleB                =  fs->make<TH1D>("h_ca8chs_doubleB"                   ,"",100,0,  1); 
  h_ca8chs_ndau                =  fs->make<TH1D>("h_ca8chs_ndau"                   ,"",300,0,300); 
  h_ca8chs_subjetMass          =  fs->make<TH1D>("h_ca8chs_subjetMass"             ,"",100,0,400); 
  h_ca8chs_subjetPt                  =  fs->make<TH1D>("h_ca8chs_subjetPt"                     ,"",100,0,3000); 
  h_ca8chs_subjetEta            =  fs->make<TH1D>("h_ca8chs_subjetEta"               ,"",100,-5, 5); 
  h_ca8chs_subjetPhi            =  fs->make<TH1D>("h_ca8chs_subjetPhi"               ,"",100,-5, 5); 
  h_ca8chs_subjetBdisc                =  fs->make<TH1D>("h_ca8chs_subjetBdisc"                   ,"",100,0,  1); 

  h_kt8chs_pt                  =  fs->make<TH1D>("h_kt8chs_pt"                     ,"",100,0,3000); 
  h_kt8chs_mass                =  fs->make<TH1D>("h_kt8chs_mass"                   ,"",100,0,500); 
  h_kt8chs_eta            =  fs->make<TH1D>("h_kt8chs_eta"               ,"",100,-5, 5); 
  h_kt8chs_phi            =  fs->make<TH1D>("h_kt8chs_phi"               ,"",100,-5, 5); 
  h_kt8chs_PrunedMass          =  fs->make<TH1D>("h_kt8chs_PrunedMass"             ,"",100,0,500); 
  h_kt8chs_SoftDropMass          =  fs->make<TH1D>("h_kt8chs_SoftDropMass"             ,"",100,0,500); 
  h_kt8chs_Tau1                =  fs->make<TH1D>("h_kt8chs_Tau1"                   ,"",100,0,  1); 
  h_kt8chs_Tau2                =  fs->make<TH1D>("h_kt8chs_Tau2"                   ,"",100,0,  1); 
  h_kt8chs_Tau3                =  fs->make<TH1D>("h_kt8chs_Tau3"                   ,"",100,0,  1); 
  h_kt8chs_Tau4                =  fs->make<TH1D>("h_kt8chs_Tau4"                   ,"",100,0,  1); 
  h_kt8chs_Tau32               =  fs->make<TH1D>("h_kt8chs_Tau32"                  ,"",100,0,  1); 
  h_kt8chs_Tau21               =  fs->make<TH1D>("h_kt8chs_Tau21"                  ,"",100,0,  1); 
  h_kt8chs_area                =  fs->make<TH1D>("h_kt8chs_area"                   ,"",100,0,  8); 
  h_kt8chs_doubleB                =  fs->make<TH1D>("h_kt8chs_doubleB"                   ,"",100,0,  1); 
  h_kt8chs_ndau                =  fs->make<TH1D>("h_kt8chs_ndau"                   ,"",300,0,300); 
  h_kt8chs_subjetMass          =  fs->make<TH1D>("h_kt8chs_subjetMass"             ,"",100,0,400); 
  h_kt8chs_subjetPt                  =  fs->make<TH1D>("h_kt8chs_subjetPt"                     ,"",100,0,3000); 
  h_kt8chs_subjetEta            =  fs->make<TH1D>("h_kt8chs_subjetEta"               ,"",100,-5, 5); 
  h_kt8chs_subjetPhi            =  fs->make<TH1D>("h_kt8chs_subjetPhi"               ,"",100,-5, 5); 
  h_kt8chs_subjetBdisc                =  fs->make<TH1D>("h_kt8chs_subjetBdisc"                   ,"",100,0,  1); 

  h_ak8puppimodsd_pt                  =  fs->make<TH1D>("h_ak8puppimodsd_pt"                     ,"",100,0,3000); 
  h_ak8puppimodsd_mass                =  fs->make<TH1D>("h_ak8puppimodsd_mass"                   ,"",100,0,500); 
  h_ak8puppimodsd_eta            =  fs->make<TH1D>("h_ak8puppimodsd_eta"               ,"",100,-5, 5); 
  h_ak8puppimodsd_phi            =  fs->make<TH1D>("h_ak8puppimodsd_phi"               ,"",100,-5, 5); 
  h_ak8puppimodsd_SoftDropMass          =  fs->make<TH1D>("h_ak8puppimodsd_SoftDropMass"             ,"",100,0,500); 

  h_ak8sk_pt                  =  fs->make<TH1D>("h_ak8sk_pt"                     ,"",100,0,3000); 
  h_ak8sk_mass                =  fs->make<TH1D>("h_ak8sk_mass"                   ,"",100,0,500); 
  h_ak8sk_eta            =  fs->make<TH1D>("h_ak8sk_eta"               ,"",100,-5, 5); 
  h_ak8sk_phi            =  fs->make<TH1D>("h_ak8sk_phi"               ,"",100,-5, 5); 
  h_ak8sk_SoftDropMass          =  fs->make<TH1D>("h_ak8sk_SoftDropMass"             ,"",100,0,500); 












  h_ak15chs_pt                  =  fs->make<TH1D>("h_ak15chs_pt"                     ,"",100,0,3000); 
  h_ak15chs_mass                =  fs->make<TH1D>("h_ak15chs_mass"                   ,"",100,0,500); 
  h_ak15chs_eta            =  fs->make<TH1D>("h_ak15chs_eta"               ,"",100,-5, 5); 
  h_ak15chs_prunedMass          =  fs->make<TH1D>("h_ak15chs_prunedMass"             ,"",100,0,500); 
  h_ak15chs_trimmedMass         =  fs->make<TH1D>("h_ak15chs_trimmedMass"            ,"",100,0,500); 
  h_ak15chs_filteredMass        =  fs->make<TH1D>("h_ak15chs_filteredMass"           ,"",100,0,500); 
  h_ak15chs_softDropMass        =  fs->make<TH1D>("h_ak15chs_softDropMass"           ,"",100,0,500); 
  h_ak15chs_tau1                =  fs->make<TH1D>("h_ak15chs_tau1"                   ,"",100,0,  1); 
  h_ak15chs_tau2                =  fs->make<TH1D>("h_ak15chs_tau2"                   ,"",100,0,  1); 
  h_ak15chs_tau3                =  fs->make<TH1D>("h_ak15chs_tau3"                   ,"",100,0,  1); 
  h_ak15chs_tau4                =  fs->make<TH1D>("h_ak15chs_tau4"                   ,"",100,0,  1); 
  h_ak15chs_tau32               =  fs->make<TH1D>("h_ak15chs_tau32"                  ,"",100,0,  1); 
  h_ak15chs_tau21               =  fs->make<TH1D>("h_ak15chs_tau21"                  ,"",100,0,  1); 
  h_ak15chs_ndau                =  fs->make<TH1D>("h_ak15chs_ndau"                   ,"",300,0,300); 
  h_ak15chs_subjetMass          =  fs->make<TH1D>("h_ak15chs_subjetMass"             ,"",100,0,400); 
  h_ak15chs_area                =  fs->make<TH1D>("h_ak15chs_area"                   ,"",100,0,  8); 
  h_ak15chs_pt200_mass          =  fs->make<TH1D>("h_ak15chs_pt200_mass"             ,"",100,0,500); 
  h_ak15chs_pt200_prunedMass    =  fs->make<TH1D>("h_ak15chs_pt200_prunedMass"       ,"",100,0,500); 
  h_ak15chs_pt200_trimmedMass   =  fs->make<TH1D>("h_ak15chs_pt200_trimmedMass"      ,"",100,0,500); 
  h_ak15chs_pt200_filteredMass  =  fs->make<TH1D>("h_ak15chs_pt200_filteredMass"     ,"",100,0,500); 
  h_ak15chs_pt200_softDropMass  =  fs->make<TH1D>("h_ak15chs_pt200_softDropMass"     ,"",100,0,500); 
  h_ak15chs_pt200_tau32         =  fs->make<TH1D>("h_ak15chs_pt200_tau32"            ,"",100,0,  1); 
  h_ak15chs_pt200_tau21         =  fs->make<TH1D>("h_ak15chs_pt200_tau21"            ,"",100,0,  1); 
  h_ak15chs_pt200_subjetMass    =  fs->make<TH1D>("h_ak15chs_pt200_subjetMass"       ,"",100,0,400); 
  h_ak15chs_pt500_mass          =  fs->make<TH1D>("h_ak15chs_pt500_mass"             ,"",100,0,500); 
  h_ak15chs_pt500_prunedMass    =  fs->make<TH1D>("h_ak15chs_pt500_prunedMass"       ,"",100,0,500); 
  h_ak15chs_pt500_trimmedMass   =  fs->make<TH1D>("h_ak15chs_pt500_trimmedMass"      ,"",100,0,500); 
  h_ak15chs_pt500_filteredMass  =  fs->make<TH1D>("h_ak15chs_pt500_filteredMass"     ,"",100,0,500); 
  h_ak15chs_pt500_softDropMass  =  fs->make<TH1D>("h_ak15chs_pt500_softDropMass"     ,"",100,0,500); 
  h_ak15chs_pt500_tau32         =  fs->make<TH1D>("h_ak15chs_pt500_tau32"            ,"",100,0,  1); 
  h_ak15chs_pt500_tau21         =  fs->make<TH1D>("h_ak15chs_pt500_tau21"            ,"",100,0,  1); 
  h_ak15chs_pt500_subjetMass    =  fs->make<TH1D>("h_ak15chs_pt500_subjetMass"       ,"",100,0,400); 




}


JetTester::~JetTester()
{
}


//
// member functions
//

// ------------ method called for each event  ------------
void
JetTester::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace reco;
  using namespace pat;
  //bool verbose = false;

  //--------------------------------------------------------------------------------------------
  // AK R=0.4 CHS jets - from miniAOD

  edm::Handle<pat::JetCollection> AK4CHSminiAOD;
  iEvent.getByToken(ak4PFCHSminiAODjetToken_, AK4CHSminiAOD);

  int count_AK4CHSminiAOD = 0;
  for (const pat::Jet &ijet : *AK4CHSminiAOD) {  
    count_AK4CHSminiAOD++;
    if (count_AK4CHSminiAOD>=2) break;

    h_ak4chsminiAOD_pt           ->Fill( ijet.pt()    );
    h_ak4chsminiAOD_uncpt        ->Fill( ijet.pt()*ijet.jecFactor("Uncorrected") );
    h_ak4chsminiAOD_eta          ->Fill( ijet.eta()   );
    h_ak4chsminiAOD_btagCSVv2    ->Fill( ijet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") );
    h_ak4chsminiAOD_area         ->Fill( ijet.jetArea() );
    h_ak4chsminiAOD_nhf          ->Fill( ijet.neutralHadronEnergyFraction() );
    h_ak4chsminiAOD_nemf         ->Fill( ijet.neutralEmEnergyFraction() );
    h_ak4chsminiAOD_chf          ->Fill( ijet.chargedHadronEnergyFraction() );
    h_ak4chsminiAOD_muf          ->Fill( ijet.muonEnergyFraction() );
    h_ak4chsminiAOD_cemf         ->Fill( ijet.chargedEmEnergyFraction() );
    h_ak4chsminiAOD_numConst     ->Fill( ijet.chargedMultiplicity()+ijet.neutralMultiplicity() );
    h_ak4chsminiAOD_numNeuPar    ->Fill( ijet.neutralMultiplicity() );
    h_ak4chsminiAOD_chm          ->Fill( ijet.chargedMultiplicity() );

  }



  //--------------------------------------------------------------------------------------------
  // AK R=0.4 Puppi jets - from miniAOD

  edm::Handle<pat::JetCollection> AK4PuppiminiAOD;
  iEvent.getByToken(ak4PFPuppiminiAODjetToken_, AK4PuppiminiAOD);

  int count_AK4PuppiminiAOD = 0;
  for (const pat::Jet &ijet : *AK4PuppiminiAOD) {  
    count_AK4PuppiminiAOD++;
    if (count_AK4PuppiminiAOD>=2) break;

    h_ak4puppiminiAOD_pt           ->Fill( ijet.pt()    );
    h_ak4puppiminiAOD_uncpt        ->Fill( ijet.pt()*ijet.jecFactor("Uncorrected") );
    h_ak4puppiminiAOD_eta          ->Fill( ijet.eta()   );
    h_ak4puppiminiAOD_btagCSVv2    ->Fill( ijet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") );
    h_ak4puppiminiAOD_area         ->Fill( ijet.jetArea() );
    h_ak4puppiminiAOD_nhf          ->Fill( ijet.neutralHadronEnergyFraction() );
    h_ak4puppiminiAOD_nemf         ->Fill( ijet.neutralEmEnergyFraction() );
    h_ak4puppiminiAOD_chf          ->Fill( ijet.chargedHadronEnergyFraction() );
    h_ak4puppiminiAOD_muf          ->Fill( ijet.muonEnergyFraction() );
    h_ak4puppiminiAOD_cemf         ->Fill( ijet.chargedEmEnergyFraction() );
    h_ak4puppiminiAOD_numConst     ->Fill( ijet.chargedMultiplicity()+ijet.neutralMultiplicity() );
    h_ak4puppiminiAOD_numNeuPar    ->Fill( ijet.neutralMultiplicity() );
    h_ak4puppiminiAOD_chm          ->Fill( ijet.chargedMultiplicity() );

  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.4 CHS jets - update slimmedJets from toolbox

  edm::Handle<pat::JetCollection> AK4CHSUpdated;
  iEvent.getByToken(ak4PFCHSUpdatedjetToken_, AK4CHSUpdated);

  int count_AK4CHSUpdated = 0;
  for (const pat::Jet &ijet : *AK4CHSUpdated) {  
    count_AK4CHSUpdated++;
    if (count_AK4CHSUpdated>=2) break;
   
    h_ak4chsupdated_pt           ->Fill( ijet.pt()    );
    h_ak4chsupdated_uncpt        ->Fill( ijet.pt()*ijet.jecFactor("Uncorrected") );
    h_ak4chsupdated_eta          ->Fill( ijet.eta()   );
    h_ak4chsupdated_btagCSVv2    ->Fill( ijet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") );
    h_ak4chsupdated_btagCvsL     ->Fill( ijet.bDiscriminator("pfCombinedCvsLJetTags") );
    h_ak4chsupdated_btagCvsB     ->Fill( ijet.bDiscriminator("pfCombinedCvsBJetTags") );
    h_ak4chsupdated_btagDeepCSVb ->Fill( ijet.bDiscriminator("pfDeepCSVJetTags:probb") );
    h_ak4chsupdated_btagDeepCSVbb->Fill( ijet.bDiscriminator("pfDeepCSVJetTags:probbb") );
    h_ak4chsupdated_btagDeepCSVc ->Fill( ijet.bDiscriminator("pfDeepCSVJetTags:probc") );
    h_ak4chsupdated_btagDeepCSVl ->Fill( ijet.bDiscriminator("pfDeepCSVJetTags:probudsg") );
    h_ak4chsupdated_btagDeepFlavourb ->Fill( ijet.bDiscriminator("pfDeepFlavourJetTags:probb") );
    h_ak4chsupdated_btagDeepFlavourbb->Fill( ijet.bDiscriminator("pfDeepFlavourJetTags:probbb") );
    h_ak4chsupdated_btagDeepFlavourc ->Fill( ijet.bDiscriminator("pfDeepFlavourJetTags:probc") );
    h_ak4chsupdated_btagDeepFlavourl ->Fill( ijet.bDiscriminator("pfDeepFlavourJetTags:probuds") );
    h_ak4chsupdated_btagDeepFlavourg ->Fill( ijet.bDiscriminator("pfDeepFlavourJetTags:probg") );
    h_ak4chsupdated_btagDeepFlavourlepb->Fill( ijet.bDiscriminator("pfDeepFlavourJetTags:problepb") );
    h_ak4chsupdated_area         ->Fill( ijet.jetArea() );
//    h_ak4chsupdated_pileupJetId  ->Fill( ijet.userFloat("pileupJetId:fullDiscriminant") );
    h_ak4chsupdated_nhf          ->Fill( ijet.neutralHadronEnergyFraction() );
    h_ak4chsupdated_nemf         ->Fill( ijet.neutralEmEnergyFraction() );
    h_ak4chsupdated_chf          ->Fill( ijet.chargedHadronEnergyFraction() );
    h_ak4chsupdated_muf          ->Fill( ijet.muonEnergyFraction() );
    h_ak4chsupdated_cemf         ->Fill( ijet.chargedEmEnergyFraction() );
    h_ak4chsupdated_numConst     ->Fill( ijet.chargedMultiplicity()+ijet.neutralMultiplicity() );
    h_ak4chsupdated_numNeuPar    ->Fill( ijet.neutralMultiplicity() );
    h_ak4chsupdated_chm          ->Fill( ijet.chargedMultiplicity() );

  }



  //--------------------------------------------------------------------------------------------
  // AK R=0.4 CHS jets - from toolbox

  edm::Handle<pat::JetCollection> AK4CHS;
  iEvent.getByToken(ak4PFCHSjetToken_, AK4CHS);

  int count_AK4CHS = 0;
  for (const pat::Jet &ijet : *AK4CHS) {  
    count_AK4CHS++;
    if (count_AK4CHS>=2) break;

    h_ak4chs_pt           ->Fill( ijet.pt()    );
    h_ak4chs_uncpt        ->Fill( ijet.pt()*ijet.jecFactor("Uncorrected") );
    h_ak4chs_eta          ->Fill( ijet.eta()   );
    h_ak4chs_btagCSVv2    ->Fill( ijet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") );
    h_ak4chs_area         ->Fill( ijet.jetArea() );
    h_ak4chs_pileupJetId  ->Fill( ijet.userFloat("AK4PFCHSpileupJetIdEvaluator:fullDiscriminant") );
    h_ak4chs_qglikelihood  ->Fill( ijet.userFloat("QGTaggerAK4PFCHS:qgLikelihood") );
    h_ak4chs_nhf          ->Fill( ijet.neutralHadronEnergyFraction() );
    h_ak4chs_nemf         ->Fill( ijet.neutralEmEnergyFraction() );
    h_ak4chs_chf          ->Fill( ijet.chargedHadronEnergyFraction() );
    h_ak4chs_muf          ->Fill( ijet.muonEnergyFraction() );
    h_ak4chs_cemf         ->Fill( ijet.chargedEmEnergyFraction() );
    h_ak4chs_numConst     ->Fill( ijet.chargedMultiplicity()+ijet.neutralMultiplicity() );
    h_ak4chs_numNeuPar    ->Fill( ijet.neutralMultiplicity() );
    h_ak4chs_chm          ->Fill( ijet.chargedMultiplicity() );

  }


  //--------------------------------------------------------------------------------------------
  // AK R=0.4 Puppi jets - from toolbox

  edm::Handle<pat::JetCollection> AK4Puppi;
  iEvent.getByToken(ak4PFPuppijetToken_, AK4Puppi);

  int count_AK4Puppi = 0;
  for (const pat::Jet &ijet : *AK4Puppi) {  
    count_AK4Puppi++;
    if (count_AK4Puppi>=2) break;

    h_ak4puppi_pt           ->Fill( ijet.pt()    );
    h_ak4puppi_uncpt        ->Fill( ijet.pt()*ijet.jecFactor("Uncorrected") );
    h_ak4puppi_eta          ->Fill( ijet.eta()   );
    h_ak4puppi_btagCSVv2    ->Fill( ijet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") );
    h_ak4puppi_area         ->Fill( ijet.jetArea() );
    h_ak4puppi_nhf          ->Fill( ijet.neutralHadronEnergyFraction() );
    h_ak4puppi_nemf         ->Fill( ijet.neutralEmEnergyFraction() );
    h_ak4puppi_chf          ->Fill( ijet.chargedHadronEnergyFraction() );
    h_ak4puppi_muf          ->Fill( ijet.muonEnergyFraction() );
    h_ak4puppi_cemf         ->Fill( ijet.chargedEmEnergyFraction() );
    h_ak4puppi_numConst     ->Fill( ijet.chargedMultiplicity()+ijet.neutralMultiplicity() );
    h_ak4puppi_numNeuPar    ->Fill( ijet.neutralMultiplicity() );
    h_ak4puppi_chm            ->Fill( ijet.chargedMultiplicity() );

  }


  //--------------------------------------------------------------------------------------------
  // AK R=0.4 PF jets - from toolbox

  edm::Handle<pat::JetCollection> AK4PF;
  iEvent.getByToken(ak4PFjetToken_, AK4PF);

  int count_AK4PF = 0;
  for (const pat::Jet &ijet : *AK4PF) {  
    count_AK4PF++;
    if (count_AK4PF>=2) break;

    h_ak4pf_pt           ->Fill( ijet.pt()    );
    h_ak4pf_uncpt        ->Fill( ijet.pt()*ijet.jecFactor("Uncorrected") );
    h_ak4pf_eta          ->Fill( ijet.eta()   );
    h_ak4pf_btagCSVv2    ->Fill( ijet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") );
    h_ak4pf_area         ->Fill( ijet.jetArea() );
    h_ak4pf_nhf          ->Fill( ijet.neutralHadronEnergyFraction() );
    h_ak4pf_nemf         ->Fill( ijet.neutralEmEnergyFraction() );
    h_ak4pf_chf          ->Fill( ijet.chargedHadronEnergyFraction() );
    h_ak4pf_muf          ->Fill( ijet.muonEnergyFraction() );
    h_ak4pf_cemf         ->Fill( ijet.chargedEmEnergyFraction() );
    h_ak4pf_numConst     ->Fill( ijet.chargedMultiplicity()+ijet.neutralMultiplicity() );
    h_ak4pf_numNeuPar    ->Fill( ijet.neutralMultiplicity() );
    h_ak4pf_chm            ->Fill( ijet.chargedMultiplicity() );

  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 Puppi jets - default miniAOD

  edm::Handle<pat::JetCollection> AK8MINI;
  iEvent.getByToken(ak8PFPuppiminiAODjetToken_, AK8MINI);

  //edm::Handle<reco::GenJetCollection> AK8GENJET;  
  //iEvent.getByToken(ak8genjetToken_, AK8GENJET);

  for (const pat::Jet &ijet : *AK8MINI) {  
    //if (pt<400) continue;
    h_ak8miniAOD_pt         ->Fill( ijet.pt()    );
    h_ak8miniAOD_eta        ->Fill( ijet.eta()    );
    h_ak8miniAOD_phi        ->Fill( ijet.phi()    );
    h_ak8miniAOD_mass       ->Fill( ijet.mass()    );
    h_ak8miniAOD_CHSPrunedMass ->Fill( ijet.userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass") );
    h_ak8miniAOD_CHSSoftDropMass ->Fill( ijet.userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass") );
    h_ak8miniAOD_PuppiSoftDropMass ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropMass") );

    double ak8miniAOD_PuppiTau1         = ijet.userFloat("NjettinessAK8Puppi:tau1");
    double ak8miniAOD_PuppiTau2         = ijet.userFloat("NjettinessAK8Puppi:tau2");
    double ak8miniAOD_PuppiTau3         = ijet.userFloat("NjettinessAK8Puppi:tau3");
    //double ak8miniAOD_PuppiTau4         = ijet.userFloat("NjettinessAK8Puppi:tau4");
    h_ak8miniAOD_PuppiTau1 ->Fill( ak8miniAOD_PuppiTau1 );
    h_ak8miniAOD_PuppiTau2 ->Fill( ak8miniAOD_PuppiTau2 );
    h_ak8miniAOD_PuppiTau3 ->Fill( ak8miniAOD_PuppiTau3 );
    //h_ak8miniAOD_PuppiTau4 ->Fill( ak8miniAOD_PuppiTau4 );
    h_ak8miniAOD_PuppiTau21 ->Fill( (ak8miniAOD_PuppiTau1!=0) ? ak8miniAOD_PuppiTau2/ak8miniAOD_PuppiTau1 : -999  ) ;
    h_ak8miniAOD_PuppiTau32 ->Fill( (ak8miniAOD_PuppiTau2!=0) ? ak8miniAOD_PuppiTau3/ak8miniAOD_PuppiTau2 : -999  ) ;

    double ak8miniAOD_CHSTau1         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau1");
    double ak8miniAOD_CHSTau2         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau2");
    double ak8miniAOD_CHSTau3         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau3");
    //double ak8miniAOD_CHSTau4         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau4");
    h_ak8miniAOD_CHSTau1 ->Fill( ak8miniAOD_CHSTau1 );
    h_ak8miniAOD_CHSTau2 ->Fill( ak8miniAOD_CHSTau2 );
    h_ak8miniAOD_CHSTau3 ->Fill( ak8miniAOD_CHSTau3 );
    //h_ak8miniAOD_CHSTau4 ->Fill( ak8miniAOD_CHSTau4 );
    h_ak8miniAOD_CHSTau21 ->Fill( (ak8miniAOD_CHSTau1!=0) ? ak8miniAOD_CHSTau2/ak8miniAOD_CHSTau1 : -999  ) ;
    h_ak8miniAOD_CHSTau32 ->Fill( (ak8miniAOD_CHSTau2!=0) ? ak8miniAOD_CHSTau3/ak8miniAOD_CHSTau2 : -999  ) ;

    /*h_ak8miniAOD_PuppiECFnb1N2 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2") );
    h_ak8miniAOD_PuppiECFnb1N3 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN3") );
    h_ak8miniAOD_PuppiECFnb2N2 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN2") );
    h_ak8miniAOD_PuppiECFnb2N3 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN3") );
    */

    h_ak8miniAOD_ndau          ->Fill( ijet.numberOfDaughters() );
    h_ak8miniAOD_area          ->Fill( ijet.jetArea() );

    // Get Soft drop subjets for subjet b-tagging
    auto const & sdSubjets = ijet.subjets("SoftDropPuppi");
    for ( auto const & it : sdSubjets ) {
      h_ak8miniAOD_subjetMass    ->Fill( it->mass() );
      h_ak8miniAOD_subjetPt      ->Fill( it->pt() );
      h_ak8miniAOD_subjetPhi     ->Fill( it->phi() );
      h_ak8miniAOD_subjetEta     ->Fill( it->eta() );
      h_ak8miniAOD_subjetBdisc   ->Fill( it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") ); 
    }

  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 Puppi jets - update slimmedJetsAK8 using jetToolbox

  edm::Handle<pat::JetCollection> AK8Updated;
  iEvent.getByToken(ak8PFPuppiUpdatedjetToken_, AK8Updated);

  //edm::Handle<reco::GenJetCollection> AK8GENJET;  
  //iEvent.getByToken(ak8genjetToken_, AK8GENJET);

  for (const pat::Jet &ijet : *AK8Updated) {  
    //if (pt<400) continue;
    h_ak8puppiupdated_pt         ->Fill( ijet.pt()    );
    h_ak8puppiupdated_eta        ->Fill( ijet.eta()    );
    h_ak8puppiupdated_phi        ->Fill( ijet.phi()    );
    h_ak8puppiupdated_mass       ->Fill( ijet.mass()    );
    h_ak8puppiupdated_CHSPrunedMass ->Fill( ijet.userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass") );
    h_ak8puppiupdated_CHSSoftDropMass ->Fill( ijet.userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass") );
    h_ak8puppiupdated_PuppiSoftDropMass ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropMass") );

    double ak8puppiupdated_PuppiTau1         = ijet.userFloat("NjettinessAK8Puppi:tau1");
    double ak8puppiupdated_PuppiTau2         = ijet.userFloat("NjettinessAK8Puppi:tau2");
    double ak8puppiupdated_PuppiTau3         = ijet.userFloat("NjettinessAK8Puppi:tau3");
    //double ak8puppiupdated_PuppiTau4         = ijet.userFloat("NjettinessAK8Puppi:tau4");
    h_ak8puppiupdated_PuppiTau1 ->Fill( ak8puppiupdated_PuppiTau1 );
    h_ak8puppiupdated_PuppiTau2 ->Fill( ak8puppiupdated_PuppiTau2 );
    h_ak8puppiupdated_PuppiTau3 ->Fill( ak8puppiupdated_PuppiTau3 );
    //h_ak8puppiupdated_PuppiTau4 ->Fill( ak8puppiupdated_PuppiTau4 );
    h_ak8puppiupdated_PuppiTau21 ->Fill( (ak8puppiupdated_PuppiTau1!=0) ? ak8puppiupdated_PuppiTau2/ak8puppiupdated_PuppiTau1 : -999  ) ;
    h_ak8puppiupdated_PuppiTau32 ->Fill( (ak8puppiupdated_PuppiTau2!=0) ? ak8puppiupdated_PuppiTau3/ak8puppiupdated_PuppiTau2 : -999  ) ;

    double ak8puppiupdated_CHSTau1         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau1");
    double ak8puppiupdated_CHSTau2         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau2");
    double ak8puppiupdated_CHSTau3         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau3");
    //double ak8puppiupdated_CHSTau4         = ijet.userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau4");
    h_ak8puppiupdated_CHSTau1 ->Fill( ak8puppiupdated_CHSTau1 );
    h_ak8puppiupdated_CHSTau2 ->Fill( ak8puppiupdated_CHSTau2 );
    h_ak8puppiupdated_CHSTau3 ->Fill( ak8puppiupdated_CHSTau3 );
    //h_ak8puppiupdated_CHSTau4 ->Fill( ak8puppiupdated_CHSTau4 );
    h_ak8puppiupdated_CHSTau21 ->Fill( (ak8puppiupdated_CHSTau1!=0) ? ak8puppiupdated_CHSTau2/ak8puppiupdated_CHSTau1 : -999  ) ;
    h_ak8puppiupdated_CHSTau32 ->Fill( (ak8puppiupdated_CHSTau2!=0) ? ak8puppiupdated_CHSTau3/ak8puppiupdated_CHSTau2 : -999  ) ;

    /*h_ak8puppiupdated_PuppiECFnb1N2 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2") );
    h_ak8puppiupdated_PuppiECFnb1N3 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN3") );
    h_ak8puppiupdated_PuppiECFnb2N2 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN2") );
    h_ak8puppiupdated_PuppiECFnb2N3 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN3") );
    */

    h_ak8puppiupdated_ndau          ->Fill( ijet.numberOfDaughters() );
    h_ak8puppiupdated_area          ->Fill( ijet.jetArea() );
    h_ak8puppiupdated_doubleB   ->Fill( ijet.bDiscriminator("pfBoostedDoubleSecondaryVertexAK8BJetTags") ); 
    h_ak8puppiupdated_deepDoubleBvLQCD ->Fill( ijet.bDiscriminator("pfMassIndependentDeepDoubleBvLJetTags:probQCD") ); 
    h_ak8puppiupdated_deepDoubleBvLHbb ->Fill( ijet.bDiscriminator("pfMassIndependentDeepDoubleBvLJetTags:probHbb") ); 
    h_ak8puppiupdated_deepDoubleCvLQCD ->Fill( ijet.bDiscriminator("pfMassIndependentDeepDoubleCvLJetTags:probQCD") ); 
    h_ak8puppiupdated_deepDoubleCvLHcc ->Fill( ijet.bDiscriminator("pfMassIndependentDeepDoubleCvLJetTags:probHcc") ); 
    h_ak8puppiupdated_deepDoubleCvBHbb ->Fill( ijet.bDiscriminator("pfMassIndependentDeepDoubleCvBJetTags:probHbb") ); 
    h_ak8puppiupdated_deepDoubleCvBHcc ->Fill( ijet.bDiscriminator("pfMassIndependentDeepDoubleCvBJetTags:probHcc") ); 

    // Get Soft drop subjets for subjet b-tagging
    auto const & sdSubjets = ijet.subjets("SoftDropPuppi");
    for ( auto const & it : sdSubjets ) {
      h_ak8puppiupdated_subjetMass    ->Fill( it->mass() );
      h_ak8puppiupdated_subjetPt      ->Fill( it->pt() );
      h_ak8puppiupdated_subjetPhi     ->Fill( it->phi() );
      h_ak8puppiupdated_subjetEta     ->Fill( it->eta() );
      h_ak8puppiupdated_subjetBdisc   ->Fill( it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") ); 
    }

  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 PUPPI jets - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8Puppi;
  iEvent.getByToken( ak8PFPuppijetToken_, AK8Puppi );

  for (const pat::Jet &ijet : *AK8Puppi) {  
    //if (pt<400) continue;
    h_ak8puppi_pt         ->Fill( ijet.pt()    );
    h_ak8puppi_eta        ->Fill( ijet.eta()    );
    h_ak8puppi_phi        ->Fill( ijet.phi()    );
    h_ak8puppi_mass       ->Fill( ijet.mass()    );
    h_ak8puppi_PrunedMass ->Fill( ijet.userFloat("ak8PFJetsPuppiPrunedMass") );
    h_ak8puppi_SoftDropMass ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropMass") );
    h_ak8puppi_FilteredMass ->Fill( ijet.userFloat("ak8PFJetsPuppiFilteredMass") );
    h_ak8puppi_TrimmedMass ->Fill( ijet.userFloat("ak8PFJetsPuppiTrimmedMass") );

    double ak8puppiTau1         = ijet.userFloat("NjettinessAK8Puppi:tau1");
    double ak8puppiTau2         = ijet.userFloat("NjettinessAK8Puppi:tau2");
    double ak8puppiTau3         = ijet.userFloat("NjettinessAK8Puppi:tau3");
    double ak8puppiTau4         = ijet.userFloat("NjettinessAK8Puppi:tau4");
    h_ak8puppi_Tau1 ->Fill( ak8puppiTau1 );
    h_ak8puppi_Tau2 ->Fill( ak8puppiTau2 );
    h_ak8puppi_Tau3 ->Fill( ak8puppiTau3 );
    h_ak8puppi_Tau4 ->Fill( ak8puppiTau4 );
    h_ak8puppi_Tau21 ->Fill( (ak8puppiTau1!=0) ? ak8puppiTau2/ak8puppiTau1 : -999  ) ;
    h_ak8puppi_Tau32 ->Fill( (ak8puppiTau2!=0) ? ak8puppiTau3/ak8puppiTau2 : -999  ) ;


    h_ak8puppi_ECFnb1N2 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2") );
    h_ak8puppi_ECFnb1N3 ->Fill( ijet.userFloat("ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN3") );

    h_ak8puppi_ndau          ->Fill( ijet.numberOfDaughters() );
    h_ak8puppi_area          ->Fill( ijet.jetArea() );
    h_ak8puppi_doubleB   ->Fill( ijet.bDiscriminator("pfBoostedDoubleSecondaryVertexAK8BJetTags") ); 

    // Get Soft drop subjets for subjet b-tagging
    auto const & sdSubjets = ijet.subjets("SoftDrop");
    for ( auto const & it : sdSubjets ) {
      h_ak8puppi_subjetMass    ->Fill( it->mass() );
      h_ak8puppi_subjetPt      ->Fill( it->pt() );
      h_ak8puppi_subjetPhi     ->Fill( it->phi() );
      h_ak8puppi_subjetEta     ->Fill( it->eta() );
      h_ak8puppi_subjetBdisc   ->Fill( it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") ); 
    }
  }


  //--------------------------------------------------------------------------------------------
  // AK R=0.8 CHS jets - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8CHS;
  iEvent.getByToken( ak8PFCHSjetToken_, AK8CHS );

  for (const pat::Jet &ijet : *AK8CHS) {  
    //if (pt<400) continue;
    h_ak8chs_pt         ->Fill( ijet.pt()    );
    h_ak8chs_eta        ->Fill( ijet.eta()    );
    h_ak8chs_phi        ->Fill( ijet.phi()    );
    h_ak8chs_mass       ->Fill( ijet.mass()    );
    h_ak8chs_PrunedMass ->Fill( ijet.userFloat("ak8PFJetsCHSPrunedMass") );
    h_ak8chs_SoftDropMass ->Fill( ijet.userFloat("ak8PFJetsCHSSoftDropMass") );
    h_ak8chs_FilteredMass ->Fill( ijet.userFloat("ak8PFJetsCHSFilteredMass") );
    h_ak8chs_TrimmedMass ->Fill( ijet.userFloat("ak8PFJetsCHSTrimmedMass") );

    double ak8chsTau1         = ijet.userFloat("NjettinessAK8CHS:tau1");
    double ak8chsTau2         = ijet.userFloat("NjettinessAK8CHS:tau2");
    double ak8chsTau3         = ijet.userFloat("NjettinessAK8CHS:tau3");
    double ak8chsTau4         = ijet.userFloat("NjettinessAK8CHS:tau4");
    h_ak8chs_Tau1 ->Fill( ak8chsTau1 );
    h_ak8chs_Tau2 ->Fill( ak8chsTau2 );
    h_ak8chs_Tau3 ->Fill( ak8chsTau3 );
    h_ak8chs_Tau4 ->Fill( ak8chsTau4 );
    h_ak8chs_Tau21 ->Fill( (ak8chsTau1!=0) ? ak8chsTau2/ak8chsTau1 : -999  ) ;
    h_ak8chs_Tau32 ->Fill( (ak8chsTau2!=0) ? ak8chsTau3/ak8chsTau2 : -999  ) ;


    //h_ak8chs_ECFnb1N2 ->Fill( ijet.userFloat("ak8PFJetsCHSSoftDropValueMap:nb1AK8CHSSoftDropN2") );
    //h_ak8chs_ECFnb1N3 ->Fill( ijet.userFloat("ak8PFJetschsSoftDropValueMap:nb1AK8chsSoftDropN3") );

    h_ak8chs_ndau          ->Fill( ijet.numberOfDaughters() );
    h_ak8chs_area          ->Fill( ijet.jetArea() );
    h_ak8chs_doubleB   ->Fill( ijet.bDiscriminator("pfBoostedDoubleSecondaryVertexAK8BJetTags") ); 

    // Get Soft drop subjets for subjet b-tagging
    auto const & sdSubjets = ijet.subjets("SoftDrop");
    for ( auto const & it : sdSubjets ) {
      h_ak8chs_subjetMass    ->Fill( it->mass() );
      h_ak8chs_subjetPt      ->Fill( it->pt() );
      h_ak8chs_subjetPhi     ->Fill( it->phi() );
      h_ak8chs_subjetEta     ->Fill( it->eta() );
      h_ak8chs_subjetBdisc   ->Fill( it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") ); 
    }
  }
  

  //--------------------------------------------------------------------------------------------
  // CA R=0.8 jets - from toolbox

  edm::Handle<pat::JetCollection> CA8CHS;
  iEvent.getByToken(ca8PFCHSjetToken_, CA8CHS);
  
  for (const pat::Jet &ijet : *CA8CHS) {  
    //if (pt<400) continue;
    h_ca8chs_pt         ->Fill( ijet.pt()    );
    h_ca8chs_eta        ->Fill( ijet.eta()    );
    h_ca8chs_phi        ->Fill( ijet.phi()    );
    h_ca8chs_mass       ->Fill( ijet.mass()    );
    h_ca8chs_PrunedMass ->Fill( ijet.userFloat("ca8PFJetsCHSPrunedMass") );
    h_ca8chs_SoftDropMass ->Fill( ijet.userFloat("ca8PFJetsCHSSoftDropMass") );

    h_ca8chs_ndau          ->Fill( ijet.numberOfDaughters() );
    h_ca8chs_area          ->Fill( ijet.jetArea() );
    h_ca8chs_doubleB   ->Fill( ijet.bDiscriminator("pfBoostedDoubleSecondaryVertexca8BJetTags") ); 

  }
  

  //--------------------------------------------------------------------------------------------
  // KT R=0.8 jets - from toolbox

  edm::Handle<pat::JetCollection> KT8CHS;
  iEvent.getByToken(kt8PFCHSjetToken_, KT8CHS);

  for (const pat::Jet &ijet : *KT8CHS) {  
    //if (pt<400) continue;
    h_kt8chs_pt         ->Fill( ijet.pt()    );
    h_kt8chs_eta        ->Fill( ijet.eta()    );
    h_kt8chs_phi        ->Fill( ijet.phi()    );
    h_kt8chs_mass       ->Fill( ijet.mass()    );
    h_kt8chs_PrunedMass ->Fill( ijet.userFloat("kt8PFJetsCHSPrunedMass") );
    h_kt8chs_SoftDropMass ->Fill( ijet.userFloat("kt8PFJetsCHSSoftDropMass") );

    h_kt8chs_ndau          ->Fill( ijet.numberOfDaughters() );
    h_kt8chs_area          ->Fill( ijet.jetArea() );
    h_kt8chs_doubleB   ->Fill( ijet.bDiscriminator("pfBoostedDoubleSecondaryVertexkt8BJetTags") ); 

  }
  
  //--------------------------------------------------------------------------------------------
  // AK R=0.8 jets - from toolbox

  edm::Handle<pat::JetCollection> AK8PuppimodSD;
  iEvent.getByToken(ak8PFPuppimodSDjetToken_, AK8PuppimodSD);

  for (const pat::Jet &ijet : *AK8PuppimodSD) {  
    h_ak8puppimodsd_pt         ->Fill( ijet.pt()    );
    h_ak8puppimodsd_eta        ->Fill( ijet.eta()    );
    h_ak8puppimodsd_phi        ->Fill( ijet.phi()    );
    h_ak8puppimodsd_mass       ->Fill( ijet.mass()    );
    h_ak8puppimodsd_SoftDropMass ->Fill( ijet.userFloat("ak8PFJetsPuppimodSDSoftDropMass") );

  }
  
  
  //--------------------------------------------------------------------------------------------
  // AK R=0.8 jets - SoftKiller from toolbox

  edm::Handle<pat::JetCollection> AK8SK;
  iEvent.getByToken(ak8PFSKjetToken_, AK8SK);

  for (const pat::Jet &ijet : *AK8SK) {  
    h_ak8sk_pt         ->Fill( ijet.pt()    );
    h_ak8sk_eta        ->Fill( ijet.eta()    );
    h_ak8sk_phi        ->Fill( ijet.phi()    );
    h_ak8sk_mass       ->Fill( ijet.mass()    );
    h_ak8sk_SoftDropMass ->Fill( ijet.userFloat("ak8PFJetsSKSoftDropMass") );

  }

  /*/--------------------------------------------------------------------------------------------
  // AK R=0.8 jets - Constituent Substraction from toolbox

  edm::Handle<pat::JetCollection> AK8CS;
  iEvent.getByToken(ak8PFCSjetToken_, AK8CS);

  for (const pat::Jet &ijet : *AK8CS) {  
    h_ak8cs_pt         ->Fill( ijet.pt()    );
    h_ak8cs_eta        ->Fill( ijet.eta()    );
    h_ak8cs_phi        ->Fill( ijet.phi()    );
    h_ak8cs_mass       ->Fill( ijet.mass()    );
    h_ak8cs_SoftDropMass ->Fill( ijet.userFloat("ak8PFJetsCSSoftDropMass") );

  }*/

  //--------------------------------------------------------------------------------------------
  // CA R=1.2 jets - from toolbox

  /*edm::Handle<pat::JetCollection> CA12CHS;
  iEvent.getByToken(ca12PFCHSjetToken_, CA12CHS);

  for (const pat::Jet &ijet : *CA12CHS) {  
        //cout << ijet.tagInfoLabels() << endl;
        cout << ijet.tagInfo("hepTopTagPFJetsCHS") << endl;
      //for ( auto st : ijet.tagInfoLabels() ) {
        cout << st << endl; //ijet.tagInfo("CATop") << endl;
      }//
  }*/
  



  /*/--------------------------------------------------------------------------------------------
  // AK R=1.5 jets - from toolbox

  edm::Handle<pat::JetCollection> AK15CHS;
  iEvent.getByToken(ak15PFCHSjetToken_, AK15CHS);

  edm::Handle<pat::JetCollection> AK15CHSsub;
  iEvent.getByToken(ak15PFCHSSoftDropSubjetsToken_, AK15CHSsub);

  int count_AK15CHS = 0;
  for (const pat::Jet &ijet : *AK15CHS) {  
    count_AK15CHS++;
    if (count_AK15CHS>=2) break;     
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double eta     = ijet.eta();
    double prunedMass   = ijet.userFloat("ak15PFJetsCHSPrunedMass");
    double trimmedMass  = ijet.userFloat("ak15PFJetsCHSTrimmedMass");
    double filteredMass = ijet.userFloat("ak15PFJetsCHSFilteredMass");
    double softDropMass = ijet.userFloat("ak15PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK15CHS:tau1");
    double tau2         = ijet.userFloat("NjettinessAK15CHS:tau2");
    double tau3         = ijet.userFloat("NjettinessAK15CHS:tau3");
    double tau4         = ijet.userFloat("NjettinessAK15CHS:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *AK15CHSsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<1.5){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_ak15chs_pt           ->Fill( pt           );
    h_ak15chs_mass         ->Fill( mass         );
    h_ak15chs_eta     ->Fill( eta     );
    h_ak15chs_prunedMass   ->Fill( prunedMass   );
    h_ak15chs_trimmedMass  ->Fill( trimmedMass  );
    h_ak15chs_filteredMass ->Fill( filteredMass );
    h_ak15chs_softDropMass ->Fill( softDropMass );
    h_ak15chs_tau1         ->Fill( tau1         );
    h_ak15chs_tau2         ->Fill( tau2         );
    h_ak15chs_tau3         ->Fill( tau3         );
    h_ak15chs_tau4         ->Fill( tau4         );
    h_ak15chs_tau32        ->Fill( tau32        );
    h_ak15chs_tau21        ->Fill( tau21        );
    h_ak15chs_ndau         ->Fill( ndau         );
    h_ak15chs_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_ak15chs_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_ak15chs_pt200_mass         ->Fill( mass                            );
      h_ak15chs_pt200_prunedMass   ->Fill( prunedMass                      );
      h_ak15chs_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_ak15chs_pt200_filteredMass ->Fill( filteredMass                    );
      h_ak15chs_pt200_softDropMass ->Fill( softDropMass                    );
      h_ak15chs_pt200_tau32        ->Fill( tau32                           );
      h_ak15chs_pt200_tau21        ->Fill( tau21                           );
      h_ak15chs_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_ak15chs_pt500_mass         ->Fill( mass                            );
      h_ak15chs_pt500_prunedMass   ->Fill( prunedMass                      );
      h_ak15chs_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_ak15chs_pt500_filteredMass ->Fill( filteredMass                    );
      h_ak15chs_pt500_softDropMass ->Fill( softDropMass                    );
      h_ak15chs_pt500_tau32        ->Fill( tau32                           );
      h_ak15chs_pt500_tau21        ->Fill( tau21                           );
      h_ak15chs_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }*/




}


// ------------ method called once each job just before starting event loop  ------------
void 
JetTester::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetTester::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetTester::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetTester);
