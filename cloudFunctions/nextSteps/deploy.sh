#!/usr/bin/sh

. $(dirname $(pwd))/common/deployVars.sh
gcloud functions deploy 'TV-nextSteps'\
 --runtime=$RUNTIME\
 --service-account=$SERVICE_ACCOUNT\
 --allow-unauthenticated\
 --trigger-http\
 --entry-point='main'\
 --region=$REGION
