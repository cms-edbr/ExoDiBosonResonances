import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_10_1_6OU.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_11_1_nEu.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_12_1_1Ga.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_13_1_Zjw.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_14_1_hmZ.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_15_1_9MN.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_16_1_COc.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_17_1_aIc.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_18_1_ArA.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_19_1_1Hv.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_sDL.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_20_1_YLK.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_21_1_cZx.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_eLj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_6NU.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_sKx.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_zKW.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_me1.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_LNH.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_Mzb.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_s3R.root',
    ])