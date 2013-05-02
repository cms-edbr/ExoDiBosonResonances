import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_0.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_1.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_10.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_11.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_12.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_13.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_14.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_15.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_16.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_17.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_18.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_19.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_2.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_20.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_21.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_22.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_23.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_24.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_25.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_26.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_27.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_28.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_29.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_3.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_30.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_31.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_32.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_33.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_34.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_35.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_36.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_37.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_38.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_39.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_4.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_40.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_41.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_42.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_43.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_44.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_45.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_46.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_47.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_48.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_49.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_5.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_50.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_6.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_7.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_8.root',
    '/store/user/shuai/ExoDiBosonResonances/CMGtuple/production0428/Summer12/CA8//SingleTopTchannel_xww/cmgTuple_9.root',
    ])
