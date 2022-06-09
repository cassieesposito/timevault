#!/usr/bin/sh

. ../common/deployVars.sh
gcloud functions deploy 'TV-confirm'\
 --runtime=$RUNTIME\
 --service-account=$SERVICE_ACCOUNT\
 --trigger-topic='updateBabyNameData'\
 --entry-point='main'\
 --region=$REGION
