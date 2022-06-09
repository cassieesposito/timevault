# Timevault
### Sending e-mails to the future!

This was a pet project of mine inspired by my seventh grade history teacher. He had each of us write ourselves a letter 5 years in the future. I moved to a different school in the 10th grade, but despite that, he had someone track me down and hand deliver that letter. I thought it was a neat idea and set out to write a program to provide this functionality by email in an automated way.

I wrote it, got it working, told a few friends, some of whom used it, and then never did much else with it. After a few years, when the last scheduled email was sent, I shut the service down. Maybe one day I'll reactivate it and try to get the service in front of enough eyes to be an interesting project. Or maybe you want to do it. You're invited to use the portion of the code that I wrote however you want. The only code that isn't mine is calendar.js. You can use that under the terms of the LGPL the author released it under.

In order to make this run on GCP, you will need to:

* Create a PostgreSQL database on GCP.
* Create a SendGrid account for sending e-mails. You may use another SMTP provider, but you will have to rewrite the functions that send e-mails, as this uses the SendGrid API library.
* Add a single table to your database using the SQL query found in tableCreation.sql
* Update most lines of cloudFunctions/common/models.py to match your deployment
* Create a GCP service account for running the cloud functions
* Create a pub/sub topic called TV-processVault
* Use Cloud Scheduler to publish to TV-processVault daily.
* Deploy Cloud Functions
** From Linux or MacOS you should be able to use deploy.sh scripts found in each folder after updating the service account.
** If you are deploying from a Windows machine you can get all the information necessary to deploy from the GCP web interface from the deploy.sh scripts. Make sure you include cloudFunctions/common/* in each cloud function deployment.
* Add database password and SendGrid API key to GCP Secret Manager
** Import database password to all cloud functions as environment variable: DB_PASSWORD
** Import SendGrid API key to TV-nextSteps and TV-processVault as environment variable: SENDGRID_API_KEY
* Upload the contents of /public to your web server
* Alias /nextSteps and /confirm on your web server to their respective cloud functions.


