import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_10_1_Jam.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_11_1_9K1.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_12_1_gaF.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_13_1_ynA.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_14_1_CBA.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_15_1_1au.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_16_1_5mv.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_17_1_D0w.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_18_1_6rP.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_19_1_3YY.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_1_1_ZSZ.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_20_1_UQE.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_21_1_Ktv.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_22_1_s5v.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_23_1_Icb.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_24_1_1rN.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_25_1_Pun.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_26_1_ydN.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_2_1_36D.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_3_1_za9.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_4_1_W8a.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_5_1_wcj.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_6_1_RtY.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_7_1_qTp.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_8_1_6BZ.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_SingleTOP_POWHEG_20130225_233807/santanas/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_9_1_67U.root',
]);
