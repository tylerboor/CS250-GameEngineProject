__author__="rosbaldeston"
__date__ ="$Jan 9, 2012 11:07:23 AM$"

class Powers:
	# Power Format: [String name, int[] powerLevelNeeded, int currentLevel, int maxLevel, String description]
	def __init__(self):
		self.initializeBlink(10, None)
		self.initializeFire(10, None)
		self.initializeHydras(10, None)
		self.initializeLight(10, None)
		self.initializeManipulation(10, None)
		self.initializeMend(10, None)
		self.initializeSense(10, None)
		self.initializeShift(10, None)
		self.initializeSight(10, None)
		self.initializeStep(10, None)
		self.initializeStrength(10, None)
		self.initializeTerra(10, None)

	def activated(self):
		active = list()
		active.append(self.getBlinkActivated())
		active.append(self.getFireActivated())
		active.append(self.getHydrasActivated())
		active.append(self.getLightActivated())
		active.append(self.getManipulationActivated())
		active.append(self.getMendActivated())
		active.append(self.getSenseActivated())
		active.append(self.getShiftActivated())
		active.append(self.getSightActivated())
		active.append(self.getStepActivated())
		active.append(self.getStrengthActivated())
		active.append(self.getTerraActivated())
		return active

	# Start Blink Block
	def initializeBlink(self, withLevel, withPowers):
		self.blinkLV = withLevel
		self.blinkMod = 1
		self.blinkPowers = list()
		self.blinkPowers.append(["Improved Teleportation", [10, 25, 50, 75, 100], 0, 5, "Increases maximum distance by 5 meters each level."])
		self.blinkPowers.append(["Traveler", [20], 0, 1, "Allow for fast travel to key locations (Followers cannot join and must walk and can only be used once per day.)"])
		self.blinkPowers.append(["Rapid Blinking", [20, 40, 60], 0, 3, "Cooldown time reduced by 2 seconds each level."])
		self.blinkPowers.append(["Temporal Rip", [30], 0, 1, "Creates a portal which anyone can pass through, 1 charge."])
		self.blinkPowers.append(["Conservation", [40, 50, 60, 80, 100], 0, 5, "Reduces blink cost by 10% each level."])
		self.blinkPowers.append(["Improved Rip", [50, 70, 90], 0, 1, "Charges increase to 3, 5 and infinite."])
		self.blinkPowers.append(["Energy Burst", [60, 80], 0, 2, "Blinking restores 10% of max stamina each level."])
		self.blinkPowers.append(["Intangability", [90], 0, 1, "For 2 seconds after blinking you cannot be harmed."])
		self.blinkPowers.append(["Explosive Entrence", [100], 0, 1, "Blinking causes an explosion doing a great amount of damage."])

	def getBlinkPowerLevel(self):
		return self.blinkLV

	def getBlinkActivated(self):
		active = list()
		for item in self.blinkPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getBlinkAvailable(self):
		avail = list()
		for item in self.blinkPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.blinkLV:
					avail.append(item)
		return avail

	def getBlinkUnavailable(self):
		unavail = list()
		for item in self.blinkPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.blinkLV:
					unavail.append(item)
		return unavail

	def activateBlinkPower(self, power):
		if power in self.getBlinkAvailable():
			for item in self.blinkPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setBlinkPowerLevel(self, lv):
		self.blinkLV = lv
	
	def setBlinkLevelingRateModifier(self, mod):
		self.blinkMod = mod
	# End Blink Block

	# Start Fire Block
	def initializeFire(self, withLevel, withPowers):
		self.fireLV = withLevel
		self.fireMod = 1
		self.firePowers = list()
		self.firePowers.append(["Kindle", [10, 25, 50, 75, 100], 0, 5, "Increases damage output with flames by 20% each level."])
		self.firePowers.append(["Burning", [15], 0, 1, "Fire attacks have a chance to set target on fire."])
		self.firePowers.append(["Rapid Fire", [20, 60], 0, 2, "Doubles speed of fire casting."])
		self.firePowers.append(["Weapon of Fire", [30, 60, 90], 0, 3, "Choose a weapon to conjure in flames, scales with that skill stat."])
		self.firePowers.append(["Flame Sprite", [40], 0, 1, "Summon a ball of fire which will follow the player and rush to nearby enemies before exploding."])
		self.firePowers.append(["Forest Fire", [40, 80], 0, 2, "Enemies on fire catch nearby enimies on fire (lv 1). Fire spreads on grass, burning everything in a 5 meter radius (lv 2)."])
		self.firePowers.append(["Shock", [50], 0, 1, "Unlocks shock variations of abilities which can parylize rather than burn (Note: forest fire spreads through water rather than grass)."])
		self.firePowers.append(["Improved Flame Sprite", [60], 0, 1, "Increases the size of the explosion."])
		self.firePowers.append(["Multi-Sprite", [70], 0, 1, "Can have three active sprites at once."])
		self.firePowers.append(["Magma", [80], 0, 1, "Burning the ground will melt the sand and create a pit of lava."])
		self.firePowers.append(["Lightning", [80], 0, 1, "Summon a bolt of lightning to strike the target and cause them to explode."])
		self.firePowers.append(["Burning Soul", [100], 0, 1, "All attacks have a 25% chance to burn and a 25% chance to parylize the target."])

	def getFirePowerLevel(self):
		return self.fireLV

	def getFireActivated(self):
		active = list()
		for item in self.firePowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getFireAvailable(self):
		avail = list()
		for item in self.firePowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.fireLV:
					avail.append(item)
		return avail

	def getFireUnavailable(self):
		unavail = list()
		for item in self.firePowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.fireLV:
					unavail.append(item)
		return unavail

	def activateFirePower(self, power):
		if power in self.getFireAvailable():
			for item in self.firePowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setFirePowerLevel(self, lv):
		self.fireLV = lv
	
	def setFireLevelingRateModifier(self, mod):
		self.fireMod = mod
	# End Fire Block

	# Start Hydras Block
	def initializeHydras(self, withLevel, withPowers):
		self.hydrasLV = withLevel
		self.hydrasMod = 1
		self.hydrasPowers = list()
		self.hydrasPowers.append(["Flow", [10, 25, 50, 75, 100], 0, 5, "Increases damage output with water based attacks by 20% each level."])
		self.hydrasPowers.append(["Control", [20, 40, 60], 0, 3, "Turns target to fight for you."])
		self.hydrasPowers.append(["Fog", [20, 40, 60], 0, 3, "Summon fog making you 10% harder to detect with each level."])
		self.hydrasPowers.append(["Ice", [30], 0, 1, "Freezes water attack into ice with a chance to slow the target by 50%."])
		self.hydrasPowers.append(["Rain", [40], 0, 1, "Causes it to rain and increases vitavis regeneration in rain."])
		self.hydrasPowers.append(["Ice Weapon", [40, 60, 80], 0, 3, "Choose a weapon to conjure in ice, scales with that skill stat."])
		self.hydrasPowers.append(["Shards", [60, 80], 0, 2, "Increase number of ice shards thrown at a time by 2 each level"])
		self.hydrasPowers.append(["Hurricane", [75], 0, 1, "Summons a hurricane which has a chance to throw eminies off ballance and to strike them with lightning."])
		self.hydrasPowers.append(["Frozen Blood", [100], 0, 1, "Instantly freezes target, 50% chance target will shatter if attacked."])

	def getHydrasPowerLevel(self):
		return self.hydrasLV

	def getHydrasActivated(self):
		active = list()
		for item in self.hydrasPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getHydrasAvailable(self):
		avail = list()
		for item in self.hydrasPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.hydrasLV:
					avail.append(item)
		return avail

	def getHydrasUnavailable(self):
		unavail = list()
		for item in self.hydrasPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.hydrasLV:
					unavail.append(item)
		return unavail

	def activateHydrasPower(self, power):
		if power in self.getHydrasAvailable():
			for item in self.hydrasPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setHydrasPowerLevel(self, lv):
		self.hydrasLV = lv
	
	def setHydrasLevelingRateModifier(self, mod):
		self.hydrasMod = mod
	# End Hydras Block

	# Start Light Block
	def initializeLight(self, withLevel, withPowers):
		self.lightLV = withLevel
		self.lightMod = 1
		self.lightPowers = list()
		self.lightPowers.append(["Light Enchant", [10, 25, 50, 75, 100], 0, 5, "Increases damage output with light based enchantments on weapons by 20% each level."])
		self.lightPowers.append(["Flash", [20], 0, 1, "Causes a bright flash which temporarily blinds all targets in the area. Targets go into a Blind Frenzy."])
		self.lightPowers.append(["Light Skin", [30, 40, 50], 0, 3, "Skin gives off a glow, illuminating a one meter greater radius each level."])
		self.lightPowers.append(["Improved Flash", [40, 70], 0, 2, "Enemies are blinded 50% longer from 50% farther away each level."])
		self.lightPowers.append(["Light Ray", [50, 75, 100], 0, 3, "Shoots a bolt of light (up to three) which damages target. Extra damage if cursed or suffering madness."])
		self.lightPowers.append(["Orb of Light", [60], 0, 1, "Creates a ball of light which explodes when an enemy comes in contact with it."])
		self.lightPowers.append(["Moth to the Flame", [70], 0, 1, "Orb of Light attracts enemies to it."])
		self.lightPowers.append(["Immunity", [80, 100], 0, 2, "LV 1: Immune to curses, poisoning, and disease. LV 2: Immune to Madness."])
		self.lightPowers.append(["Smart Orb", [90], 0, 1, "An Orb of Light which follows behind the caster and darts toward approaching enemies before exploding."])
		self.lightPowers.append(["Blind and Binde", [100], 0, 1, "Flash does not cause Blind Frenzy and enemies fall to the ground for durration of blindness."])

	def getLightPowerLevel(self):
		return self.lightLV

	def getLightActivated(self):
		active = list()
		for item in self.lightPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getLightAvailable(self):
		avail = list()
		for item in self.lightPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.lightLV:
					avail.append(item)
		return avail

	def getLightUnavailable(self):
		unavail = list()
		for item in self.lightPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.lightLV:
					unavail.append(item)
		return unavail

	def activateLightPower(self, power):
		if power in self.getLightAvailable():
			for item in self.lightPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setLightPowerLevel(self, lv):
		self.lightLV = lv
	
	def setLightLevelingRateModifier(self, mod):
		self.lightMod = mod
	# End Light Block

	# Start Manipulation Block
	def initializeManipulation(self, withLevel, withPowers):
		self.manipulationLV = withLevel
		self.manipulationMod = 1
		self.manipulationPowers = list()
		self.manipulationPowers.append(["", [10, 25, 50, 75, 100], 0, 5, ""])

	def getManipulationPowerLevel(self):
		return self.manipulationLV

	def getManipulationActivated(self):
		active = list()
		for item in self.manipulationPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getManipulationAvailable(self):
		avail = list()
		for item in self.manipulationPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.manipulationLV:
					avail.append(item)
		return avail

	def getManipulationUnavailable(self):
		unavail = list()
		for item in self.manipulationPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.manipulationLV:
					unavail.append(item)
		return unavail

	def activateManipulationPower(self, power):
		if power in self.getManipulationAvailable():
			for item in self.manipulationPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setManipulationPowerLevel(self, lv):
		self.manipulationLV = lv
	
	def setManipulationLevelingRateModifier(self, mod):
		self.manipulationMod = mod
	# End Manipulation Block

	# Start Mend Block
	def initializeMend(self, withLevel, withPowers):
		self.mendLV = withLevel
		self.mendMod = 1
		self.mendPowers = list()
		self.mendPowers.append(["Healer", [10, 25, 50, 75, 100], 0, 5, "Increases healing by 20% each level."])
		self.mendPowers.append(["Carrier", [10, 25, 50, 75, 100], 0, 5, "Increases poisoning by 20% each level."])
		self.mendPowers.append(["Raise Dead", [25, 50, 75], 0, 3, "Brings a fallen enemy back to life to fight on your side. Each level increases the number of enemies that may be risen."])
		self.mendPowers.append(["Cure", [30], 0, 1, "Removes status abnormalities."])
		self.mendPowers.append(["Healer's Blood", [50, 70, 90], 0, 3, "Health regeneration increases by 20% each level."])
		self.mendPowers.append(["Zombification", [75], 0, 1, "Risen dead are 50% more powerful and carry the plague."])
		self.mendPowers.append(["Transendence", [100], 0, 1, "Become completely immune to any type of damage for 10 seconds."])
		self.mendPowers.append(["Soul Sucker", [100], 0, 1, "You and your zombies absorb 20% of base health from fallen enemies."])

	def getMendPowerLevel(self):
		return self.mendLV

	def getMendActivated(self):
		active = list()
		for item in self.mendPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getMendAvailable(self):
		avail = list()
		for item in self.mendPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.mendLV:
					avail.append(item)
		return avail

	def getMendUnavailable(self):
		unavail = list()
		for item in self.mendPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.mendLV:
					unavail.append(item)
		return unavail

	def activateMendPower(self, power):
		if power in self.getMendAvailable():
			for item in self.mendPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setMendPowerLevel(self, lv):
		self.mendLV = lv
	
	def setMendLevelingRateModifier(self, mod):
		self.mendMod = mod
	# End Mend Block

	# Start Sense Block
	def initializeSense(self, withLevel, withPowers):
		self.senseLV = withLevel
		self.senseMod = 1

	def getSensePowerLevel(self):
		return self.senseLV

	def getSenseActivated(self):
		active = list()
		for item in self.sensePowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getSenseAvailable(self):
		avail = list()
		for item in self.sensePowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.senseLV:
					avail.append(item)
		return avail

	def getSenseUnavailable(self):
		unavail = list()
		for item in self.sensePowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.senseLV:
					unavail.append(item)
		return unavail

	def activateSensePower(self, power):
		if power in self.getSenseAvailable():
			for item in self.sensePowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setSensePowerLevel(self, lv):
		self.senseLV = lv
	
	def setSenseLevelingRateModifier(self, mod):
		self.senseMod = mod
	# End Sense Block

	# Start Shift Block
	def initializeShift(self, withLevel, withPowers):
		self.shiftLV = withLevel
		self.shiftMod = 1

	def getShiftPowerLevel(self):
		return self.shiftLV

	def getShiftActivated(self):
		active = list()
		for item in self.shiftPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getShiftAvailable(self):
		avail = list()
		for item in self.shiftPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.shiftLV:
					avail.append(item)
		return avail

	def getShiftUnavailable(self):
		unavail = list()
		for item in self.shiftPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.shiftLV:
					unavail.append(item)
		return unavail

	def activateShiftPower(self, power):
		if power in self.getShiftAvailable():
			for item in self.shiftPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setShiftPowerLevel(self, lv):
		self.shiftLV = lv
	
	def setShiftLevelingRateModifier(self, mod):
		self.shiftMod = mod
	# End Shift Block

	# Start Sight Block
	def initializeSight(self, withLevel, withPowers):
		self.sightLV = withLevel
		self.sightMod = 1
		self.sightPowers = list()
		self.sightPowers.append(["Eagle Eye", [10, 25, 50, 75, 100], 0, 5, "Can see enemies 20% farther away with Sight ability each level."])
		self.sightPowers.append(["Remote Viewing", [20], 0, 1, "Can see what enemies see."])
		self.sightPowers.append(["Zoom", [25, 50, 75, 100], 0, 4, "2x, 3x, 5x, and 10x optical zoom with ranged attacks."])
		self.sightPowers.append(["Future Sight", [40, 60, 80], 0, 3, "Next attack (up to three) is forseen, you automatically dodge it."])
		self.sightPowers.append(["Night Vision", [50, 70, 90], 0, 3, "Can see 25% better in the dark with each level."])
		self.sightPowers.append(["Blind", [60, 80, 100], 0, 3, "Decreases target's ability to see by 30% each level"])
		self.sightPowers.append(["Forseen Death", [100], 0, 1, "Next time player would die, they are healed instead (once per day)."])

	def getSightPowerLevel(self):
		return self.sightLV

	def getSightActivated(self):
		active = list()
		for item in self.sightPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getSightAvailable(self):
		avail = list()
		for item in self.sightPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.sightLV:
					avail.append(item)
		return avail

	def getSightUnavailable(self):
		unavail = list()
		for item in self.sightPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.sightLV:
					unavail.append(item)
		return unavail

	def activateSightPower(self, power):
		if power in self.getSightAvailable():
			for item in self.sightPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setSightPowerLevel(self, lv):
		self.sightLV = lv
	
	def setSightLevelingRateModifier(self, mod):
		self.sightMod = mod
	# End Sight Block

	# Start Step Block
	def initializeStep(self, withLevel, withPowers):
		self.stepLV = withLevel
		self.stepMod = 1
		self.stepPowers = list()
		self.stepPowers.append(["Sprinter", [10, 25, 50, 75, 100], 0, 5, "Increases base running speed by 20% each level."])
		self.stepPowers.append(["Hyper Dash", [20], 0, 1, "Dash forward, knocking enemies over."])
		self.stepPowers.append(["Speedster", [25, 50, 75], 0, 3, "Increases speed increase of step ability by 30% each level."])
		self.stepPowers.append(["Jumper", [30, 60, 90], 0, 3, "Doubles jump height with each level."])
		self.stepPowers.append(["Unhindered", [40], 0, 1, "Armor does not effect run speed."])
		self.stepPowers.append(["Swiftness", [50, 70, 90], 0, 3, "10%, 20%, and 30% chance to dodge melee."])
		self.stepPowers.append(["Reflex", [70, 100], 0, 2, "50%, 100% chance to dodge ranged."])
		self.stepPowers.append(["Counter", [90], 0, 1, "Every successful dodge results in a counter attack."])
		self.stepPowers.append(["Rush", [100], 0, 1, "In the heat of battle enemies appear 30% slower and doubles likelihood of dodging melee."])

	def getStepPowerLevel(self):
		return self.stepLV

	def getStepActivated(self):
		active = list()
		for item in self.stepPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getStepAvailable(self):
		avail = list()
		for item in self.stepPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.stepLV:
					avail.append(item)
		return avail

	def getStepUnavailable(self):
		unavail = list()
		for item in self.stepPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.stepLV:
					unavail.append(item)
		return unavail

	def activateStepPower(self, power):
		if power in self.getStepAvailable():
			for item in self.stepPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setStepPowerLevel(self, lv):
		self.stepLV = lv
	
	def setStepLevelingRateModifier(self, mod):
		self.stepMod = mod
	# End Step Block

	# Start Strength Block
	def initializeStrength(self, withLevel, withPowers):
		self.strengthLV = withLevel
		self.strengthMod = 1
		self.strengthPowers = list()
		self.strengthPowers.append(["Strong Arm", [10, 25, 50, 75, 100], 0, 5, "Increases base damage of all weapons by 20% each level."])
		self.strengthPowers.append(["Adrenaline", [20], 0, 1, "Gives a 50% boost to all weapons for 60 seconds."])
		self.strengthPowers.append(["Heavy Attack Specialty", [25, 50, 75], 0, 3, "10% chance to do critical damage with each level."])
		self.strengthPowers.append(["Brawler", [30, 60, 90], 0, 3, "Unarmed attacks do 20% more damage with each level."])
		self.strengthPowers.append(["Strong Back", [40], 0, 1, "Carry weight is increased by 100."])
		self.strengthPowers.append(["Blow Back", [50, 70, 90], 0, 3, "Weak, average, and strong enemies and thrown back with heavy attacks."])
		self.strengthPowers.append(["Golem", [50, 80, 100], 0, 3, "Physical defence and health is increased by 50 each level."])
		self.strengthPowers.append(["Titan", [100], 0, 1, "Perminantly under the effects of adrenaline."])

	def getStrengthPowerLevel(self):
		return self.strengthLV

	def getStrengthActivated(self):
		active = list()
		for item in self.strengthPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getStrengthAvailable(self):
		avail = list()
		for item in self.strengthPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.strengthLV:
					avail.append(item)
		return avail

	def getStrengthUnavailable(self):
		unavail = list()
		for item in self.strengthPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.strengthLV:
					unavail.append(item)
		return unavail

	def activateStrengthPower(self, power):
		if power in self.getStrengthAvailable():
			for item in self.strengthPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setStrengthPowerLevel(self, lv):
		self.strengthLV = lv
	
	def setStrengthLevelingRateModifier(self, mod):
		self.stregnthMod = mod
	# End Strength Block

	# Start Terra Block
	def initializeTerra(self, withLevel, withPowers):
		self.terraLV = withLevel
		self.terraMod = 1
		self.terraPowers = list()
		self.terraPowers.append(["Stone", [10, 25, 50, 75, 100], 0, 5, "Increases damage output with terra based attacks by 20% each level."])
		self.terraPowers.append(["Extra Force", [20], 0, 1, "Struck enemies have a chance of falling down."])
		self.terraPowers.append(["Stoneskin", [30, 60, 90], 0, 3, "Increases physical defence by 50% each level."])
		self.terraPowers.append(["Pellets", [30, 60, 90], 0, 3, "Assaults target with a barrage of stones."])
		self.terraPowers.append(["Hands", [40], 0, 1, "Causes hands of stone to rise from the earth and attempt to hinder nearby enemies from getting close to the caster."])
		self.terraPowers.append(["Earthquake", [50, 70, 90], 0, 3, "Starts an earthquake (lv 1 = causes enemies to fall down, lv 2 = causes damage, lv 3 = can topple buildings and trees)."])
		self.terraPowers.append(["Sandstorm", [50, 70, 90], 0, 3, "Summons a sandstorm which decreases enemy accuracy and slowly lowers their health. Effects increase with each level."])
		self.terraPowers.append(["Crush", [100], 0, 1, "Raises the earth around an enemy and causes it to crush in upon them until they die."])

	def getTerraPowerLevel(self):
		return self.terraLV

	def getTerraActivated(self):
		active = list()
		for item in self.terraPowers:
			if item[3] != 0:
				active.append(item)
		return active

	def getTerraAvailable(self):
		avail = list()
		for item in self.terraPowers:
			if item[3] < item[4]:
				if item[2][item[3]] < self.terraLV:
					avail.append(item)
		return avail

	def getTerraUnavailable(self):
		unavail = list()
		for item in self.terraPowers:
			if item[3] < item[4]:
				if item[2][item[3]] > self.terraLV:
					unavail.append(item)
		return unavail

	def activateTerraPower(self, power):
		if power in self.getTerraAvailable():
			for item in self.terraPowers:
				if item[0] == power[0]:
					item[3] += 1
	
	def setTerraPowerLevel(self, lv):
		self.terraLV = lv
	
	def setTerraLevelingRateModifier(self, mod):
		self.terraMod = mod
	# End Terra Block
