CREATE TABLE email_queue  (
    from_name VARCHAR(255),
    from_email VARCHAR(255) NOT NULL,
    to_name VARCHAR(255),
    to_email VARCHAR(255) NOT NULL,
    subject VARCHAR(255),
    body TEXT,
    date_sent DATE NOT NULL,
    delivery_date DATE NOT NULL,
    confirmation_key CHAR(45) NOT NULL,
    confirmed BOOLEAN,
    PRIMARY KEY (confirmation_key)
);
