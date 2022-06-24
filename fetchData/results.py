def saveCpeToFile(filename, cpes):
    for cpe in cpes:
        pass


def parseCpe(cpe):
    cpeInfo = CpeInfo(cpe)
    print(str(cpeInfo))


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

        print(paramValues)
        paramStr += "\t".join(paramKeys)
        paramStr += '\r\n'+'\t'.join(paramValues)

        return paramStr


class CveInfo:
    cvss = None
    cwe = None
    cve = None
    description = None
