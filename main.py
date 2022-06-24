from ensurepip import version
import constants
from fetchData import fetch, params, results
import sys
import getopt


def parseArgs(argv):

    try:
        opts, args = getopt.getopt(argv, "kpvo", [
                                   "apiKey", "production", "version", "outfile", "cpe23uri", "verbose"])
    except getopt.GetoptError:
        print("main.py Get special produciton's CVE info from NVD. ")
    print(opts, args)
    for opt, arg in zip(opts, args):
        print(opt[0], arg)
        if opt[0] in ('-k', '--apikey'):
            constants.apiKey = arg
        elif opt[0] in ('-p', '--production'):
            constants.production = arg
        elif opt[0] in ('-v', '--version'):
            constants.version = arg
        elif opt[0] in ('-o', '--outfile'):
            constants.outfile = arg
        elif opt[0] == '--cpe23uri':
            constants.cpe23uri = arg
        elif opt[0] == '--verbose':
            constants.verbose = True


if __name__ == "__main__":
    parseArgs(sys.argv[1:])
    if constants.production != None:
        constants.totalResults = 1000
        print('In fetch')
        fetchCpe = fetch.Fetch()
        i = 0
        for cpe in fetchCpe.productions():
            results.parseCpe(cpe)
            i += 1
            if i > 5:
                break
