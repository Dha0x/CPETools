from ast import If
import re
from turtle import title
from fetchData import params
from fetchData import results
import requests
import json
import constants


class Fetch:

    cveParams = None
    cpeParams = None

    def __init__(self):
        self.cpeParams = params.CpeParams(constants.apiKey)
        self.cveParams = params.CveParams(constants.apiKey)

        self.cpeParams.addOns = 'cves'
        self.cveParams.addOns = 'dictionaryCpes'
        print("Fetch Create success", constants.production)

    def productions(self):

        cpeResults = []
        self.cpeParams.keyword = constants.production

        url = constants.cpeUrls + '?' + str(self.cpeParams)
        response = requests.get(url).json()

        totalResults = constants.totalResults if constants.totalResults != None\
            and constants.totalResults < response['totalResults'] else response['totalResults']
        print('totalResult:', totalResults)
        for startIndex in range(self.cpeParams.startIndex, totalResults, self.cpeParams.resultsPerPage):
            self.cpeParams.startIndex = startIndex
            url = constants.cpeUrls + '?' + str(self.cpeParams)
            response = requests.get(url).json()

            for cpe in response['result']['cpes']:
                if constants.regexStr != None and re.search(constants.regexStr, cpe['titles'][0]['title'], re.M | re.I) != None:
                    cpeResults.append(cpe)
                elif constants.regexStr == None:
                    cpeResults.append(cpe)

        self.cpeParams.startIndex = 0
        self.cpeParams.keyword = None

        return cpeResults

    def cves(self, cpe23Uri):

        self.cveParams.cpeMatchString = cpe23Uri
        url = constants.cpeUrls + '?' + str(self.cveParams)
        response = requests.get(url).json()
        totalResults = response['totalResults']

        print('totalResult:', totalResults)
        for startIndex in range(self.cpeParams.startIndex, totalResults, self.cpeParams.resultsPerPage):

            self.cpeParams.startIndex = startIndex
            url = constants.cpeUrls + '?' + str(self.cpeParams)
            print(url)
            response = requests.get(url).json()

            for cpe in response['result']['cpes']:
                title = cpe['titles'][0]['title']
                cpe23Uri = cpe['cpe23Uri']

                print(title, cpe23Uri)

        self.cpeParams.startIndex = 0

        pass

    def cveDetails(self, cve):

        url = constants.cveUrls + "/" + cve+'?'+str(self.cveParams)
        print(url)
        respose = requests.get(url)
        print(respose.text)
