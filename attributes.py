# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rosbaldeston"
__date__ ="$Mar 20, 2012 11:37:40 AM$"

import powers
import skills

class Attributes:
	def __init__(self, startingClass):
		self.powers = powers.Powers()
		self.skills = skills.Skills()
		self.playerClass = startingClass
		values = self.determineStartingAttribs(startingClass)
		self.vitality = values[0] # HP control
		self.endurance = values[1] # Stamina and equipt burden control
		self.vitavis = values[2] # Vitavis points control
		self.madness = values[3] # Madness points control
		self.intellegnece = values[4] # Base power damage control
		self.dexterity = values[5] # Archery, unarmed, and One-Handed damage control
		self.strength = values[6] # Staff, Two-Handed, and shield damage/defense control
		self.agility = values[7] # Dodge likelihood control
		self.luck = values[8] # Critical hit likelihood control

	def getHP(self):
		return 100 + (self.vitality * 10)

	def getVP(self):
		return 25 + (self.vitavis * 5)

	def getStamina(self):
		return 50 + (self.endurance * 7)

	def getEquiptBurden(self):
		return 30 + (self.endurance * 3)

	def getMP(self):
		return self.madness * 10

	def getBasePowerDamage(self):
		return self.intellegnece

	def getBaseDexSkillDamage(self):
		return self.dexterity

	def getBaseStrSkillDamage(self):
		return self.strength

	def getBaseDefenseVsPhysical(self):
		return int((self.strength + self.dexterity)/2)

	def getBaseDefenseVsMagic(self):
		return int((self.intellegnece + ((self.vitavis + self.madness)/2))/2)

	def getDodgeLikelihood(self):
		return float(self.agility / 500)

	def getCriticalHitChance(self):
		return float(self.luck / 300)

	def createSubPrimes(self, spOne, spTwo):
		if "Blink" in [spOne, spTwo]:
			self.powers.setBlinkPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setBlinkLevelingRateModifier(1.1)
		elif "Fire" in [spOne, spTwo]:
			self.powers.setFirePowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setFireLevelingRateModifier(1.1)
		elif "Hydras" in [spOne, spTwo]:
			self.powers.setHydrasPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setHydrasLevelingRateModifier(1.1)
		elif "Light" in [spOne, spTwo]:
			self.powers.setLightPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setLightLevelingRateModifier(1.1)
		elif "Manipulation" in [spOne, spTwo]:
			self.powers.setManipulationPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setManipulationLevelingRateModifier(1.1)
		elif "Mend" in [spOne, spTwo]:
			self.powers.setMendPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setMendLevelingRateModifier(1.1)
		elif "Sense" in [spOne, spTwo]:
			self.powers.setSensePowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setSenseLevelingRateModifier(1.1)
		elif "Shift" in [spOne, spTwo]:
			self.powers.setShiftPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setShiftLevelingRateModifier(1.1)
		elif "Sight" in [spOne, spTwo]:
			self.powers.setSightPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setSightLevelingRateModifier(1.1)
		elif "Step" in [spOne, spTwo]:
			self.powers.setStepPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setStepLevelingRateModifier(1.1)
		elif "Strength" in [spOne, spTwo]:
			self.powers.setStrengthPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setStrengthLevelingRateModifier(1.1)
		elif "Terra" in [spOne, spTwo]:
			self.powers.setTerraPowerLevel(20)
			if self.PlayerClass != "Wanderer": self.powers.setTerraLevelingRateModifier(1.1)
		elif "Archery" in [spOne, spTwo]:
			self.skills.setArcherySkillLevel(20)
			if self.PlayerClass != "Wanderer": self.skills.setArcheryLevelingRateModifier(1.1)
		elif "One-Handed" in [spOne, spTwo]:
			self.skills.setOneHandedSkillLevel(20)
			if self.PlayerClass != "Wanderer": self.skills.setOneHandedLevelingRateModifier(1.1)
		elif "Shield" in [spOne, spTwo]:
			self.skills.setShieldSkillLevel(20)
			if self.PlayerClass != "Wanderer": self.skills.setShieldLevelingRateModifier(1.1)
		elif "Staff" in [spOne, spTwo]:
			self.skills.setStaffSkillLevel(20)
			if self.PlayerClass != "Wanderer": self.skills.setStaffLevelingRateModifier(1.1)
		elif "Two-Handed" in [spOne, spTwo]:
			self.skills.setTwoHandedSkillLevel(20)
			if self.PlayerClass != "Wanderer": self.skills.setTwoHandedLevelingRateModifier(1.1)
		elif "Unarmed" in [spOne, spTwo]:
			self.skills.setUnarmedSkillLevel(20)
			if self.PlayerClass != "Wanderer": self.skills.setUnarmedLevelingRateModifier(1.1)

	def determineStartingAttribs(self, sClass):
		stats = None
		self.PlayerClass = sClass
		if sClass == "Thief": # Unarmed and step Expert
			self.powers.setStepPowerLevel(25)
			self.skills.setUnarmedSkillLevel(25)
			self.powers.setStepLevelingRateModifier(1.15)
			self.skills.setUnarmedLevelingRateModifier(1.15)
			stats = [8, 10, 9, 0, 9, 14, 7, 12, 11]
		elif sClass == "Warrior": # Two Handed and strength Expert
			self.powers.setStrengthPowerLevel(25)
			self.skills.setTwoHandedSkillLevel(25)
			self.powers.setStrengthLevelingRateModifier(1.15)
			self.skills.setTwoHandedLevelingRateModifier(1.15)
			stats = [13, 14, 5, 0, 7, 8, 15, 8, 10]
		elif sClass == "Mage": # Hydas and terra Expert
			self.powers.setHydrasPowerLevel(25)
			self.powers.setTerraPowerLevel(25)
			self.powers.setHydrasLevelingRateModifier(1.15)
			self.powers.setTerraLevelingRateModifier(1.15)
			stats = [11, 8, 14, 0, 13, 8, 7, 8, 11]
		elif sClass == "Wytch": # Fire and shift Expert
			self.powers.setFirePowerLevel(25)
			self.powers.setShiftPowerLevel(25)
			self.powers.setFireLevelingRateModifier(1.15)
			self.powers.setShiftLevelingRateModifier(1.15)
			stats = [9, 11, 13, 0, 15, 8, 7, 8, 9]
		elif sClass == "Descendant": # Light and shield expert
			self.powers.setLightPowerLevel(25)
			self.skills.setShieldSkillLevel(25)
			self.powers.setLightLevelingRateModifier(1.15)
			self.skills.setShieldLevelingRateModifier(1.15)
			stats = [9, 8, 14, 0, 13, 6, 12, 9, 9]
		elif sClass == "Healer": # Mend and manipulation Expert
			self.powers.setMendPowerLevel(25)
			self.powers.setManipulationPowerLevel(25)
			self.powers.setMendLevelingRateModifier(1.15)
			self.powers.setManipulationLevelingRateModifier(1.15)
			stats = [13, 8, 15, 0, 15, 8, 5, 10, 6]
		elif sClass == "Seer": # Sight and staff Expert
			self.powers.setSightPowerLevel(25)
			self.skills.setStaffSkillLevel(25)
			self.powers.setSightLevelingRateModifier(1.15)
			self.skills.setStaffLevelingRateModifier(1.15)
			stats = [8, 10, 11, 0, 11, 7, 13, 12, 8]
		elif sClass == "Ranger": # Archery and sense Expert
			self.powers.setSensePowerLevel(25)
			self.skills.setArcherySkillLevel(25)
			self.powers.setSenseLevelingRateModifier(1.15)
			self.skills.setArcheryLevelingRateModifier(1.15)
			stats = [10, 13, 9, 0, 9, 13, 8, 10, 8]
		elif sClass == "Assassin": # One-handed and blink Expert
			self.powers.setBlinkPowerLevel(25)
			self.skills.setOneHandedSkillLevel(25)
			self.powers.setBlinkLevelingRateModifier(1.15)
			self.skills.setOneHandedLevelingRateModifier(1.15)
			stats = [7, 12, 9, 0, 10, 12, 7, 12, 11]
		elif sClass == "Wanderer": # Completely balanced
			self.powers.setStepPowerLevel(15)
			self.skills.setUnarmedSkillLevel(15)
			self.powers.setBlinkPowerLevel(15)
			self.skills.setOneHandedSkillLevel(15)
			self.powers.setSensePowerLevel(15)
			self.skills.setArcherySkillLevel(15)
			self.powers.setSightPowerLevel(15)
			self.skills.setStaffSkillLevel(15)
			self.powers.setMendPowerLevel(15)
			self.powers.setManipulationPowerLevel(15)
			self.powers.setLightPowerLevel(15)
			self.skills.setShieldSkillLevel(15)
			self.powers.setFirePowerLevel(15)
			self.powers.setShiftPowerLevel(15)
			self.powers.setHydrasPowerLevel(15)
			self.powers.setTerraPowerLevel(15)
			self.powers.setStrengthPowerLevel(15)
			self.skills.setTwoHandedSkillLevel(15)
			self.powers.setStrengthLevelingRateModifier(1.05)
			self.skills.setTwoHandedLevelingRateModifier(1.05)
			self.powers.setHydrasLevelingRateModifier(1.05)
			self.powers.setTerraLevelingRateModifier(1.05)
			self.powers.setFireLevelingRateModifier(1.05)
			self.powers.setShiftLevelingRateModifier(1.05)
			self.powers.setLightLevelingRateModifier(1.05)
			self.skills.setShieldLevelingRateModifier(1.05)
			self.powers.setMendLevelingRateModifier(1.05)
			self.powers.setManipulationLevelingRateModifier(1.05)
			self.powers.setSightLevelingRateModifier(1.05)
			self.skills.setStaffLevelingRateModifier(1.05)
			self.powers.setSenseLevelingRateModifier(1.05)
			self.skills.setArcheryLevelingRateModifier(1.05)
			self.powers.setBlinkLevelingRateModifier(1.05)
			self.skills.setOneHandedLevelingRateModifier(1.05)
			self.powers.setStepLevelingRateModifier(1.05)
			self.skills.setUnarmedLevelingRateModifier(1.05)
			stats = [10, 10, 10, 0, 10, 10, 10, 10, 10]
		return stats
