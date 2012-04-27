__author__="rosbaldeston"
__date__ ="$Mar 23, 2012 10:14:59 AM$"

import attack

class Spell:
	def __init__(self):
		self.spells = list()
		self.initBlink()
		self.initFire()
		self.initHydras()
		self.initLight()
		self.initManipulation()
		self.initMend()
		self.initSense()
		self.initShift()
		self.initSight()
		self.initStep()
		self.initStrength()
		self.initTerra()
		self.active = None
	
	def getAll(self):
		return self.spells
	
	def getKnown(self):
		ret = list()
		for spell in self.spells:
			if spell.status:
				ret.append(spell)
		return ret
	
	def getUnknown(self):
		ret = list()
		for spell in self.spells:
			if not spell.status:
				ret.append(spell)
		return ret
	
	def setActive(self, spell):
		self.active = spell
	
	def initBlink(self):
		self.spells.append(attack.Attack("Teleport", "Passive Spell", "int", 0, (("Teleport", 5)), 10, 0, ("VP", 50), ("Use", "Blink"), False))
	
	def initFire(self):
		self.spells.append(attack.Attack("Flames", "Active Spell", "int", 0, (("Range", 3)), 0, 0, ("VP", 5), ("Damage Output", "Fire"), False))
	
	def initHydras(self):
		self.spells.append(attack.Attack("Splash", "Active Spell", "int", -0.5, (("Range", 3), ("Daze", 1)), 1, 0, ("VP", 3), ("Damage Output", "Hydras"), False))
	
	def initLight(self):
		self.spells.append(attack.Attack("Enchanted Light", "Passive Spell", "int", -0.6, (("Augment"), ("Duration", 100)), 10, 0, ("VP", 30), ("Use", "Light"), False))
	
	def initManipulation(self):
		self.spells.append(attack.Attack("Conjure Weapon", "Passive Spell", "int", -0.5, (("Aux Scaling", -0.05), ("Duration", 200)), 30, 0, ("VP", 50), ("Damage Output", "Manipulation"), False))
	
	def initMend(self):
		self.spells.append(attack.Attack("Minor Heal", "Passive Spell", "int", 0, None, 5, 0, ("VP", 10), ("Amount Healed", "Mend"), False))
	
	def initSense(self):
		self.spells.append(attack.Attack("Detect", "Passive Spell", "int", 0, (("Range", 25)), 10, 0, ("VP", 15), ("Use", "Sense"), False))
	
	def initShift(self):
		self.spells.append(attack.Attack("Transform", "Passive Spell", "int", 0, (("Duration", 50)), 100, 0, ("VP", 55), ("Damage Output", "Shift"), False))
	
	def initSight(self):
		self.spells.append(attack.Attack("Two Seconds", "Passive Spell", "int", 0, None, 20, 0, ("VP", 20), ("Use", "Sight"), False))
	
	def initStep(self):
		self.spells.append(attack.Attack("Sprint", "Passive Spell", "int", 0, None, 0, 0, ("VP", 4), ("Use", "Step"), False))
	
	def initStrength(self):
		self.spells.append(attack.Attack("Strong Arm", "Passive Spell", "int", -0.5, (("Augment"), ("Duration", 50)), 100, 0, ("VP", 45), ("Damage Output", "Strength"), False))
	
	def initTerra(self):
		self.spells.append(attack.Attack("Stone", "Active Spell", "int", 0, (("Range", 3)), 0, 0, ("VP", 5), ("Damage Output", "Terra"), False))
	



