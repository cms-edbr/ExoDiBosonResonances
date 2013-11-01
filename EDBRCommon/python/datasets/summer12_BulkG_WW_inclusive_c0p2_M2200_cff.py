import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_10_1_8R0.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_11_1_46x.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_12_1_lHR.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_13_1_iAo.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_14_1_eGO.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_15_1_hYy.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_16_1_fKN.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_17_1_HC8.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_18_1_L12.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_19_1_VEp.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_z9T.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_20_1_RWe.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_21_1_Rd3.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_2Yq.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_IAH.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_7C5.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_rHO.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_ZUu.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_Ycm.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_orL.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M2200-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M2200-JHU__qili-BulkG_WW_jjjj_c0p2_M2200-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_OOB.root',
    ])