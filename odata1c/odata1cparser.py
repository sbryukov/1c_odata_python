# -*- coding: utf-8 -*-




class Obj1C(object):
	
	def __init__(self, service, name):
		self.service = service
		self.name = name
		self.items=dict()	


	def load(self):
		#http://95.79.53.147:9080/bit_nn123/odata/standard.odata/Document_Order
		for i in self.items:
			print self.name, i
			root = self.service.read(self.name, i)
			self.parse_xml(root,i)
		return self.items
			

	def parse_xml(self,xml,table):
		entrys = xml.findall('{http://www.w3.org/2005/Atom}entry')
		if len(entrys) > 0:
			#print len(entrys)

			self.items[table]['content']=list()
			

			for entry in entrys:

				contents = entry.findall('{http://www.w3.org/2005/Atom}content')
				for content in contents:
					properties = content.findall('{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties')
					prop_dict = dict()
					for prop in properties[0]:
						key = prop.tag.split('}')[-1]
						prop_dict[key]=prop.text
				
			    	self.items[table]['content'].append(prop_dict)
			    	#print prop_dict

			#print self.items[table]['content']	


	def append_items(self, items):
		for i in items:
			self.items[i]=dict()

	def __str__(self):
		return str(self.items)

	def __getitem__(self,index):
		print index
		pass



class Odata1cObj(Obj1C):
	pass