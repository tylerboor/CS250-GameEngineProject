# Attack Class
#   Manages the powers and abilities of the player

__author__="rosbaldeston"
__date__ ="$Mar 23, 2012 10:14:59 AM$"

import attributes
import weapons
import spells

class Attack:
	def __init__(self, name, Type, modStat, modVal, auxEffects, cooldown, weight, cost, leveling, status):
		self.name = name # Name of either a weapon or a spell
		self.Type = Type # Signifies whether it is a weapon or a spell
		self.modStat = modStat # Signifies which stat it modifies with
		self.modVal = modVal # Signifies how much additional damage it does
		self.auxEffects = auxEffects # Effects such as burning, freezing, paralyzing, poisoning... recieved in the form of a list of lists
		self.cooldown = cooldown # Amount of time which passes before one can use this attack again
		self.weight = weight # The weight of the weapon (spells are usually 0)
		self.cost = cost # The reduction in Stamina or VP/MP
		self.leveling = leveling # How it levels with skill or power
		self.status = status # Whether the weapon or spell is owned/known