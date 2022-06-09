#!/usr/bin/sh

. ../common/deployVars.sh
gcloud functions deploy 'TV-processVault'\
 --runtime=$RUNTIME\
 --service-account=$SERVICE_ACCOUNT\
 --trigger-topic='TV-processVault'\
 --entry-point='main'\
 --region=$REGION
