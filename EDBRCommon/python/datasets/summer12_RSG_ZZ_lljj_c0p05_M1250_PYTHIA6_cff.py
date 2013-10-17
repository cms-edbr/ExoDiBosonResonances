import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_10_1_9Jd.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_11_1_nJh.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_1_1_Z1A.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_2_1_wRu.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_3_1_cTr.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_4_1_dbs.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_5_1_vZb.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_6_1_MQd.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_7_1_pK5.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_8_1_ABo.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1250_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_9_1_MXD.root' 
]);
