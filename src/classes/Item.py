import json

class Item():
	def __init__(self, name, description, affect, apply_to, type):
		self._name = name
		self._description = description
		self._affect = affect
		self._apply_to = apply_to
		self._type = type

	def __repr__(self):
		item = {
			"description": self._description, 
			"affect": self._affect, 
			"apply_to": self._apply_to, 
			"type": self._type
		}
		
		return str(item)
		
	@staticmethod
	def create_item(name):
		with open("json/items.json") as file:
			data = json.load(file)
			item_data = data[name]
			description = item_data["description"]
			affect = item_data["affect"]
			apply_to = item_data["apply_to"]
			type = item_data["type"]
			item = Item(name, description, affect, apply_to, type)
			return item
	

	def get_name(self):
		return self._name
		
	def get_description(self):
		return self._description
		
	def get_affect(self):
		return self._affect
		
	def get_apply_to(self):
		return self._apply_to
		
	def get_type(self):
		return self._type


