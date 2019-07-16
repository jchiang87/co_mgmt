export CO_MGMT_DIR=$( cd $(dirname $BASH_SOURCE); pwd -P )
export PATH=${CO_MGMT_DIR}/bin:${PATH}
export PYTHONPATH=${CO_MGMT_DIR}/python:${PYTHONPATH}
