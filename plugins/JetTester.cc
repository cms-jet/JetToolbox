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
      edm::EDGetTokenT<pat::JetCollection> ak4jetMiniToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8jetMiniToken_;
      edm::EDGetTokenT<pat::JetCollection> puppijetMiniToken_;
      edm::EDGetTokenT<pat::JetCollection> ak4PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ca8PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> kt8PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFPUPPIjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak12PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak15PFCHSjetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak4PFCHSSoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFSoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFCHSSoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> ca8PFCHSSoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> kt8PFCHSSoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8PFPUPPISoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> ak12PFCHSSoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> ak15PFCHSSoftDropSubjetsToken_;
      edm::EDGetTokenT<pat::JetCollection> puppijetToken_;
      edm::EDGetTokenT<reco::GenJetCollection> ak4genjetToken_;
      edm::EDGetTokenT<reco::GenJetCollection> ak8genjetToken_;
      edm::EDGetTokenT<edm::View<reco::GenParticle> > prunedGenToken_;
      edm::EDGetTokenT<double> rhoToken_;
      edm::EDGetTokenT<std::vector<reco::Vertex> > vtxToken_;


      TH1D * h_ak4chs_pt            ;
      TH1D * h_ak4chs_mass          ;
      TH1D * h_ak4chs_rapidity      ;
      TH1D * h_ak4chs_prunedMass    ;
      TH1D * h_ak4chs_trimmedMass   ;
      TH1D * h_ak4chs_filteredMass  ;
      TH1D * h_ak4chs_softDropMass  ;
      TH1D * h_ak4chs_tau1          ;
      TH1D * h_ak4chs_tau2          ;
      TH1D * h_ak4chs_tau3          ;
      TH1D * h_ak4chs_tau4          ;
      TH1D * h_ak4chs_tau32         ;
      TH1D * h_ak4chs_tau21         ;
      TH1D * h_ak4chs_ndau          ;
      TH1D * h_ak4chs_subjetMass    ;  
      TH1D * h_ak4chs_area          ;  
      TH1D * h_ak4chs_pt200_mass          ; 
      TH1D * h_ak4chs_pt200_prunedMass    ; 
      TH1D * h_ak4chs_pt200_trimmedMass   ; 
      TH1D * h_ak4chs_pt200_filteredMass  ; 
      TH1D * h_ak4chs_pt200_softDropMass  ; 
      TH1D * h_ak4chs_pt200_tau32         ; 
      TH1D * h_ak4chs_pt200_tau21         ; 
      TH1D * h_ak4chs_pt200_subjetMass    ; 
      TH1D * h_ak4chs_pt500_mass          ; 
      TH1D * h_ak4chs_pt500_prunedMass    ; 
      TH1D * h_ak4chs_pt500_trimmedMass   ; 
      TH1D * h_ak4chs_pt500_filteredMass  ; 
      TH1D * h_ak4chs_pt500_softDropMass  ; 
      TH1D * h_ak4chs_pt500_tau32         ; 
      TH1D * h_ak4chs_pt500_tau21         ; 
      TH1D * h_ak4chs_pt500_subjetMass    ; 
  

      TH1D * h_ak8pf_pt            ;
      TH1D * h_ak8pf_mass          ;
      TH1D * h_ak8pf_rapidity      ;
      TH1D * h_ak8pf_prunedMass    ;
      TH1D * h_ak8pf_trimmedMass   ;
      TH1D * h_ak8pf_filteredMass  ;
      TH1D * h_ak8pf_softDropMass  ;
      TH1D * h_ak8pf_tau1          ;
      TH1D * h_ak8pf_tau2          ;
      TH1D * h_ak8pf_tau3          ;
      TH1D * h_ak8pf_tau4          ;
      TH1D * h_ak8pf_tau32         ;
      TH1D * h_ak8pf_tau21         ;
      TH1D * h_ak8pf_ndau          ;
      TH1D * h_ak8pf_subjetMass    ;  
      TH1D * h_ak8pf_area          ;  
      TH1D * h_ak8pf_pt200_mass          ;  
      TH1D * h_ak8pf_pt200_prunedMass    ; 
      TH1D * h_ak8pf_pt200_trimmedMass   ; 
      TH1D * h_ak8pf_pt200_filteredMass  ; 
      TH1D * h_ak8pf_pt200_softDropMass  ; 
      TH1D * h_ak8pf_pt200_tau32         ; 
      TH1D * h_ak8pf_pt200_tau21         ; 
      TH1D * h_ak8pf_pt200_subjetMass    ; 
      TH1D * h_ak8pf_pt500_mass          ; 
      TH1D * h_ak8pf_pt500_prunedMass    ; 
      TH1D * h_ak8pf_pt500_trimmedMass   ; 
      TH1D * h_ak8pf_pt500_filteredMass  ; 
      TH1D * h_ak8pf_pt500_softDropMass  ; 
      TH1D * h_ak8pf_pt500_tau32         ; 
      TH1D * h_ak8pf_pt500_tau21         ; 
      TH1D * h_ak8pf_pt500_subjetMass    ; 

      TH1D * h_ak8chs_pt            ;
      TH1D * h_ak8chs_mass          ;
      TH1D * h_ak8chs_rapidity      ;
      TH1D * h_ak8chs_prunedMass    ;
      TH1D * h_ak8chs_trimmedMass   ;
      TH1D * h_ak8chs_filteredMass  ;
      TH1D * h_ak8chs_softDropMass  ;
      TH1D * h_ak8chs_tau1          ;
      TH1D * h_ak8chs_tau2          ;
      TH1D * h_ak8chs_tau3          ;
      TH1D * h_ak8chs_tau4          ;
      TH1D * h_ak8chs_tau32         ;
      TH1D * h_ak8chs_tau21         ;
      TH1D * h_ak8chs_ndau          ;
      TH1D * h_ak8chs_subjetMass    ;  
      TH1D * h_ak8chs_area          ;  
      TH1D * h_ak8chs_pt200_mass          ; 
      TH1D * h_ak8chs_pt200_prunedMass    ; 
      TH1D * h_ak8chs_pt200_trimmedMass   ; 
      TH1D * h_ak8chs_pt200_filteredMass  ; 
      TH1D * h_ak8chs_pt200_softDropMass  ; 
      TH1D * h_ak8chs_pt200_tau32         ; 
      TH1D * h_ak8chs_pt200_tau21         ; 
      TH1D * h_ak8chs_pt200_subjetMass    ; 
      TH1D * h_ak8chs_pt500_mass          ; 
      TH1D * h_ak8chs_pt500_prunedMass    ; 
      TH1D * h_ak8chs_pt500_trimmedMass   ; 
      TH1D * h_ak8chs_pt500_filteredMass  ; 
      TH1D * h_ak8chs_pt500_softDropMass  ; 
      TH1D * h_ak8chs_pt500_tau32         ; 
      TH1D * h_ak8chs_pt500_tau21         ; 
      TH1D * h_ak8chs_pt500_subjetMass    ; 

      TH1D * h_ak8puppi_pt            ;
      TH1D * h_ak8puppi_mass          ;
      TH1D * h_ak8puppi_rapidity      ;
      TH1D * h_ak8puppi_prunedMass    ;
      TH1D * h_ak8puppi_trimmedMass   ;
      TH1D * h_ak8puppi_filteredMass  ;
      TH1D * h_ak8puppi_softDropMass  ;
      TH1D * h_ak8puppi_tau1          ;
      TH1D * h_ak8puppi_tau2          ;
      TH1D * h_ak8puppi_tau3          ;
      TH1D * h_ak8puppi_tau4          ;
      TH1D * h_ak8puppi_tau32         ;
      TH1D * h_ak8puppi_tau21         ;
      TH1D * h_ak8puppi_ndau          ;
      TH1D * h_ak8puppi_subjetMass    ;  
      TH1D * h_ak8puppi_area          ;  
      TH1D * h_ak8puppi_pt200_mass          ; 
      TH1D * h_ak8puppi_pt200_prunedMass    ; 
      TH1D * h_ak8puppi_pt200_trimmedMass   ; 
      TH1D * h_ak8puppi_pt200_filteredMass  ; 
      TH1D * h_ak8puppi_pt200_softDropMass  ; 
      TH1D * h_ak8puppi_pt200_tau32         ; 
      TH1D * h_ak8puppi_pt200_tau21         ; 
      TH1D * h_ak8puppi_pt200_subjetMass    ; 
      TH1D * h_ak8puppi_pt500_mass          ; 
      TH1D * h_ak8puppi_pt500_prunedMass    ; 
      TH1D * h_ak8puppi_pt500_trimmedMass   ; 
      TH1D * h_ak8puppi_pt500_filteredMass  ; 
      TH1D * h_ak8puppi_pt500_softDropMass  ; 
      TH1D * h_ak8puppi_pt500_tau32         ; 
      TH1D * h_ak8puppi_pt500_tau21         ; 
      TH1D * h_ak8puppi_pt500_subjetMass    ; 


      TH1D * h_kt8chs_pt            ;
      TH1D * h_kt8chs_mass          ;
      TH1D * h_kt8chs_rapidity      ;
      TH1D * h_kt8chs_prunedMass    ;
      TH1D * h_kt8chs_trimmedMass   ;
      TH1D * h_kt8chs_filteredMass  ;
      TH1D * h_kt8chs_softDropMass  ;
      TH1D * h_kt8chs_tau1          ;
      TH1D * h_kt8chs_tau2          ;
      TH1D * h_kt8chs_tau3          ;
      TH1D * h_kt8chs_tau4          ;
      TH1D * h_kt8chs_tau32         ;
      TH1D * h_kt8chs_tau21         ;
      TH1D * h_kt8chs_ndau          ;
      TH1D * h_kt8chs_subjetMass    ;  
      TH1D * h_kt8chs_area          ;  
      TH1D * h_kt8chs_pt200_mass          ; 
      TH1D * h_kt8chs_pt200_prunedMass    ; 
      TH1D * h_kt8chs_pt200_trimmedMass   ; 
      TH1D * h_kt8chs_pt200_filteredMass  ; 
      TH1D * h_kt8chs_pt200_softDropMass  ; 
      TH1D * h_kt8chs_pt200_tau32         ; 
      TH1D * h_kt8chs_pt200_tau21         ; 
      TH1D * h_kt8chs_pt200_subjetMass    ; 
      TH1D * h_kt8chs_pt500_mass          ; 
      TH1D * h_kt8chs_pt500_prunedMass    ; 
      TH1D * h_kt8chs_pt500_trimmedMass   ; 
      TH1D * h_kt8chs_pt500_filteredMass  ; 
      TH1D * h_kt8chs_pt500_softDropMass  ; 
      TH1D * h_kt8chs_pt500_tau32         ; 
      TH1D * h_kt8chs_pt500_tau21         ; 
      TH1D * h_kt8chs_pt500_subjetMass    ; 


      TH1D * h_ca8chs_pt            ;
      TH1D * h_ca8chs_mass          ;
      TH1D * h_ca8chs_rapidity      ;
      TH1D * h_ca8chs_prunedMass    ;
      TH1D * h_ca8chs_trimmedMass   ;
      TH1D * h_ca8chs_filteredMass  ;
      TH1D * h_ca8chs_softDropMass  ;
      TH1D * h_ca8chs_tau1          ;
      TH1D * h_ca8chs_tau2          ;
      TH1D * h_ca8chs_tau3          ;
      TH1D * h_ca8chs_tau4          ;
      TH1D * h_ca8chs_tau32         ;
      TH1D * h_ca8chs_tau21         ;
      TH1D * h_ca8chs_ndau          ;
      TH1D * h_ca8chs_subjetMass    ;  
      TH1D * h_ca8chs_area          ;  
      TH1D * h_ca8chs_pt200_mass          ; 
      TH1D * h_ca8chs_pt200_prunedMass    ; 
      TH1D * h_ca8chs_pt200_trimmedMass   ; 
      TH1D * h_ca8chs_pt200_filteredMass  ; 
      TH1D * h_ca8chs_pt200_softDropMass  ; 
      TH1D * h_ca8chs_pt200_tau32         ; 
      TH1D * h_ca8chs_pt200_tau21         ; 
      TH1D * h_ca8chs_pt200_subjetMass    ; 
      TH1D * h_ca8chs_pt500_mass          ; 
      TH1D * h_ca8chs_pt500_prunedMass    ; 
      TH1D * h_ca8chs_pt500_trimmedMass   ; 
      TH1D * h_ca8chs_pt500_filteredMass  ; 
      TH1D * h_ca8chs_pt500_softDropMass  ; 
      TH1D * h_ca8chs_pt500_tau32         ; 
      TH1D * h_ca8chs_pt500_tau21         ; 
      TH1D * h_ca8chs_pt500_subjetMass    ; 

      TH1D * h_ak12chs_pt            ;
      TH1D * h_ak12chs_mass          ;
      TH1D * h_ak12chs_rapidity      ;
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
      TH1D * h_ak15chs_rapidity      ;
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
    ak4jetMiniToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJets"))),
    ak8jetMiniToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJetsAK8"))),
    ak4PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK4PFCHS"))),
    ak8PFjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PF"))),
    ak8PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFCHS"))),
    ca8PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsCA8PFCHS"))),
    kt8PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsKT8PFCHS"))),
    ak8PFPUPPIjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFPuppi"))),
    ak12PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK12PFCHS"))),
    ak15PFCHSjetToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK15PFCHS"))),
    ak4PFCHSSoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK4PFCHSSoftDropPacked","SubJets"))),
    ak8PFSoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFSoftDropPacked","SubJets"))),
    ak8PFCHSSoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFCHSSoftDropPacked","SubJets"))),
    ca8PFCHSSoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsCA8PFCHSSoftDropPacked","SubJets"))),
    kt8PFCHSSoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsKT8PFCHSSoftDropPacked","SubJets"))),
    ak8PFPUPPISoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK8PFPuppiSoftDropPacked","SubJets"))),
    ak12PFCHSSoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK12PFCHSSoftDropPacked","SubJets"))),
    ak15PFCHSSoftDropSubjetsToken_(consumes<pat::JetCollection>(edm::InputTag("selectedPatJetsAK15PFCHSSoftDropPacked","SubJets"))),
    puppijetToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJetsPuppi"))),
    ak4genjetToken_(consumes<reco::GenJetCollection>(edm::InputTag("slimmedGenJets"))),
    ak8genjetToken_(consumes<reco::GenJetCollection>(edm::InputTag("slimmedGenJetsAK8"))),
    prunedGenToken_(consumes<edm::View<reco::GenParticle> >(edm::InputTag("prunedGenParticles"))),
    rhoToken_(consumes<double>(edm::InputTag("fixedGridRhoFastjetAll"))),
    vtxToken_(consumes<std::vector<reco::Vertex> >(edm::InputTag("offlineSlimmedPrimaryVertices")))
{

  edm::Service<TFileService> fs;

  h_ak4chs_pt                  =  fs->make<TH1D>("h_ak4chs_pt"                     ,"",100,0,3000); 
  h_ak4chs_mass                =  fs->make<TH1D>("h_ak4chs_mass"                   ,"",100,0,500); 
  h_ak4chs_rapidity            =  fs->make<TH1D>("h_ak4chs_rapidity"               ,"",100,-5, 5); 
  h_ak4chs_prunedMass          =  fs->make<TH1D>("h_ak4chs_prunedMass"             ,"",100,0,500); 
  h_ak4chs_trimmedMass         =  fs->make<TH1D>("h_ak4chs_trimmedMass"            ,"",100,0,500); 
  h_ak4chs_filteredMass        =  fs->make<TH1D>("h_ak4chs_filteredMass"           ,"",100,0,500); 
  h_ak4chs_softDropMass        =  fs->make<TH1D>("h_ak4chs_softDropMass"           ,"",100,0,500); 
  h_ak4chs_tau1                =  fs->make<TH1D>("h_ak4chs_tau1"                   ,"",100,0,  1); 
  h_ak4chs_tau2                =  fs->make<TH1D>("h_ak4chs_tau2"                   ,"",100,0,  1); 
  h_ak4chs_tau3                =  fs->make<TH1D>("h_ak4chs_tau3"                   ,"",100,0,  1); 
  h_ak4chs_tau4                =  fs->make<TH1D>("h_ak4chs_tau4"                   ,"",100,0,  1); 
  h_ak4chs_tau32               =  fs->make<TH1D>("h_ak4chs_tau32"                  ,"",100,0,  1); 
  h_ak4chs_tau21               =  fs->make<TH1D>("h_ak4chs_tau21"                  ,"",100,0,  1); 
  h_ak4chs_ndau                =  fs->make<TH1D>("h_ak4chs_ndau"                   ,"",300,0,300); 
  h_ak4chs_subjetMass          =  fs->make<TH1D>("h_ak4chs_subjetMass"             ,"",100,0,400); 
  h_ak4chs_area                =  fs->make<TH1D>("h_ak4chs_area"                   ,"",100,0,  8); 
  h_ak4chs_pt200_mass          =  fs->make<TH1D>("h_ak4chs_pt200_mass"             ,"",100,0,500); 
  h_ak4chs_pt200_prunedMass    =  fs->make<TH1D>("h_ak4chs_pt200_prunedMass"       ,"",100,0,500); 
  h_ak4chs_pt200_trimmedMass   =  fs->make<TH1D>("h_ak4chs_pt200_trimmedMass"      ,"",100,0,500); 
  h_ak4chs_pt200_filteredMass  =  fs->make<TH1D>("h_ak4chs_pt200_filteredMass"     ,"",100,0,500); 
  h_ak4chs_pt200_softDropMass  =  fs->make<TH1D>("h_ak4chs_pt200_softDropMass"     ,"",100,0,500); 
  h_ak4chs_pt200_tau32         =  fs->make<TH1D>("h_ak4chs_pt200_tau32"            ,"",100,0,  1); 
  h_ak4chs_pt200_tau21         =  fs->make<TH1D>("h_ak4chs_pt200_tau21"            ,"",100,0,  1); 
  h_ak4chs_pt200_subjetMass    =  fs->make<TH1D>("h_ak4chs_pt200_subjetMass"       ,"",100,0,400); 
  h_ak4chs_pt500_mass          =  fs->make<TH1D>("h_ak4chs_pt500_mass"             ,"",100,0,500); 
  h_ak4chs_pt500_prunedMass    =  fs->make<TH1D>("h_ak4chs_pt500_prunedMass"       ,"",100,0,500); 
  h_ak4chs_pt500_trimmedMass   =  fs->make<TH1D>("h_ak4chs_pt500_trimmedMass"      ,"",100,0,500); 
  h_ak4chs_pt500_filteredMass  =  fs->make<TH1D>("h_ak4chs_pt500_filteredMass"     ,"",100,0,500); 
  h_ak4chs_pt500_softDropMass  =  fs->make<TH1D>("h_ak4chs_pt500_softDropMass"     ,"",100,0,500); 
  h_ak4chs_pt500_tau32         =  fs->make<TH1D>("h_ak4chs_pt500_tau32"            ,"",100,0,  1); 
  h_ak4chs_pt500_tau21         =  fs->make<TH1D>("h_ak4chs_pt500_tau21"            ,"",100,0,  1); 
  h_ak4chs_pt500_subjetMass    =  fs->make<TH1D>("h_ak4chs_pt500_subjetMass"       ,"",100,0,400); 


  h_ak8pf_pt                  =  fs->make<TH1D>("h_ak8pf_pt"                     ,"",100,0,3000); 
  h_ak8pf_mass                =  fs->make<TH1D>("h_ak8pf_mass"                   ,"",100,0,500); 
  h_ak8pf_rapidity            =  fs->make<TH1D>("h_ak8pf_rapidity"               ,"",100,-5, 5); 
  h_ak8pf_prunedMass          =  fs->make<TH1D>("h_ak8pf_prunedMass"             ,"",100,0,500); 
  h_ak8pf_trimmedMass         =  fs->make<TH1D>("h_ak8pf_trimmedMass"            ,"",100,0,500); 
  h_ak8pf_filteredMass        =  fs->make<TH1D>("h_ak8pf_filteredMass"           ,"",100,0,500); 
  h_ak8pf_softDropMass        =  fs->make<TH1D>("h_ak8pf_softDropMass"           ,"",100,0,500); 
  h_ak8pf_tau1                =  fs->make<TH1D>("h_ak8pf_tau1"                   ,"",100,0,  1); 
  h_ak8pf_tau2                =  fs->make<TH1D>("h_ak8pf_tau2"                   ,"",100,0,  1); 
  h_ak8pf_tau3                =  fs->make<TH1D>("h_ak8pf_tau3"                   ,"",100,0,  1); 
  h_ak8pf_tau4                =  fs->make<TH1D>("h_ak8pf_tau4"                   ,"",100,0,  1); 
  h_ak8pf_tau32               =  fs->make<TH1D>("h_ak8pf_tau32"                  ,"",100,0,  1); 
  h_ak8pf_tau21               =  fs->make<TH1D>("h_ak8pf_tau21"                  ,"",100,0,  1); 
  h_ak8pf_ndau                =  fs->make<TH1D>("h_ak8pf_ndau"                   ,"",300,0,300); 
  h_ak8pf_subjetMass          =  fs->make<TH1D>("h_ak8pf_subjetMass"             ,"",100,0,400); 
  h_ak8pf_area                =  fs->make<TH1D>("h_ak8pf_area"                   ,"",100,0,  8); 
  h_ak8pf_pt200_mass          =  fs->make<TH1D>("h_ak8pf_pt200_mass"             ,"",100,0,500); 
  h_ak8pf_pt200_prunedMass    =  fs->make<TH1D>("h_ak8pf_pt200_prunedMass"       ,"",100,0,500); 
  h_ak8pf_pt200_trimmedMass   =  fs->make<TH1D>("h_ak8pf_pt200_trimmedMass"      ,"",100,0,500); 
  h_ak8pf_pt200_filteredMass  =  fs->make<TH1D>("h_ak8pf_pt200_filteredMass"     ,"",100,0,500); 
  h_ak8pf_pt200_softDropMass  =  fs->make<TH1D>("h_ak8pf_pt200_softDropMass"     ,"",100,0,500); 
  h_ak8pf_pt200_tau32         =  fs->make<TH1D>("h_ak8pf_pt200_tau32"            ,"",100,0,  1); 
  h_ak8pf_pt200_tau21         =  fs->make<TH1D>("h_ak8pf_pt200_tau21"            ,"",100,0,  1); 
  h_ak8pf_pt200_subjetMass    =  fs->make<TH1D>("h_ak8pf_pt200_subjetMass"       ,"",100,0,400); 
  h_ak8pf_pt500_mass          =  fs->make<TH1D>("h_ak8pf_pt500_mass"             ,"",100,0,500); 
  h_ak8pf_pt500_prunedMass    =  fs->make<TH1D>("h_ak8pf_pt500_prunedMass"       ,"",100,0,500); 
  h_ak8pf_pt500_trimmedMass   =  fs->make<TH1D>("h_ak8pf_pt500_trimmedMass"      ,"",100,0,500); 
  h_ak8pf_pt500_filteredMass  =  fs->make<TH1D>("h_ak8pf_pt500_filteredMass"     ,"",100,0,500); 
  h_ak8pf_pt500_softDropMass  =  fs->make<TH1D>("h_ak8pf_pt500_softDropMass"     ,"",100,0,500); 
  h_ak8pf_pt500_tau32         =  fs->make<TH1D>("h_ak8pf_pt500_tau32"            ,"",100,0,  1); 
  h_ak8pf_pt500_tau21         =  fs->make<TH1D>("h_ak8pf_pt500_tau21"            ,"",100,0,  1); 
  h_ak8pf_pt500_subjetMass    =  fs->make<TH1D>("h_ak8pf_pt500_subjetMass"       ,"",100,0,400); 


  h_ak8chs_pt                  =  fs->make<TH1D>("h_ak8chs_pt"                     ,"",100,0,3000); 
  h_ak8chs_mass                =  fs->make<TH1D>("h_ak8chs_mass"                   ,"",100,0,500); 
  h_ak8chs_rapidity            =  fs->make<TH1D>("h_ak8chs_rapidity"               ,"",100,-5, 5); 
  h_ak8chs_prunedMass          =  fs->make<TH1D>("h_ak8chs_prunedMass"             ,"",100,0,500); 
  h_ak8chs_trimmedMass         =  fs->make<TH1D>("h_ak8chs_trimmedMass"            ,"",100,0,500); 
  h_ak8chs_filteredMass        =  fs->make<TH1D>("h_ak8chs_filteredMass"           ,"",100,0,500); 
  h_ak8chs_softDropMass        =  fs->make<TH1D>("h_ak8chs_softDropMass"           ,"",100,0,500); 
  h_ak8chs_tau1                =  fs->make<TH1D>("h_ak8chs_tau1"                   ,"",100,0,  1); 
  h_ak8chs_tau2                =  fs->make<TH1D>("h_ak8chs_tau2"                   ,"",100,0,  1); 
  h_ak8chs_tau3                =  fs->make<TH1D>("h_ak8chs_tau3"                   ,"",100,0,  1); 
  h_ak8chs_tau4                =  fs->make<TH1D>("h_ak8chs_tau4"                   ,"",100,0,  1); 
  h_ak8chs_tau32               =  fs->make<TH1D>("h_ak8chs_tau32"                  ,"",100,0,  1); 
  h_ak8chs_tau21               =  fs->make<TH1D>("h_ak8chs_tau21"                  ,"",100,0,  1); 
  h_ak8chs_ndau                =  fs->make<TH1D>("h_ak8chs_ndau"                   ,"",300,0,300); 
  h_ak8chs_subjetMass          =  fs->make<TH1D>("h_ak8chs_subjetMass"             ,"",100,0,400); 
  h_ak8chs_area                =  fs->make<TH1D>("h_ak8chs_area"                   ,"",100,0,  8); 
  h_ak8chs_pt200_mass          =  fs->make<TH1D>("h_ak8chs_pt200_mass"             ,"",100,0,500); 
  h_ak8chs_pt200_prunedMass    =  fs->make<TH1D>("h_ak8chs_pt200_prunedMass"       ,"",100,0,500); 
  h_ak8chs_pt200_trimmedMass   =  fs->make<TH1D>("h_ak8chs_pt200_trimmedMass"      ,"",100,0,500); 
  h_ak8chs_pt200_filteredMass  =  fs->make<TH1D>("h_ak8chs_pt200_filteredMass"     ,"",100,0,500); 
  h_ak8chs_pt200_softDropMass  =  fs->make<TH1D>("h_ak8chs_pt200_softDropMass"     ,"",100,0,500); 
  h_ak8chs_pt200_tau32         =  fs->make<TH1D>("h_ak8chs_pt200_tau32"            ,"",100,0,  1); 
  h_ak8chs_pt200_tau21         =  fs->make<TH1D>("h_ak8chs_pt200_tau21"            ,"",100,0,  1); 
  h_ak8chs_pt200_subjetMass    =  fs->make<TH1D>("h_ak8chs_pt200_subjetMass"       ,"",100,0,400); 
  h_ak8chs_pt500_mass          =  fs->make<TH1D>("h_ak8chs_pt500_mass"             ,"",100,0,500); 
  h_ak8chs_pt500_prunedMass    =  fs->make<TH1D>("h_ak8chs_pt500_prunedMass"       ,"",100,0,500); 
  h_ak8chs_pt500_trimmedMass   =  fs->make<TH1D>("h_ak8chs_pt500_trimmedMass"      ,"",100,0,500); 
  h_ak8chs_pt500_filteredMass  =  fs->make<TH1D>("h_ak8chs_pt500_filteredMass"     ,"",100,0,500); 
  h_ak8chs_pt500_softDropMass  =  fs->make<TH1D>("h_ak8chs_pt500_softDropMass"     ,"",100,0,500); 
  h_ak8chs_pt500_tau32         =  fs->make<TH1D>("h_ak8chs_pt500_tau32"            ,"",100,0,  1); 
  h_ak8chs_pt500_tau21         =  fs->make<TH1D>("h_ak8chs_pt500_tau21"            ,"",100,0,  1); 
  h_ak8chs_pt500_subjetMass    =  fs->make<TH1D>("h_ak8chs_pt500_subjetMass"       ,"",100,0,400); 


  h_ak8puppi_pt                  =  fs->make<TH1D>("h_ak8puppi_pt"                     ,"",100,0,3000); 
  h_ak8puppi_mass                =  fs->make<TH1D>("h_ak8puppi_mass"                   ,"",100,0,500); 
  h_ak8puppi_rapidity            =  fs->make<TH1D>("h_ak8puppi_rapidity"               ,"",100,-5, 5); 
  h_ak8puppi_prunedMass          =  fs->make<TH1D>("h_ak8puppi_prunedMass"             ,"",100,0,500); 
  h_ak8puppi_trimmedMass         =  fs->make<TH1D>("h_ak8puppi_trimmedMass"            ,"",100,0,500); 
  h_ak8puppi_filteredMass        =  fs->make<TH1D>("h_ak8puppi_filteredMass"           ,"",100,0,500); 
  h_ak8puppi_softDropMass        =  fs->make<TH1D>("h_ak8puppi_softDropMass"           ,"",100,0,500); 
  h_ak8puppi_tau1                =  fs->make<TH1D>("h_ak8puppi_tau1"                   ,"",100,0,  1); 
  h_ak8puppi_tau2                =  fs->make<TH1D>("h_ak8puppi_tau2"                   ,"",100,0,  1); 
  h_ak8puppi_tau3                =  fs->make<TH1D>("h_ak8puppi_tau3"                   ,"",100,0,  1); 
  h_ak8puppi_tau4                =  fs->make<TH1D>("h_ak8puppi_tau4"                   ,"",100,0,  1); 
  h_ak8puppi_tau32               =  fs->make<TH1D>("h_ak8puppi_tau32"                  ,"",100,0,  1); 
  h_ak8puppi_tau21               =  fs->make<TH1D>("h_ak8puppi_tau21"                  ,"",100,0,  1); 
  h_ak8puppi_ndau                =  fs->make<TH1D>("h_ak8puppi_ndau"                   ,"",300,0,300); 
  h_ak8puppi_subjetMass          =  fs->make<TH1D>("h_ak8puppi_subjetMass"             ,"",100,0,400); 
  h_ak8puppi_area                =  fs->make<TH1D>("h_ak8puppi_area"                   ,"",100,0,  8); 
  h_ak8puppi_pt200_mass          =  fs->make<TH1D>("h_ak8puppi_pt200_mass"             ,"",100,0,500); 
  h_ak8puppi_pt200_prunedMass    =  fs->make<TH1D>("h_ak8puppi_pt200_prunedMass"       ,"",100,0,500); 
  h_ak8puppi_pt200_trimmedMass   =  fs->make<TH1D>("h_ak8puppi_pt200_trimmedMass"      ,"",100,0,500); 
  h_ak8puppi_pt200_filteredMass  =  fs->make<TH1D>("h_ak8puppi_pt200_filteredMass"     ,"",100,0,500); 
  h_ak8puppi_pt200_softDropMass  =  fs->make<TH1D>("h_ak8puppi_pt200_softDropMass"     ,"",100,0,500); 
  h_ak8puppi_pt200_tau32         =  fs->make<TH1D>("h_ak8puppi_pt200_tau32"            ,"",100,0,  1); 
  h_ak8puppi_pt200_tau21         =  fs->make<TH1D>("h_ak8puppi_pt200_tau21"            ,"",100,0,  1); 
  h_ak8puppi_pt200_subjetMass    =  fs->make<TH1D>("h_ak8puppi_pt200_subjetMass"       ,"",100,0,400); 
  h_ak8puppi_pt500_mass          =  fs->make<TH1D>("h_ak8puppi_pt500_mass"             ,"",100,0,500); 
  h_ak8puppi_pt500_prunedMass    =  fs->make<TH1D>("h_ak8puppi_pt500_prunedMass"       ,"",100,0,500); 
  h_ak8puppi_pt500_trimmedMass   =  fs->make<TH1D>("h_ak8puppi_pt500_trimmedMass"      ,"",100,0,500); 
  h_ak8puppi_pt500_filteredMass  =  fs->make<TH1D>("h_ak8puppi_pt500_filteredMass"     ,"",100,0,500); 
  h_ak8puppi_pt500_softDropMass  =  fs->make<TH1D>("h_ak8puppi_pt500_softDropMass"     ,"",100,0,500); 
  h_ak8puppi_pt500_tau32         =  fs->make<TH1D>("h_ak8puppi_pt500_tau32"            ,"",100,0,  1); 
  h_ak8puppi_pt500_tau21         =  fs->make<TH1D>("h_ak8puppi_pt500_tau21"            ,"",100,0,  1); 
  h_ak8puppi_pt500_subjetMass    =  fs->make<TH1D>("h_ak8puppi_pt500_subjetMass"       ,"",100,0,400); 


  h_kt8chs_pt                  =  fs->make<TH1D>("h_kt8chs_pt"                     ,"",100,0,3000); 
  h_kt8chs_mass                =  fs->make<TH1D>("h_kt8chs_mass"                   ,"",100,0,500); 
  h_kt8chs_rapidity            =  fs->make<TH1D>("h_kt8chs_rapidity"               ,"",100,-5, 5); 
  h_kt8chs_prunedMass          =  fs->make<TH1D>("h_kt8chs_prunedMass"             ,"",100,0,500); 
  h_kt8chs_trimmedMass         =  fs->make<TH1D>("h_kt8chs_trimmedMass"            ,"",100,0,500); 
  h_kt8chs_filteredMass        =  fs->make<TH1D>("h_kt8chs_filteredMass"           ,"",100,0,500); 
  h_kt8chs_softDropMass        =  fs->make<TH1D>("h_kt8chs_softDropMass"           ,"",100,0,500); 
  h_kt8chs_tau1                =  fs->make<TH1D>("h_kt8chs_tau1"                   ,"",100,0,  1); 
  h_kt8chs_tau2                =  fs->make<TH1D>("h_kt8chs_tau2"                   ,"",100,0,  1); 
  h_kt8chs_tau3                =  fs->make<TH1D>("h_kt8chs_tau3"                   ,"",100,0,  1); 
  h_kt8chs_tau4                =  fs->make<TH1D>("h_kt8chs_tau4"                   ,"",100,0,  1); 
  h_kt8chs_tau32               =  fs->make<TH1D>("h_kt8chs_tau32"                  ,"",100,0,  1); 
  h_kt8chs_tau21               =  fs->make<TH1D>("h_kt8chs_tau21"                  ,"",100,0,  1); 
  h_kt8chs_ndau                =  fs->make<TH1D>("h_kt8chs_ndau"                   ,"",300,0,300); 
  h_kt8chs_subjetMass          =  fs->make<TH1D>("h_kt8chs_subjetMass"             ,"",100,0,400); 
  h_kt8chs_area                =  fs->make<TH1D>("h_kt8chs_area"                   ,"",100,0,  8); 
  h_kt8chs_pt200_mass          =  fs->make<TH1D>("h_kt8chs_pt200_mass"             ,"",100,0,500); 
  h_kt8chs_pt200_prunedMass    =  fs->make<TH1D>("h_kt8chs_pt200_prunedMass"       ,"",100,0,500); 
  h_kt8chs_pt200_trimmedMass   =  fs->make<TH1D>("h_kt8chs_pt200_trimmedMass"      ,"",100,0,500); 
  h_kt8chs_pt200_filteredMass  =  fs->make<TH1D>("h_kt8chs_pt200_filteredMass"     ,"",100,0,500); 
  h_kt8chs_pt200_softDropMass  =  fs->make<TH1D>("h_kt8chs_pt200_softDropMass"     ,"",100,0,500); 
  h_kt8chs_pt200_tau32         =  fs->make<TH1D>("h_kt8chs_pt200_tau32"            ,"",100,0,  1); 
  h_kt8chs_pt200_tau21         =  fs->make<TH1D>("h_kt8chs_pt200_tau21"            ,"",100,0,  1); 
  h_kt8chs_pt200_subjetMass    =  fs->make<TH1D>("h_kt8chs_pt200_subjetMass"       ,"",100,0,400); 
  h_kt8chs_pt500_mass          =  fs->make<TH1D>("h_kt8chs_pt500_mass"             ,"",100,0,500); 
  h_kt8chs_pt500_prunedMass    =  fs->make<TH1D>("h_kt8chs_pt500_prunedMass"       ,"",100,0,500); 
  h_kt8chs_pt500_trimmedMass   =  fs->make<TH1D>("h_kt8chs_pt500_trimmedMass"      ,"",100,0,500); 
  h_kt8chs_pt500_filteredMass  =  fs->make<TH1D>("h_kt8chs_pt500_filteredMass"     ,"",100,0,500); 
  h_kt8chs_pt500_softDropMass  =  fs->make<TH1D>("h_kt8chs_pt500_softDropMass"     ,"",100,0,500); 
  h_kt8chs_pt500_tau32         =  fs->make<TH1D>("h_kt8chs_pt500_tau32"            ,"",100,0,  1); 
  h_kt8chs_pt500_tau21         =  fs->make<TH1D>("h_kt8chs_pt500_tau21"            ,"",100,0,  1); 
  h_kt8chs_pt500_subjetMass    =  fs->make<TH1D>("h_kt8chs_pt500_subjetMass"       ,"",100,0,400); 


  h_ca8chs_pt                  =  fs->make<TH1D>("h_ca8chs_pt"                     ,"",100,0,3000); 
  h_ca8chs_mass                =  fs->make<TH1D>("h_ca8chs_mass"                   ,"",100,0,500); 
  h_ca8chs_rapidity            =  fs->make<TH1D>("h_ca8chs_rapidity"               ,"",100,-5, 5); 
  h_ca8chs_prunedMass          =  fs->make<TH1D>("h_ca8chs_prunedMass"             ,"",100,0,500); 
  h_ca8chs_trimmedMass         =  fs->make<TH1D>("h_ca8chs_trimmedMass"            ,"",100,0,500); 
  h_ca8chs_filteredMass        =  fs->make<TH1D>("h_ca8chs_filteredMass"           ,"",100,0,500); 
  h_ca8chs_softDropMass        =  fs->make<TH1D>("h_ca8chs_softDropMass"           ,"",100,0,500); 
  h_ca8chs_tau1                =  fs->make<TH1D>("h_ca8chs_tau1"                   ,"",100,0,  1); 
  h_ca8chs_tau2                =  fs->make<TH1D>("h_ca8chs_tau2"                   ,"",100,0,  1); 
  h_ca8chs_tau3                =  fs->make<TH1D>("h_ca8chs_tau3"                   ,"",100,0,  1); 
  h_ca8chs_tau4                =  fs->make<TH1D>("h_ca8chs_tau4"                   ,"",100,0,  1); 
  h_ca8chs_tau32               =  fs->make<TH1D>("h_ca8chs_tau32"                  ,"",100,0,  1); 
  h_ca8chs_tau21               =  fs->make<TH1D>("h_ca8chs_tau21"                  ,"",100,0,  1); 
  h_ca8chs_ndau                =  fs->make<TH1D>("h_ca8chs_ndau"                   ,"",300,0,300); 
  h_ca8chs_subjetMass          =  fs->make<TH1D>("h_ca8chs_subjetMass"             ,"",100,0,400); 
  h_ca8chs_area                =  fs->make<TH1D>("h_ca8chs_area"                   ,"",100,0,  8); 
  h_ca8chs_pt200_mass          =  fs->make<TH1D>("h_ca8chs_pt200_mass"             ,"",100,0,500); 
  h_ca8chs_pt200_prunedMass    =  fs->make<TH1D>("h_ca8chs_pt200_prunedMass"       ,"",100,0,500); 
  h_ca8chs_pt200_trimmedMass   =  fs->make<TH1D>("h_ca8chs_pt200_trimmedMass"      ,"",100,0,500); 
  h_ca8chs_pt200_filteredMass  =  fs->make<TH1D>("h_ca8chs_pt200_filteredMass"     ,"",100,0,500); 
  h_ca8chs_pt200_softDropMass  =  fs->make<TH1D>("h_ca8chs_pt200_softDropMass"     ,"",100,0,500); 
  h_ca8chs_pt200_tau32         =  fs->make<TH1D>("h_ca8chs_pt200_tau32"            ,"",100,0,  1); 
  h_ca8chs_pt200_tau21         =  fs->make<TH1D>("h_ca8chs_pt200_tau21"            ,"",100,0,  1); 
  h_ca8chs_pt200_subjetMass    =  fs->make<TH1D>("h_ca8chs_pt200_subjetMass"       ,"",100,0,400); 
  h_ca8chs_pt500_mass          =  fs->make<TH1D>("h_ca8chs_pt500_mass"             ,"",100,0,500); 
  h_ca8chs_pt500_prunedMass    =  fs->make<TH1D>("h_ca8chs_pt500_prunedMass"       ,"",100,0,500); 
  h_ca8chs_pt500_trimmedMass   =  fs->make<TH1D>("h_ca8chs_pt500_trimmedMass"      ,"",100,0,500); 
  h_ca8chs_pt500_filteredMass  =  fs->make<TH1D>("h_ca8chs_pt500_filteredMass"     ,"",100,0,500); 
  h_ca8chs_pt500_softDropMass  =  fs->make<TH1D>("h_ca8chs_pt500_softDropMass"     ,"",100,0,500); 
  h_ca8chs_pt500_tau32         =  fs->make<TH1D>("h_ca8chs_pt500_tau32"            ,"",100,0,  1); 
  h_ca8chs_pt500_tau21         =  fs->make<TH1D>("h_ca8chs_pt500_tau21"            ,"",100,0,  1); 
  h_ca8chs_pt500_subjetMass    =  fs->make<TH1D>("h_ca8chs_pt500_subjetMass"       ,"",100,0,400); 



  h_ak12chs_pt                  =  fs->make<TH1D>("h_ak12chs_pt"                     ,"",100,0,3000); 
  h_ak12chs_mass                =  fs->make<TH1D>("h_ak12chs_mass"                   ,"",100,0,500); 
  h_ak12chs_rapidity            =  fs->make<TH1D>("h_ak12chs_rapidity"               ,"",100,-5, 5); 
  h_ak12chs_prunedMass          =  fs->make<TH1D>("h_ak12chs_prunedMass"             ,"",100,0,500); 
  h_ak12chs_trimmedMass         =  fs->make<TH1D>("h_ak12chs_trimmedMass"            ,"",100,0,500); 
  h_ak12chs_filteredMass        =  fs->make<TH1D>("h_ak12chs_filteredMass"           ,"",100,0,500); 
  h_ak12chs_softDropMass        =  fs->make<TH1D>("h_ak12chs_softDropMass"           ,"",100,0,500); 
  h_ak12chs_tau1                =  fs->make<TH1D>("h_ak12chs_tau1"                   ,"",100,0,  1); 
  h_ak12chs_tau2                =  fs->make<TH1D>("h_ak12chs_tau2"                   ,"",100,0,  1); 
  h_ak12chs_tau3                =  fs->make<TH1D>("h_ak12chs_tau3"                   ,"",100,0,  1); 
  h_ak12chs_tau4                =  fs->make<TH1D>("h_ak12chs_tau4"                   ,"",100,0,  1); 
  h_ak12chs_tau32               =  fs->make<TH1D>("h_ak12chs_tau32"                  ,"",100,0,  1); 
  h_ak12chs_tau21               =  fs->make<TH1D>("h_ak12chs_tau21"                  ,"",100,0,  1); 
  h_ak12chs_ndau                =  fs->make<TH1D>("h_ak12chs_ndau"                   ,"",300,0,300); 
  h_ak12chs_subjetMass          =  fs->make<TH1D>("h_ak12chs_subjetMass"             ,"",100,0,400); 
  h_ak12chs_area                =  fs->make<TH1D>("h_ak12chs_area"                   ,"",100,0,  8); 
  h_ak12chs_pt200_mass          =  fs->make<TH1D>("h_ak12chs_pt200_mass"             ,"",100,0,500); 
  h_ak12chs_pt200_prunedMass    =  fs->make<TH1D>("h_ak12chs_pt200_prunedMass"       ,"",100,0,500); 
  h_ak12chs_pt200_trimmedMass   =  fs->make<TH1D>("h_ak12chs_pt200_trimmedMass"      ,"",100,0,500); 
  h_ak12chs_pt200_filteredMass  =  fs->make<TH1D>("h_ak12chs_pt200_filteredMass"     ,"",100,0,500); 
  h_ak12chs_pt200_softDropMass  =  fs->make<TH1D>("h_ak12chs_pt200_softDropMass"     ,"",100,0,500); 
  h_ak12chs_pt200_tau32         =  fs->make<TH1D>("h_ak12chs_pt200_tau32"            ,"",100,0,  1); 
  h_ak12chs_pt200_tau21         =  fs->make<TH1D>("h_ak12chs_pt200_tau21"            ,"",100,0,  1); 
  h_ak12chs_pt200_subjetMass    =  fs->make<TH1D>("h_ak12chs_pt200_subjetMass"       ,"",100,0,400); 
  h_ak12chs_pt500_mass          =  fs->make<TH1D>("h_ak12chs_pt500_mass"             ,"",100,0,500); 
  h_ak12chs_pt500_prunedMass    =  fs->make<TH1D>("h_ak12chs_pt500_prunedMass"       ,"",100,0,500); 
  h_ak12chs_pt500_trimmedMass   =  fs->make<TH1D>("h_ak12chs_pt500_trimmedMass"      ,"",100,0,500); 
  h_ak12chs_pt500_filteredMass  =  fs->make<TH1D>("h_ak12chs_pt500_filteredMass"     ,"",100,0,500); 
  h_ak12chs_pt500_softDropMass  =  fs->make<TH1D>("h_ak12chs_pt500_softDropMass"     ,"",100,0,500); 
  h_ak12chs_pt500_tau32         =  fs->make<TH1D>("h_ak12chs_pt500_tau32"            ,"",100,0,  1); 
  h_ak12chs_pt500_tau21         =  fs->make<TH1D>("h_ak12chs_pt500_tau21"            ,"",100,0,  1); 
  h_ak12chs_pt500_subjetMass    =  fs->make<TH1D>("h_ak12chs_pt500_subjetMass"       ,"",100,0,400); 



  h_ak15chs_pt                  =  fs->make<TH1D>("h_ak15chs_pt"                     ,"",100,0,3000); 
  h_ak15chs_mass                =  fs->make<TH1D>("h_ak15chs_mass"                   ,"",100,0,500); 
  h_ak15chs_rapidity            =  fs->make<TH1D>("h_ak15chs_rapidity"               ,"",100,-5, 5); 
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
  bool verbose = false;


  //--------------------------------------------------------------------------------------------
  // AK R=0.4 jets - from toolbox

  edm::Handle<pat::JetCollection> AK4CHS;
  iEvent.getByToken(ak4PFCHSjetToken_, AK4CHS);

  edm::Handle<pat::JetCollection> AK4CHSsub;
  iEvent.getByToken(ak4PFCHSSoftDropSubjetsToken_, AK4CHSsub);

  int count_AK4CHS = 0;
  for (const pat::Jet &ijet : *AK4CHS) {  
    count_AK4CHS++;
    if (count_AK4CHS>=2) break;
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double prunedMass   = ijet.userFloat("ak4PFJetsCHSPrunedMass");
    double trimmedMass  = ijet.userFloat("ak4PFJetsCHSTrimmedMass");
    double filteredMass = ijet.userFloat("ak4PFJetsCHSFilteredMass");
    double softDropMass = ijet.userFloat("ak4PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK4CHS:tau1");
    double tau2         = ijet.userFloat("NjettinessAK4CHS:tau2");
    double tau3         = ijet.userFloat("NjettinessAK4CHS:tau3");
    double tau4         = ijet.userFloat("NjettinessAK4CHS:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *AK4CHSsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<0.4){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_ak4chs_pt           ->Fill( pt           );
    h_ak4chs_mass         ->Fill( mass         );
    h_ak4chs_rapidity     ->Fill( rapidity     );
    h_ak4chs_prunedMass   ->Fill( prunedMass   );
    h_ak4chs_trimmedMass  ->Fill( trimmedMass  );
    h_ak4chs_filteredMass ->Fill( filteredMass );
    h_ak4chs_softDropMass ->Fill( softDropMass );
    h_ak4chs_tau1         ->Fill( tau1         );
    h_ak4chs_tau2         ->Fill( tau2         );
    h_ak4chs_tau3         ->Fill( tau3         );
    h_ak4chs_tau4         ->Fill( tau4         );
    h_ak4chs_tau32        ->Fill( tau32        );
    h_ak4chs_tau21        ->Fill( tau21        );
    h_ak4chs_ndau         ->Fill( ndau         );
    h_ak4chs_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_ak4chs_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_ak4chs_pt200_mass         ->Fill( mass                            );
      h_ak4chs_pt200_prunedMass   ->Fill( prunedMass                      );
      h_ak4chs_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_ak4chs_pt200_filteredMass ->Fill( filteredMass                    );
      h_ak4chs_pt200_softDropMass ->Fill( softDropMass                    );
      h_ak4chs_pt200_tau32        ->Fill( tau32                           );
      h_ak4chs_pt200_tau21        ->Fill( tau21                           );
      h_ak4chs_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_ak4chs_pt500_mass         ->Fill( mass                            );
      h_ak4chs_pt500_prunedMass   ->Fill( prunedMass                      );
      h_ak4chs_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_ak4chs_pt500_filteredMass ->Fill( filteredMass                    );
      h_ak4chs_pt500_softDropMass ->Fill( softDropMass                    );
      h_ak4chs_pt500_tau32        ->Fill( tau32                           );
      h_ak4chs_pt500_tau21        ->Fill( tau21                           );
      h_ak4chs_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }


  //--------------------------------------------------------------------------------------------
  // AK R=0.8 PF jets - from toolbox

  edm::Handle<pat::JetCollection> AK8PF;
  iEvent.getByToken(ak8PFCHSjetToken_, AK8PF);

  edm::Handle<pat::JetCollection> AK8PFsub;
  iEvent.getByToken(ak8PFCHSSoftDropSubjetsToken_, AK8PFsub);

  int count_AK8PF = 0;
  for (const pat::Jet &ijet : *AK8PF) {  
    count_AK8PF++;
    if (count_AK8PF>=2) break;  
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double prunedMass   = ijet.userFloat("ak8PFJetsCHSPrunedMass");
    double trimmedMass  = ijet.userFloat("ak8PFJetsCHSTrimmedMass");
    double filteredMass = ijet.userFloat("ak8PFJetsCHSFilteredMass");
    double softDropMass = ijet.userFloat("ak8PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK8CHS:tau1");
    double tau2         = ijet.userFloat("NjettinessAK8CHS:tau2");
    double tau3         = ijet.userFloat("NjettinessAK8CHS:tau3");
    double tau4         = ijet.userFloat("NjettinessAK8CHS:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *AK8PFsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<0.8){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_ak8pf_pt           ->Fill( pt           );
    h_ak8pf_mass         ->Fill( mass         );
    h_ak8pf_rapidity     ->Fill( rapidity     );
    h_ak8pf_prunedMass   ->Fill( prunedMass   );
    h_ak8pf_trimmedMass  ->Fill( trimmedMass  );
    h_ak8pf_filteredMass ->Fill( filteredMass );
    h_ak8pf_softDropMass ->Fill( softDropMass );
    h_ak8pf_tau1         ->Fill( tau1         );
    h_ak8pf_tau2         ->Fill( tau2         );
    h_ak8pf_tau3         ->Fill( tau3         );
    h_ak8pf_tau4         ->Fill( tau4         );
    h_ak8pf_tau32        ->Fill( tau32        );
    h_ak8pf_tau21        ->Fill( tau21        );
    h_ak8pf_ndau         ->Fill( ndau         );
    h_ak8pf_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_ak8pf_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_ak8pf_pt200_mass         ->Fill( mass                            );
      h_ak8pf_pt200_prunedMass   ->Fill( prunedMass                      );
      h_ak8pf_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_ak8pf_pt200_filteredMass ->Fill( filteredMass                    );
      h_ak8pf_pt200_softDropMass ->Fill( softDropMass                    );
      h_ak8pf_pt200_tau32        ->Fill( tau32                           );
      h_ak8pf_pt200_tau21        ->Fill( tau21                           );
      h_ak8pf_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_ak8pf_pt500_mass         ->Fill( mass                            );
      h_ak8pf_pt500_prunedMass   ->Fill( prunedMass                      );
      h_ak8pf_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_ak8pf_pt500_filteredMass ->Fill( filteredMass                    );
      h_ak8pf_pt500_softDropMass ->Fill( softDropMass                    );
      h_ak8pf_pt500_tau32        ->Fill( tau32                           );
      h_ak8pf_pt500_tau21        ->Fill( tau21                           );
      h_ak8pf_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }
  

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 CHS jets - from toolbox

  edm::Handle<pat::JetCollection> AK8CHS;
  iEvent.getByToken(ak8PFCHSjetToken_, AK8CHS);

  edm::Handle<pat::JetCollection> AK8CHSsub;
  iEvent.getByToken(ak8PFCHSSoftDropSubjetsToken_, AK8CHSsub);

  int count_AK8CHS = 0;
  for (const pat::Jet &ijet : *AK8CHS) {  
    count_AK8CHS++;
    if (count_AK8CHS>=2) break; 
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double prunedMass   = ijet.userFloat("ak8PFJetsCHSPrunedMass");
    double trimmedMass  = ijet.userFloat("ak8PFJetsCHSTrimmedMass");
    double filteredMass = ijet.userFloat("ak8PFJetsCHSFilteredMass");
    double softDropMass = ijet.userFloat("ak8PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK8CHS:tau1");
    double tau2         = ijet.userFloat("NjettinessAK8CHS:tau2");
    double tau3         = ijet.userFloat("NjettinessAK8CHS:tau3");
    double tau4         = ijet.userFloat("NjettinessAK8CHS:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *AK8CHSsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<0.8){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_ak8chs_pt           ->Fill( pt           );
    h_ak8chs_mass         ->Fill( mass         );
    h_ak8chs_rapidity     ->Fill( rapidity     );
    h_ak8chs_prunedMass   ->Fill( prunedMass   );
    h_ak8chs_trimmedMass  ->Fill( trimmedMass  );
    h_ak8chs_filteredMass ->Fill( filteredMass );
    h_ak8chs_softDropMass ->Fill( softDropMass );
    h_ak8chs_tau1         ->Fill( tau1         );
    h_ak8chs_tau2         ->Fill( tau2         );
    h_ak8chs_tau3         ->Fill( tau3         );
    h_ak8chs_tau4         ->Fill( tau4         );
    h_ak8chs_tau32        ->Fill( tau32        );
    h_ak8chs_tau21        ->Fill( tau21        );
    h_ak8chs_ndau         ->Fill( ndau         );
    h_ak8chs_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_ak8chs_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_ak8chs_pt200_mass         ->Fill( mass                            );
      h_ak8chs_pt200_prunedMass   ->Fill( prunedMass                      );
      h_ak8chs_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_ak8chs_pt200_filteredMass ->Fill( filteredMass                    );
      h_ak8chs_pt200_softDropMass ->Fill( softDropMass                    );
      h_ak8chs_pt200_tau32        ->Fill( tau32                           );
      h_ak8chs_pt200_tau21        ->Fill( tau21                           );
      h_ak8chs_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_ak8chs_pt500_mass         ->Fill( mass                            );
      h_ak8chs_pt500_prunedMass   ->Fill( prunedMass                      );
      h_ak8chs_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_ak8chs_pt500_filteredMass ->Fill( filteredMass                    );
      h_ak8chs_pt500_softDropMass ->Fill( softDropMass                    );
      h_ak8chs_pt500_tau32        ->Fill( tau32                           );
      h_ak8chs_pt500_tau21        ->Fill( tau21                           );
      h_ak8chs_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }
  

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 PUPPI jets - from toolbox

  edm::Handle<pat::JetCollection> AK8PUPPI;
  iEvent.getByToken(ak8PFPUPPIjetToken_, AK8PUPPI);

  edm::Handle<pat::JetCollection> AK8PUPPIsub;
  iEvent.getByToken(ak8PFPUPPISoftDropSubjetsToken_, AK8PUPPIsub);

  int count_AK8PUPPI = 0;
  for (const pat::Jet &ijet : *AK8PUPPI) {  
    count_AK8PUPPI++;
    if (count_AK8PUPPI>=2) break;    
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double prunedMass   = ijet.userFloat("ak8PFJetsPuppiPrunedMass");
    double trimmedMass  = ijet.userFloat("ak8PFJetsPuppiTrimmedMass");
    double filteredMass = ijet.userFloat("ak8PFJetsPuppiFilteredMass");
    double softDropMass = ijet.userFloat("ak8PFJetsPuppiSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK8Puppi:tau1");
    double tau2         = ijet.userFloat("NjettinessAK8Puppi:tau2");
    double tau3         = ijet.userFloat("NjettinessAK8Puppi:tau3");
    double tau4         = ijet.userFloat("NjettinessAK8Puppi:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *AK8PUPPIsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<0.8){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_ak8puppi_pt           ->Fill( pt           );
    h_ak8puppi_mass         ->Fill( mass         );
    h_ak8puppi_rapidity     ->Fill( rapidity     );
    h_ak8puppi_prunedMass   ->Fill( prunedMass   );
    h_ak8puppi_trimmedMass  ->Fill( trimmedMass  );
    h_ak8puppi_filteredMass ->Fill( filteredMass );
    h_ak8puppi_softDropMass ->Fill( softDropMass );
    h_ak8puppi_tau1         ->Fill( tau1         );
    h_ak8puppi_tau2         ->Fill( tau2         );
    h_ak8puppi_tau3         ->Fill( tau3         );
    h_ak8puppi_tau4         ->Fill( tau4         );
    h_ak8puppi_tau32        ->Fill( tau32        );
    h_ak8puppi_tau21        ->Fill( tau21        );
    h_ak8puppi_ndau         ->Fill( ndau         );
    h_ak8puppi_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_ak8puppi_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_ak8puppi_pt200_mass         ->Fill( mass                            );
      h_ak8puppi_pt200_prunedMass   ->Fill( prunedMass                      );
      h_ak8puppi_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_ak8puppi_pt200_filteredMass ->Fill( filteredMass                    );
      h_ak8puppi_pt200_softDropMass ->Fill( softDropMass                    );
      h_ak8puppi_pt200_tau32        ->Fill( tau32                           );
      h_ak8puppi_pt200_tau21        ->Fill( tau21                           );
      h_ak8puppi_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_ak8puppi_pt500_mass         ->Fill( mass                            );
      h_ak8puppi_pt500_prunedMass   ->Fill( prunedMass                      );
      h_ak8puppi_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_ak8puppi_pt500_filteredMass ->Fill( filteredMass                    );
      h_ak8puppi_pt500_softDropMass ->Fill( softDropMass                    );
      h_ak8puppi_pt500_tau32        ->Fill( tau32                           );
      h_ak8puppi_pt500_tau21        ->Fill( tau21                           );
      h_ak8puppi_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }

  //--------------------------------------------------------------------------------------------
  // CA R=0.8 jets - from toolbox

  edm::Handle<pat::JetCollection> CA8CHS;
  iEvent.getByToken(ca8PFCHSjetToken_, CA8CHS);

  edm::Handle<pat::JetCollection> CA8CHSsub;
  iEvent.getByToken(ca8PFCHSSoftDropSubjetsToken_, CA8CHSsub);

  int count_CA8CHS = 0;
  for (const pat::Jet &ijet : *CA8CHS) {  
    count_CA8CHS++;
    if (count_CA8CHS>=2) break;   
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double prunedMass   = ijet.userFloat("ca8PFJetsCHSPrunedMass");
    double trimmedMass  = ijet.userFloat("ca8PFJetsCHSTrimmedMass");
    double filteredMass = ijet.userFloat("ca8PFJetsCHSFilteredMass");
    double softDropMass = ijet.userFloat("ca8PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessCA8CHS:tau1");
    double tau2         = ijet.userFloat("NjettinessCA8CHS:tau2");
    double tau3         = ijet.userFloat("NjettinessCA8CHS:tau3");
    double tau4         = ijet.userFloat("NjettinessCA8CHS:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *CA8CHSsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<0.8){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_ca8chs_pt           ->Fill( pt           );
    h_ca8chs_mass         ->Fill( mass         );
    h_ca8chs_rapidity     ->Fill( rapidity     );
    h_ca8chs_prunedMass   ->Fill( prunedMass   );
    h_ca8chs_trimmedMass  ->Fill( trimmedMass  );
    h_ca8chs_filteredMass ->Fill( filteredMass );
    h_ca8chs_softDropMass ->Fill( softDropMass );
    h_ca8chs_tau1         ->Fill( tau1         );
    h_ca8chs_tau2         ->Fill( tau2         );
    h_ca8chs_tau3         ->Fill( tau3         );
    h_ca8chs_tau4         ->Fill( tau4         );
    h_ca8chs_tau32        ->Fill( tau32        );
    h_ca8chs_tau21        ->Fill( tau21        );
    h_ca8chs_ndau         ->Fill( ndau         );
    h_ca8chs_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_ca8chs_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_ca8chs_pt200_mass         ->Fill( mass                            );
      h_ca8chs_pt200_prunedMass   ->Fill( prunedMass                      );
      h_ca8chs_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_ca8chs_pt200_filteredMass ->Fill( filteredMass                    );
      h_ca8chs_pt200_softDropMass ->Fill( softDropMass                    );
      h_ca8chs_pt200_tau32        ->Fill( tau32                           );
      h_ca8chs_pt200_tau21        ->Fill( tau21                           );
      h_ca8chs_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_ca8chs_pt500_mass         ->Fill( mass                            );
      h_ca8chs_pt500_prunedMass   ->Fill( prunedMass                      );
      h_ca8chs_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_ca8chs_pt500_filteredMass ->Fill( filteredMass                    );
      h_ca8chs_pt500_softDropMass ->Fill( softDropMass                    );
      h_ca8chs_pt500_tau32        ->Fill( tau32                           );
      h_ca8chs_pt500_tau21        ->Fill( tau21                           );
      h_ca8chs_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }
  

  //--------------------------------------------------------------------------------------------
  // KT R=0.8 jets - from toolbox

  edm::Handle<pat::JetCollection> KT8CHS;
  iEvent.getByToken(kt8PFCHSjetToken_, KT8CHS);

  edm::Handle<pat::JetCollection> KT8CHSsub;
  iEvent.getByToken(kt8PFCHSSoftDropSubjetsToken_, KT8CHSsub);

  int count_KT8CHS = 0;
  for (const pat::Jet &ijet : *KT8CHS) {  
    count_KT8CHS++;
    if (count_KT8CHS>=2) break;   
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double prunedMass   = ijet.userFloat("kt8PFJetsCHSPrunedMass");
    double trimmedMass  = ijet.userFloat("kt8PFJetsCHSTrimmedMass");
    double filteredMass = ijet.userFloat("kt8PFJetsCHSFilteredMass");
    double softDropMass = ijet.userFloat("kt8PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessKT8CHS:tau1");
    double tau2         = ijet.userFloat("NjettinessKT8CHS:tau2");
    double tau3         = ijet.userFloat("NjettinessKT8CHS:tau3");
    double tau4         = ijet.userFloat("NjettinessKT8CHS:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *KT8CHSsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<0.8){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_kt8chs_pt           ->Fill( pt           );
    h_kt8chs_mass         ->Fill( mass         );
    h_kt8chs_rapidity     ->Fill( rapidity     );
    h_kt8chs_prunedMass   ->Fill( prunedMass   );
    h_kt8chs_trimmedMass  ->Fill( trimmedMass  );
    h_kt8chs_filteredMass ->Fill( filteredMass );
    h_kt8chs_softDropMass ->Fill( softDropMass );
    h_kt8chs_tau1         ->Fill( tau1         );
    h_kt8chs_tau2         ->Fill( tau2         );
    h_kt8chs_tau3         ->Fill( tau3         );
    h_kt8chs_tau4         ->Fill( tau4         );
    h_kt8chs_tau32        ->Fill( tau32        );
    h_kt8chs_tau21        ->Fill( tau21        );
    h_kt8chs_ndau         ->Fill( ndau         );
    h_kt8chs_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_kt8chs_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_kt8chs_pt200_mass         ->Fill( mass                            );
      h_kt8chs_pt200_prunedMass   ->Fill( prunedMass                      );
      h_kt8chs_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_kt8chs_pt200_filteredMass ->Fill( filteredMass                    );
      h_kt8chs_pt200_softDropMass ->Fill( softDropMass                    );
      h_kt8chs_pt200_tau32        ->Fill( tau32                           );
      h_kt8chs_pt200_tau21        ->Fill( tau21                           );
      h_kt8chs_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_kt8chs_pt500_mass         ->Fill( mass                            );
      h_kt8chs_pt500_prunedMass   ->Fill( prunedMass                      );
      h_kt8chs_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_kt8chs_pt500_filteredMass ->Fill( filteredMass                    );
      h_kt8chs_pt500_softDropMass ->Fill( softDropMass                    );
      h_kt8chs_pt500_tau32        ->Fill( tau32                           );
      h_kt8chs_pt500_tau21        ->Fill( tau21                           );
      h_kt8chs_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }
  

  //--------------------------------------------------------------------------------------------
  // AK R=1.2 jets - from toolbox

  edm::Handle<pat::JetCollection> AK12CHS;
  iEvent.getByToken(ak12PFCHSjetToken_, AK12CHS);

  edm::Handle<pat::JetCollection> AK12CHSsub;
  iEvent.getByToken(ak12PFCHSSoftDropSubjetsToken_, AK12CHSsub);

  int count_AK12CHS = 0;
  for (const pat::Jet &ijet : *AK12CHS) {  
    count_AK12CHS++;
    if (count_AK12CHS>=2) break; 
    double pt           = ijet.pt();
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double prunedMass   = ijet.userFloat("ak12PFJetsCHSPrunedMass");
    double trimmedMass  = ijet.userFloat("ak12PFJetsCHSTrimmedMass");
    double filteredMass = ijet.userFloat("ak12PFJetsCHSFilteredMass");
    double softDropMass = ijet.userFloat("ak12PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK12CHS:tau1");
    double tau2         = ijet.userFloat("NjettinessAK12CHS:tau2");
    double tau3         = ijet.userFloat("NjettinessAK12CHS:tau3");
    double tau4         = ijet.userFloat("NjettinessAK12CHS:tau4");
    double ndau         = ijet.numberOfDaughters();
    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;
   
    double mostMassiveSDsubjetMass = 0;
    for (const pat::Jet &isub : *AK12CHSsub) {  
      double subjetEta      = isub.eta();
      double subjetPhi      = isub.phi();
      double subjetMass     = isub.mass();
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (deltaRsubjetJet<1.2){
        if (verbose) cout<<"matched subjet with mass "<< subjetMass<<endl;
        if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      }
    }

    h_ak12chs_pt           ->Fill( pt           );
    h_ak12chs_mass         ->Fill( mass         );
    h_ak12chs_rapidity     ->Fill( rapidity     );
    h_ak12chs_prunedMass   ->Fill( prunedMass   );
    h_ak12chs_trimmedMass  ->Fill( trimmedMass  );
    h_ak12chs_filteredMass ->Fill( filteredMass );
    h_ak12chs_softDropMass ->Fill( softDropMass );
    h_ak12chs_tau1         ->Fill( tau1         );
    h_ak12chs_tau2         ->Fill( tau2         );
    h_ak12chs_tau3         ->Fill( tau3         );
    h_ak12chs_tau4         ->Fill( tau4         );
    h_ak12chs_tau32        ->Fill( tau32        );
    h_ak12chs_tau21        ->Fill( tau21        );
    h_ak12chs_ndau         ->Fill( ndau         );
    h_ak12chs_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    h_ak12chs_area         ->Fill( ijet.jetArea() );

    if (pt>200){ 
      h_ak12chs_pt200_mass         ->Fill( mass                            );
      h_ak12chs_pt200_prunedMass   ->Fill( prunedMass                      );
      h_ak12chs_pt200_trimmedMass  ->Fill( trimmedMass                     );
      h_ak12chs_pt200_filteredMass ->Fill( filteredMass                    );
      h_ak12chs_pt200_softDropMass ->Fill( softDropMass                    );
      h_ak12chs_pt200_tau32        ->Fill( tau32                           );
      h_ak12chs_pt200_tau21        ->Fill( tau21                           );
      h_ak12chs_pt200_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
    if (pt>500){ 
      h_ak12chs_pt500_mass         ->Fill( mass                            );
      h_ak12chs_pt500_prunedMass   ->Fill( prunedMass                      );
      h_ak12chs_pt500_trimmedMass  ->Fill( trimmedMass                     );
      h_ak12chs_pt500_filteredMass ->Fill( filteredMass                    );
      h_ak12chs_pt500_softDropMass ->Fill( softDropMass                    );
      h_ak12chs_pt500_tau32        ->Fill( tau32                           );
      h_ak12chs_pt500_tau21        ->Fill( tau21                           );
      h_ak12chs_pt500_subjetMass   ->Fill( mostMassiveSDsubjetMass         );
    }
  }
  



  //--------------------------------------------------------------------------------------------
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
    double rapidity     = ijet.rapidity();
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
    h_ak15chs_rapidity     ->Fill( rapidity     );
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
  }



  //--------------------------------------------------------------------------------------------
  // AK R=0.8 jets - default miniAOD

  edm::Handle<pat::JetCollection> AK8MINI;
  iEvent.getByToken(ak8jetMiniToken_, AK8MINI);

  edm::Handle<reco::GenJetCollection> AK8GENJET;  
  iEvent.getByToken(ak8genjetToken_, AK8GENJET);

  for (const pat::Jet &ijet : *AK8MINI) {  
    double pt           = ijet.pt();
    if (pt<400) continue;
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double ndau         = ijet.numberOfDaughters();
    double prunedMass   = ijet.userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass");
    double softDropMass = ijet.userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK8Puppi:tau1");
    double tau2         = ijet.userFloat("NjettinessAK8Puppi:tau2");
    double tau3         = ijet.userFloat("NjettinessAK8Puppi:tau3");
    double tau21        = 99;
    double tau32        = 99;

    double puppi_pt           = ijet.pt();//userFloat("ak8PFJetsPuppiValueMap:pt");
    double puppi_mass         = ijet.mass();//userFloat("ak8PFJetsPuppiValueMap:mass");
    double puppi_eta          = ijet.eta();//userFloat("ak8PFJetsPuppiValueMap:eta");
    double puppi_phi          = ijet.phi();//userFloat("ak8PFJetsPuppiValueMap:phi");
    double puppi_tau1         = ijet.userFloat("NjettinessAK8Puppi:tau1");
    double puppi_tau2         = ijet.userFloat("NjettinessAK8Puppi:tau2");
    double puppi_tau3         = ijet.userFloat("NjettinessAK8Puppi:tau3");
    double puppi_tau21        = 99;
    double puppi_tau32        = 99;

   
    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;

    if (puppi_tau1!=0) puppi_tau21 = puppi_tau2/puppi_tau1;
    if (puppi_tau2!=0) puppi_tau32 = puppi_tau3/puppi_tau2;

    if (verbose) cout<<"\nJet with pT "<<pt<<" sdMass "<<softDropMass<<endl;

    if (verbose) cout<<"tau21 "<<tau21<<endl;
    if (verbose) cout<<"tau32 "<<tau32<<endl;

    if (verbose) cout<<"puppi_tau21 "<<puppi_tau21<<endl;
    if (verbose) cout<<"puppi_tau32 "<<puppi_tau32<<endl;

    // Soft Drop + Nsubjettiness tagger
    bool SoftDropTau32Tagged = false;
    if (softDropMass<230 && softDropMass>140 && tau32 <0.65) SoftDropTau32Tagged = true;

    // Get Soft drop subjets for subjet b-tagging
    double mostMassiveSDsubjetMass = 0;
    auto const & sdSubjets = ijet.subjets("SoftDropPuppi");
    for ( auto const & it : sdSubjets ) {
      double subjetPt       = it->pt();
      double subjetPtUncorr = it->pt();
      double subjetEta      = it->eta();
      double subjetPhi      = it->phi();
      double subjetMass     = it->mass();
      double subjetBdisc    = it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (verbose) cout<<" SD Subjet pt "<<subjetPt<<" uncorr "<<subjetPtUncorr<<" Eta "<<subjetEta<<" deltaRsubjetJet "<<deltaRsubjetJet<<" Mass "<<subjetMass<<" Bdisc "<<subjetBdisc<<endl;
      // h_ak8chs_sdSubjetMass ->Fill( subjetMass );
      if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
    }

    // Get Soft drop PUPPI subjets 
    TLorentzVector pup0;
    TLorentzVector pup1;
    double mostMassiveSDPUPPIsubjetMass = 0;
    auto const & sdSubjetsPuppi = ijet.subjets("SoftDropPuppi");
    int count_pup=0;
    for ( auto const & it : sdSubjetsPuppi ) {
      double subjetPt       = it->pt();
      double subjetPtUncorr = it->pt();
      double subjetEta      = it->eta();
      double subjetPhi      = it->phi();
      double subjetMass     = it->mass();
      double subjetBdisc    = it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (verbose) cout<<" SD Subjet pt "<<subjetPt<<" uncorr "<<subjetPtUncorr<<" Eta "<<subjetEta<<" deltaRsubjetJet "<<deltaRsubjetJet<<" Mass "<<subjetMass<<" Bdisc "<<subjetBdisc<<endl; 
      // h_ak8puppi_sdSubjetMass ->Fill( subjetMass );
      if (count_pup==0) pup0.SetPtEtaPhiM( subjetPt, subjetEta, subjetPhi, subjetMass);
      if (count_pup==1) pup1.SetPtEtaPhiM( subjetPt, subjetEta, subjetPhi, subjetMass);
      if (subjetMass > mostMassiveSDPUPPIsubjetMass) mostMassiveSDPUPPIsubjetMass = subjetMass;
      count_pup++;
    }

    TLorentzVector puppiSD;
    if (count_pup>1)
    {
      puppiSD = pup0 + pup1;
      if (verbose) cout<<pup0.M()<<" "<<pup1.M()<<" "<<puppiSD.M()<<" "<<endl;
    }

    //Print some jet info
    if (verbose && SoftDropTau32Tagged) cout<<"->SoftDropTau32Tagged"<<endl;
    if (verbose){
      cout<<"mass         "<<mass         <<endl;  
      cout<<"rapidity     "<<rapidity     <<endl;  
      cout<<"ndau         "<<ndau         <<endl;  
      cout<<"prunedMass   "<<prunedMass   <<endl;  
      cout<<"softDropMass "<<softDropMass <<endl;
      cout<<"tau1         "<<tau1         <<endl;  
      cout<<"tau2         "<<tau2         <<endl;  
      cout<<"tau3         "<<tau3         <<endl;  
      cout<<"tau21        "<<tau21        <<endl;  
      cout<<"tau32        "<<tau32        <<endl;  
      cout<<"puppi_pt     "<<puppi_pt     <<endl;  
      cout<<"puppi_mass   "<<puppi_mass   <<endl;  
      cout<<"puppi_eta    "<<puppi_eta    <<endl;  
      cout<<"puppi_phi    "<<puppi_phi    <<endl;  
      cout<<"puppi_tau1   "<<puppi_tau1   <<endl;  
      cout<<"puppi_tau2   "<<puppi_tau2   <<endl;  
      cout<<"puppi_tau3   "<<puppi_tau3   <<endl;  
      cout<<"puppi_tau21  "<<puppi_tau21  <<endl;  
      cout<<"puppi_tau32  "<<puppi_tau32  <<endl;  
    }


  }


  // edm::Handle<std::vector<pat::Jet> > AK8MINI;
  // iEvent.getByLabel( "slimmedJetsAK8", AK8MINI );
  // edm::Handle<std::vector<pat::Jet> > AK8MINI_SD_Subjets;
  // iEvent.getByLabel( "slimmedJetsAK8PFCHSSoftDropPacked", "SubJets", AK8MINI_SD_Subjets );
  // edm::Handle<std::vector<pat::Jet> > AK8MINI_CMSTopTag_Subjets;
  // iEvent.getByLabel( "slimmedJetsCMSTopTagCHSPacked", "SubJets", AK8MINI_CMSTopTag_Subjets );


  // for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8MINI_SD_Subjets->begin(), jetEnd = AK8MINI_SD_Subjets->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  // {
  //       double pt           = ijet->pt();
  //       double bdisc        = ijet->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags");
  //       cout<<"SD subjet pt "<<pt<<" bdisc "<<bdisc<<endl;
  // }
  // cout<<endl;
  // for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8MINI_CMSTopTag_Subjets->begin(), jetEnd = AK8MINI_CMSTopTag_Subjets->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  // {
  //       double pt           = ijet->pt();
  //       double bdisc        = ijet->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags");
  //       cout<<"CMSTT subjet pt "<<pt<<" bdisc "<<bdisc<<endl;
  // }


  // for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8MINI->begin(), jetEnd = AK8MINI->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  // {
  //   double pt           = ijet->pt();
  //   if (pt<150) continue;
  //   double mass         = ijet->mass();
  //   double rapidity     = ijet->rapidity();
  //   double prunedMass   = ijet->userFloat("ak8PFJetsCHSPrunedMass");
  //   double trimmedMass  = ijet->userFloat("ak8PFJetsCHSTrimmedMass");
  //   double filteredMass = ijet->userFloat("ak8PFJetsCHSFilteredMass");
  //   double softDropMass = ijet->userFloat("ak8PFJetsCHSSoftDropMass");
  //   double tau1         = ijet->userFloat("NjettinessAK8:tau1");
  //   double tau2         = ijet->userFloat("NjettinessAK8:tau2");
  //   double tau3         = ijet->userFloat("NjettinessAK8:tau3");
  //   double ndau         = ijet->numberOfDaughters();

  //   double tau21 = 99;
  //   double tau32 = 99;
  //   if (tau1!=2) tau21 = tau2/tau1;
  //   if (tau2!=2) tau32 = tau3/tau2;

  //   cout<<"\nJet with pT "<<pt<<" sdMass "<<softDropMass<<endl;


  //   // Soft Drop + Nsubjettiness tagger
  //   bool SoftDropTau32Tagged = false;
  //   if (softDropMass<230 && softDropMass>140 && tau32 <0.65) SoftDropTau32Tagged = true;

  //   //CMS Top Tagger
  //   reco::CATopJetTagInfo const * tagInfo =  dynamic_cast<reco::CATopJetTagInfo const *>( ijet->tagInfo("caTop"));
  //   bool Run1CMStopTagged = false;
  //   int nSubJetsCATop = 0;
  //   if ( tagInfo != 0 ) {
  //     double minMass = tagInfo->properties().minMass;
  //     double topMass = tagInfo->properties().topMass;
  //     nSubJetsCATop = tagInfo->properties().nSubJets;
  //     if ( nSubJetsCATop > 2 && minMass > 50.0 && topMass > 140.0 &&  topMass < 250.0 ) Run1CMStopTagged = true;  
  //   }

  //   // Get Soft drop subjets for subjet b-tagging
  //   auto const & sdSubjets = ijet->subjets("SoftDrop");
  //   cout<<"sdSubjets size "<<sdSubjets.size()<<endl;
  //   for ( auto const & it : sdSubjets ) {
  //     double subjetPt       = it->pt();
  //     double subjetPtUncorr = it->pt();
  //     double subjetEta      = it->eta();
  //     double subjetPhi      = it->phi();
  //     double subjetMass     = it->mass();
  //     double subjetBdisc    = it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
  //     double deltaRsubjetJet = deltaR(ijet->eta(), ijet->phi(), subjetEta, subjetPhi);
  //     cout<<" SD Subjet pt "<<subjetPt<<" uncorr "<<subjetPtUncorr<<" Eta "<<subjetEta<<" deltaRsubjetJet "<<deltaRsubjetJet<<" Mass "<<subjetMass<<" Bdisc "<<subjetBdisc<<endl;
  //   }

  //   // Get top tagged subjets 
  //   auto const & topSubjets = ijet->subjets("CMSTopTag");
  //   cout<<"topSubjets size "<<topSubjets.size()<<endl;
  //   int countTopSubjetLoop = 0;
  //   for ( auto const & it : topSubjets ) {
  //     countTopSubjetLoop++;
  //     double subjetPt       = it->pt();
  //     double subjetPtUncorr = it->pt();
  //     double subjetEta      = it->eta();
  //     double subjetPhi      = it->phi();
  //     double subjetMass     = it->mass();
  //     double subjetBdisc    = it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
  //     double deltaRsubjetJet = deltaR(ijet->eta(), ijet->phi(), subjetEta, subjetPhi);
  //     cout<<" CMSTT Subjet pt "<<subjetPt<<" uncorr "<<subjetPtUncorr<<" Eta "<<subjetEta<<" deltaRsubjetJet "<<deltaRsubjetJet<<" Mass "<<subjetMass<<" Bdisc "<<subjetBdisc<<endl;
  //   }

  //   cout<<"nSubJetsCATop     "<< nSubJetsCATop     <<endl;
  //   cout<<"topSubjets.size() "<< topSubjets.size() <<endl;
  //   cout<<"countSubjetLoop   "<< countTopSubjetLoop<<endl;

  //   //Print some jet info
  //   if (SoftDropTau32Tagged) cout<<"->SoftDropTau32Tagged"<<endl;
  //   if (Run1CMStopTagged)    cout<<"->Run1CMStopTagged"<<endl;

  //   // Fill histograms
  //   h_ak8chs_pt           ->Fill( pt           );
  //   h_ak8chs_mass         ->Fill( mass         );
  //   h_ak8chs_rapidity     ->Fill( rapidity     );
  //   h_ak8chs_prunedMass   ->Fill( prunedMass   );
  //   h_ak8chs_trimmedMass  ->Fill( trimmedMass  );
  //   h_ak8chs_filteredMass ->Fill( filteredMass );
  //   h_ak8chs_softDropMass ->Fill( softDropMass );
  //   h_ak8chs_tau1         ->Fill( tau1         );
  //   h_ak8chs_tau2         ->Fill( tau2         );
  //   h_ak8chs_tau3         ->Fill( tau3         );
  //   h_ak8chs_tau32        ->Fill( tau32        );
  //   h_ak8chs_tau21        ->Fill( tau21        );
  //   h_ak8chs_ndau         ->Fill( ndau         );
  // }
/*
  //--------------------------------------------------------------------------------------------
  // AK R=0.8 PUPPI jets - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8Puppi;
  iEvent.getByLabel( "selectedPatJetsAK8PFPuppi", AK8Puppi );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8Puppi->begin(), jetEnd = AK8Puppi->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak8PFJetsPuppiPrunedMass");
    double trimmedMass  = ijet->userFloat("ak8PFJetsPuppiTrimmedMass");
    double filteredMass = ijet->userFloat("ak8PFJetsPuppiFilteredMass");
    double softDropMass = ijet->userFloat("ak8PFJetsPuppiSoftDropMass");
    double ndau         = ijet->numberOfDaughters();

    h_ak8puppi_pt           ->Fill( pt           );
    h_ak8puppi_mass         ->Fill( mass         );
    h_ak8puppi_rapidity     ->Fill( rapidity     );
    h_ak8puppi_prunedMass   ->Fill( prunedMass   );
    h_ak8puppi_trimmedMass  ->Fill( trimmedMass  );
    h_ak8puppi_filteredMass ->Fill( filteredMass );
    h_ak8puppi_softDropMass ->Fill( softDropMass );
    h_ak8puppi_ndau         ->Fill( ndau         );
  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 PF jets - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8PF;
  iEvent.getByLabel( "selectedPatJetsAK8PF", AK8PF );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8PF->begin(), jetEnd = AK8PF->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak8PFJetsPrunedMass");
    double trimmedMass  = ijet->userFloat("ak8PFJetsTrimmedMass");
    double filteredMass = ijet->userFloat("ak8PFJetsFilteredMass");
    double softDropMass = ijet->userFloat("ak8PFJetsSoftDropMass");
    double ndau         = ijet->numberOfDaughters();

    h_ak8pf_pt           ->Fill( pt           );
    h_ak8pf_mass         ->Fill( mass         );
    h_ak8pf_rapidity     ->Fill( rapidity     );
    h_ak8pf_prunedMass   ->Fill( prunedMass   );
    h_ak8pf_trimmedMass  ->Fill( trimmedMass  );
    h_ak8pf_filteredMass ->Fill( filteredMass );
    h_ak8pf_softDropMass ->Fill( softDropMass );
    h_ak8pf_ndau         ->Fill( ndau         );
  }


  //--------------------------------------------------------------------------------------------
  // AK R=0.8 CHS jets with modified grooming parameters - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8CHS;
  iEvent.getByLabel( "selectedPatJetsAK8PFCHS", AK8CHS );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8CHS->begin(), jetEnd = AK8CHS->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak8CHSJetsCHSPrunedMass");
    double trimmedMass  = ijet->userFloat("ak8CHSJetsCHSTrimmedMass");
    double filteredMass = ijet->userFloat("ak8CHSJetsCHSFilteredMass");
    double softDropMass = ijet->userFloat("ak8CHSJetsCHSSoftDropMass");
    double ndau         = ijet->numberOfDaughters();

    h_ak8chsmod_pt           ->Fill( pt           );
    h_ak8chsmod_mass         ->Fill( mass         );
    h_ak8chsmod_rapidity     ->Fill( rapidity     );
    h_ak8chsmod_prunedMass   ->Fill( prunedMass   );
    h_ak8chsmod_trimmedMass  ->Fill( trimmedMass  );
    h_ak8chsmod_filteredMass ->Fill( filteredMass );
    h_ak8chsmod_softDropMass ->Fill( softDropMass );
    h_ak8chsmod_ndau         ->Fill( ndau         );
  }
*/
//   [jdolen@cmslpc24 python]$ edmdump jettoolbox.root 
// Type                           Module                      Label            Process   
// --------------------------------------------------------------------------------------
// edm::ValueMap<float>           "ak12PFJetsCHSFilteredMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak12PFJetsCHSPrunedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak12PFJetsCHSSoftDropMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak12PFJetsCHSTrimmedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsCHSFilteredMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsCHSSoftDropMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsCHSTrimmedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsFilteredMass"     ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsPuppiFilteredMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsPuppiSoftDropMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsPuppiTrimmedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsSoftDropMass"     ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsTrimmedMass"      ""               "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau1"           "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau2"           "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau3"           "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau4"           "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK12PFCHS"   ""               "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK8PF"      ""               "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK8PFCHS"   ""               "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK8PFPuppi"   ""               "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK12PFCHS"   "genJets"        "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK8PF"      "genJets"        "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK8PFCHS"   "genJets"        "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK8PFPuppi"   "genJets"        "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK12PFCHS"   "pfCandidates"   "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK8PF"      "pfCandidates"   "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK8PFCHS"   "pfCandidates"   "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK8PFPuppi"   "pfCandidates"   "Ana"  
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
