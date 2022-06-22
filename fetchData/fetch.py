import re
from turtle import title
from unittest import result
from fetchData import params
import requests
import json
import constants


class Fetch:

    cveParams = None
    cpeParams = None

    def __init__(self):
        self.cpeParams = params.CpeParams(constants.apiKey)
        self.cveParams = params.CveParams(constants.apiKey)

    def productions(self, keyword):

        self.cpeParams.keyword = keyword

        url = constants.cpeUrls + '?' + str(self.cpeParams)
        results = requests.get(url).json()
        print(results)
        totalResults = results['totalResults']
        print('totalResult:', totalResults)
        for startIndex in range(self.cpeParams.startIndex, totalResults, self.cpeParams.resultsPerPage):

            self.cpeParams.startIndex = startIndex
            url = constants.cpeUrls + '?' + str(self.cpeParams)
            print(url)
            results = requests.get(url).json()

            for cpe in results['result']['cpes']:
                title = cpe['titles'][0]['title']
                cpe23Uri = cpe['cpe23Uri']

                print(title, cpe23Uri)

        self.cpeParams.startIndex = 0
        self.cpeParams.keyword = None

    def cves(self, cpe23Uri):

        self.cveParams.cpeMatchString = cpe23Uri
        url = constants.cpeUrls + '?' + str(self.cveParams)
        results = requests.get(url).json()
        print(results)
        totalResults = results['totalResults']
        print('totalResult:', totalResults)
        for startIndex in range(self.cpeParams.startIndex, totalResults, self.cpeParams.resultsPerPage):

            self.cpeParams.startIndex = startIndex
            url = constants.cpeUrls + '?' + str(self.cpeParams)
            print(url)
            results = requests.get(url).json()

            for cpe in results['result']['cpes']:
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
