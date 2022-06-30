
from openpyxl import Workbook
import xlsxwriter
import constants


def saveCveToFile(filename, cves):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    i = 0
    for cve in cves:

        str = parseCve(cve)

        if i == 0:
            k = 0
            for key in str.split('\r\n')[0].split('\t'):
                worksheet.write(i, k, key)
                k += 1
            i += 1

        values = str.split('\r\n')[-1]
        print(values.split('\t'))
        k = 0
        for value in values.split('\t'):
            worksheet.write(i, k, value)
            k += 1

        i += 1

    workbook.close()


def saveCpeToFile(filename, cpes):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    i = 0
    for cpe in cpes:

        str = parseCpe(cpe)

        if i == 0:
            k = 0
            for key in str.split('\r\n')[0].split('\t'):
                worksheet.write(i, k, key)
                k += 1
            i += 1

        values = str.split('\r\n')[-1]
        print(values.split('\t'))
        k = 0
        for value in values.split('\t'):
            worksheet.write(i, k, value)
            k += 1

        i += 1

    workbook.close()


def parseCpe(cpe):
    return str(CpeInfo(cpe))


def parseCve(cve):
    return str(CveInfo(cve))


class CpeInfo:

    cpe23Uri = None
    lastModifiedDate = None
    deprecatedBy = None
    deprecated = None
    titles = None
    refs = None
    vulnerabilities = None

    def __init__(self, jsonData):
        self.cpe23Uri = jsonData["cpe23Uri"]
        self.lastModifiedDate = jsonData["lastModifiedDate"]
        self.deprecatedBy = jsonData["deprecatedBy"]
        self.deprecated = jsonData["deprecated"]
        self.titles = jsonData["titles"]
        self.refs = jsonData["refs"]
        self.vulnerabilities = jsonData["vulnerabilities"]

    def __str__(self) -> str:

        paramStr = ''

        paramKeys = ["cpe23Uri", "lastModifiedDate",
                     "deprecated", "titles", "refs", "vulnerabilities"]
        paramValues = []

        for param in paramKeys:
            if param == "cpe23Uri":
                paramValues.append(self.cpe23Uri)
            elif param == "lastModifiedDate":
                paramValues.append(self.lastModifiedDate)
            elif param == "deprecated":
                paramValues.append(str(self.deprecated))
            elif param == "titles":
                tmpTitle = ""
                for title in self.titles:
                    if len(tmpTitle) > 0:
                        tmpTitle += ','
                    tmpTitle += title['title']
                paramValues.append(tmpTitle)
            elif param == "refs":
                tmpRef = ""
                for ref in self.refs:
                    if len(tmpRef) > 0:
                        tmpRef += ','
                    tmpRef += ref['type'] + ':' + ref['ref']

                paramValues.append(tmpRef)

            elif param == "vulnerabilities":
                tmpStr = ''
                for cve in self.vulnerabilities:
                    if len(tmpStr) > 0:
                        tmpStr += ','
                    tmpStr += cve

                paramValues.append(tmpStr)

        paramStr += "\t".join(paramKeys).upper()
        paramStr += '\r\n'+'\t'.join(paramValues)

        return paramStr


class CveInfo:
    cve = None
    configurations = None
    impact = None
    publishedDate = None
    lastModifiedDate = None

    def __init__(self, jsonData):
        self.cve = jsonData["cve"]
        self.configurations = jsonData["configurations"]
        self.impact = jsonData["impact"]
        self.publishedDate = jsonData["publishedDate"]
        self.lastModifiedDate = jsonData["lastModifiedDate"]

    def __str__(self):

        paramStr = ''
        paramKeys = ["cveId", "cweId", "description",
                     "cvssV3", "baseScore", "baseSeverity", "exploitabilityScore", "impactScore", "publishedDate", "lastModifiedDate", "version"]
        paramValues = []

        for param in paramKeys:
            if param == 'publishedDate':
                publishedDate = self.publishedDate
                paramValues.append(publishedDate)
            elif param == 'version':
                versions = ''
                for node in self.configurations['nodes']:
                    for cpeMatch in node['cpe_match']:
                        currentUri = cpeMatch['cpe23Uri'].split(':')
                        constUri = constants.cpe23uri.split(":")
                        if ":".join(currentUri[0:5]) == ":".join(constUri[0:5]):
                            if 'versionStartIncluding' in cpeMatch.keys() and 'versionEndIncluding' in cpeMatch.keys():
                                if len(versions) > 0:
                                    versions += ','
                                versions += cpeMatch['versionStartIncluding'] + \
                                    '-'+cpeMatch['versionEndIncluding']
                            elif 'versionStartIncluding' in cpeMatch.keys() and 'versionEndIncluding' not in cpeMatch.keys():
                                if len(versions) > 0:
                                    versions += ','
                                versions += cpeMatch['versionStartIncluding']+'-'+'*'
                            elif 'versionStartIncluding' not in cpeMatch.keys() and 'versionEndIncluding' in cpeMatch.keys():
                                if len(versions) > 0:
                                    versions += ','
                                versions += '*'+'-' + \
                                    cpeMatch['versionEndIncluding']
                            elif 'versionStartIncluding' not in cpeMatch.keys() and 'versionEndIncluding' not in cpeMatch.keys():
                                if len(versions) > 0:
                                    versions += ','
                                versions += currentUri[5]
                paramValues.append(versions)
            elif param == 'lastModifiedDate':
                lastModifiedDate = self.lastModifiedDate
                paramValues.append(lastModifiedDate)
            elif param == "cveId":
                cveId = self.cve["CVE_data_meta"]["ID"]
                paramValues.append(cveId)
            elif param == "cweId":
                cweId = self.cve["problemtype"]['problemtype_data'][0]['description'][0]["value"]
                paramValues.append(cweId)
            elif param == "description":
                description = self.cve["description"]["description_data"][0]["value"]
                paramValues.append(description)
            elif param == "cvssV3":
                cvssV3 = self.impact['baseMetricV2']['cvssV2']['vectorString']
                if 'baseMetricV3' in self.impact.keys():
                    cvssV3 = self.impact['baseMetricV3']['cvssV3']['vectorString']
                paramValues.append(cvssV3)
            elif param == 'baseScore':
                baseScore = str(
                    self.impact['baseMetricV2']['cvssV2']['baseScore'])
                if 'baseMetricV3' in self.impact.keys():
                    baseScore = str(
                        self.impact['baseMetricV3']['cvssV3']['baseScore'])
                paramValues.append(baseScore)
            elif param == "baseSeverity":
                baseSeverity = self.impact['baseMetricV2']['severity']
                if 'baseMetricV3' in self.impact.keys():
                    baseSeverity = self.impact['baseMetricV3']['cvssV3']['baseSeverity']
                paramValues.append(baseSeverity)
            elif param == "exploitabilityScore":
                exploitabilityScore = str(
                    self.impact['baseMetricV2']['exploitabilityScore'])
                if 'baseMetricV3' in self.impact.keys():
                    exploitabilityScore = str(
                        self.impact['baseMetricV3']['exploitabilityScore'])
                paramValues.append(exploitabilityScore)
            elif param == "impactScore":
                impactScore = str(self.impact['baseMetricV2']['impactScore'])
                if 'baseMetricV3' in self.impact.keys():
                    impactScore = str(
                        self.impact['baseMetricV3']['impactScore'])
                paramValues.append(impactScore)

        paramStr += "\t".join(paramKeys).upper()
        paramStr += '\r\n'+'\t'.join(paramValues)

        return paramStr
