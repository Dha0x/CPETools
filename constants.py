from audioop import add
from ensurepip import version
from tabnanny import verbose
from tkinter.messagebox import NO


cpeUrls = 'https://services.nvd.nist.gov/rest/json/cpes/1.0'
cveUrls = 'https://services.nvd.nist.gov/rest/json/cves/1.0'


regexStr = None
verbose = None
apiKey = "bb54d80a-6dfc-43a9-8771-aa0b09940240"
production = None
version = None
outfile = None
cpe23uri = None
resultsPerPage = 1000
totalResults = None
