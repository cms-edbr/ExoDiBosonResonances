import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_Summer12MC_WprimeWZ_PYTHIA_20131013_190656/bonato/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6/EDBR_PATtuple_edbr_zz_20131013_Summer12MC_WprimeWZ_PYTHIA/1b325ddfb984c14533be7920e22baeef/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6__Summer12_DR53X-PU_S10_START53_V19-v1__AODSIM_1_1_f6n.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_Summer12MC_WprimeWZ_PYTHIA_20131013_190656/bonato/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6/EDBR_PATtuple_edbr_zz_20131013_Summer12MC_WprimeWZ_PYTHIA/1b325ddfb984c14533be7920e22baeef/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6__Summer12_DR53X-PU_S10_START53_V19-v1__AODSIM_2_1_VsO.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_Summer12MC_WprimeWZ_PYTHIA_20131013_190656/bonato/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6/EDBR_PATtuple_edbr_zz_20131013_Summer12MC_WprimeWZ_PYTHIA/1b325ddfb984c14533be7920e22baeef/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6__Summer12_DR53X-PU_S10_START53_V19-v1__AODSIM_3_1_WHD.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_Summer12MC_WprimeWZ_PYTHIA_20131013_190656/bonato/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6/EDBR_PATtuple_edbr_zz_20131013_Summer12MC_WprimeWZ_PYTHIA/1b325ddfb984c14533be7920e22baeef/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6__Summer12_DR53X-PU_S10_START53_V19-v1__AODSIM_4_1_Foe.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_Summer12MC_WprimeWZ_PYTHIA_20131013_190656/bonato/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6/EDBR_PATtuple_edbr_zz_20131013_Summer12MC_WprimeWZ_PYTHIA/1b325ddfb984c14533be7920e22baeef/WprimeToWZ_M_2200_TuneZ2star_8TeV_pythia6__Summer12_DR53X-PU_S10_START53_V19-v1__AODSIM_5_1_WhP.root'
]);
