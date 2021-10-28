import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *
### NanoAOD v5 (for 2016,2017,2018), for different recipe please modify accordingly
from Configuration.Eras.Modifier_run2_nanoAOD_94X2016_cff import run2_nanoAOD_94X2016
from Configuration.Eras.Modifier_run2_nanoAOD_94XMiniAODv2_cff import run2_nanoAOD_94XMiniAODv2
from Configuration.Eras.Modifier_run2_nanoAOD_102Xv1_cff import run2_nanoAOD_102Xv1
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox

# ---------------------------------------------------------
# This is the part the user should modify
def setupCustomizedJetToolbox(process):

    #### AK4 PUPPI jets

    ak4btagdiscriminators = [
            'pfDeepCSVJetTags:probb',
            'pfDeepCSVJetTags:probbb',
            'pfDeepCSVJetTags:probc',
            'pfDeepCSVJetTags:probudsg',
#            'pfDeepFlavourJetTags:probb',
#            'pfDeepFlavourJetTags:probbb',
#            'pfDeepFlavourJetTags:problepb',
#            'pfDeepFlavourJetTags:probc',
#            'pfDeepFlavourJetTags:probuds',
#            'pfDeepFlavourJetTags:probg',
    ]
    ak4btaginfos = [ 'pfDeepCSVTagInfos' ] #'pfDeepFlavourTagInfos'

    jetToolbox(process, 'ak4', 'dummyseq', 'noOutput',
               dataTier='nanoAOD',
               PUMethod='Puppi', JETCorrPayload='AK4PFPuppi',
               #addQGTagger=True,
               runOnMC=True,
               Cut='pt > 15.0 && abs(eta) < 2.4',
               bTagDiscriminators=ak4btagdiscriminators,
               bTagInfos=ak4btaginfos,
               verbosity=4
               )

    #### AK8 PUPPI jets
    ak8btagdiscriminators = [
                        'pfBoostedDoubleSecondaryVertexAK8BJetTags',
#                        'pfMassIndependentDeepDoubleBvLJetTags:probQCD',
#                        'pfMassIndependentDeepDoubleBvLJetTags:probHbb',
#                        'pfMassIndependentDeepDoubleCvLJetTags:probQCD',
#                        'pfMassIndependentDeepDoubleCvLJetTags:probHcc',
#                        'pfMassIndependentDeepDoubleCvBJetTags:probHbb',
#                        'pfMassIndependentDeepDoubleCvBJetTags:probHcc',
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:bbvsLight",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ccvsLight",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHccvsQCD",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:WvsQCD",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHbbvsQCD"
            ]

    jetToolbox(process, 'ak8', 'adummyseq', 'noOutput',
               dataTier='nanoAOD',
               PUMethod='Puppi', JETCorrPayload='AK8PFPuppi',
               runOnMC=True,
               Cut='pt > 170.0 && abs(eta) < 2.4',
               bTagDiscriminators=ak8btagdiscriminators,
               addSoftDrop=True,
               addSoftDropSubjets=True,
               addPruning=True,
               addNsub=True,
               addEnergyCorrFunc=True,
               )
    return process

# ---------------------------------------------------------

def nanoJTB_customizeMC(process):
    run2_nanoAOD_94X2016.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_94XMiniAODv2.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_102Xv1.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_106Xv2.toModify(process, setupCustomizedJetToolbox)
    process.NANOAODSIMoutput.fakeNameForCrab = cms.untracked.bool(True)  # needed for crab publication
    return process
