import schedule
import sys
import time

from mailprinter.core import reader
from mailprinter.core import config
from mailprinter.core import printer

if __name__ == '__main__':
    configuration = config.get_config()
    if not configuration['printer_name']:
        print('Please set up a printer_name from the available names:')
        print(printer.get_printers())
        print('Please set the \'printer_name\' in config.json')
        sys.exit(1)

    schedule.every(int(configuration['send_receive_interval'])) \
        .seconds.do(reader.read_email)

    print('MailPrinter is now running...')

    while True:
        schedule.run_pending()
        time.sleep(1)
