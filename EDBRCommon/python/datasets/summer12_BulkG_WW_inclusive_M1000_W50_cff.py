import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_10_1_pVj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_11_1_crA.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_12_1_CbI.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_13_1_7aE.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_14_1_qPe.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_15_1_l5W.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_16_2_sv4.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_17_1_M4o.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_18_1_ud4.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_19_1_s0I.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_1_1_sk5.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_20_1_R1R.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_21_1_tUD.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_2_1_Xpj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_3_1_ohL.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_4_1_OCQ.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_5_1_jWE.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_6_1_KF8.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_7_1_ead.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_8_1_aDm.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20131015_200317/santanas/BulkG_WW_inclusive_M1000_W50_GENSIM/EDBR_PATtuple_edbr_zz_20130605/9e8031288ea905f4456666a2f5084e75/BulkG_WW_inclusive_M1000_W50_GENSIM__shuai-BulkG_WW_inclusive_M1000_W50_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_9_1_zvv.root',
    ])