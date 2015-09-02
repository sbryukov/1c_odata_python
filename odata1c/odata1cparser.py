# -*- coding: utf-8 -*-




class Obj1C(object):
	
	def __init__(self, service, name):
		self.service = service
		self.name = name
		self.items=dict()
		#self.load()	


	def load(self):
		#http://95.79.53.147:9080/bit_nn123/odata/standard.odata/Document_Order
		if self.name in self.service.workspace.keys():
			print 'Downloading ',self.name, '...'
			#self.items = self.service.get_workspace()[self.name]
			for i in self.items:
				print self.name, i
				root = self.service.read(self.name, i)
				self.parse_xml(root,i)

		return self.items
			

	def parse_xml(self,root,table):
		entrys = root.findall('{http://www.w3.org/2005/Atom}entry')
		if len(entrys) > 0:
			#print len(entrys)

			self.items[table]={'entry' : { 'content' : [] } }
			

			for entry in entrys:

				contents = entry.findall('{http://www.w3.org/2005/Atom}content')
				for content in contents:
					properties = content.findall('{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties')
					prop_dict = dict()
					for prop in properties[0]:
						key = prop.tag.split('}')[-1]
						prop_dict[key]=prop.text
				
			    	self.items[table]['entry']['content'].append(prop_dict)
		


	def append_items(self, items):
		for i in items:
			self.items[i]=dict()

	def __str__(self):
		return str(self.items)

	def __getitem__(self,index):
		
		if index in self.service.workspace[self.name]:
			print self.name+'_'+index
		 	root = self.service.read(self.name, index)
		 	print root.tag
		 	self.parse_xml(root,index)
		 	res = self.items[index]
		else:
			print index,' Not in ', self.name
			res = {}
		# if index in :
		# 	print self.name+'_'+index
		# 	root = self.service.read(self.name, index)
		# 	print root.tag

		return res





class Odata1cObj(Obj1C):
	pass