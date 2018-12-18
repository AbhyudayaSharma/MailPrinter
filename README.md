# MailPrinter

A Python 3 app to automatically print email attachments sent to your printer.
Requires a printer configured with CUPS (Common Unix Printing System).
Works on any Unix-like system including macOS and Linux, even the Raspberry Pi.
It is recommended to use an account separate from your own email account.

## Setup

- Configure your printer using your operating system settings.
- Clone the repository and `cd` to the cloned folder.
- Run `[sudo] ./setup.py install`.
- Make the configurations for your email and printer in config.json.
- Set the email and password for the account to be used:

```bash
export MAIL_PRINTER_USERNAME="foo@bar.com"
export MAIL_PRINTER_PASSWORD="password"
```

- Run `python mailprinter` to start printing your email attachments from anywhere in the world.

### Configuration options

All configurations are made in config.json:

```JSON
{
  "IMAP_port": 993,
  "IMAP_server": "imap.gmail.com",
  "SSL_required": true,
  "printer_name": "My_Printer",
  "send_receive_interval": 60
}
```

- `IMAP_port:` The port used for IMAP by your email provider. Generally port `993`. 
- `IMAP_server`: The IP/domain of the IMAP server.
- `SSL_required`: A boolean signifying whether the server requires SSL
- `printer_name`: The name of the printer as used by CUPS. Run the program to see the list
    of all configured printers visible to the program. Copy the name of the printer to use
    and paste it in this field.
- `send_recieve_interval`: The interval after which emails are checked repeatedly.

NOTE: Only PDF attachments are printed right now.
