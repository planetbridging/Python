


import requests
import xml.etree.ElementTree as ET
from prettytable import PrettyTable
    


#url = 'http://declair.in/cpelookup?cpe=cpe:/o:linux:linux_kernel:2.6'
url = 'http://declair.in/cpelookupxml?cpe=cpe:/a:lighttpd:lighttpd:1.4.2'
r = requests.get(url)


# file tree = ET.parse('country_data.xml')


tbl = PrettyTable()
tbl.field_names = ["CVEName", "AttackType", "Score", "AccessVector", "AccessComplexity", "Authentication", "ConfidentialityImpact", "IntegrityImpact", "AvailabilityImpact", "Source"]
tree = ET.fromstring(r.text)

for cve in tree.iter('CVE'):
    cvename = cve.find('CVEName').text
    attacktype = cve.find('AttackType').text
    score = cve.find('Score').text
    accessvector = cve.find('AccessVector').text
    accesscomplexity = cve.find('AccessComplexity').text
    authentication = cve.find('Authentication').text
    confidentialityimpact = cve.find('ConfidentialityImpact').text
    integrityimpact = cve.find('IntegrityImpact').text
    availabilityimpact = cve.find('AvailabilityImpact').text
    source = cve.find('Source').text
    #cpelst = cve.find('CPELST').text.split(',')
    tbl.add_row([cvename, attacktype, score, accessvector , accesscomplexity, authentication , confidentialityimpact , integrityimpact , availabilityimpact , source])

print(tbl)

class ObjCVE():
    def __init__(self, cve,atype,score,accessvector,accesscomplexity,authentication,confidentialityimpact
                 ,integrityimpact,availabilityimpact,source,cpelst):
        self.CVE = cve
        self.AttackType = atype
        self.Score = score
        self.AccessVector = accessvector
        self.AccessComplexity = accesscomplexity
        self.Authentication = authentication
        self.ConfidentialityImpact = confidentialityimpact
        self.IntegrityImpact = integrityimpact
        self.AvailabilityImpact = availabilityimpact
        self.Source = source
        self.CPELST = cpelst
