
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join



class ObjBusiness():
    def __init__(self, ett,a,nii,inn,ba):
        self.EntityTypeText = ett
        self.Abn = a
        self.NonIndividualNameText = nii
        self.IndividualName = inn
        self.BusinessAddress = ba

#abnxml = "D:\\abnbulk\\20190918_Public01.xml"
#mypath = "D:\\abnbulk\\"
abnxml = "./abnxml/20200826_Public01.xml"
mypath = "./abnxml/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

ObjBusinessLst = []

def appendabn(ob):
    f = open("abnappend.csv","a+")
    output = ob.Abn.replace(",","") + "," + ob.NonIndividualNameText.replace(",","") + "," + ob.EntityTypeText.replace(",","")
    f.write(output + "\n")
    f.close()


def readxml(abnfiles):

    tree = ET.parse(abnfiles)
    root = tree.getroot()

    for t in root:
        attributes = t.attrib
        attributes.get("recordLastUpdatedDate")
        abn = ""
        EntityTypeText = ""
        NonIndividualNameText = ""
        IndividualName = []
        BusinessAddress = []
        for i in t:

            if i.tag == "EntityType":
                for et in i:
                    if et.tag == "EntityTypeText":
                        EntityTypeText = et.text

            if i.tag == "ABN":
                abn = i.text

            if i.tag == "OtherEntity":
                for oe in i:
                    if oe.tag == "NonIndividualName":
                        for nin in oe:
                            if nin.tag == "NonIndividualNameText":
                                NonIndividualNameText = nin.text

            if i.tag == "LegalEntity":
                for le in i:
                    if le.tag == "IndividualName":
                        IndividualName.append(le)
                    if le.tag == "BusinessAddress":
                        BusinessAddress.append(le)
        obusiness = ObjBusiness(EntityTypeText,abn,NonIndividualNameText,IndividualName,BusinessAddress)
        #print(EntityTypeText + " " + abn + " " + NonIndividualNameText)
        #ObjBusinessLst.append(obusiness)
        appendabn(obusiness)

#for f in onlyfiles:
#print(f)
#readxml(mypath + f)
print(abnxml)

print('done')
