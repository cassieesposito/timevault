from sqlalchemy import update
import MODELS


def main(req):
    key = req.args.get("key")
    try:
        with MODELS.ENGINE.begin() as conn:
            result = conn.execute(
                update(MODELS.TABLE)
                .where(MODELS.TABLE.c.confirmation_key == key)
                .values(confirmed=True)
                .returning(MODELS.TABLE.c.to_email, MODELS.TABLE.c.delivery_date)
            ).first()
    except:
        print(
            "Error when connecting to database. Please contact "
            "<a href='mailto:sysadmin@timevault.org'>sysadmin@timevault.org</a>"
        )

    if result:
        return (
            f"The time machine is powering up! Your e-mail to {result[0]} is traveling "
            f"forward in time to be delivered on {result[1].strftime('%A, %B %-d, %Y')}."
        )

    return (
        "The key you've submitted is expired or invalid. Please double check the link "
        "you've clicked, and verify the date of delivery has not passed."
    )
