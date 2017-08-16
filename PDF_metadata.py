import PyPDF2
from PyPDF2 import PdfFileReader
import argparse
import os.path

parser = argparse.ArgumentParser(prog = 'PDF_metadata ver 1.0.0 by Coder.Nobrain', 
                                description = 'Finding & Reading metadata in PDF file', 
                                epilog = 'Ex: PDF_metata.py -f <PDF file>')
parser.add_argument('-f', dest = 'file', default = None, help = 'PDF file needed to get metadata')
options = parser.parse_args()

def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print '[*] Print Metadata for: ' + str(fileName) 
    for meta in docInfo:
        print '[+] ' + meta + ': ' + docInfo[meta]

def main():
    if options.file != None and os.path.isfile(options.file):
            printMeta(options.file)
    else:
        print 'Cannot find the file'
        print parser.usage

if __name__ == '__main__':
    main()
