# Timevault
### Sending e-mails to the future!

This was a pet project of mine inspired by my seventh grade history teacher. He had each of us write ourselves a letter 5 years in the future. I moved to a different school in the 10th grade, but despite that, he had someone track me down and hand deliver that letter. I thought it was a neat idea and set out to write a program to provide this functionality by email in an automated way.

I wrote it, got it working, told a few friends, some of whom used it, and then never did much else with it. After a few years, when the last scheduled email was sent, I shut the service down. Maybe one day I'll reactivate it and try to get the service in front of enough eyes to be an interesting project. Or maybe you want to do it. You're invited to use the portion of the code that I wrote however you want. The only code that isn't mine is calendar.js. You can use that under the terms of the LGPL the author released it under.

In order to make this run, you will need to:

* Create a mySQL database
* Add your credentials to the MySQLdb.connect line at the top of tvlib.py
* Update the webmaster e-mail address in the describeError function of nextSteps.py
* The sendConfirmationEmail function of processVault.py and the sendConfirmationEmail function of nextSteps.py probably need to be modified to work with your server's setup.
* Update the From e-mail address in the sendConfirmationEmail function of nextSteps.py
* Add a single table to your database using the SQL query found in tableCreation.sql
* Schedule processVault.py to run daily. I used cron. You could do it another way.
* Decide whether you want to use index.html or index.py. The only difference is index.py has a note about the time the page was loaded and informs the user the system oprates on UTC.

...

...

...

* Okay, lets be real, do something about my atrocious UI. Not strictly necessary, but I realistically I am just not a designer.


