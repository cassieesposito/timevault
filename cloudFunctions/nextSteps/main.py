#!/usr/bin/python

from datetime import datetime
from random import SystemRandom
import string
from sqlalchemy import insert
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

import MODELS
import CONST


def main(req):
    try:
        values = parseForm(req)
        validate(values)
        saveToDatabase(values)
        sendConfirmationEmail(values)
    except Exception as err:
        return buildErrorMessage(err, req)
        # import traceback

        # return buildErrorMessage(f"{err}\n\n\{traceback.format_exc()}\n\n", req)

    return success(values["delivery_date"])


def parseForm(req):
    try:
        values = {
            "from_name": req.form["fromName"],
            "from_email": req.form["fromEmail"],
            "to_name": req.form["toName"],
            "to_email": req.form["toEmail"],
            "subject": req.form["subject"],
            "body": req.form["body"],
            "date_sent": datetime.utcnow().date(),
        }
    except:
        raise Exception(
            "You must include fromName, fromEmail, toName, toEmail, subject, and body in your POST"
        )
    values |= {"delivery_date": getDate(req)}
    try:
        values |= {
            "confirmation_key": "".join(
                SystemRandom().choice(string.ascii_uppercase + string.digits)
                for n in range(45)
            ),
        }
    except:
        Exception(f"Randomizer error. Please contact {CONST.SYSADMIN}.")
    return values


def getDate(req):
    try:
        return datetime.strptime(req.form["date"], "%Y-%m-%d").date()
    except:
        raise Exception("The date you're trying to send an e-mail will not exist.")


def validate(values):
    if not isEmail(values["from_email"]):
        raise Exception("Your e-mail address is invalid. Please try agin.")

    if not isEmail(values["to_email"]):
        raise Exception("Recipient e-mail address is invalid. Please try again.")

    if values["date_sent"] > values["delivery_date"]:
        raise Exception(
            "Sending an e-mail to the past violates the temporal prime directive. The Temporal Integrity Comission has been notified of this incident."
        )

    if values["date_sent"] == values["delivery_date"]:
        raise Exception(
            "If you want to send an e-mail today, you don't need a time machine"
        )


def isEmail(email):
    validity = 1
    if "@" not in email:
        validity = 0

    splitEmail = email.split("@")
    if "." not in splitEmail[len(splitEmail) - 1]:
        validity = 0

    # Allow email address username to start with @ while rejecting no username
    if splitEmail[0] == "" and len(splitEmail) < 3:
        validity = 0

    return validity


def saveToDatabase(values):
    try:
        with MODELS.ENGINE.begin() as conn:
            conn.execute(insert(MODELS.TABLE).values(values))

    except:
        raise Exception(
            "Did you forget to include your e-mail address, the recipient's e-mail address, or the date?"
        )


def sendConfirmationEmail(values):
    try:
        sg = SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
        fromEmail = Email(CONST.SYSTEM_EMAIL, "The Time Vault")
        toEmail = To(values["from_email"], values["from_name"])
        subject = f"Please confirm email to the future: {values['subject']}"
        content = Content(
            "text/plain",
            "You're one step away from sending your e-mail in to the future. "
            "All you need to do is click on the link below:\n\n"
            f"http://timevault.org/confirm?key={values['confirmation_key']}",
        )

        mail = Mail(fromEmail, toEmail, subject, content)
        response = sg.client.mail.send.post(request_body=mail.get())

    except:
        raise Exception("E-mail failed to send.")

    if response.status_code // 100 != 2:
        raise Exception("E-mail failed to send.")


def success(deliveryDate):
    message = (
        "We've sent you an e-mail with a link in it. Click the link in order to power "
        f"the time machine that will send your e-mail to {deliveryDate.strftime('%A, %B %-d, %Y')}."
    )
    return message


def buildErrorMessage(err, req):
    return (
        f"Oops, there was an error!<br><br>{err}<br><br>"
        f"Please try again. If the problem persists, please contact {CONST.SYSADMIN}.<br><br>"
        f'From: {req.form["fromName"]} &lt;{req.form["fromEmail"]}&gt;<br>'
        f'To: {req.form["toName"]} &lt;{req.form["toEmail"]}&gt;<br>'
        f'Subject: {req.form["subject"]}<br>'
        f'Body: {req.form["body"]}<br>'
    ), 400
