import imaplib
import email
import os
import sys

from mailprinter.core import printer
from mailprinter.core import config


def read_email():
    configuration = config.get_config()
    print('Checking for emails')

    if configuration['SSL_required']:
        m = imaplib.IMAP4_SSL(configuration['IMAP_server'], configuration['IMAP_port'])
    else:
        m = imaplib.IMAP4(configuration['IMAP_server'], configuration['IMAP_port'])

    try:
        username = os.environ['MAIL_PRINTER_USERNAME']
        password = os.environ['MAIL_PRINTER_PASSWORD']
    except KeyError:
        print('Please set the username and password as environment variables. '
              'See README.md for more details.', file=sys.stderr)
        sys.exit(-1)

    m.login(username, password)
    m.select('Inbox')

    # only check unseen emails
    typ, data = m.search(None, '(UNSEEN)')
    for num in data[0].split():
        typ, data = m.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])

        for part in msg.walk():
            if part.get_content_type() == 'application/pdf':
                printer.print_pdf(part.get_payload(decode=True),
                                  configuration['printer_name'])
