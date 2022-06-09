import CONST
from sqlalchemy import (
    engine,
    create_engine,
    Table,
    MetaData,
    Column,
    String,
    Date,
    Boolean,
)

ENGINE = create_engine(engine.URL.create(**CONST.DB_KWARGS))
TABLE = Table(
    CONST.DB_TABLE_NAME,
    MetaData(),
    Column("from_name", String(255)),
    Column("from_email", String(255), nullable=False),
    Column("to_name", String(255)),
    Column("to_email", String(255), nullable=False),
    Column("subject", String(255)),
    Column("body", String()),
    Column("date_sent", Date, nullable=False),
    Column("delivery_date", Date, nullable=False),
    Column("confirmation_key", String(45), primary_key=True),
    Column("confirmed", Boolean),
)
