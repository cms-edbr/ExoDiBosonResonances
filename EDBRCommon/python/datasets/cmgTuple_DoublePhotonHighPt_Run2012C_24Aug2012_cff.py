import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/tomei_edbr_vv_20130313/Run2012/CA8//DoublePhotonHighPt_Run2012C_24Aug2012/cmgTuple_0.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/tomei_edbr_vv_20130313/Run2012/CA8//DoublePhotonHighPt_Run2012C_24Aug2012/cmgTuple_1.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/tomei_edbr_vv_20130313/Run2012/CA8//DoublePhotonHighPt_Run2012C_24Aug2012/cmgTuple_2.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/tomei_edbr_vv_20130313/Run2012/CA8//DoublePhotonHighPt_Run2012C_24Aug2012/cmgTuple_3.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/tomei_edbr_vv_20130313/Run2012/CA8//DoublePhotonHighPt_Run2012C_24Aug2012/cmgTuple_4.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/tomei_edbr_vv_20130313/Run2012/CA8//DoublePhotonHighPt_Run2012C_24Aug2012/cmgTuple_5.root',
]);
