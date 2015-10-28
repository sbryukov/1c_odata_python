# 1c_odata_python

Библиотека работы с odata протоколом 1С.

https://gitter.im/surge-/1c_odata_python

url = 'http://localhost/odata/standard.odata/'
 
service = odata1c.service(url=url, login='admin', password='')

brands = service.Catalog['Brands']

for i in brands['entry']['content']:
   print i['Description']
