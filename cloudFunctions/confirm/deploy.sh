#!/usr/bin/sh

. $(dirname $(pwd))/common/deployVars.sh
gcloud functions deploy 'TV-confirm-test'\
 --runtime=$RUNTIME\
 --service-account=$SERVICE_ACCOUNT\
 --trigger-topic='updateBabyNameData'\
 --entry-point='main'\
 --region=$REGION
