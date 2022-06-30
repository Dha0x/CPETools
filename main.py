from ast import arg
import getopt
import sys

from parso import parse
from fetchData import fetch, params, results
import constants
import argparse


def parseArgs():
    parser = argparse.ArgumentParser(description='Used to parse CPE info')
    parser.add_argument('--production', '-p')
    parser.add_argument('--version', '-v')
    parser.add_argument('--outfile', '-o')
    parser.add_argument('--regexStr', '-e')
    parser.add_argument('--cpe23uri')
    parser.add_argument('--verbose')

    args = vars(parser.parse_args())
    for key, arg in args.items():
        if key == 'production':
            constants.production = arg
        elif key == 'version':
            constants.version = arg
        elif key == 'outfile':
            constants.outfile = arg
        elif key == 'regexStr':
            constants.regexStr = arg
        elif key == 'cpe23uri':
            constants.cpe23uri = arg
        elif key == 'verbose':
            constants.verbose = arg


if __name__ == "__main__":
    parseArgs()

    fetchInfo = fetch.Fetch()
    if constants.cpe23uri != None:
        #constants.totalResults = 10000
        cves = fetchInfo.cves()
        if constants.outfile != None:
            results.saveCveToFile(filename=constants.outfile, cves=cves)
        else:
            for cve in cves:
                print(results.parseCve(cve))
    elif constants.production != None:
        cpes = fetchInfo.productions()
        if constants.outfile != None:
            results.saveCpeToFile(filename=constants.outfile, cpes=cpes)
        else:
            for cpe in cpes:
                print(results.parseCpe(cpe=cpe))
        # i = 0
        # for cpe in cpes:

        #     i += 1
        #     if i > 5:
        #         break
