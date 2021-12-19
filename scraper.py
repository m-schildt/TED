
def scraper(file_names,destination):

    from lxml import etree
    
    for xml in file_names:

        root = etree.parse(xml).getroot()
        NMSP = namespace(root)

        # IF stantment checks if the xml is a Contract award notice | see function doc_typ(Code 7)
        if doc_typ(root,NMSP):

            try:
                form_sec = root.xpath('ted:FORM_SECTION/ted:F03_2014[@CATEGORY = "ORIGINAL"]', namespaces=NMSP)[0]
            except: continue

            body_sec = form_sec.xpath('ted:CONTRACTING_BODY/ted:ADDRESS_CONTRACTING_BODY', namespaces=NMSP)[0]
            contractee = body_sec.findtext('ted:OFFICIALNAME', namespaces=NMSP) # extract contractee
            nuts = body_sec.xpath('n20xx:NUTS/@CODE', namespaces=NMSP)[0] # NUTS
            country = body_sec.xpath('ted:COUNTRY/@VALUE', namespaces=NMSP)[0] # country
            id = root.get('DOC_ID', default=None) 

            cpv = form_sec.xpath('ted:OBJECT_CONTRACT/ted:CPV_MAIN/ted:CPV_CODE/@CODE', namespaces=NMSP)[0] # CPV Code
            type = form_sec.xpath('ted:OBJECT_CONTRACT/ted:TYPE_CONTRACT/@CTYPE', namespaces=NMSP)[0] # extract currency

            for item in form_sec.findall('ted:AWARD_CONTRACT', namespaces=NMSP): # loop over all awardes item / lots in the AWARD_CONTRACT section

                try:
                    value_path = etree.XPath("ted:AWARDED_CONTRACT/ted:VALUES/ted:VAL_TOTAL", namespaces=NMSP)
                    value = value_path(item)[0].text
                    currency = value_path(item)[0].attrib['CURRENCY']
                    contractor = item.findtext('ted:AWARDED_CONTRACT/ted:CONTRACTORS/ted:CONTRACTOR/ted:ADDRESS_CONTRACTOR/ted:OFFICIALNAME', namespaces=NMSP) # extract contractor

                    try:
                        with open(destination, 'a') as file:
                            file.write(f'{id},{contractee.replace(",", "")},{contractor.replace(",", "")},{cpv},{type},{country},{nuts},{float(value)},{currency}\n') # store everything in a CSV File
                    except:
                        pass

                except: continue




def namespace(root):
    none = root.nsmap[None]
    version = list(root.nsmap)[3]
    n20xx = root.nsmap[version]
    return {"ted": none, "n20xx": n20xx}


## doc_typ function scrapes the document type code. Only documents with code 7 ( 7 = Contract award notice) are if interest. function return true if the code is 7
def doc_typ(root,NMSP):
    from lxml import etree
    document_type = etree.XPath('ted:CODED_DATA_SECTION/ted:CODIF_DATA/ted:TD_DOCUMENT_TYPE/@CODE', namespaces=NMSP)
    return document_type(root) == ['7']

#destination = "new_file2.csv"
#scraper(['20211217_245/642507_2021.xml', '20211217_245/642508_2021.xml', '20211217_245/642509_2021.xml', '20211217_245/642510_2021.xml', '20211217_245/642511_2021.xml'],destination)
