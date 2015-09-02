from odata1c import odata1c
import xml.etree.ElementTree as etree 
import requests


url = 'http://95.79.53.147:9080/bit_nn123/odata/standard.odata/'
 
service = odata1c.service(url=url, login='admin', password='')

#print service.workspace['Catalog']

catalogs = service.Catalog

for i in catalogs['SKUGroup']['entry']['content']:
	print i
#print service.Document['Order']






