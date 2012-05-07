# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rosbaldeston"
__date__ ="$Jan 9, 2012 10:40:21 AM$"

class Skills:
    def __init__(self):
        None
        
    def activated(self):
        active = list()
        for item in self.archerySkills:
            if item[3] != 0:
                active.append(item)
        for item in self.oneHandedSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.shieldSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.staffSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.twoHandedSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.unarmedSkills:
            if item[3] != 0:
                active.append(item)
        return active

    # Start Archery Block
    def initializeArchery(self, withLevel, withSkills):
        self.archeryLV = withLevel
		self.archeryMod = 1
		self.archerySkills = list()
		self.archerySkills.append(["Pine", [0], 1, 1, "Ability to wield Iron Bows and Crossbows"])
		self.archerySkills.append(["Cedar", [25], 0, 1, "Ability to wield Steel Bows and Crossbows"])
		self.archerySkills.append(["Ebony", [50], 0, 1, "Ability to wield Ebony Bows and Crossbows"])
		self.archerySkills.append(["Dragon Wing", [75], 0, 1, "Ability to wield Dragon Wing Bows and Crossbows"])
		self.archerySkills.append(["White Cobalt", [100], 0, 1, "Ability to wield White Cobalt Bows and Crossbows"])

    def getArcherySkillLevel(self):
		return self.archeryLV

	def getArcheryActivated(self):
		active = list()
		for item in self.archerySkills:
			if item[3] != 0:
				active.append(item)
		return active

	def getArcheryAvailable(self):
		avail = list()
		for item in self.archerySkills:
			if item[3] < item[4]:
				if item[2][item[3]] < self.archeryLV:
					avail.append(item)
		return avail

	def getArcheryUnavailable(self):
		unavail = list()
		for item in self.archerySkills:
			if item[3] < item[4]:
				if item[2][item[3]] > self.archeryLV:
					unavail.append(item)
		return unavail

	def activateArcherySkill(self, Skill):
		if Skill in self.getArcheryAvailable():
			for item in self.archerySkills:
				if item[0] == Skill[0]:
					item[3] += 1
	
    def setArcherySkillLevel(self, lv):
            self.archeryLV = lv

    def setArcheryLevelingRateModifier(self, mod):
            self.archeryMod = mod
    # End Archery Block

    # Stary One-Handed Block
    # One-Handed Weapon Types and Stat Modifiers:
    #   Dagger:
    #   Sai:
    #   Sword:
    #   Battle Axe:
    #   Mace:
    def initializeOneHanded(self, withLevel, withSkills):
        self.oneHandedLV = withLevel
		self.oneHandedMod = 1
		self.oneHandedSkills = list()
		self.oneHandedSkills.append(["Iron", [0], 1, 1, "Ability to wield Iron One-Handed Weapons"])
		self.oneHandedSkills.append(["Steel", [25], 0, 1, "Ability to wield Steel One-Handed Weapons"])
		self.oneHandedSkills.append(["Dragon Bone", [50], 0, 1, "Ability to wield Dragon Bone One-Handed Weapons"])
		self.oneHandedSkills.append(["Diamond", [75], 0, 1, "Ability to wield Diamond One-Handed Weapons"])
		self.oneHandedSkills.append(["White Cobalt", [100], 0, 1, "Ability to wield White Cobalt One-Handed Weapons"])

    def getOneHandedSkillLevel(self):
		return self.oneHandedLV

	def getOneHandedActivated(self):
		active = list()
		for item in self.oneHandedSkills:
			if item[3] != 0:
				active.append(item)
		return active

	def getOneHandedAvailable(self):
		avail = list()
		for item in self.oneHandedSkills:
			if item[3] < item[4]:
				if item[2][item[3]] < self.oneHandedLV:
					avail.append(item)
		return avail

	def getOneHandedUnavailable(self):
		unavail = list()
		for item in self.oneHandedSkills:
			if item[3] < item[4]:
				if item[2][item[3]] > self.oneHandedLV:
					unavail.append(item)
		return unavail

	def activateOneHandedSkill(self, power):
		if power in self.getOneHandedAvailable():
			for item in self.oneHandedSkills:
				if item[0] == power[0]:
					item[3] += 1
	
    def setOneHandedSkillLevel(self, lv):
            self.oneHandedLV = lv

    def setOneHandedLevelingRateModifier(self, mod):
            self.oneHandedMod = mod
    # End One-Handed Block

    # Start Shield Block
    # Shield Types and Stat Modifiers:
    #   Buckler:
    #   Kite:
    #   Heater:
    #   Parma:
    #   Scutum:
    def initializeShield(self, withLevel, withSkills):
        self.shieldLV = withLevel
		self.shieldMod = 1
		self.shieldSkills = list()
		self.shieldSkills.append(["Iron", [0], 1, 1, "Ability to wield Iron Shields"])
		self.shieldSkills.append(["Steel", [25], 0, 1, "Ability to wield Steel Shields"])
		self.shieldSkills.append(["Dragon Bone", [50], 0, 1, "Ability to wield Dragon Bone Shields"])
		self.shieldSkills.append(["Diamond", [75], 0, 1, "Ability to wield Diamond Shields"])
		self.shieldSkills.append(["White Cobalt", [100], 0, 1, "Ability to wield White Cobalt Shields"])

    def getShieldSkillLevel(self):
		return self.shieldLV

	def getShieldActivated(self):
		active = list()
		for item in self.shieldSkills:
			if item[3] != 0:
				active.append(item)
		return active

	def getShieldAvailable(self):
		avail = list()
		for item in self.shieldSkills:
			if item[3] < item[4]:
				if item[2][item[3]] < self.shieldLV:
					avail.append(item)
		return avail

	def getShieldUnavailable(self):
		unavail = list()
		for item in self.shieldSkills:
			if item[3] < item[4]:
				if item[2][item[3]] > self.shieldLV:
					unavail.append(item)
		return unavail

	def activateShieldSkill(self, power):
		if power in self.getShieldAvailable():
			for item in self.shieldSkills:
				if item[0] == power[0]:
					item[3] += 1
	
    def setShieldSkillLevel(self, lv):
            self.shieldLV = lv

    def setShieldLevelingRateModifier(self, mod):
            self.shieldMod = mod
    # End Shield Block

    # Start Staff Block
    # Staff Weapon Types and Stat Modifiers:
    #   Bo:
    #   Spear:
    #   Halberd:
    #   Glaives:
    #   Bardiche:
    def initializeStaff(self, withLevel, withSkills):
        self.staffLV = withLevel
		self.staffMod = 1
		self.staffSkills = list()
		self.staffSkills.append(["Iron", [0], 1, 1, "Ability to wield Iron Staffs"])
		self.staffSkills.append(["Steel", [25], 0, 1, "Ability to wield Steel Staffs"])
		self.staffSkills.append(["Dragon Bone", [50], 0, 1, "Ability to wield Dragon Bone Staffs"])
		self.staffSkills.append(["Diamond", [75], 0, 1, "Ability to wield Diamond Staffs"])
		self.staffSkills.append(["White Cobalt", [100], 0, 1, "Ability to wield White Cobalt Staffs"])
    
    def getStaffSkillLevel(self):
		return self.staffLV

	def getStaffActivated(self):
		active = list()
		for item in self.staffSkills:
			if item[3] != 0:
				active.append(item)
		return active

	def getStaffAvailable(self):
		avail = list()
		for item in self.staffSkills:
			if item[3] < item[4]:
				if item[2][item[3]] < self.staffLV:
					avail.append(item)
		return avail

	def getStaffUnavailable(self):
		unavail = list()
		for item in self.staffSkills:
			if item[3] < item[4]:
				if item[2][item[3]] > self.staffLV:
					unavail.append(item)
		return unavail

	def activateStaffSkill(self, power):
		if power in self.getStaffAvailable():
			for item in self.staffSkills:
				if item[0] == power[0]:
					item[3] += 1
	
    def setStaffSkillLevel(self, lv):
            self.staffLV = lv

    def setStaffLevelingRateModifier(self, mod):
            self.staffMod = mod
    # End Staff Block

    # Start Two-Handed Block
    # Two-Handed Weapon Types and Stat Modifiers:
    #   Club:
    #   Greatsword:
    #   War Axe:
    #   War Hammar:
    #   
    def initializeTwoHanded(self, withLevel, withSkills):
        self.twoHandedLV = withLevel
		self.twoHandedMod = 1
		self.twoHandedSkills = list()
		self.twoHandedSkills.append(["Iron", [0], 1, 1, "Ability to wield Iron Two-Handed Weapons"])
		self.twoHandedSkills.append(["Steel", [25], 0, 1, "Ability to wield Steel Two-Handed Weapons"])
		self.twoHandedSkills.append(["Dragon Bone", [50], 0, 1, "Ability to wield Dragon Bone Two-Handed Weapons"])
		self.twoHandedSkills.append(["Diamond", [75], 0, 1, "Ability to wield Diamond Two-Handed Weapons"])
		self.twoHandedSkills.append(["White Cobalt", [100], 0, 1, "Ability to wield White Cobalt Two-Handed Weapons"])
    
    def getTwoHandedSkillLevel(self):
		return self.twoHandedLV

	def getTwoHandedActivated(self):
		active = list()
		for item in self.twoHandedSkills:
			if item[3] != 0:
				active.append(item)
		return active

	def getTwoHandedAvailable(self):
		avail = list()
		for item in self.twoHandedSkills:
			if item[3] < item[4]:
				if item[2][item[3]] < self.twoHandedLV:
					avail.append(item)
		return avail

	def getTwoHandedUnavailable(self):
		unavail = list()
		for item in self.twoHandedSkills:
			if item[3] < item[4]:
				if item[2][item[3]] > self.twoHandedLV:
					unavail.append(item)
		return unavail

	def activateTwoHandedSkill(self, power):
		if power in self.getTwoHandedAvailable():
			for item in self.twoHandedSkills:
				if item[0] == power[0]:
					item[3] += 1
	
    def setTwoHandedSkillLevel(self, lv):
            self.twoHandedLV = lv

    def setTwoHandedLevelingRateModifier(self, mod):
            self.twoHandedMod = mod
    # End Two-Handed Block
    
    # Start Unarmed Block
    def initializeUnarmed(self, withLevel, withSkills):
        self.unarmedLV = withLevel
		self.unarmedMod = 1
		self.unarmedSkills = list()
		self.unarmedSkills.append(["Iron", [0], 1, 1, "Ability to wield Iron Unarmed Weapons"])
		self.unarmedSkills.append(["Steel", [25], 0, 1, "Ability to wield Steel Unarmed Weapons"])
		self.unarmedSkills.append(["Dragon Bone", [50], 0, 1, "Ability to wield Dragon Bone Unarmed Weapons"])
		self.unarmedSkills.append(["Diamond", [75], 0, 1, "Ability to wield Diamond Unarmed Weapons"])
		self.unarmedSkills.append(["White Cobalt", [100], 0, 1, "Ability to wield White Cobalt Unarmed Weapons"])
    
    def getUnarmedSkillLevel(self):
		return self.unarmedLV

	def getUnarmedActivated(self):
		active = list()
		for item in self.unarmedSkills:
			if item[3] != 0:
				active.append(item)
		return active

	def getUnarmedAvailable(self):
		avail = list()
		for item in self.unarmedSkills:
			if item[3] < item[4]:
				if item[2][item[3]] < self.unarmedLV:
					avail.append(item)
		return avail

	def getUnarmedUnavailable(self):
		unavail = list()
		for item in self.unarmedSkills:
			if item[3] < item[4]:
				if item[2][item[3]] > self.unarmedLV:
					unavail.append(item)
		return unavail

	def activateUnarmedSkill(self, power):
		if power in self.getUnarmedAvailable():
			for item in self.unarmedSkills:
				if item[0] == power[0]:
					item[3] += 1
	
    def setUnarmedSkillLevel(self, lv):
            self.unarmedLV = lv

    def setUnarmedLevelingRateModifier(self, mod):
            self.unarmedMod = mod
    # End Unarmed Block
