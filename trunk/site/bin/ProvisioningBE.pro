#!/bin/bash
. settings

export PYTHONPATH=$PROVISIONING_DEV_PATH/sources/py/
export PROVISIONING_MODE=PRODUCTION
export PROVISIONING_SIDE=BACKEND

/bin/env python $PROVISIONING_DEV_PATH/sources/py/Provisioning.py