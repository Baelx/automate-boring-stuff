import pprint # importing to help with outputing dictionary later

dragon_loot = [
"gold coin",
"ruby",
"dragon scale",
"dragon scale",
"ruby",
"emerald",
"old newspapers dragon was meaning to read"
] # list of dragon loot dropped when you killed him

player_inventory = {
"rope": 3,
"torch": 5,
"knife": 2,
"rations": 10,
"suicide pill": 1
}

def add_to_inventory(inventory_to_update, added_items): # implemented error handling to accomplish adding the list items to the dict
	for i in added_items:
		try:
			inventory_to_update[i] += 1 # program will try to add 1 to inventory if dict key exists
		except KeyError:
			inventory_to_update[i] = 1 # if dict key doesn't exist, error gets thrown but will add key-value pair of item and 1
	pprint.pprint(inventory_to_update)

add_to_inventory(player_inventory, dragon_loot)
