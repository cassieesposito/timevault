#!/usr/bin/python
import os
from datetime import datetime
from sqlalchemy import delete
from sendgrid import SendGridAPIClient
import MODELS
import CONST


def main(event, context):
    emails = fetchAndDeleteEmails()
    res = send(emails)
    return


def fetchAndDeleteEmails():
    today = datetime.utcnow().date()
    with MODELS.ENGINE.begin() as conn:
        emails = conn.execute(
            delete(MODELS.TABLE)
            .where(MODELS.TABLE.c.delivery_date <= today)
            .returning(MODELS.TABLE)
        ).all()

    return emails


def send(emails):
    sg = SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    log = {"success": [], "failures": []}
    for email in emails:
        if email[9]:
            failed = 0
            try:
                email = parse(email)
                response = sg.client.mail.send.post(request_body=email)
            except:
                failed = 1

            try:
                failed += 1 if response.status_code // 100 != 2 else 0
            except:
                failed = 1

            if failed:
                log["failures"].append(email)
                continue
            log["success"].append(email)

    return log


def parse(email):
    return {
        "from": {"name": email[0], "email": CONST.SYSTEM_EMAIL},
        "reply_to": {"name": email[0], "email": email[1]},
        "personalizations": [
            {
                "to": [{"name": email[2], "email": email[3]}],
            }
        ],
        "subject": email[4],
        "content": [
            {
                "type": "text/plain",
                "value": f"The following email was sent to you by {email[0]} <{email[1]}> on {email[6]}:\n\n{email[5]}",
            }
        ],
    }
