import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *
### NanoAOD v5 (for 2016,2017,2018), for different recipe please modify accordingly
from Configuration.Eras.Modifier_run2_nanoAOD_94X2016_cff import run2_nanoAOD_94X2016
from Configuration.Eras.Modifier_run2_nanoAOD_94XMiniAODv2_cff import run2_nanoAOD_94XMiniAODv2
from Configuration.Eras.Modifier_run2_nanoAOD_102Xv1_cff import run2_nanoAOD_102Xv1

# ---------------------------------------------------------
# This is the part the user should modify
def setupCustomizedJetToolbox(process):

    # recluster Puppi jets, add N-Subjettiness and ECF
    bTagDiscriminators = [
        #'pfCombinedInclusiveSecondaryVertexV2BJetTags',
        #'pfBoostedDoubleSecondaryVertexAK8BJetTags',
        'pfMassIndependentDeepDoubleBvLJetTags:probQCD',
        'pfMassIndependentDeepDoubleBvLJetTags:probHbb',
        #'pfDeepCSVJetTags:probb',
        #'pfDeepCSVJetTags:probbb',
    ]
    subjetBTagDiscriminators = [
        'pfCombinedInclusiveSecondaryVertexV2BJetTags',
        'pfDeepCSVJetTags:probb',
        'pfDeepCSVJetTags:probbb',
    ]
    JETCorrLevels = ['L2Relative', 'L3Absolute', 'L2L3Residual']

    from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
    jetToolbox(process, 'ak8', 'dummyseq', 'noOutput',
               dataTier='nanoAOD',
               PUMethod='Puppi', JETCorrPayload='AK4PFPuppi', JETCorrLevels=JETCorrLevels,
               #addQGTagger=True,
               Cut='pt > 170.0 && abs(rapidity()) < 2.4',
               runOnMC=True,
               addNsub=True, maxTau=3, addEnergyCorrFunc=True,
               addSoftDrop=True, addSoftDropSubjets=True, subJETCorrPayload='AK4PFPuppi', subJETCorrLevels=JETCorrLevels,
               #bTagDiscriminators=bTagDiscriminators,
               #subjetBTagDiscriminators=subjetBTagDiscriminators
               )

# ---------------------------------------------------------

def nanoJTB_customizeMC(process):
    run2_nanoAOD_94X2016.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_94XMiniAODv2.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_102Xv1.toModify(process, setupCustomizedJetToolbox)
    process.NANOAODSIMoutput.fakeNameForCrab = cms.untracked.bool(True)  # needed for crab publication
    return process
