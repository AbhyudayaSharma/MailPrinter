import cups
import os


def __print_file(_file, printer, description=""):
    #try:
    conn = cups.Connection()
    conn.printFile(printer, _file, description, {})
    # except Exception as e:
    #     print('Error:', e)


def get_printers():
    printers = []
    for printer in cups.Connection().getPrinters():
        printers.append(printer)
    return printers


def print_pdf(pdf_bytes, printer):
    with open('temp.pdf', 'bw') as f:
        f.write(pdf_bytes)
        __print_file(f.name, printer)
        os.remove(f.name)  # delete file when not needed
