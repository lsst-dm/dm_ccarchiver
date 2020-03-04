#/bin/bash


##
# Python setup
##

#setup ts_idl
export TS_IDL_DIR=/opt/lsst/ts_idl
export PYTHONPATH=${TS_IDL_DIR}/python:${PYTHONPATH}

# setup ts_salobj
export TS_SALOBJ_DIR=/opt/lsst/ts_salobj
export PYTHONPATH=${TS_SALOBJ_DIR}/python:${PYTHONPATH}


# setup CCArchiverCSC and ArchiveController

export DM_CCARCHIVER_DIR=/opt/lsst/dm_CCArchiver
export DM_CSC_BASE_DIR=/opt/lsst/dm_csc_base
export DM_CONFIG_CC_DIR=/opt/lsst/dm_config_cc

export PYTHONPATH=${PYTHONPATH}:${DM_CCARCHIVER_DIR}/python:${DM_CSC_BASE_DIR}/python

# setup path for commands
export PATH=$PATH:${DM_CCARCHIVER_DIR}/bin:${DM_CSC_BASE_DIR}/bin

#setup sal
source /opt/lsst/setup_SAL.env

# LSST DDS DOMAIN for DDS/SAL communications
export LSST_DDS_DOMAIN=lsatmcs
