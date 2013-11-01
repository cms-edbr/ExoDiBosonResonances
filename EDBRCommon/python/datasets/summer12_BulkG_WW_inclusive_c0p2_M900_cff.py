import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_10_1_9g2.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_11_1_xBS.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_12_1_qwu.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_13_1_lAr.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_14_1_UBy.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_15_1_Yjg.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_16_1_4aV.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_17_1_93Y.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_18_1_Lpl.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_19_1_klX.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_1_1_jQw.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_20_1_DLV.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_21_1_SUT.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_2_1_mKq.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_3_1_NMo.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_4_1_HiE.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_5_1_9JP.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_6_1_m3m.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_7_1_WRk.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_8_1_XpK.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_c0p2_M900_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_c0p2_M900_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M900_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_9_1_TZH.root',
    ])