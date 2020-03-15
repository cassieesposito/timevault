CREATE TABLE emailQueue  (
    sendTime DATETIME NOT NULL,
    fromName VARCHAR[255],
    fromEmail VARCHAR[255] NOT NULL,
    toName VARCHAR[255],
    toEmail VARCHAR[255] NOT NULL,
    subject VARCHAR[255],
    body VARCHAR[65535],
    confirmationKey CHAR[45] NOT NULL,
    PRIMARY KEY (confirmationKey)
);
