#!/usr/bin/python

'''CLI utility that creates a FITS file from a ASCII table.'''

from optparse import OptionParser

import scipy
import pyfits

def main(args=None):
    '''Entry point for the CLI.'''

    usage = "usage: %prog [options] filename"
    parser = OptionParser(usage=usage, version="%prog 0.1")
    parser.add_option('-o', action="store", dest="output",
                      metavar="FILE", 
                      help="write output to FILE (%default by default)",
                      default="output.fits")
    parser.add_option('-c', '--clobber', action="store_true", dest="clobber",
                      help="overwrites destination file",
                      default=False)
    (options, args) = parser.parse_args(args)

    if len(args) == 0:
        print "ERROR: one argument required"
        parser.print_help()
        return 1

    filename = args[0]

    data = scipy.loadtxt(filename, dtype="float32")
    phdu = pyfits.PrimaryHDU(data)
    hdulist = pyfits.HDUList([phdu])
    try:
        hdulist.writeto(options.output, clobber=options.clobber)
    except IOError, e:
        print "ERROR:", e
        return 1
    return 0

if __name__ == '__main__':
    main()
