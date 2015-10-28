# 1c_odata_python

[![Join the chat at https://gitter.im/surge-/1c_odata_python](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/surge-/1c_odata_python?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Библиотека работы с odata протоколом 1С.

url = 'http://localhost/odata/standard.odata/'
 
service = odata1c.service(url=url, login='admin', password='')

brands = service.Catalog['Brands']

for i in brands['entry']['content']:
   print i['Description']
