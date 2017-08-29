#!/usr/bin/env python3

import spekki
import subprocess
import sys
import os
import logging
import re
import argparse
import tempfile
import pkg_resources

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=spekki.__description__)
    parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + spekki.__version__)
    parser.add_argument("fastq", metavar='FASTQ', nargs='*', help='FASTQ sequence file')
    parser.add_argument('--kmer', '-k', type=int, default=25, help='k-mer size') 
    parser.add_argument('--quiet', '-q', action="store_true", help='Only print the errors')
    parser.add_argument('--tmpdir', type=dir, default=tempfile.gettempdir(), help='fast temp folder')
    parser.add_argument('--threads', type=int, default=1, help='Use this many cores')
    parser.add_argument('--citation', action='store_true', help='Show citation information')
    parser.add_argument('--check', action='store_true', help='Ensure dependencies installed')
    args = parser.parse_args()

    #set logging level
    if args.quiet:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.DEBUG)

    #citation
    if args.citation:
        print(spekki.__name__ + ' is not published yet')
        sys.exit(0)

    # use process ID to name temp files
    pid = str(os.getpid())
    logging.info("the pid is: " + pid)

    # talk to the user
    logging.info("You provided this fastq file: {}". format(args.fastq))
    cmd = ['ls', '-l']
#    logging.info("Now running KMC with these commands:")
#    cmd = ["kmc", "-k"+str(args.kmer), "-n"+str(args.nbins), "-ci"+str(args.cutoff), "--threads"+str(args.threads), args.fastq_file, pid, args.tmpdir]
#    logging.debug(cmd)
    # -ci3 option discards kmers with freq <3
    # -n200 sets number of bins to 200 because you can only have 256 files open at once
    # could also change this with ulimit
    #/tmp is the working directory

    # check that kmc ran properly
    try:
        result = subprocess.check_output(cmd) #this makes a bytes thing
        #subprocess.check_output is equivalent to subprocess.run with the default arg check=True
    except:
        logging.exception("error running kmc")
        sys.exit(1)
    
    txt = str(result, 'utf-8')
    print( txt )
    
    #delete unnecessary files
    logging.info("removing unnecessary files")
#    os.remove(pid + ".kmc_pre")
#    os.remove(pid + ".kmc_suf")



if __name__ == '__main__':
    main()
