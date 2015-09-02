from odata1c import odata1c
import xml.etree.ElementTree as etree 
import requests


url = 'http://localhost/odata/standard.odata/'
 
service = odata1c.service(url=url, login='admin', password='')

#print service.workspace['Catalog']

catalogs = service.Catalog

for i in catalogs['SKUGroup']['entry']['content']:
	print i
#print service.Document['Order']






