from tkinter.messagebox import NO
import constants


class CveParams:
    addOns = None
    apiKey = None
    cpeMatchString = None
    cvssV2Metrics = None
    cvssV2Severity = None
    cvssV3Metrics = None
    cvssV3Severity = None
    cweId = None
    includeMatchStringChange = None
    isExactMatch = None
    keyword = None
    modStartDate = None
    modEndDate = None
    pubStartDate = None
    pubEndDate = None
    resultsPerPage = None
    startIndex = None

    def __init__(self, apikey,
                 addOns=None,
                 cpeMatchString=None,
                 cvssV2Metrics=None,
                 cvssV2Severity=None,
                 cvssV3Metrics=None,
                 cvssV3Severity=None,
                 cweId=None,
                 includeMatchStringChange=None,
                 isExactMatch=None,
                 keyword=None,
                 modStartDate=None,
                 modEndDate=None,
                 pubStartDate=None,
                 pubEndDate=None,
                 resultsPerPage=None,
                 startIndex=0):

        self.apiKey = apikey
        self.addOns = addOns
        self.cpeMatchString = cpeMatchString
        self.cvssV2Metrics = cvssV2Metrics
        self.cvssV2Severity = cvssV2Severity
        self.cvssV3Metrics = cvssV3Metrics
        self.cvssV3Severity = cvssV3Severity
        self.cweId = cweId
        self.includeMatchStringChange = includeMatchStringChange
        self.isExactMatch = isExactMatch
        self.keyword = keyword
        self.modStartDate = modStartDate
        self.modEndDate = modEndDate
        self.pubStartDate = pubStartDate
        self.pubEndDate = pubEndDate
        self.resultsPerPage = resultsPerPage if resultsPerPage != None else constants.resultsPerPage
        self.startIndex = startIndex

    def __str__(self):

        paramStr = ''

        for param in dir(self):
            if not param.startswith('__') and getattr(self, param) != None:
                if len(paramStr) > 0:
                    paramStr += '&'
                paramStr = paramStr+param+'=' + str(getattr(self, param))

        return paramStr


class CpeParams:
    addOns = None
    apiKey = None
    cpeMatchString = None
    includeDeprecated = None
    keyword = None
    modStartDate = None
    modEndDate = None
    resultsPerPage = None
    startIndex = None

    def __init__(self, apikey,
                 addOns=None,
                 cpeMatchString=None,
                 includeDeprecated=None,
                 keyword=None,
                 modStartDate=None,
                 modEndDate=None,
                 resultsPerPage=None,
                 startIndex=0):

        self.addOns = addOns
        self.apiKey = apikey
        self.cpeMatchString = cpeMatchString
        self.includeDeprecated = includeDeprecated
        self.keyword = keyword
        self.modStartDate = modStartDate
        self.modEndDate = modEndDate
        self.resultsPerPage = resultsPerPage if resultsPerPage != None else constants.resultsPerPage
        self.startIndex = startIndex

    def __str__(self):

        paramStr = ''

        for param in dir(self):
            if not param.startswith('__') and getattr(self, param) != None:
                if len(paramStr) > 0:
                    paramStr += '&'
                paramStr = paramStr+param+'=' + str(getattr(self, param))

        return paramStr
