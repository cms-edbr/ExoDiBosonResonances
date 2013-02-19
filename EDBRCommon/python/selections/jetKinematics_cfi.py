import FWCore.ParameterSet.Config as cms


jetKinematics = cms.PSet(
    pt = cms.string('pt() > 30.0'),
    eta = cms.string('abs(eta()) < 2.4'),
    phi = cms.string('abs(phi()) < 3.2')
    )



zjj = cms.PSet(
    mass = cms.string('mass() >= 60 && mass() < 130'),
)
isSignal = cms.PSet(
    mass = cms.string('mass() >= 75 && mass() < 105'),
)
isSideband = cms.PSet(
    mass = cms.string('(mass() >= 60 && mass() < 75) || ( mass() >= 105 && mass() < 130 )'),
)

### used for merged jet topology
mergedJetKinematics = cms.PSet(
    pt = cms.string('pt() > 50.0'),
    eta = cms.string('abs(eta()) < 2.4'),
    phi = cms.string('abs(phi()) < 3.2'),
    prunedMass = cms.string('prunedMass()>50.0&&prunedMass()<130.0')
    )

mergedJetVTagging = cms.PSet(
    qjet = cms.string('qjet() < 999.0 '),
    nsubjettiness = cms.string('ntau12() < 999.0 '),
    mdrop = cms.string('mdrop()<999.0')
    )

isMergedSignal = cms.PSet(
    prunedMass = cms.string('prunedMass()>75.0 && prunedMass()<105.0')
    )

isMergedSideband = cms.PSet(
    prunedMass = cms.string('prunedMass()<75.0 || prunedMass()>105.0')
    )