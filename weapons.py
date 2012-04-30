__author__="rosbaldeston"
__date__ ="$Mar 23, 2012 10:14:59 AM$"

import attack

class Weapon:
	# Weapons can be:
	#		Iron: +0 to weight, +0 to mod
	#		Steel: +1 to weight and cost, +0.2 to mod
	#		Dragon Bone: +10 to weight and cost, +1.5 to mod
	#		Diamond: +2 to weight and cost, +0.9 to mod
	#		White Cobalt: -50% to weight and cost, + 1.75 to mod
	def __init__(self):
		self.weapons = list()
		self.initArchery()
		self.initOneHanded()
		self.initShields()
		self.initStaffs()
		self.initTwoHanded()
		self.initUnarmed()
		self.setActive(self.getOwned()[0])
	
	def getAll(self):
		return self.weapons
	
	def getOwned(self):
		ret = list()
		for weapon in self.weapons:
			if weapon.status:
				ret.append(weapon)
		return ret
	
	def getUnowned(self):
		ret = list()
		for weapon in self.weapons:
			if not weapon.status:
				ret.append(weapon)
		return ret
	
	def setActive(self, weapon):
		self.active = weapon
	
	def setOwned(self, weapon):
		for item in self.weapons:
			if weapon.name == item.name:
				if item.status:
					if weapon.Type != item.Type:
						self.weapons.append(weapon)
				else:
					item.status = True
	
	def initArchery(self):
		self.weapons.append(attack.Attack("Short Bow", "Iron", "dex", 0, (("Range", 15)), 1, 3, ("Stamina", 10), ("Damage Output", "Archery"), False))
		self.weapons.append(attack.Attack("Long Bow", "Iron", "dex", 0.2, (("Range", 20)), 1.2, 5, ("Stamina", 15), ("Damage Output", "Archery"), False))
		self.weapons.append(attack.Attack("Composite Bow", "Iron", "dex", 0.6, (("Range", 30)), 1.5, 8, ("Stamina", 20), ("Damage Output", "Archery"), False))
		self.weapons.append(attack.Attack("Compound Bow", "Iron", "dex", 0.7, (("Range", 25)), 0.75, 5, ("Stamina", 12), ("Damage Output", "Archery"), False))
		self.weapons.append(attack.Attack("Crossbow", "Iron", "dex", 0.8, (("Range", 8)), 2, 3, ("Stamina", 5), ("Damage Output", "Archery"), False))
	
	def initOneHanded(self):
		self.weapons.append(attack.Attack("Short Sword", "Iron", "dex", 0, None, 1, 2, ("Stamina", 5), ("Damage Output", "One Handed"), True))
		self.weapons.append(attack.Attack("Long Sword", "Iron", "dex", 0.4, None, 1.3, 4, ("Stamina", 7), ("Damage Output", "One Handed"), False))
		self.weapons.append(attack.Attack("Split-Blade Sword", "Iron", "dex", 0.6, None, 1.2, 3, ("Stamina", 6), ("Damage Output", "One Handed"), False))
		self.weapons.append(attack.Attack("Dagger", "Iron", "dex", -0.2, (("CritBonus", 1.5)), 0.7, 0.5, ("Stamina", 2), ("Damage Output", "One Handed"), False))
		self.weapons.append(attack.Attack("Sai", "Iron", "dex", -0.1, (("CritBonus", 1)), 0.75, 0.75, ("Stamina", 3), ("Damage Output", "One Handed"), False))
		self.weapons.append(attack.Attack("Battle Axe", "Iron", "dex", 0.8, None, 2, 7, ("Stamina", 10), ("Damage Output", "One Handed"), False))
		self.weapons.append(attack.Attack("Mace", "Iron", "dex", 0.7, None, 1.8, 6, ("Stamina", 9), ("Damage Output", "One Handed"), False))
		self.weapons.append(attack.Attack("Falchion", "Iron", "dex", 0.2, (("Bleed", 15)), 1, 2.5, ("Stamina", 5), ("Damage Output", "One Handed"), False))
		self.weapons.append(attack.Attack("Katana", "Iron", "dex", 0.4, (("Bleed", 25)), 0.7, 1.5, ("Stamina", 4), ("Damage Output", "One Handed"), False))
	
	def initShields(self):
		self.weapons.append(attack.Attack("Buckler", "Iron", "str", 1.5, None, 0, 3, ("Stamina", 25), ("Damage Blocked", "Shields"), False))
		self.weapons.append(attack.Attack("Kite", "Iron", "str", 1.75, None, 0, 4, ("Stamina", 21), ("Damage Blocked", "Shields"), False))
		self.weapons.append(attack.Attack("Heater", "Iron", "str", 2, None, 0, 4, ("Stamina", 21), ("Damage Blocked", "Shields"), False))
		self.weapons.append(attack.Attack("Parma", "Iron", "str", 2.5, (("Bash", "str", 0, 0.5)), 0, 5, ("Stamina", 18), ("Damage Blocked", "Shields"), False))
		self.weapons.append(attack.Attack("Scutum", "Iron", "str", 3, (("Bash", "str", 1.5, 3)), 0, 7, ("Stamina", 15), ("Damage Blocked", "Shields"), False))
		self.weapons.append(attack.Attack("Spiked", "Iron", "str", 2, (("Spikes", "str", 1.5)), 0, 6, ("Stamina", 20), ("Damage Blocked", "Shields"), False))
		self.weapons.append(attack.Attack("Wall", "Iron", "str", 2, (("Bash", "str", 5, 5)), 0, 10, ("Stamina", 9), ("Damage Blocked", "Shields"), False))
	
	def initStaffs(self):
		self.weapons.append(attack.Attack("Bo", "Iron", "str", 0.2, (("Reach", 3)), 2, 3, ("Stamina", 15), ("Damage Output", "Staffs"), False))
		self.weapons.append(attack.Attack("Spear", "Iron", "str", 0.4, (("Reach", 3)), 2, 4, ("Stamina", 18), ("Damage Output", "Staffs"), False))
		self.weapons.append(attack.Attack("Halberd", "Iron", "str", 0.7, (("Reach", 4)), 3, 6, ("Stamina", 24), ("Damage Output", "Staffs"), False))
		self.weapons.append(attack.Attack("Glaive", "Iron", "str", 0.6, (("Reach", 2.5), ("Bleed", 5)), 2.5, 5, ("Stamina", 21), ("Damage Output", "Staffs"), False))
		self.weapons.append(attack.Attack("Bardiche", "Iron", "str", 0.9, (("Reach", 2.5), ("Bleed", 8)), 3.5, 7, ("Stamina", 27), ("Damage Output", "Staffs"), False))
		self.weapons.append(attack.Attack("War Scythe", "Iron", "str", 1.1, (("Reach", 3), ("Bleed", 10)), 3, 6, ("Stamina", 24), ("Damage Output", "Staffs"), False))
	
	def initTwoHanded(self):
		self.weapons.append(attack.Attack("Club", "Iron", "str", 0.3, (("Sweep")), 3.5, 8, ("Stamina", 18), ("Damage Output", "Two Handed"), False))
		self.weapons.append(attack.Attack("Greatsword", "Iron", "str", 0.6, (("Sweep")), 3, 9, ("Stamina", 22), ("Damage Output", "Two Handed"), False))
		self.weapons.append(attack.Attack("War Axe", "Iron", "str", 0.8, (("Sweep")), 3.5, 10, ("Stamina", 26), ("Damage Output", "Two Handed"), False))
		self.weapons.append(attack.Attack("War Hammer", "Iron", "str", 0.9, (("Sweep")), 4, 11, ("Stamina", 30), ("Damage Output", "Two Handed"), False))
		self.weapons.append(attack.Attack("Uchigatana", "Iron", "str", 1, (("Sweep"), ("Bleed", 20)), 3, 9, ("Stamina", 22), ("Damage Output", "Two Handed"), False))
		self.weapons.append(attack.Attack("Zweihander", "Iron", "str", 1.4, (("Sweep")), 3, 13, ("Stamina", 38), ("Damage Output", "Two Handed"), False))
		self.weapons.append(attack.Attack("Claymore", "Iron", "str", 1.6, (("Sweep")), 3.5, 12, ("Stamina", 34), ("Damage Output", "Two Handed"), False))
		self.weapons.append(attack.Attack("Dotanuki", "Iron", "str", 1.7, (("Sweep"), ("Bleed", 40)), 3.5, 9, ("Stamina", 22), ("Damage Output", "Two Handed"), False))
	
	def initUnarmed(self):
		self.weapons.append(attack.Attack("Gloves", "Iron", "dex", -0.5, None, 0, 0, ("Stamina", 2), ("Damage Output", "Unarmed"), True))
		self.weapons.append(attack.Attack("Brass Knuckles", "Iron", "dex", -0.3, None, 0, 0.2, ("Stamina", 4), ("Damage Output", "Unarmed"), False))
		self.weapons.append(attack.Attack("Cestus", "Iron", "dex", -0.2, None, 0, 0.2, ("Stamina", 4), ("Damage Output", "Unarmed"), False))
		self.weapons.append(attack.Attack("Gauntlets", "Iron", "dex", -0.1, None, 0, 0.2, ("Stamina", 4), ("Damage Output", "Unarmed"), False))
		self.weapons.append(attack.Attack("Spiked Knuckles", "Iron", "dex", 0, (("Bleed", 5)), 0, 0.3, ("Stamina", 6), ("Damage Output", "Unarmed"), False))
		self.weapons.append(attack.Attack("Push Dagger", "Iron", "dex", 0.2, (("Bleed", 7)), 0, 0.3, ("Stamina", 6), ("Damage Output", "Unarmed"), False))
	